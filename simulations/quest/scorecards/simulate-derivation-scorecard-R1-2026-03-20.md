Now I have everything I need. Let me score all five variations.

---

## simulate-derivation — Round 1 Scorecard

**Scoring approach**: Each variation is evaluated on how reliably its prompt design would produce LLM outputs satisfying each rubric criterion. Scored at the prompt level — not a live run. Points are fractional for PARTIAL compliance.

**Point weights**: C-01–C-05 = 12 pts each (essential, 60 total) · C-06–C-08 = 10 pts each (recommended, 30 total) · C-09–C-10 = 5 pts each (aspirational, 10 total)

---

### V-01 — Master Table Format

**Axis**: Compress per-step blocks into one master verification table.

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | 6-column table defined; "Do not skip any S-ID" implicit in master table instruction |
| C-02 Verification block per step | PASS | 10/12 | Master table rows cover alg/dim/sign/verdict columns — technically satisfies, but YES/NO without prose context risks thin coverage on edge steps |
| C-03 APPROX flagging | PARTIAL | 7/12 | Table has "APPROX: stated?" and "APPROX: validity stated?" columns — captures (c) and part of (b). Missing (a): "what quantity is being approximated" is not required anywhere in the verification section. SOUND APPROX rows have no obligation to state what is approximated. |
| C-04 Fault register | PASS | 12/12 | Full 6-column register with P1/P2/P3 defined; "No faults found" case handled |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and all required fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 5 has named verdict section with 3 options |
| C-07 Amend maps to faults | PARTIAL | 7/10 | Three fixes citing F-ID — no explicit rule requiring P1/P2 prioritization in Amend |
| C-08 Step types classified | PARTIAL | 5/10 | Types defined in derivation map; no instruction to justify EXACT with algebraic identity or state PHYSICAL assumptions explicitly |
| C-09 Catches fault not in paper | FAIL | 0/5 | Not prompted |
| C-10 Expands compressed steps | FAIL | 0/5 | Not prompted |

**V-01 Total: 75 / 100**

---

### V-02 — Type-Classifier Pass First

**Axis**: Dedicated classification phase before building the derivation map.

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 3 table; types must match Phase 2 — cross-phase consistency enforced |
| C-02 Verification block per step | PASS | 12/12 | Phase 4 uses per-step block format with all checks; same structure as baseline |
| C-03 APPROX flagging | PARTIAL | 9/12 | Phase 2 classification explicitly captures (a) what is approximated + (b) validity condition + (c) paper acknowledgment. But Phase 4 blocks only have "APPROX check: approximation named in paper? YES/NO" — (a) is in Phase 2, not in the verification block itself. C-03 rubric requires (a) in the verification block. |
| C-04 Fault register | PASS | 12/12 | Phase 5 register with full columns and severity |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and all fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 6 "Global verdict" in summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | "Exactly three targeted fixes, each citing an F-ID" — no explicit P1/P2 priority rule |
| C-08 Step types classified | PASS | 8/10 | Pre-classification phase forces labeling before map — stronger than any inline-only approach; mismatch note required on revision |
| C-09 Catches fault not in paper | PARTIAL | 2/5 | Classification pass asks "whether the paper names this approximation" — creates implicit detection path for unstated approximations; not explicit |
| C-10 Expands compressed steps | FAIL | 0/5 | Not prompted |

**V-02 Total: 85 / 100**

---

### V-03 — First-Person Imperative

**Axis**: All instructions as imperatives ("Do X. Then do Y.") to reduce section skipping.

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Step 2: "add one row... include every non-trivial step, minimum 3 rows" |
| C-02 Verification block per step | PASS | 12/12 | Step 3: "For every S-ID in your map, produce a verification block. Do not skip any S-ID." Imperative framing reduces skip probability |
| C-03 APPROX flagging | PARTIAL | 8/12 | Step 3: "the two APPROX lines are not optional... mark WEAK/BROKEN" — strong enforcement of consequence. But the block lines are "approximation named in paper? YES/NO" and "validity condition given? YES/NO" — captures (b)+(c) from paper's side, not (a): "what is being approximated" (the tracer's own statement). No instruction to state the approximation substantively. |
| C-04 Fault register | PASS | 12/12 | Step 4: full table; P1/P2/P3 defined; "No faults found" case handled |
| C-05 Artifact frontmatter | PASS | 12/12 | Step 6 is most explicit frontmatter instruction of any variation: YAML block shown with field descriptions |
| C-06 Global soundness verdict | PASS | 10/10 | Step 5: "State the global verdict in a section called 'Derivation Soundness'" — named section required |
| C-07 Amend maps to faults | PASS | 10/10 | "Exactly three fixes. Each must cite an F-ID. If P1 faults exist, at least one fix must address a P1. If P2 faults exist, at least one fix must address a P2." — strongest C-07 instruction; explicit severity-priority rule present |
| C-08 Step types classified | PARTIAL | 5/10 | Types defined in Step 2; no instruction to justify EXACT algebraically or state PHYSICAL assumptions |
| C-09 Catches fault not in paper | FAIL | 0/5 | Not prompted |
| C-10 Expands compressed steps | FAIL | 0/5 | Not prompted |

**V-03 Total: 81 / 100**

---

### V-04 — Compressed Acquisition, Expanded Verification

