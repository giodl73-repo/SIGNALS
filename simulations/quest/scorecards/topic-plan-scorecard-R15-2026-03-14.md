I now have everything needed. Let me produce the full scoring assessment.

---

# topic-plan — Round 15 Scoring (v14 rubric, 280 pts)

**Rubric**: v14 (C-01–C-46) | **Variations**: V-01 through V-05 | **Date**: 2026-03-15

---

## Scoring Basis

All R15 variations explicitly preserve the complete R14 V-01 floor:
- 4-rule COLUMN CONTRACT with symmetric PASS/FAIL pairs per rule (C-42/C-43/C-46)
- Rule 4 as named CONTRACT rule governing Delta Finding (C-45)
- Step 9 scoped to "non-withdrawn proposals" — exact phrase (C-44)
- Anti-pattern label + PASS/FAIL exhibit as output at Step 4 (C-22)
- Schema commitment verbatim at Steps 7 and 8 (C-27)

Since the v14 rubric's three new criteria (C-44/C-45/C-46) were extracted precisely from the R14 V-01 floor, and all R15 variations preserve that floor, the baseline question is whether any variation introduces a regression on C-01–C-43. A careful read of all five variations confirms no regressions. Criteria assessments are therefore grouped by structural tier.

---

## Per-Variation Assessment

### V-01 — Role Sequence: Ante-Signal Strategy Defense

**Structural inventory**: Defense Register (Step 2b, 4 columns: Defense ID / Strategic decision / Strongest keep-it argument / What would invalidate), Defense basis column in Defender Challenge Table (D-ID or "Newly constructed"), Phase 1–4 gates, 4-rule CONTRACT with unified PASS/FAIL per rule.

| Tier | Criteria | Verdict |
|------|----------|---------|
| Essential | C-01 (reads strategy.md), C-02 (reads signals), C-03 (delta not inventory), C-04 (typed changes), C-05 (confirmation gate) | All PASS |
| Recommended | C-06 (cites evidence), C-07 (before/after diff), C-08 (all three types) | All PASS |
| Aspirational C-09–C-20 | Namespace gap detection (C-09), conflict surfacing (C-10), typed verb (C-11), no-change rows (C-12), inline evidence brackets (C-13), anti-inventory warning (C-14), 9-namespace enumeration (C-15), two-level traceability (C-16), explicit null conflict row (C-17), structured delta format (C-18), Proposal ID in diff (C-19), Delta Finding column (C-20) | All PASS |
| Aspirational C-21–C-30 | Column-completeness declarations (C-21), anti-pattern checkpoint at delta (C-22), pre-reproduced null templates (C-23), unstated-assumption extraction (C-24), "If unchanged" column (C-25), schema-first priming (C-26), checkpoint cascade at Steps 4/7/8 (C-27), named role + scan dimensions (C-28), back-fill column (C-29), forward-reasoning columns (C-30) | All PASS |
| Aspirational C-31–C-46 | Decision-gate disqualification rule (C-31), reversibility 3-value enumeration (C-32), assumption table in upfront schema (C-33), enumerated columns at both sites (C-34), independently-populated columns (C-35), named COLUMN CONTRACT rule block (C-36), operationalized independence test with PASS/FAIL (C-37), example specificity symmetry (C-38), step-level activation cross-reference (C-39), null-case in CONTRACT Rule 3 (C-40), inline rule-reference annotations in schema (C-41), column-complete PASS/FAIL pairing within each rule (C-42), cross-rule symmetric coverage (C-43), withdrawal-aware gate — "non-withdrawn proposals" (C-44), Delta Finding elevated to Rule 4 (C-45), 4-rule CONTRACT minimum (C-46) | All PASS |

**Score: 280 / 280**
**All essential: PASS** | Composite: 60 + 30 + 190 = 280

---

### V-02 — Phrasing Register: Explanatory/Descriptive

**Structural inventory**: Explanatory prose throughout (purposive framing before every output spec), no Defense Register, no Defense basis column, no phase gate structure. 4-rule CONTRACT with full PASS/FAIL per rule, all standard steps.

