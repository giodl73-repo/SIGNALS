## validate-inertia Round 8 — Scorecard

### Entering Context

V-35 scored 270/270 on R7. Against R8's 290-pt ceiling (adds C-28 + C-29), V-35 carries two unnamed citation boundaries: Phase 2 → Phase 5(2) and Phase 6 Part B → Phase 7 both produce prose without named artifacts, making them paraphrase chains.

---

### C-28 / C-29 Boundary Analysis

| Boundary | Artifact required | V-36 | V-37 | V-38 | V-39 | V-40 |
|----------|-----------------|------|------|------|------|------|
| Phase 1 → Phase 4 | SCORING INFRASTRUCTURE DECLARED | Y | Y | Y | Y | Y |
| Phase 2 → Phase 5(2) | PERSONA INVENTORY DECLARED | Y | N | N | Y | Y |
| Phase 5(3) → AMEND | LEVER POINT: [label] | Y | Y | Y | Y | Y |
| Phase 6 Part B → Phase 7 | TRAJECTORY VERDICT: [direction] | N | N | Y | Y | Y |
| **Boundaries met** | | 3/4 | 2/4 | 3/4 | **4/4** | **4/4** |

**C-28:** PARTIAL for V-36/V-37/V-38; PASS for V-39/V-40.
**C-29:** Coupled — every description link prevents exact-copy at that consumer. PARTIAL for V-36/V-37/V-38; PASS for V-39/V-40.

---

### Per-Variation Scores

| Variation | C-28 | C-29 | Total | Rank |
|-----------|------|------|-------|------|
| **V-40** | PASS (10) | PASS (10) | **290/290** | 1 — structural ceiling |
| **V-39** | PASS (10) | PASS (10) | **290/290** | 2 |
| V-36 | PARTIAL (5) | PARTIAL (5) | 280/290 | 3 |
| V-38 | PARTIAL (5) | PARTIAL (5) | 280/290 | 4 |
| V-37 | PARTIAL (5) | PARTIAL (5) | 280/290 | 5 |

**All essential criteria (C-01–C-05): PASS across all variations.**

**Tiebreak V-40 > V-39:** V-40 adds a Citation Architecture preamble + `CITATION ARCHITECTURE DECLARED` meta-artifact that front-loads all four artifact definitions and exact-copy requirements in one table before Phase 1, plus explicit "Do not write 'Phase X.' Write the artifact name." prohibitions at every consumer. V-39 achieves 290/290 via distributed per-phase instructions — the minimum-overhead path.

**Tiebreak among 280 variations:** V-36 > V-38 > V-37. V-36 closes Phase 2 → Phase 5(2) (structural persistence is the causal core of the kill-barrier). V-38 closes Phase 6 Part B → Phase 7 (summary-level citation, fewer downstream consequences). V-37 strengthens an already-passing link without adding any new boundary artifact.

---

### Excellence Signals

1. **Named artifact pattern must propagate to every upstream citation source** — the R7 lesson (Phase 5(3) needs a named label) generalizes: every section that is itself cited downstream must emit a named artifact at its own output boundary. Retroactive naming cannot convert a paraphrase chain into a reference chain.

2. **Citation chain verifiability is binary** — V-36 and V-38 each close one gap and both score 280. A single description link requires content-equivalence judgment at that link; exact-copy is defeated. Either the entire chain is verifiable by label comparison or it is not.

3. **Citation Architecture preamble as single-read authority** — concentrating all four artifact definitions before Phase 1 reduces per-phase instructional drift across a 1500+ token output, where a Phase 2 instruction may be read 1000 tokens before Phase 5(2) is written.

---

```json
{"top_score": 290, "all_essential_pass": true, "new_patterns": ["Named artifact pattern must propagate to every upstream citation source -- any section cited downstream must emit a named artifact at its own boundary before any downstream cite is written", "Citation chain verifiability is binary -- a single description link makes the entire chain non-verifiable by label comparison regardless of how many other links use exact-copy", "Citation Architecture preamble concentrates all four artifact definitions and exact-copy requirements into one table read before Phase 1, providing a single structural authority that per-phase instructions reference rather than restate"]}
```
 boundaries satisfied; Phase 6 Part B still produces prose
