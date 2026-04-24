Now I have enough context. The rubric file (v6) was truncated at the beginning — I'll reconstruct C-01–C-04 from the v5 file which contains the full essential criteria. Let me score V-01 and V-02 against all 23 criteria.

---

# topic-retro — Quest Score — Round 8
**Rubric:** v6 (C-01 through C-23; total available = 120)
**Variations available:** V-01 and V-02 (V-03 through V-05 not present in prompt context — scored from available input only)
**Trace artifact:** None. Scores assess spec design quality against rubric criteria.

---

## Per-Criterion Scoring

### Essential Criteria (C-01–C-05, 12 pts each)

| Criterion | V-01 | Evidence | V-02 | Evidence |
|-----------|------|----------|------|----------|
| C-01 Signal Accuracy Present | PASS | Phase 2 table: Signal / Predicted / Actual / Verdict columns. | PASS | Phase 3 prose blocks: Signal/Predicted/Actual/Verdict per entry. |
| C-02 Verdict Per Signal | PASS | Verdict column enforces C/P/W/ND set; rules state enumerated labels. | PASS | Each block: `Verdict: [C / P / W / ND]` — explicit label per signal. |
| C-03 Gaps Present and Actionable | PASS | Phase 3 Gap Table: "Would It Have Changed the Decision?" column (Yes/Possibly/No) — decision impact explicit. | PASS | Phase 2: high-leverage gap entries each carry "Would have changed the decision: Yes/Possibly/No." |
| C-04 Echo Present (One Only) | PASS | Phase 4: "single-row table," "Only one row," explicit anti-restatement rule. | PASS | Phase 4: "One Echo only. A wrong prediction restated as unexpected is not an Echo." |
| C-05 Topic + Commitment Context | PASS | Phase 1: topic name + commitment in one sentence as fixed reference point. | PASS | Phase 1: "(a) the topic name, (b) the nature of the commitment in one sentence." |

**Essential: V-01 = 60/60 | V-02 = 60/60. All essential: YES (both).**

---

### Recommended Criteria (C-06–C-08, 10 pts each)

| Criterion | V-01 | Evidence | V-02 | Evidence |
|-----------|------|----------|------|----------|
| C-06 Signal Coverage Summary | FAIL (0) | ND rows in Phase 2 surface absent signals but no 9-namespace enumeration table. Spec says "one row per signal" — namespaces with zero signals can be silently absent. | PASS (10) | Phase 2 explicitly enumerates all 9 namespaces: "For each of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic), state: what signal was gathered / absent." |
| C-07 Recommendation Tied to Gap/Echo | PARTIAL (5) | Practice Change column in Echo table is tied to the Echo via Systemic Pattern, but no standalone recommendation section that explicitly names "this addresses [gap/echo]." Linkage is structural, not stated. | PASS (10) | Phase 5 Recommendation requires: specific gap or Echo it addresses + namespace/process step + measurable outcome. Linkage is explicit and required. |
| C-08 Accuracy Ratio Stated | PASS (10) | "Immediately below the table, state the accuracy ratio: X C + Y P out of Z gathered signals." | PASS (10) | "After all signals, state the accuracy ratio: X C + Y P out of Z gathered (ND excluded)." |

**Recommended: V-01 = 15/30 | V-02 = 30/30.**

---

### Aspirational Criteria (C-09–C-23, 2 pts each)