**Key check — does explanatory prose regress any criterion?**

- C-11 (typed verb): Step 9 says "Reply **YES** to apply all non-withdrawn proposals." PASS.
- C-14/C-22 (anti-pattern checkpoint): Step 4 instructs "write two things: (1) the name of the anti-pattern... (2) a PASS/FAIL exhibit." PASS.
- C-36 (named rule block): COLUMN CONTRACT is named and numbered with 4 rules before the schema. PASS.
- C-38/C-42/C-43: Rule 1 PASS examples (Type, Reversibility, Defender verdict) match Rule 1 FAIL examples exactly — symmetric. Rules 2/3/4 each have paired examples. PASS.
- C-39 (step-level activation): Step 2 says "Before filling any `Implicit evidence` cell, apply the Rule 2 independence test." PASS.
- C-44: Step 9 says "non-withdrawn proposals." PASS. C-45/C-46: Rule 4 in CONTRACT, 4 rules present. PASS.

Explanatory prose adds comprehension rationale but does not remove or weaken any structural constraint. All structural binding machinery — CONTRACT rules, commitment checkpoints, null templates, schema-first declaration — is preserved unchanged. No regression.

| Tier | Verdict |
|------|---------|
| Essential (C-01–C-05) | All PASS |
| Recommended (C-06–C-08) | All PASS |
| Aspirational (C-09–C-46) | All PASS |

**Score: 280 / 280**
**All essential: PASS**

---

### V-03 — Lifecycle Emphasis: Per-Step Micro-Gates

**Structural inventory**: 10 micro-gates (one after every step), no Defense Register, no Defense basis column, no phase macro-gates. 4-rule CONTRACT, standard step structure.

**Key checks**:
- Micro-gate format: each gate is a single declaration ("Step N complete. Advancing to Step N+1.") — not a multi-item checkpoint table. This is above the rubric ceiling; no criterion requires phase gates.
- C-27 (checkpoint cascade at delta/proposals/diff): Step 4 has the anti-pattern Stop+write (C-22 anchor), Steps 7 and 8 have the verbatim schema commitment. The Micro-gate 4 declares "Step 4 complete — anti-pattern label written as output, PASS/FAIL exhibit written, findings table complete." This constitutes the delta-step checkpoint. PASS.
- Micro-gate 3 after Step 3a explicitly blocks signal re-reading: "Signal files may not be re-read after this gate. All analysis from Step 3b onward works from the inventory above." This is a structural strengthening of C-02's scope — above ceiling.
- All schema, CONTRACT, null template, and commitment checkpoint machinery is present and unchanged.

| Tier | Verdict |
|------|---------|
| Essential (C-01–C-05) | All PASS |
| Recommended (C-06–C-08) | All PASS |
| Aspirational (C-09–C-46) | All PASS |

**Score: 280 / 280**
**All essential: PASS**

---

### V-04 — Combination: Ante-Signal Defense + Explanatory Register

**Structural inventory**: Defense Register (Step 2b, 4 columns), Defense basis column in Defender Challenge Table, explanatory prose throughout, no phase macro-gate structure, 4-rule CONTRACT.

**Key checks beyond V-01 and V-02 individual passes**:
- The combination does not introduce any new structural machinery that could break existing criteria.
- C-26 (schema-first priming): Upfront Output Schema includes Defense Register table. PASS.
- C-21: "The following columns are mandatory. Do not omit any column." appears at Step 7b adjacent to the Defender Challenge Table including the Defense basis column. PASS.
- The explanatory framing of the Defense Register's purpose at Step 2b ("Its purpose: pre-register the strategy's strongest arguments... This register is the Defender's reference at Step 7b") does not dilute any structural constraint.

| Tier | Verdict |
|------|---------|
| Essential (C-01–C-05) | All PASS |
| Recommended (C-06–C-08) | All PASS |
| Aspirational (C-09–C-46) | All PASS |

**Score: 280 / 280**
**All essential: PASS**