cited by Phase 7 without a named artifact.

**C-29 analysis:**
- Phase 4 -> Phase 1: "Cite Phase 1 by reference -- the SCORING INFRASTRUCTURE DECLARED there is the named source" -> exact-copy
- Phase 5(2) -> Phase 2: "cite the PERSONA INVENTORY DECLARED source... A structural persistence claim that references Phase 2 content without naming the PERSONA INVENTORY DECLARED artifact is a paraphrase chain" -> exact-copy of artifact label
- AMEND(d) -> Phase 5(3): "copy the exact LEVER POINT label from Phase 5(3)" -> exact-copy
- Phase 7 -> Phase 6 Part B: No named artifact at Phase 6 Part B; instruction uses description ("Kill-barrier trajectory direction from Phase 6 Part B") -> cannot be exact-copy

**C-29: PARTIAL** -- three of four consumption sites require exact-copy; Phase 7 cannot
satisfy exact-copy because its upstream source (Phase 6 Part B) produced no named artifact.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01--C-05 (Essential) | 50/50 | PASS -- inherited V-35 |
| C-06--C-08 (Recommended) | 30/30 | PASS -- inherited V-35 |
| C-09--C-27 (Aspirational 1-19) | 190/190 | PASS -- inherited V-35 |
| C-28 | 5/10 | PARTIAL -- Phase 6 Part B has no named artifact |
| C-29 | 5/10 | PARTIAL -- Phase 7 uses description, not exact-copy |

**V-36 Total: 280/290**

---

#### V-37 -- C-29 Double-Specification at Production Site

**Single axis:** Adds forward-declaration of exact-copy requirement at Phase 5(3) immediately
after the LEVER POINT label, before the falsifiability test. AMEND(d) instruction strengthened
to "Character-for-character." Citation Chain Verification retains 4 fields (same as V-35).
No named artifact at Phase 2 or Phase 6 Part B.

**C-28 analysis:**
- Phase 1 boundary: PASS (inherited V-35)
- Phase 2 boundary: No "PERSONA INVENTORY DECLARED" artifact; completeness gate present but no named boundary statement -> PARTIAL at this link
- Phase 5(3) boundary: PASS (inherited V-35, strengthened with production-site forward-declaration)
- Phase 6 Part B boundary: No named artifact -> PARTIAL at this link

**C-28: PARTIAL** -- two of four boundaries have named artifacts. V-37 is the weakest R8
variation on C-28; it strengthens the LEVER POINT link but leaves Phase 2 and Phase 6 Part B
unresolved.

**C-29 analysis:**
- Phase 4 -> Phase 1: exact-copy (inherited V-35)
- Phase 5(2) -> Phase 2: No named artifact at Phase 2; instruction says "reference the relevant Phase 2 durability property by name" -- property-name citation, not artifact-label copy -> description chain
- AMEND(d) -> Phase 5(3): Forward-declaration at production ("Only the exact string above, character-for-character") + consumption ("Character-for-character. A paraphrase of the mechanism does not satisfy the exact-copy citation requirement") -> double-specified exact-copy
- Phase 7 -> Phase 6 Part B: No named artifact; description citation

**C-29: PARTIAL** -- V-37's contribution is strengthening the LEVER POINT link to
double-specification. This is the only variation that tests production-site C-29; the Phase
5(3) -> AMEND link is the most robustly specified of all R8 variations. But two other links
remain description-based due to missing C-28 artifacts.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01--C-05 (Essential) | 50/50 | PASS -- inherited V-35 |
| C-06--C-08 (Recommended) | 30/30 | PASS -- inherited V-35 |
| C-09--C-27 (Aspirational 1-19) | 190/190 | PASS -- inherited V-35 |
| C-28 | 5/10 | PARTIAL -- Phase 2 and Phase 6 Part B lack named artifacts |
| C-29 | 5/10 | PARTIAL -- two description links; LEVER POINT link double-specified but insufficient alone |

