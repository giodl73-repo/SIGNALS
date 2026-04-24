# mock-ns Round 14 Scoring — Rubric v13

## Shared Baseline

All five variations carry the complete R12 V-03 + R13 V-01 foundation. Before assessing C-36/C-37, I verify all prior criteria are preserved.

---

## Criterion Matrix

### Essential (C-01 – C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|-----------|------|------|------|------|------|------|
| C-01 Header block | PASS | PASS | PASS | PASS | PASS | [MOCK ARTIFACT -- NOT VERIFIED] + 5 fields present in all |
| C-02 Category correct | PASS | PASS | PASS | PASS | PASS | Category table preserved in S-2 across all |
| C-03 Golden structure | PASS | PASS | PASS | PASS | PASS | A-3 directs skill-specific body in all |
| C-04 Flag present/correct | PASS | PASS | PASS | PASS | PASS | Flag line in A-1 header block in all |
| C-05 Artifact path | PASS | PASS | PASS | PASS | PASS | `simulations/mock/{topic}-{namespace}-mock-{date}.md` in A-4 |

Essential: **5/5 all variations** = 60 pts

---

### Recommended (C-06 – C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|-----------|------|------|------|------|------|------|
| C-06 Default skill | PASS | PASS | PASS | PASS | PASS | Namespace default table with topic-plan as default preserved |
| C-07 Fidelity warning | PASS | PASS | PASS | PASS | PASS | All three category variants present + HIGH-STRUCTURE includes REAL-REQUIRED at Tier 2+ |
| C-08 Next-step line | PASS | PASS | PASS | PASS | PASS | A-5 present in all |

Recommended: **3/3 all variations** = 30 pts

---

### Aspirational (C-09 – C-37)

**C-09 through C-35** — all 27 pre-v13 criteria are preserved identically in every variation. Key spot checks:

| Criterion | Status (all) | Evidence |
|-----------|--------------|----------|
| C-09 Tier-conditional flag | PASS | Case 1 for critical + Tier 2+ in S-3 |
| C-10 TOPICS.md emit | PASS | Dedicated `> TOPICS.md:` line in S-1 |
| C-11 Flag as named step | PASS | S-3 dedicated step before A-1 |
| C-12 topic-status exclusion inline | PASS | Exclusion column in default table |
| C-13 Fidelity warning lead position | PASS | A-2 before any mock content, `---` delimiters |
| C-14 Dual-site immutability | PASS | Prohibition at both S-3 and A-1 |
| C-15 Exclusion column in table | PASS | Three-column table with Exclusion constraint column |
| C-16 Run-scoped prohibition | PASS | "anywhere in this run" at compute site |
| C-17 First rule at consumption site | PASS | First row of A-1 table is "First rule" |
| C-18 Named path class enumeration | PASS | S-3 Scope + Path classes rows enumerate all classes |
| C-19 Anti-displacement closure | PASS | A-1: "before any field…category lookup…formatting instruction, or any other" |
| C-20 Failure consequence at A-1 | PASS | "Failure conseq [A-1:FC]" row names mechanism + silent corruption |
| C-21 No-exemption affirmative closure | PASS | Affirmative closure + No-exemption rows in S-3 |
| C-22 Catch-all instruction clause | PASS | "or any other instruction in this step" in A-1 Anti-displacement |
| C-23 Failure consequence at S-3 | PASS | "Failure consequence" row names contamination + A-1 corruption |
| C-24 No-instruction-exempt closure | PASS | All-governed + No-exemption rows in A-1 |
| C-25 Guarantee-break framing | PASS | "Guarantee-break" row: "breaks the closure guarantee stated above" |
| C-26 Cross-site reference | PASS | "[A-1:FC] -- the Failure consequence row in step A-1" |
| C-27 Structural isolation | PASS | Tabular form: each claim is an independently scannable row |
| C-28 Navigation anchor | PASS | Step and row type named in cross-site reference |
| C-29 Bidirectional anchor | PASS | A-1 carries "[Mutual target of S-3:CS -- Cross-site reference row in S-3]" |
| C-30 Bracket token notation | PASS | [S-3:CS] / [A-1:FC] at both sites |
| C-31 Pre-chain preamble | PASS | P-0 dedicated step orients all tokens before S-3 |
| C-32 Preamble before computation | PASS | P-0 is a separate step before S-1; S-3 computation encountered only after P-0 |
| C-33 Structured token table | PASS | Abbreviation key + 5-column resolution table in P-0 |
| C-34 Lookup obligation | PASS | "required before writing any bracket-token row" + mandatory table use; two-phase requirement structurally prohibits memory bypass |
| C-35 Use-site navigation labels | PASS | "(P-0 table, row 1)" and "(P-0 table, row 2)" at both S-3 and A-1 |