**Axis**: Cut Phase 1 to a preamble; double instruction space on verification phase with expanded APPROX sub-block.

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table with all 6 columns; "minimum 3 rows" stated |
| C-02 Verification block per step | PASS | 12/12 | Phase 2 is most expanded verification of any variation: separate sub-headings for algebraic, dimensional, sign, APPROX checks. "Do not collapse multiple steps. Do not omit a step because it looks trivial." |
| C-03 APPROX flagging | PASS | 12/12 | APPROX check sub-block explicitly requires: (a) "What quantity or relationship is being approximated? [state explicitly]" (b) "Under what conditions does this approximation hold? [state the validity condition]" (c) "Does the source paper state this approximation? YES / NO" (c') "Does the source paper give the validity condition? YES / NO" — all three rubric parts (a/b/c) in the verification block itself, plus auto-pass note instruction for zero-APPROX case |
| C-04 Fault register | PASS | 12/12 | Phase 3 register; "P2 — any WEAK/BROKEN from the APPROX check" explicit |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and all fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 "Derivation Soundness Verdict" uses a definition table (SOUND/CONDITIONALLY SOUND/BROKEN) plus required 1–3 sentence explanation |
| C-07 Amend maps to faults | PARTIAL | 8/10 | "[F-ID] [severity]: [specific fix]" format excellent; but no explicit P1/P2 priority rule for Amend ordering (unlike V-03) |
| C-08 Step types classified | PARTIAL | 7/10 | APPROX type definition includes "state what, under what conditions, whether paper names it" inline — strongest APPROX-type guidance; EXACT/PHYSICAL less explicit |
| C-09 Catches fault not in paper | PARTIAL | 2/5 | Expanded APPROX check requires tracer to state validity conditions independently — proactive elicitation may surface unstated approximations; not explicit |
| C-10 Expands compressed steps | FAIL | 0/5 | Not prompted |

**V-04 Total: 87 / 100**

---

### V-05 — Combined: Master Table + Type-Classifier

**Axis**: Stack V-01 (master table) + V-02 (type-classifier-first).

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 3 table; "Types must match Phase 2 exactly" — consistency constraint carried forward |
| C-02 Verification block per step | PASS | 10/12 | Master verification table (Phase 4) covers all checks as columns; "Do not skip any row." Table rows satisfy criterion structurally but lack prose depth of block format |
| C-03 APPROX flagging | PARTIAL | 9/12 | Phase 2 classifier captures (a) "what is being approximated" + (b) validity condition + (c) paper acknowledgment. Phase 4 table has "APPROX: stated?" and "APPROX: validity?" columns. Coverage is split: (a) in Phase 2, (b)+(c) in Phase 4. Rubric requires all three in the verification block — Phase 4 table alone misses (a). Better than V-01 because Phase 2 captures it, but weaker integration than V-04. |
| C-04 Fault register | PASS | 12/12 | Phase 5 register with full columns and severity |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and all fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 6 "Derivation Soundness" section; verdict in one sentence |
| C-07 Amend maps to faults | PARTIAL | 9/10 | "[F-ID] [P1/P2/P3]: [fix]" includes severity inline — good signal; no explicit P1/P2 priority rule |
| C-08 Step types classified | PASS | 8/10 | Pre-classification forces labeling; map-phase consistency constraint; same strength as V-02 |
| C-09 Catches fault not in paper | PARTIAL | 2/5 | Phase 2 asks "whether the paper names this approximation" — same implicit detection path as V-02 |
| C-10 Expands compressed steps | FAIL | 0/5 | Not prompted |

**V-05 Total: 84 / 100**

---

## Ranking

| Rank | Variation | Score | All Essential Pass? | Notes |
|------|-----------|-------|-------------------|-------|
| 1 | **V-04** | **87** | YES | Best C-03; best C-02 depth; strongest APPROX elicitation |
| 2 | **V-02** | **85** | YES | Pre-classification strongest C-08; C-03 split across phases |
| 3 | **V-05** | **84** | YES | Combination works; table format weakens C-03 integration |
| 4 | **V-03** | **81** | YES | Strongest C-07; imperative phrasing doesn't fix C-03 gap |
| 5 | **V-01** | **75** | NO (C-03 7/12) | Table format alone cannot satisfy C-03 without prose |

---

## Excellence Signals from V-04

**What made V-04 better than the others:**

1. **Prose-required APPROX sub-block** — Instead of YES/NO columns for APPROX checks, V-04 requires the tracer to *state* the approximation in prose: "What quantity or relationship is being approximated? [state explicitly]" and "Under what conditions does this approximation hold? [state the validity condition]." This puts (a), (b), and (c) in the verification block itself, which is where the rubric requires them. Every other variation only captures paper-coverage (YES/NO) without requiring the tracer's own statement.

2. **Token-budget redirection** — "This phase is the core deliverable of this skill — allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial." Explicitly telling the LLM which phase matters most redirects effort away from acquisition and toward the highest-weight criteria (C-02, C-03).

3. **Severity label inline in Amend fixes** — "[F-ID] [severity]: [specific fix]" format forces severity to appear in the action section, not just in the fault register. This makes P1/P2/P3 triage visible at the point of use.

---

## Gap Common to All Variations

**C-09 and C-10 are unaddressed across all five.** No variation prompts the tracer to note "not acknowledged by paper" or to supply interpolated intermediate steps. These are aspirational (10 pts total), but consistently earning 0/10 represents 10 free points in a future variation. A V-06 that adds "(label any fault not flagged by the paper as 'NEW')" and "(expand any compressed step with sub-steps marked 'interpolated')" should recover most of this.

---

```json
{"top_score": 87, "all_essential_pass": true, "new_patterns": ["prose-required-approx-sub-block: require the tracer to state (a) what is approximated and (b) validity condition as prose in the verification block itself — not just YES/NO paper-coverage columns", "token-budget-redirect: explicitly label the verification phase as the core deliverable to concentrate LLM effort on highest-weight criteria", "severity-inline-amend: include P1/P2/P3 severity in the Amend fix format so triage is visible at the action step, not only in the fault register"]}
```