**V-37 Total: 280/290**

---

#### V-38 -- C-28 at Phase 6 Part B Boundary

**Single axis:** Adds "TRAJECTORY VERDICT: [direction]" as required named artifact at Phase 6
Part B completion. Phase 7 instruction requires exact-copy of this label. Citation Chain
Verification expands to 5 fields. Phase 2 unchanged from V-35 (no named artifact).

**C-28 analysis:**
- Phase 1 boundary: PASS (inherited V-35)
- Phase 2 boundary: No "PERSONA INVENTORY DECLARED" artifact -> PARTIAL at this link
- Phase 5(3) boundary: PASS (inherited V-35)
- Phase 6 Part B boundary: "TRAJECTORY VERDICT: [direction]" written on its own line -> PASS (V-38 adds)

**C-28: PARTIAL** -- three of four boundaries satisfied; Phase 2 still produces prose cited
by Phase 5(2) without a named artifact.

**C-29 analysis:**
- Phase 4 -> Phase 1: exact-copy
- Phase 5(2) -> Phase 2: No named artifact at Phase 2; instruction uses description ("reference the relevant Phase 2 durability property by name") -- not artifact-label copy
- AMEND(d) -> Phase 5(3): "copy the exact LEVER POINT label from Phase 5(3) -- confirmed in Citation Chain Verification step (3)" -> exact-copy
- Phase 7 -> Phase 6 Part B: "copy the exact TRAJECTORY VERDICT label from Phase 6 Part B (e.g., 'TRAJECTORY VERDICT: Worsening'). A Phase 7 that references 'Phase 6 Part B' without copying the exact label is a paraphrase chain" -> exact-copy

**C-29: PARTIAL** -- three of four consumption sites require exact-copy; Phase 5(2) cannot
satisfy exact-copy because Phase 2 has no named artifact. V-38 mirrors V-36 in structure but
closes the opposite single-axis gap.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01--C-05 (Essential) | 50/50 | PASS -- inherited V-35 |
| C-06--C-08 (Recommended) | 30/30 | PASS -- inherited V-35 |
| C-09--C-27 (Aspirational 1-19) | 190/190 | PASS -- inherited V-35 |
| C-28 | 5/10 | PARTIAL -- Phase 2 has no named artifact |
| C-29 | 5/10 | PARTIAL -- Phase 5(2) uses description, not exact-copy |

**V-38 Total: 280/290**

---

#### V-39 -- Full C-28 Propagation (All Four Boundaries)

**Combination axis:** V-36 + V-38 layered onto V-35. All four citation source boundaries now
produce named artifacts. Citation Chain Verification expands to 6 fields covering all four
source boundaries and their downstream consumers. Exact-copy instruction at all four
downstream consumers.

**C-28 analysis:**
- Phase 1 boundary: "SCORING INFRASTRUCTURE DECLARED" -> PASS
- Phase 2 boundary: "PERSONA INVENTORY DECLARED" -> PASS (V-36 contribution)
- Phase 5(3) boundary: "LEVER POINT: [label]" -> PASS
- Phase 6 Part B boundary: "TRAJECTORY VERDICT: [direction]" -> PASS (V-38 contribution)

All four boundaries produce named artifacts. **C-28: PASS.**

**C-29 analysis:**
- Phase 4 -> Phase 1: "Cite Phase 1 by reference -- the SCORING INFRASTRUCTURE DECLARED there is the named source" -> exact-copy
- Phase 5(2) -> Phase 2: "cite the PERSONA INVENTORY DECLARED source: reference the specific Durability property by its Phase 2 label. A structural persistence claim that does not name the PERSONA INVENTORY DECLARED artifact is a paraphrase chain, not a reference chain" -> exact-copy of artifact label
- AMEND(d) -> Phase 5(3): "copy the exact LEVER POINT label from Phase 5(3) -- confirmed in Citation Chain Verification step (5)" -> exact-copy
- Phase 7 -> Phase 6 Part B: "copy the exact TRAJECTORY VERDICT label from Phase 6 Part B (e.g., 'TRAJECTORY VERDICT: Worsening'). A Phase 7 that references 'Phase 6 Part B' without copying the exact label is a paraphrase chain" -> exact-copy