| Criterion | V-01 | Evidence | V-02 | Evidence |
|-----------|------|----------|------|----------|
| C-09 Echo Linked to Systemic Pattern | PASS (2) | Echo Table column "Systemic Pattern" is explicit. | PASS (2) | Echo section: "Systemic Pattern: the recurring failure mode this belongs to." |
| C-10 AMEND Scope Per Table | PASS (2) | Scope declared at top of Phase 2; primary table = in-scope only; secondary table = excluded only. Secondary table IS the per-phase enforcement; clean separation satisfies intent. | PARTIAL (1) | Scope declared at top (confirmed). Per-table enforcement of prose phases unclear — V-02's Phase 2 and 3 are prose-based, not tabular. AMEND modifier was truncated. Scope-top declared; per-table unconfirmed. |
| C-11 Systemic Pattern Echo Field (Structural) | PASS (2) | "Systemic Pattern" is a named column in the Echo Table. Structural. | PARTIAL (1) | "**Systemic Pattern:**" is a bold-labeled prose field — labeled but not a table column. Pass condition allows "named row"; marginal PARTIAL given prose embedding. |
| C-12 Three-Way Isolation | PASS (2) | Phase 2 = accuracy (wrongs in Verdict), Phase 3 = gaps, Phase 4 = Echo. No structural path for cross-contamination. | PASS (2) | Phase 2 = gaps, Phase 3 = accuracy, Phase 4 = Echo. Distinct; anti-restatement rule explicit in Phase 4. |
| C-13 Inertia Framing for Gaps | FAIL (0) | Phase 3 Gap Table: "Why Absent" names structural reason (skipped, no owner, no process, out of scope) — not the assumption held without evidence. | FAIL (0) | Phase 2: "Why it was absent (structural reason, not blame)" — same failure: structural reason named, not inertia assumption. |
| C-14 Verdict Label Not Prose | PASS (2) | Verdict column in table enforces C/P/W/ND. Table column = structural. | PARTIAL (1) | `Verdict: [C / P / W / ND]` in prose block — enumerated label set, but prose format. "Prose verdicts that happen to be clear = PARTIAL." |
| C-15 Accuracy Ratio Not Just Count | PARTIAL (1) | "X C + Y P out of Z gathered" — ratio form present (N/M), but no explicit "= X%" percentage form required by spec. | PARTIAL (1) | Same format: "X C + Y P out of Z gathered (ND excluded)." No percentage form. |
| C-16 Namespace Coverage Table | FAIL (0) | No namespace table. Signal accuracy table is per-signal; namespace coverage not explicitly structured. | PARTIAL (1) | Phase 2 enumerates all 9 namespaces explicitly in prose. All 9 present but text format, not 9-row structured table. |
| C-17 Recommendation Template | FAIL (0) | No recommendation section. Practice Change in Echo table is free prose. No bracket-slot template. | PARTIAL (1) | Phase 5 lists three required components structurally but as prose requirements, not a bracket-slot fill-in template. |
| C-18 Echo Pattern Named (Not Blank/Restatement) | PARTIAL (1) | "Systemic Pattern" column label is directional but no explicit constraint against blank or against restating a wrong prediction in that field. | PARTIAL (1) | "Systemic Pattern: the recurring failure mode" — directive but no explicit guard against blank or restatement within the field definition. |
| C-19 Phase Completion Self-Contained | PARTIAL (1) | Phases 2–4 are tabular (rows self-contained). Phase 1 (prose) and Phase 5 (seal block) unprotected against silent truncation. | PARTIAL (1) | All phases (1–5) are prose or structured prose blocks. No phase has a row-level self-containment guarantee. Prose sections unprotected throughout. |
| C-20 Gap Inertia Assumption Named | FAIL (0) | Phase 3 Gap Table: no "assumption held without evidence" column or field. "Why Absent" is the only explanatory field. | FAIL (0) | Phase 2 gap entries: "why it was absent (structural reason)" only. No inertia assumption field. |
| C-21 Phase Seal Explicit | PASS (2) | Phase 5 RETRO SEAL enumerates: Topic, Commitment, Accuracy Rate, Gap Count, Echo, AMEND Scope — all required output fields named. | PASS (2) | Phase 6 RETRO SEAL: same structure. Enumerates all required fields explicitly. |
| C-22 OOS Secondary Table | PASS (2) | AMEND modifier: explicit secondary table `\| Signal \| Namespace \| Exclusion Reason \|` with rule "no commentary from the primary table bleeds into the secondary table." | PARTIAL (1) | AMEND modifier truncated in context. Scope declaration confirmed; secondary table for excluded signals not confirmed. V-02 Phase 2 is prose, raising question of whether secondary TABLE is required. |
| C-23 Phase Seal Format Strings | PASS (2) | Phase 5 Seal: `Topic: {topic name}`, `Commitment: {C/P/W/ND} -- {one-line summary}`, `Accuracy Rate: {ratio}`, `Gap Count: {n}`, `Echo: {one-phrase label}`, `AMEND Scope: {scope or N/A}`. Each field has format string. | PASS (2) | Phase 6 Seal: identical format string per field. ✓ |

