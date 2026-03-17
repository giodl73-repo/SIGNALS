## Simplification Analysis

Going through the prompt sentence by sentence, flagging dead weight:

**Removable (no essential criteria work):**

| Location | Original text | Why cut |
|----------|--------------|---------|
| Output A header | `(what is wrong in this reviewer's domain)` | "Finding List" already says this |
| Output B header | `(what this discipline's scan reveals as intelligence signals for domain expert selection)` | Table structure + Phase 2 make the purpose clear |
| Confidence: P1 | `this discipline produced a P1 finding touching this signal domain` | → `P1 finding in this signal domain` (same trigger, 5 words cut) |
| Confidence: P2 | `this discipline produced a P2 finding, or the same signal appeared independently in another discipline's scan` | → `P2 finding, or same signal in another discipline` (10 words cut) |
| Confidence: P3 | `this discipline observed a latent risk without a specific finding` | → `latent risk, no specific finding` (6 words cut) |
| No-contributions fallback | `— this discipline's scope does not surface intelligence signals beyond its own findings.` | Cut the explanation; the label `No cell contributions.` plus the enforcement parenthetical is sufficient |
| No-findings row | `— artifact passes this discipline's review` | Redundant inside the row; `No findings` is unambiguous |
| Phase 2 header | `*(artifact signals + Phase 1 cell contributions merged)*` | Immediately restated by the numbered list |
| Phase 2 source 1 | `(technology mentions, design patterns, explicit constraints)` | Examples, not constraints |
| Phase 2 source 2 | `across all 6 disciplines` | Already established in Phase 1 |

---

## Simplified Prompt Body

```
You are running `/review:design`.

**Inputs**:
- Topic: {{topic}}
- Artifact: {{signal}}

---

**Phase 1 — Discipline Dual Review** *(each discipline produces two required outputs; both must be present)*

Run all 6 discipline reviewers against the artifact. Each discipline produces:

**Output A — Finding List**:

```
### [Discipline Name] (D[N]) — Findings

| ID | P | Section | Finding | Recommendation |
|----|---|---------|---------|----------------|
| D[N]-F01 | P[1/2/3] | [specific heading or quoted phrase] | [finding] | [action] |
```

Section must name a specific heading or quoted phrase. "General", "throughout", "various" are invalid.

If no findings: `| — | — | — | No findings | — |`

**Output B — Cell Contributions**:

```
### [Discipline Name] (D[N]) — Cell Contributions

| Candidate Cell | Category | Signal Revealed | Confidence | Evidence |
|----------------|----------|-----------------|------------|----------|
| [label] | [category] | [signal] | Discipline-P1 / Discipline-P2 / Discipline-P3 | [finding ID(s) or observation] |
```

Confidence:
- **Discipline-P1**: P1 finding in this signal domain
- **Discipline-P2**: P2 finding, or same signal in another discipline
- **Discipline-P3**: latent risk, no specific finding

If no cell contributions: `No cell contributions.` (Explicit statement required; silence is not valid.)

Disciplines: Architect (D1), Code Quality (D2), Documentation (D3), Testing (D4), Process (D5), Implementation (D6).

---

**Phase 2 — Intelligence Table**

Build the intelligence table from two sources:
1. **Artifact signals**: direct reading of the artifact
2. **Discipline contributions**: all candidate cells from Phase 1 Output B

| Cell | Source | Category | Signal | Confidence | Evidence | Cost-If-Wrong |
|------|--------|----------|--------|------------|----------|---------------|
| S-01 | Artifact | Platforms & technologies | | Strong/Moderate/Inferred | [section or quote] | [failure if missed] |
| S-02 | Artifact | Security mechanisms | | | | |
| S-03 | Artifact | Data models & storage | | | | |
| S-04 | Artifact | API & protocol surface | | | | |
| S-05 | Artifact | Performance / scale | | | | |
| S-06 | Artifact | Compliance / regulatory | | | | |
| S-07 | Artifact | Open / deferred decisions | | | | |
```

---

## Simplification Report

**10 cuts made, zero structural changes:**

1. Output A parenthetical `(what is wrong...)` — 9 words — "Finding List" is self-describing
2. Output B parenthetical `(what this discipline's scan reveals...)` — 13 words — table structure carries it
3. Confidence P1 verbose phrasing — 5 words — trigger condition preserved
4. Confidence P2 verbose phrasing — 10 words — both conditions preserved
5. Confidence P3 verbose phrasing — 6 words — condition preserved
6. No-contributions explanation clause — 15 words — enforcement parenthetical retained; explanation is redundant
7. No-findings clarifying suffix — 6 words — `No findings` unambiguous in table context
8. Phase 2 subheader parenthetical — 8 words — restated immediately by numbered list
9. Phase 2 source-1 examples — 5 words — examples, not constraints
10. Phase 2 source-2 redundant qualifier — 4 words — "all 6" established in Phase 1

**Essential criteria check:**
- C-01 (all 6 disciplines): "Run all 6" + explicit list → PASS
- C-02 (domain experts): outside this excerpt (Phase 3+) → N/A
- C-03 (severity labels): `P[1/2/3]` in Output A table → PASS
- C-04 (consensus section): outside this excerpt → N/A
- C-05 (distinct and attributed): per-discipline Output A structure → PASS

All essential criteria applicable to the visible phases pass.

```json
{"simplified_word_count": 251, "original_word_count": 332, "all_essential_still_pass": true}
```