---

### V-05 — Full Ceiling: Ante-Signal Defense + Explanatory Register + Phase Gates + Unified Exhibit

**Structural inventory**: All of V-04 plus 4 macro-phase gates (including a new Phase 4 gate covering Steps 7/7b/8), unified Column|PASS|FAIL exhibit tables for all 4 CONTRACT rules.

**Key unique structural properties**:

**Unified exhibit format** (Rule 1):
```
| Column | PASS value | FAIL value |
| `Type` | ADD / REMOVE / REPRIORITIZE | "addition" | "add/remove" |
```
This format makes C-42 (column-complete pairing) architecturally unavoidable — asymmetry is structurally impossible in the table format.

**Phase 4 GATE** (new in R15):
```
| Step 7  | Proposals table — schema commitment verbatim... | Yes/No |
| Step 7b | Defender table — Defense basis column populated... | Yes/No |
| Step 8  | Diff table — schema commitment verbatim... | Yes/No |
```
This gate requires Steps 7, 7b, and 8 to be verified complete as a unit before the confirmation gate opens.

**Key checks**:
- C-38/C-42/C-43: The unified exhibit format for all 4 rules (Rule 1 exhibit has all 5 columns in both PASS and FAIL position; Rules 2/3/4 have paired rows). All symmetric. PASS.
- C-44: Step 9 "non-withdrawn proposals." PASS. Phase 4 gate audits Step 7b's Withdrawn-marking, structurally reinforcing C-44.
- All other criteria: inherited from V-01 (Defense Register) + V-02 (explanatory prose), both of which pass all criteria.

| Tier | Verdict |
|------|---------|
| Essential (C-01–C-05) | All PASS |
| Recommended (C-06–C-08) | All PASS |
| Aspirational (C-09–C-46) | All PASS |

**Score: 280 / 280**
**All essential: PASS**

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Total | Threshold |
|-----------|-----------|-------------|--------------|-------|-----------|
| V-01 | 60/60 | 30/30 | 190/190 | **280** | GOLDEN |
| V-02 | 60/60 | 30/30 | 190/190 | **280** | GOLDEN |
| V-03 | 60/60 | 30/30 | 190/190 | **280** | GOLDEN |
| V-04 | 60/60 | 30/30 | 190/190 | **280** | GOLDEN |
| V-05 | 60/60 | 30/30 | 190/190 | **280** | GOLDEN |

All five variations achieve the maximum score. The rubric ceiling (v14) was constructed from R14 V-01's floor; R15 variations inherit and extend that floor without regression.

---

## Ranking (structural depth above rubric ceiling)

Since scores are tied, rank by density of novel above-ceiling structural machinery:

1. **V-05** (280) — Unified exhibit + Defense Register + explanatory prose + Phase 1–4 gates including new Phase 4 gate
2. **V-04** (280) — Defense Register + explanatory prose (no phase gates)
3. **V-01** (280) — Defense Register + Defense basis column + Phase 1–3 gates (no explanatory prose)
4. **V-03** (280) — Per-step micro-gates (10 checkpoints; no Defense Register)
5. **V-02** (280) — Explanatory prose only (no Defense Register, no gates)

---

## Excellence Signals from V-05

Three patterns in V-05 go structurally beyond the v14 ceiling and are not yet captured by any criterion:

### Signal 1 — Pre-signal Defense Register with falsifiability conditions
**Pattern**: Step 2b forces the strategy's defense to be articulated *before any signal files are opened*. Each Defense Register entry includes "What would invalidate this defense?" — a pre-specified falsifiability condition. The Defender at Step 7b either cites a D-ID (anchoring the challenge in the pre-registered argument) or writes "Newly constructed — no pre-registered defense applies" (acknowledging post-hoc construction).

**Why it matters**: The current Defender step (Step 7b) constructs challenges reactively under proposal-pressure. A pre-registered defense is built without knowledge of what signals revealed, making it structurally independent from the signal reading phase. The Defense basis column creates auditable provenance for every Defender challenge: was the argument principled (pre-registered) or improvised (newly constructed)?