**Aspirational:**

| | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | Total |
|-|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | 2 | 2 | 2 | 2 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 2 | 2 | **21** |
| V-02 | 2 | 1 | 1 | 2 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 2 | 1 | 2 | **17** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | **%** |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-01 — Table-Dominant | 60 | 15 | 21 | **96** | 80.0% |
| V-02 — Gap-First | 60 | 30 | 17 | **107** | 89.2% |

---

## Ranking

**1. V-02 — Gap-First (107/120, 89.2%)**
Wins on Recommended tier entirely (+15 over V-01). Gap-first sequencing structurally guarantees namespace coverage (C-06 PASS) and the standalone Recommendation phase satisfies C-07 with explicit gap/Echo linkage. Loses ground to V-01 on structural criteria: prose format costs C-10 (per-table enforcement), C-11 (labeled column vs prose field), C-14 (prose blocks vs table column), C-22 (secondary table unconfirmed due to prose phase format).

**2. V-01 — Table-Dominant (96/120, 80.0%)**
All-table format earns clean PASS on C-10, C-11, C-14, C-22. Loses Recommended tier almost entirely: C-06 fails (no namespace enumeration), C-07 partial (no standalone recommendation section). The table-dominant design sacrifices breadth coverage for structural precision.

---

## Persistent Failures (both variations)

| Criterion | Status | Pattern |
|-----------|--------|---------|
| C-13 Inertia Framing | FAIL (both) | "Why Absent" / "structural reason" names *how* the gap was absent, not *what assumption made it invisible*. Neither variation separates structural reason from inertia belief. |
| C-20 Gap Inertia Assumption Named | FAIL (both) | No variation adds a dedicated column for the assumption held without evidence. This is R7's persistent gap, now in its second round. |
| C-15 Accuracy Ratio | PARTIAL (both) | "X C + Y P out of Z" gives ratio form but no "= X%" percentage. Both variations leave this partial. |

---

## Excellence Signals from V-02 (Top Scorer)

**Signal 1 — `echo-why-unexpected-named`**
V-02 Phase 4 Echo includes a labeled field: "Why Unexpected: what the signals implied instead." This makes the Echo falsifiable — not just "this was unexpected" but "signals implied X; we found Y instead." The contrast between prior implication and actual finding is structurally required. No current criterion captures this. Would become: PASS if "Why Unexpected" field names the prior signal expectation; PARTIAL if present but prose-buried.

**Signal 2 — `recommendation-measurable-outcome`**
V-02 Phase 5 Recommendation requires "the measurable outcome that would indicate success." C-07 only requires naming the gap/Echo and specifying a practice change. Measurability converts the recommendation from a commitment to a verifiable statement. Would become: PASS if outcome indicator named; PARTIAL if practice change present without measurability.

---

## Scorecard Summary

| | V-01 | V-02 |
|--|------|------|
| Score | 96/120 | **107/120** |
| All essential | YES | YES |
| C-13 (inertia) | FAIL | FAIL |
| C-20 (assumption column) | FAIL | FAIL |
| Top | — | ✓ |

```json
{"top_score": 107, "all_essential_pass": true, "new_patterns": ["echo-why-unexpected-named", "recommendation-measurable-outcome"]}
```
