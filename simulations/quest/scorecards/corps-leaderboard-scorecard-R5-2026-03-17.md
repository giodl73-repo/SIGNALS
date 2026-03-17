## Quest Score — corps-leaderboard R5

---

### Scoring Methodology

**Rubric v5 weight structure** (from criteria text):
- Essential (C-01 to C-05): 5 × 12 = 60 pts
- Recommended (C-06, C-07, C-08): 3 × 10 = 30 pts
- Aspirational (C-09 to C-19): 11 × (10/11) ≈ 10 pts — total = 100

C-18 and C-19 each worth ≈ 0.91 pts. C-09 through C-17 inherited from R4 (all scored 100/100 against v4, unchanged by R5 deltas). R5 targeted exactly C-18 and C-19.

---

### Criterion-by-Criterion Evaluation

#### C-01 — All Discovered Topics Listed with Named Gap Term

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | `matrix gap` defined: "A topic present in the artifact table but absent from the matrix is a **matrix gap**." |
| V-02 | PASS | `compilation gap` defined: "A topic in the scan result but absent from the compilation is a **compilation gap**." |
| V-03 | PASS | `topic gap` defined: "A topic that appears in the workspace but is missing from this section is a **topic gap**." |
| V-04 | PASS | `findings gap` defined: "A missing topic is a **findings gap**." |
| V-05 | PASS | `log gap` defined: "A topic in the artifact table but absent from this section is a **log gap**." |

#### C-02 — Per-Topic Achievement Evaluation with Exact Names

All five required achievement names (First Signal, Signal Depth, Full Sweep, Solo Pioneer, Team Topic) appear verbatim in every variation. V-01 uses them as matrix column headers. V-02 lists them in a definition table. V-03 through V-05 each include explicit definition tables with exact names.

| Variation | Result | Risk Note |
|-----------|--------|-----------|
| V-01 | PASS | Column headers are the achievement names — structure enforces exact naming |
| V-02 | PASS | Definition table with exact names |
| V-03 | PASS | Definition table with exact names |
| V-04 | PASS | Definition table with exact names |
| V-05 | PASS | Definition table with exact names |

#### C-03 — All Three Team Milestones Present with Exact Names

All three milestone names required verbatim: "first team signal", "shared coverage", "debate starter".

| Variation | Result | Notes |
|-----------|--------|-------|
| V-01 | PASS | Milestone table with exact string literals in row headers |
| V-02 | PASS | Milestone table with exact string literals |
| V-03 | PASS | Milestone table with exact names; status format uses `EARNED / NOT YET` |
| V-04 | PASS | `FINDINGS — Team Milestones` table with exact names |
| V-05 | PASS | `Milestone Check` table with exact names |

#### C-04 — Contributor Leaderboard Present and Ranked

| Variation | Result | Position / Fallback |
|-----------|--------|---------------------|
| V-01 | PASS | First section; fallback row `no contributor metadata found` defined |
| V-02 | PASS | First section before GATE 1; fallback defined |
| V-03 | PASS | `WHO'S CONTRIBUTING` — section name differs but ranked table present; fallback defined |
| V-04 | PASS | Nested in SECTION 1 — SITUATION; ranked; fallback defined |
| V-05 | PASS | CONTRIBUTOR ROSTER — first section; fallback defined |

V-03 note: C-04 requires "A contributor leaderboard section is present, ranked in descending order" — it does not require the section to be named "Leaderboard." PASS stands.

#### C-05 — Specific Next Actions Naming Namespace and Achievement

All R5 variations share the same three-field action template:
```
-> Unlocks: {exact achievement or milestone name}
-> Breaks: {condition name from health score}
-> Priority: [tier]
```
The `Breaks` field (requiring health condition name or `prevents:` prevention rationale when score = 0) is an aspirational addition beyond C-05 minimum. C-05 itself passes at "names namespace+topic + exact achievement/milestone."

| Variation | Result | At Least 3 Actions |
|-----------|--------|--------------------|
| V-01 | PASS | Yes — `{namespace}/{topic}` template enforced |
| V-02 | PASS | Yes — same template |
| V-03 | PASS | Yes — same template |
| V-04 | PASS | Yes — same template |
| V-05 | PASS | Yes — same template |

#### C-06 — Earned / Available Achievement Separation

| Variation | Result | Mechanism |
|-----------|--------|-----------|
| V-01 | PASS | Cell notation: `*` = earned, `-N sig/ns/contrib` = locked — column-level distinction within matrix rows |
| V-02 | PASS | Explicit `**Earned**` / `**Locked**` subsections per topic |
| V-03 | PASS | Explicit `**Earned**` / `**Locked**` subsections per topic |
| V-04 | PASS | `**Earned** (check)` / `**Locked** (circle)` labels per topic |
| V-05 | PASS | Explicit `**Earned**` / `**Locked**` subsections per topic |