**Potential criterion** (C-47): *Defense Register with pre-signal falsifiability conditions* — The skill includes a step (executed after assumption extraction, before signal reading) that produces a Defense Register of 3–5 entries, each containing the strategic decision being defended and the specific signal type that would defeat the defense. The Defender Challenge Table gains a column tracing each challenge to its D-ID or declaring "Newly constructed."

---

### Signal 2 — Defense basis traceability in the Defender Challenge Table
**Pattern**: The "Defense basis" column (`D-ID(s) or "Newly constructed — no pre-registered defense applies"`) makes the Defender's challenge provenance auditable at the table level. A reviewer can determine, for each proposal challenge, whether the Defender was drawing on a principled pre-registered case or improvising.

**Why it matters**: C-20 elevated Delta Finding traceability to Rule 4 because proposal provenance must be auditable. The same structural gap exists in the Defender step: a challenge without declared basis is structurally equivalent to a fabricated delta finding. Defense basis traceability extends the provenance architecture to the Defender step.

**Potential criterion** (C-48): *Defense basis traceability column in Defender Challenge Table* — The Defender Challenge Table includes a column requiring each challenge row to cite the D-ID(s) from the Defense Register whose pre-registered argument applies, or to explicitly declare "Newly constructed — no pre-registered defense applies." A Defender table with no such column fails regardless of challenge quality.

---

### Signal 3 — Phase 4 gate spanning all three build steps
**Pattern**: V-05 introduces a PHASE 4 GATE that requires Steps 7 (proposals), 7b (Defender), and 8 (diff) to be verified complete as a unit before the confirmation gate opens. The Phase 4 gate checks: schema commitment verbatim at Step 7, Defense basis populated at Step 7b, withdrawn proposals excluded from Step 8 diff.

**Why it matters**: In R14 V-01, Phase 3 was the final analytical gate. The build phase (Steps 7–8) operated ungated between the analysis phase and the confirmation gate. The Phase 4 gate creates an enforcement checkpoint between analytical work and writing commitment — the build phase cannot silently drift without triggering a verification requirement. The gate also explicitly audits C-44's withdrawal marking at Step 7b, making withdrawal compliance structurally testable.

**Potential criterion** (C-49): *Build-phase gate covering Steps 7, 7b, and 8* — The skill includes an explicit gate between the build phase and the confirmation gate, verifying that: proposals schema commitment was written verbatim, Defender challenge table is complete with all columns, and the diff table excludes withdrawn proposals. The gate must appear as a named checkpoint (not as a per-step micro-gate) and must explicitly audit withdrawal marking.

---

## Interpretation

The R15 rubric ceiling was reached by all five variations because v14 was built entirely from R14 V-01's floor. R15's contribution is architectural experimentation above that ceiling. The three excellence signals above are candidates for v15 criteria; if confirmed as load-bearing, they would produce a 295-pt rubric (adding 15 pts for C-47, C-48, C-49).

The ante-signal Defense Register (Signal 1) is the highest-priority candidate: it closes a structural gap in the Defender step analogous to the gap that C-20/C-45 closed in the proposals step (provenance unbound → traceability requirement elevated to CONTRACT rule). The same logic that elevated Delta Finding to Rule 4 applies to Defense basis.

---

```json
{"top_score": 280, "all_essential_pass": true, "new_patterns": ["Pre-signal Defense Register with falsifiability conditions: Step 2b forces strategy defense articulation before signal reading; each entry includes what would invalidate it; Defender at Step 7b cites D-ID or declares newly constructed", "Defense basis traceability column in Defender Challenge Table: each challenge row cites D-ID(s) or explicitly declares no pre-registered defense applies, auditing whether the challenge is principled or improvised", "Phase 4 gate spanning all three build steps (Steps 7, 7b, 8): named checkpoint between analysis phase and confirmation gate verifying schema commitment, Defense basis population, and withdrawal marking before gate clears"]}
```