---

**C-36 — Two-phase confirmation gate**

| Variation | Assessment | Evidence |
|-----------|------------|----------|
| V-01 | PASS | "Phase 1 -- Locate... Phase 2 -- Confirm: read Step + Row type cells; assert match. Confirmation is a prerequisite to writing the row." Both phases explicit, prerequisite framing. |
| V-02 | PASS | "Step 1 -- Locate... Step 2 -- Read Step/Row type cells; assert. DO NOT WRITE THE ROW until both pass. Confirmation is a prerequisite, not optional." Hard-stop framing reinforces Phase 2 as mandatory gate. |
| V-03 | PASS | Tabular Phase 1/Phase 2 form with "Required before" dependency column. Closing note: "An executor who recognizes a token without performing Phase 2 has not satisfied this protocol." Strongest anti-bypass statement of all five. |
| V-04 | PASS | P-0 two-phase gate identical to V-01. S-3 boundary checkpoint echoes requirement — references P-0, does not re-establish. Slight tension with "Do not re-establish in later steps" but checkpoint is a reference/reminder, not a new protocol definition. |
| V-05 | PASS | "Phase 1 -- Locate... Phase 2 -- Confirm... DO NOT WRITE THE ROW until Phase 2 passes. Confirmation is a prerequisite, not advisory." Adds inline confirmation record protocol — most demanding framing. |

C-36: **PASS all** — gate form passes in all five; V-03 adds explicit anti-bypass statement; V-02/V-05 add blocker language; V-04 adds boundary re-activation.

---

**C-37 — Confirmation echo at both use sites**

| Variation | S-3 site | A-1 site | Assessment |
|-----------|----------|----------|------------|
| V-01 | Row label "CONFIRMATION REQUIRED before writing this row (P-0 table, row 1)" precedes content | Same pattern "(P-0 table, row 2)" | PASS — trigger prefix before navigation label at both sites |
| V-02 | Same label + "DO NOT WRITE this row until P-0 gate passes" in content cell | Same pattern | PASS — blocker language in content cell reinforces trigger |
| V-03 | Same label structure + "apply Phase 1...Phase 2...per P-0 protocol" | Same | PASS — references P-0 protocol explicitly at use site |
| V-04 | Same as V-01 | Same as V-01 | PASS — use-site echo unchanged from V-01 |
| V-05 | Trigger label + "DO NOT WRITE until Phase 2 passes. Emit confirmation record." | Same + pre-filled record template | PASS — adds output obligation to the echo; confirmation record is in Cross-site ref row after CONFIRMATION REQUIRED row, so trigger precedes content |

C-37: **PASS all** — both sites carry the trigger in all variations; positioning precedes navigation label and row content.

---

## Composite Scores

```
Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/29 * 10)
```

| Variation | Essential (5/5) | Recommended (3/3) | Aspirational (29/29) | Composite |
|-----------|-----------------|-------------------|----------------------|-----------|
| V-01 | 60 | 30 | 10.00 | **100** |
| V-02 | 60 | 30 | 10.00 | **100** |
| V-03 | 60 | 30 | 10.00 | **100** |
| V-04 | 60 | 30 | 10.00 | **100** |
| V-05 | 60 | 30 | 10.00 | **100** |