V-01 cell notation uses the matrix column model explicitly allowed by C-06 ("table columns, badge markers like checkmark vs circle"). PASS confirmed.

#### C-07 — 1-Away Gap Detection

| Variation | Result | Section Name | If-None Clause |
|-----------|--------|--------------|----------------|
| V-01 | PASS | `1-Away Gaps` table — "Needed" and "To Unlock" columns with exact counts | "No 1-away gaps found. Closest: [topic] needs [n] more [unit]" |
| V-02 | PASS | `1-Away Gaps` with exact gap text | "No 1-away gaps. Closest: [topic] needs [n]..." |
| V-03 | PASS | `ALMOST THERE` — "add [1 signal / 1 contributor / 1 namespace]" | "Nothing is one step away. Closest is: [topic]..." |
| V-04 | PASS | `FINDINGS — 1-Away Gaps` | "No 1-away gaps. Closest: [topic]..." |
| V-05 | PASS | `1-Away Gaps` | "No 1-away gaps. Closest: [topic]..." |

V-03 "ALMOST THERE" is a valid section name under C-07 which explicitly names it as acceptable.

#### C-08 — Team Synthesis Sentence (Third Recommended Criterion)

C-19 description reveals C-08's definition: "C-08 requires a synthesizing sentence that draws a conclusion not visible from any individual-topic view." C-08 is the baseline; C-19 adds the numeric requirement on top.

| Variation | Result | Section Name |
|-----------|--------|--------------|
| V-01 | PASS | `TEAM SYNTHESIS` — cross-topic/contributor conclusion required |
| V-02 | PASS | `TEAM INSIGHT` — cross-topic/contributor conclusion required |
| V-03 | PASS | `TEAM PICTURE` — cross-topic/contributor conclusion required |
| V-04 | PASS | `DEBRIEF` — cross-topic conclusion required |
| V-05 | PASS | `TEAM SYNTHESIS` — cross-topic conclusion required |

All 5 sections explicitly require a conclusion "not visible from any single topic entry or roster row."

#### C-09 through C-17 — Aspirational (Inherited from R4)

R4 variations all scored 100/100 against v4, meaning all 9 pre-existing aspirational criteria passed. R5 changes are additive (gate lines + type enumeration) and do not disturb any existing criterion coverage. No structural regressions identified. **All 5 variations: PASS all 9 criteria.**

Key aspirational patterns that map to these criteria (from reading the variation text):
- Signal Health Score with 5 named stagnation conditions and tier rating — present in all 5 variations
- Health-condition-linked actions via `-> Breaks` field — present in all 5 variations
- Decision-risk framing — present in V-04; equivalent "What this blocks" in V-01/V-02/V-05; "What this puts at risk" in V-03

#### C-18 — Gate Markers as Literal Output Lines

This is the focal new criterion. The distinguishing factor is not just presence but auditable mechanism strength.

| Variation | Result | Gate Marker Format | Mechanism Strength |
|-----------|--------|-------------------|-------------------|
| V-01 | PASS | `[TRANSITION: X closed. Y opens now.]` | Single unidirectional marker per boundary — skip leaves one gap |
| V-02 | PASS | `[GATE N: X closed. Y opens now.]` (numbered) | Single unidirectional marker — numbering adds ordering signal |
| V-03 | PASS | `[CHECKPOINT: X complete. Y opens now.]` | Single unidirectional marker in warm register |
| V-04 | PASS | `[SITREP GATE: X closed. Y opens now.]` | Single unidirectional marker — register-coherent with military briefing format |
| V-05 | PASS | `[OPEN: X — preceded by Y]` at section start + `[CLOSE: X — Z opens next]` at section end | **Bidirectional** — a single skip violates two output positions simultaneously |

V-05 distinguishes itself within a "PASS" tier: the bidirectional contract means section omission is detectable without cross-reference — the `[CLOSE: preceding]` would name a section that never opened, and `[OPEN: next]` names a predecessor that never closed. Two structural violations per skip.

#### C-19 — Synthesis Sentence with Concrete Numeric Claim

Type enumeration is **identical** across all five variations: "contributor count, signal count, namespace count, or topic count" appears in every synthesis instruction with the same four-type list.