All four consumption sites require exact-copy. Chain integrity is checkable by string identity
at every link. **C-29: PASS.**

The 6-field Citation Chain Verification gate requires exact named text for all four artifact
boundaries before AMEND can be written. A model that silently paraphrases at any link will
fail the verification gate before AMEND is written.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01--C-05 (Essential) | 50/50 | PASS -- inherited V-35 |
| C-06--C-08 (Recommended) | 30/30 | PASS -- inherited V-35 |
| C-09--C-27 (Aspirational 1-19) | 190/190 | PASS -- inherited V-35 |
| C-28 | 10/10 | PASS -- all four boundaries have named artifacts |
| C-29 | 10/10 | PASS -- all four consumption sites require exact-copy |

**V-39 Total: 290/290**

---

#### V-40 -- Full Integration with Citation Architecture Preamble

**All axes:** V-39 base plus a "Citation Architecture" section before Phase 1. The preamble
front-loads all four named artifacts, all four downstream consumers, and all exact-copy
requirements in a single table. Closes with "CITATION ARCHITECTURE DECLARED" -- a fifth named
meta-artifact that subsequent boundary declarations reference as the structural authority.
Per-phase instructions reinforced with explicit anti-paraphrase prohibitions ("Do not write
'Phase X.' Write the artifact name.").

**C-28 analysis:**
- Phase 1 boundary: "SCORING INFRASTRUCTURE DECLARED" -> PASS
- Phase 2 boundary: "PERSONA INVENTORY DECLARED" -> PASS
- Phase 5(3) boundary: "LEVER POINT: [label]" -> PASS
- Phase 6 Part B boundary: "TRAJECTORY VERDICT: [direction]" -> PASS
- Meta-artifact: "CITATION ARCHITECTURE DECLARED" (preamble) -- fifth named artifact

All four mandatory boundaries produce named artifacts. **C-28: PASS.**

**C-29 analysis:**
- Phase 4 -> Phase 1: "Cite Phase 1 by copying the artifact name 'SCORING INFRASTRUCTURE DECLARED' (as declared in the Citation Architecture Phase 1 row). Do not write 'Phase 1.' Write the artifact name." -> explicit anti-paraphrase + exact-copy
- Phase 5(2) -> Phase 2: "cite the PERSONA INVENTORY DECLARED source (as declared in the Citation Architecture Phase 2 row): copy the artifact name... Do not write 'Phase 2.' Write 'PERSONA INVENTORY DECLARED.'" -> strongest exact-copy form
- AMEND(d) -> Phase 5(3): "copy the exact LEVER POINT label from Citation Chain Verification field (5) -- the same string declared in the Citation Architecture Phase 5(3) row. Character-for-character." -> dual-authority exact-copy
- Phase 7 -> Phase 6 Part B: "Do not write 'Phase 6 Part B.' Write the exact label." -> explicit anti-paraphrase

All four consumption sites require exact-copy with the strongest anti-paraphrase language of
any R8 variation. **C-29: PASS** (strongest implementation).

| Criterion | Score | Note |
|-----------|-------|------|
| C-01--C-05 (Essential) | 50/50 | PASS -- inherited V-35 |
| C-06--C-08 (Recommended) | 30/30 | PASS -- inherited V-35 |
| C-09--C-27 (Aspirational 1-19) | 190/190 | PASS -- inherited V-35 |
| C-28 | 10/10 | PASS -- all four boundaries named + meta-artifact |
| C-29 | 10/10 | PASS -- strongest: anti-paraphrase prohibition at every consumption site |

**V-40 Total: 290/290**

---

### Summary Table

| Variation | C-28 | C-29 | Score | Rank |
|-----------|------|------|-------|------|
| V-40 | PASS | PASS | 290/290 | 1 (structural ceiling) |
| V-39 | PASS | PASS | 290/290 | 2 |
| V-36 | PARTIAL | PARTIAL | 280/290 | 3 |
| V-38 | PARTIAL | PARTIAL | 280/290 | 4 |
| V-37 | PARTIAL | PARTIAL | 280/290 | 5 |

**Tiebreak among 280/290 variations:**
- V-36 closes Phase 2 -> Phase 5(2) (more analytically significant: structural persistence
  is the causal heart of the kill-barrier analysis).
- V-38 closes Phase 6 Part B -> Phase 7 (a summary-level citation; fewer downstream
  consequences if paraphrased).
- V-37 strengthens an already-passing link (Phase 5(3)) without adding any new boundary
  artifact; least additional coverage of the three.

**Tiebreak between 290/290 variations:**
- V-40 introduces a meta-artifact (CITATION ARCHITECTURE DECLARED), concentrates all four
  artifact definitions before Phase 1, and uses explicit "Do not write 'Phase X.'"
  anti-paraphrase prohibitions at every consumption site.
- V-39 achieves full compliance through distributed per-phase instructions without the
  preamble overhead. It is the minimum-overhead path to 290/290.

---

### Excellence Signals from V-39/V-40

**1. Named artifact pattern must propagate to every upstream citation source, not only Phase 1**
The R7 insight was that Phase 5(3) needed "LEVER POINT: [label]" as a named artifact. The R8
insight extends this: the same principle applies to Phase 2 (cited by Phase 5(2)) and Phase 6
Part B (cited by Phase 7). Any output section that is itself an upstream citation source must
emit a named artifact before any downstream cite is written. Retroactive naming (verification
table, AMEND description, downstream paraphrase) cannot satisfy this.

**2. Citation chain verifiability is binary**
V-36 and V-38 each close one gap and score 280/290. The result confirms C-28 and C-29 cannot
be partially satisfied: a chain with one description link still requires content-equivalence
judgment at that link, which defeats the purpose of the exact-copy requirement. Either the
entire chain is verifiable by label comparison or it is not.

**3. Citation Architecture preamble as single-read structural authority (V-40)**
V-39 achieves the same score as V-40 through distributed per-phase instructions. V-40's
contribution is drift reduction: concentrating all four artifact definitions in one table
before Phase 1 means the model reads the complete chain design once, as a unit, before any
analysis begins. For long outputs where Phase 2 instructions are read 1000+ tokens before
Phase 5(2) is written, the preamble may be more reliable than a per-phase instruction
encountered 1000 tokens earlier.

---

### R8 Findings

- **Single-axis variations (V-36, V-37, V-38) cannot close both C-28 and C-29.** Each closes
  one boundary gap or strengthens one existing link. Three of five R8 variations score 280/290.

- **C-28 and C-29 are structurally coupled.** A missing C-28 artifact at a boundary
  automatically makes C-29 PARTIAL at the same link (the consumption site cannot use exact-copy
  when the source has no label to copy). Closing C-28 at all four boundaries is a prerequisite
  for closing C-29.

- **V-37's production-site forward-declaration is a valid pattern but cannot create a missing
  artifact.** The forward-declaration at Phase 5(3) is the correct mechanism for production-
  side C-29 -- but V-37 applies it to a link that already satisfies C-29. V-37 demonstrates
  the pattern; V-39/V-40 apply it where it matters.

- **V-40 is the ceiling: Citation Architecture preamble + four boundary artifacts + anti-
  paraphrase prohibitions.** The meta-artifact "CITATION ARCHITECTURE DECLARED" serves as a
  structural authority that per-phase instructions reference rather than restate.

```json
{"top_score": 290, "all_essential_pass": true, "new_patterns": ["Named artifact pattern must propagate to every upstream citation source -- any section cited downstream must emit a named artifact at its own boundary before any downstream cite is written", "Citation chain verifiability is binary -- a single description link makes the entire chain non-verifiable by label comparison regardless of how many other links use exact-copy", "Citation Architecture preamble concentrates all four artifact definitions and exact-copy requirements into one table read before Phase 1, providing a single structural authority that per-phase instructions reference rather than restate"]}
```