All five variations achieve maximum composite score. The rubric denominator moves to 29 from this round. R14 is a **clean ceiling sweep** — all C-36/C-37 implementation forms satisfy both criteria.

---

## Ranking

Since all score 100, ranking is by **design quality for v14 seed value and reliability hypothesis**:

**Rank 1: V-05** (Full convergence + seeds C-38)
Combines V-01 two-phase prose + V-02 DO NOT WRITE blocker + inline confirmation record protocol. Makes Phase 2 externally observable via emitted trace. Most complete; seeds the next aspirational target.

**Rank 2: V-02** (Prerequisite-blocker language)
"DO NOT WRITE THE ROW until Phase 2 passes. Confirmation is a prerequisite, not an optional verification." Strongest single-axis constraint framing. Parallel to run-scoped immutability (C-16) over step-scoped prohibition.

**Rank 3: V-03** (Tabular phase protocol)
Table form with Phase/Action/Required-before columns makes dependency chain visible at a glance. Unique anti-bypass statement directly targets visual-recognition bypass at protocol level.

**Rank 4: V-04** (Boundary checkpoint)
P-0 two-phase + S-3 entry checkpoint for context-compacted runs. Addresses a real failure mode. Minor tension with "Do not re-establish" instruction, but checkpoint is a reference, not a re-establishment.

**Rank 5: V-01** (Numbered procedure)
Simplest and most direct. Clean Phase 1/Phase 2 numbering without additional framing. Serves as the reference implementation from R13 V-01.

---

## Excellence Signals — V-05

**Signal 1: Emitted confirmation record converts silent gate to auditable output.**
V-05 requires the executor to emit `[Confirmation: Phase 1 -- token located; Phase 2 -- Step=X, Row type=Y; match verified]` before writing each bracket-token row. A silent check satisfies C-36 but is unverifiable; an emitted record is verifiable by the same inspection that validates artifact path and header fields. Pre-filled templates in the skill body demonstrate exact output format at the point of use.

**Signal 2: DO NOT WRITE + Emit confirmation record fuses blocker and output obligation.**
Combining "DO NOT WRITE THE ROW until Phase 2 passes" with "Emit confirmation record" creates a two-signal enforcement point: the blocker prevents premature writing; the output obligation provides evidence that the gate was honored.

**Signal 3: V-03's tabular Required-before column makes Phase 1/Phase 2 dependency chain scannable.**
Expressing the two-phase gate as a table row with a "Required before" column (Phase 1 required before Phase 2; Phase 2 required before Writing the row) exposes the dependency chain as a first-class structural element — parallel to how C-33 upgraded token resolution from prose to table.

**Signal 4: V-03's anti-bypass statement explicitly closes the visual-recognition gap.**
"An executor who recognizes a token without performing Phase 2 has not satisfied this protocol" names the specific bypass scenario (recognition without semantic cell-read) in imperative form. This is more precise than a general memory-prohibition because it targets the exact cognitive shortcut C-36 was designed to block.

**Signal 5: V-04's S-3 boundary checkpoint addresses context-compaction distance decay.**
P-0 defines the protocol once; an executor entering S-3 from a long or compacted context may not have P-0 in active scope. The boundary checkpoint re-activates the gate at the exact step boundary where the first bracket-token row is encountered — without re-establishing the full protocol, just referencing it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inline confirmation record emitted before row content converts Phase 2 from silent assertion to externally observable protocol trace, making gate adherence verifiable as output rather than declarable as intent", "Tabular two-phase gate with Required-before dependency column makes Phase 1/Phase 2 ordering constraint independently scannable; explicit anti-bypass note closes visual-recognition shortcut at protocol level", "S-3 boundary checkpoint re-activates two-phase gate at compute-step entry point, addressing context-compaction failure mode where P-0 is not in active scope when the first bracket-token row is encountered"]}
```