| Variation | Result | Instruction Text |
|-----------|--------|-----------------|
| V-01 | PASS | "contributor count, signal count, namespace count, or topic count" in TEAM SYNTHESIS instruction |
| V-02 | PASS | "contributor count, signal count, namespace count, or topic count" in TEAM INSIGHT instruction |
| V-03 | PASS | "contributor count, signal count, namespace count, or topic count" in TEAM PICTURE instruction |
| V-04 | PASS | "contributor count, signal count, namespace count, or topic count" in DEBRIEF instruction |
| V-05 | PASS | "contributor count, signal count, namespace count, or topic count" as "quantified core" in TEAM SYNTHESIS instruction |

C-19 is a co-equal pass across all five — no differentiation here.

---

### Composite Scores

| Variation | C-01–05 (60) | C-06–08 (30) | C-09–17 (8.18) | C-18 (0.91) | C-19 (0.91) | **Total** |
|-----------|-------------|-------------|----------------|-------------|-------------|-----------|
| V-01 All-Tables Scorecard | 60 | 30 | 8.18 | 0.91 | 0.91 | **100.0** |
| V-02 Triple-Gate Pipeline | 60 | 30 | 8.18 | 0.91 | 0.91 | **100.0** |
| V-03 Conversational Coach | 60 | 30 | 8.18 | 0.91 | 0.91 | **100.0** |
| V-04 SITREP + Decision Risk | 60 | 30 | 8.18 | 0.91 | 0.91 | **100.0** |
| V-05 Cascading Contracts | 60 | 30 | 8.18 | 0.91 | 0.91 | **100.0** |

---

### Ranking

All five variations tied at 100.0/100. Tiebreak ranking by C-18 mechanism strength (the primary axis that differentiated R4 from R5):

1. **V-05 Cascading Contracts** — 100.0 — Bidirectional stamps; one skip violates two output positions. Strongest structural auditability.
2. **V-02 Triple-Gate Pipeline** — 100.0 — Numbered gates (`GATE 1/2/3`) add ordering signal; minimal-delta from proven R4 baseline; lowest regression risk.
3. **V-01 All-Tables Scorecard** — 100.0 — Richest diagnostic structure (SIGNAL HEALTH SCORECARD as second section before achievements); cleanest machine-readable format.
4. **V-04 SITREP + Decision Risk** — 100.0 — Gate stamp vocabulary fits register; adds `Decision risk` field unique among variations.
5. **V-03 Conversational Coach** — 100.0 — `[CHECKPOINT: ...]` format passes C-18 but boundary between "progress commentary" and "structural marker" is thinnest among the five.

---

### Excellence Signals — V-05 as Primary, V-02 as Secondary

**From V-05 (Cascading Contracts)**:

1. **Bidirectional section stamps as compliance artifacts**: Writing both `[OPEN: X — preceded by Y]` and `[CLOSE: X — Z opens next]` at the two ends of every section converts section sequencing from an ordering rule into a self-verifying output structure. A skipped section creates an observable gap at two artifact positions simultaneously. This is stronger than unidirectional stamps because it does not require sequential scanning to detect the violation — the `[OPEN]` of the following section directly names the predecessor that should have `[CLOSE]`d.

2. **Closing stamp names the successor**: The `[CLOSE: X — Z opens next]` pattern encodes a forward-pointer directly in the artifact. Any scanner can verify the claimed next section actually opened by looking for its `[OPEN]` line. This transforms the output artifact into a linked list where missing links are detectable by reference rather than by position.

**From V-02 (Triple-Gate Pipeline — Minimal Delta)**:

3. **Numbered gates vs named-only gates**: `[GATE 1:]`, `[GATE 2:]`, `[GATE 3:]` provide both a name (section identity) and an index (ordering position). A reordered gate sequence violates the expected numbering even if the section names are preserved. This is an additional compliance signal not present in other variations.

**Cross-variation pattern (C-19)**:

4. **Four-type enumeration on synthesis numeric requirement**: Specifying the permitted types (`contributor count, signal count, namespace count, or topic count`) rather than generic "specific number" constrains the synthesis in a verifiable way. A synthesis sentence using "a few" or "several" cannot satisfy any of the four named types. A reviewer can evaluate compliance without judgment about what counts as "specific."

---

### Summary

The R5 ceiling is closed. All five variations pass every criterion including the two new aspirational criteria (C-18, C-19). The v5 ceiling problem (open because no R4 variation passed both) is resolved. The next ceiling-opening question is: can a single variation surpass 100 against any future v6 criteria?

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["bidirectional section stamps (OPEN at start + CLOSE at end of every section) make skipped sections detectable at two artifact positions — a single skip violates both the preceding CLOSE and the following OPEN line, enabling reference-based rather than position-based gap detection", "type-named numeric enumeration in synthesis instruction (contributor count / signal count / namespace count / topic count) prevents generic 'specific number' claims and makes synthesis sentence compliance verifiable without scorer judgment"]}
```
