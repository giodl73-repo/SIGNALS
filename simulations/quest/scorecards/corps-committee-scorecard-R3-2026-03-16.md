Now I have everything needed. Let me analyze all five R3 variations against the full v3 rubric.

---

# corps-committee R3 — Scoring Report

## Rubric Reference

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (4) | C-01–C-04 | 60 |
| Recommended (3) | C-05–C-07 | 30 |
| Aspirational (7) | C-08–C-14 | 10 |

Each aspirational pass = 10/7 ≈ 1.43 pts. PARTIAL = 0.71 pts.
Golden = all essential PASS + composite ≥ 80.

---

## R3 Context

R3 variations target the three new v3 aspirational criteria surfaced from R2 V-05:

| Variation | Primary axis | New criteria targeted |
|-----------|-------------|----------------------|
| V-01 | CONSTRAINTS preamble | C-12 |
| V-02 | STOP-DISCARD-REWRITE gate | C-13 |
| V-03 | SYMMETRY DECLARATION block | C-14 |
| V-04 | CONSTRAINTS + REWRITE | C-12 + C-13 |
| V-05 | CONSTRAINTS + REWRITE + SYMMETRY | C-12 + C-13 + C-14 |

None of the R3 variations include ORIENTATION-LENS, ROLE-DISTINCTIVENESS RULE, Markdown tables, or injection-default framing (C-09, C-10, C-11). The aspirational ceiling is therefore lower than R2 V-05, but the goal is confirming the new v3 mechanisms in isolation and combination.

---

## Detailed Criterion-by-Criterion Evaluation

### V-01 — Pre-skeleton Rule Block

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 0 skeleton: `Committee Type: ___`, PHASE-0-COMMIT with terminal ENFORCE. Fill rules: ACCEPTABLE/FAILS examples for recognized types vs non-standard phrasing. |
| C-02 | PASS | All six PHASE-N-COMMIT markers present; each has `ENFORCE: terminal position` line in skeleton. Fill rules specify commit placement as terminal. |
| C-03 | PASS | Four INERTIA-FINDING-* slots in skeleton. Fill rules: "each entry carries a content anchor — not a bare label, not a placeholder." INERTIA INVARIANT fill: both elements (commit ref + modification prohibition) required, FAILS (a)/(b)/(c) named. |
| C-04 | PASS | DECISIONS/ACTION ITEMS/DISSENTING OPINIONS in skeleton. Fill rules: Owner + Trigger required if not APPROVED. Dissent cites INERTIA-FINDING-* label. Action items: three fields required. |
| C-05 | PASS | Bridge fill rules: "VALIDATE: YES declared only when a qualifying participant actually exists. YES without a qualifying participant fails — this is a distinct failure axis from structural absence." YES/NO both handled. |
| C-06 | PASS | Fill rules: "ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order." Standalone `STANCE:` required before prose. "VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2." STANCE MANIFEST required. |
| C-07 | PASS | "PRINT: TALLY line — count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose." OUTCOME derivation rule present. |
| C-08 | PARTIAL | Phase 0 fill specifies `[Role Name] -- [orientation]` format for participant list. Phase 5: "WRITE: dissent per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-* label, resolution path, named authority, concrete trigger." But no ORIENTATION-LENS at Phase 3 voice level; "WRITE: 2-4 sentences from their charter orientation" is structural only by instruction, not by constraint. |
| C-09 | MISS | No `ORIENTATION-LENS:` line in Phase 3 skeleton. No ROLE-DISTINCTIVENESS RULE. Generic "from their charter orientation" insufficient for non-transplantable voices. |
| C-10 | MISS | Skeleton STANCE MANIFEST: `[___] ___` list format. ACTION ITEMS: `___ -- ___ -- ___` list format. Fill rules use list format. No named-column tables. |
| C-11 | MISS | CONSTRAINTS rule 7 uses symmetric YES/NO framing: "States YES (with qualifying role identified) or NO (with Inertia-Advocate INJECTED first in Tier 1)." No injection-as-default declaration, no motivational rationale. |
| C-12 | PASS | `## CONSTRAINTS -- READ BEFORE PRINTING SKELETON` block containing 7 numbered rules precedes STEP 1 skeleton instruction. Rules cover distinct mechanisms: commit placement (R1), INERTIA RECORD sealing (R2), coupling integrity (R3), gate loop (R4), STANCE MANIFEST (R5), ACTION ITEMS (R6), bridge (R7). All framed as ENFORCE/VALIDATE imperatives. Exceeds minimum of two rules. |
| C-13 | MISS | Gate loop rule (CONSTRAINTS R4) says "write INVESTIGATION-ATTEMPT-(N+1) with entirely new findings." Fill rules: "IF NO: increment N; write INVESTIGATION-ATTEMPT-N label; rewrite all four findings; evaluate GATE-N; repeat until YES." Imperative language present but no explicit STOP/DISCARD signal, and the downstream section "## INERTIA RECORD" is not named as the gate target. C-13 requires both scope and downstream section named. |
| C-14 | PASS | CONSTRAINTS rule 3: "COUPLING INTEGRITY: PHASE-1-COMMIT carries a bidirectionality clause naming both coupling directions... The same bidirectionality contract applies identically to PHASE-3-COMMIT and ## STANCE MANIFEST." "The same bidirectionality contract applies identically" is an explicit symmetry annotation. Rule name "COUPLING INTEGRITY" is recognizable. Positioned in pre-skeleton block. This is a SIDE EFFECT of the C-12 mechanism — C-14 is co-earned without V-01 targeting it. |

**Aspirational pass count:** 0.5(C-08) + 0 + 0 + 0 + 1(C-12) + 0 + 1(C-14) = 2.5
**Score: 60 + 30 + (2.5/7 × 10) = 60 + 30 + 3.57 = 93.57**

---

### V-02 — Rewrite-before-Proceed Loop

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Standard Phase 0 skeleton. PHASE-0-COMMIT terminal with roles count. |
| C-02 | PASS | All six PHASE-N-COMMIT markers; terminal ENFORCE lines in skeleton. |
| C-03 | PASS | Four INERTIA-FINDING-* slots. Fill rules: "each entry carries a content anchor — not a bare label, not a placeholder." INERTIA INVARIANT: FAILS (a) commit ref present/prohibition absent, (b) neither element, (c) line absent entirely — all three axes named. |
| C-04 | PASS | All three Phase 5 sections. Fill rules: Verdict + Conditions + Re-entry (Owner + Trigger if not APPROVED). Action items: three fields. Dissent or explicit no-dissent. |
| C-05 | PASS | Bridge fill: "VALIDATE: YES only when qualifying participant actually exists. YES without qualification fails as a distinct axis from structural absence." |
| C-06 | PASS | Fill rules: tier order enforced, standalone STANCE required, at least one CONDITION or BLOCK. |
| C-07 | PASS | "PRINT: TALLY — count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose." |
| C-08 | PARTIAL | Phase 0: "PRINT: Agenda Item, Charter Source, Participants." No explicit orientation format requirement. Phase 3: "WRITE: 2-4 sentences per participant from their charter orientation" — same weak instruction as baseline. Phase 5 specificity: "Verdict, Conditions, Re-entry path." No named artifact or authority enforcement. Same PARTIAL as R2 V-02. |
| C-09 | MISS | No ORIENTATION-LENS. No ROLE-DISTINCTIVENESS RULE. |
| C-10 | MISS | Skeleton STANCE MANIFEST: `[___] ___` list. ACTION ITEMS: list. |
| C-11 | MISS | Bridge: standard `Inertia owner in tier sort: YES/NO` symmetric framing. No injection-as-default. No motivational rationale. |
| C-12 | MISS | No block before skeleton. STEP 1 is the first major section. REWRITE PROTOCOL appears in STEP 2 fill rules only. |
| C-13 | PASS | `*** REWRITE PROTOCOL ***` block in Phase 1 fill rules: "STOP. Do not proceed to ## INERTIA RECORD. Discard all four findings from the current attempt entirely. Write a new header: ### INVESTIGATION-ATTEMPT-[N+1]. Rewrite all four findings (A, B, C, D) from scratch — not revised, not extended: replaced." STOP signal explicit. Scope named: "all four findings." Downstream gate named: "## INERTIA RECORD." Imperative language throughout. All C-13 elements satisfied. |
| C-14 | MISS | Phase 1 fill: "PRINT: PHASE-1-COMMIT with bidirectionality clause naming both coupling directions." Phase 3 fill: "PRINT: PHASE-3-COMMIT with bidirectionality clause. Both directions required." Both clauses present in fill rules but not annotated as structurally equivalent. No pattern name ("COUPLING INTEGRITY SYMMETRY," "bidirectionality contract") links them. C-14 fails: Phase-3-COMMIT bidirectionality is present but unlabeled as identical in kind to Phase-1-COMMIT. |

**Aspirational pass count:** 0.5 + 0 + 0 + 0 + 0 + 1(C-13) + 0 = 1.5
**Score: 60 + 30 + (1.5/7 × 10) = 60 + 30 + 2.14 = 92.14**

---

### V-03 — Coupling Integrity Symmetry Declaration

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Standard Phase 0 skeleton with PHASE-0-COMMIT terminal. |
| C-02 | PASS | All six PHASE-N-COMMIT markers. PHASE-1-COMMIT and PHASE-3-COMMIT both contain bidirectionality clauses in skeleton. |
| C-03 | PASS | Four INERTIA-FINDING-* slots. Fill rules name FAILS (a)/(b)/(c) axes for INERTIA INVARIANT. Both elements required. |
| C-04 | PASS | All three Phase 5 sections. Action items: list format with three fields per row. Owner + Trigger required when not APPROVED. Dissent cites INERTIA-FINDING-* or explicit no-dissent. |
| C-05 | PASS | Bridge fill: "VALIDATE: YES only when qualifying participant actually exists. YES without a qualifying participant fails — this is a distinct failure axis from structural absence." |
| C-06 | PASS | Tier order enforced. Standalone STANCE required. At least one CONDITION or BLOCK. STANCE MANIFEST required. |
| C-07 | PASS | "COUNT tokens in ## STANCE MANIFEST. Do not re-parse Phase 3 prose." OUTCOME rule present. |
| C-08 | PARTIAL | Phase 0 fill: "PRINT: Agenda Item, Charter Source, Participants." No explicit orientation phrase format. Phase 3: "WRITE: 2-4 sentences per participant from their charter orientation." No structural forcing. SYMMETRY DECLARATION focuses on commit coupling, not voice distinctiveness. Phase 5: "WRITE: dissent... resolution path, named authority, concrete trigger" — better specificity. Partial credit for Phase 5 specificity instruction but voice distinctiveness unforced. |
| C-09 | MISS | No ORIENTATION-LENS. No ROLE-DISTINCTIVENESS RULE. |
| C-10 | MISS | STANCE MANIFEST: `[___] ___` list. ACTION ITEMS: list. SYMMETRY DECLARATION does not address table format. |
| C-11 | MISS | Bridge fill: "VALIDATE: YES only when qualifying participant exists. YES without qualification is a distinct failure axis." Standard YES/NO framing. No injection-as-default, no motivational rationale. |
| C-12 | MISS | No block before skeleton. SYMMETRY DECLARATION appears in STEP 2 (after skeleton). No numbered pre-skeleton rule block. |
| C-13 | MISS | Phase 1 fill: "IF NO: increment N; write new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; new GATE-N; repeat." Imperative rewrite instruction present but no STOP signal and downstream section ("## INERTIA RECORD") not named as the gate target. Fails C-13's named-scope-and-gate requirement. |
| C-14 | PASS | `## SYMMETRY DECLARATION -- READ BEFORE ANY PHASE FILL` explicitly defines COUPLING PAIR A (INERTIA RECORD ↔ PHASE-1-COMMIT) and COUPLING PAIR B (STANCE MANIFEST ↔ PHASE-3-COMMIT), asserts "both must be present" and "A partial implementation of either fails both." SYMMETRY CHECK block at end of skeleton lists three ticked checkboxes. Phase 3 fill: "PRINT: PHASE-3-COMMIT -- COUPLING PAIR B both directions required per SYMMETRY DECLARATION." Pattern names "COUPLING PAIR A/B" and "SYMMETRY DECLARATION" are recognizable. Positioned both in fill rules and referenced in skeleton. Strong C-14 implementation. |

**Aspirational pass count:** 0.5 + 0 + 0 + 0 + 0 + 0 + 1(C-14) = 1.5
**Score: 60 + 30 + (1.5/7 × 10) = 60 + 30 + 2.14 = 92.14**

---

### V-04 — Pre-skeleton Rule Block + Rewrite-before-Proceed Loop

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 0 skeleton standard. CONSTRAINTS rule covers terminal commit placement. PHASE-0-COMMIT terminal. |
| C-02 | PASS | All six PHASE-N-COMMIT markers. CONSTRAINTS rule 1: "Every PHASE-N-COMMIT is the terminal line of its phase." |
| C-03 | PASS | Four INERTIA-FINDING-* slots. CONSTRAINTS rule 2: "INERTIA INVARIANT must contain (a) 'sealed at PHASE-1-COMMIT' AND (b) the modification prohibition." Fill rules: ACCEPTABLE/FAILS examples. |
| C-04 | PASS | All three Phase 5 sections. Fill rules: Owner + Trigger required when not APPROVED. Action items: three fields. Dissent or no-dissent. |
| C-05 | PASS | CONSTRAINTS rule 7: "YES requires a qualifying participant named. YES without qualification is a distinct failure from structural absence." Bridge fill: validate YES with named participant; NO path injects Inertia-Advocate. |
| C-06 | PASS | Fill rules: tier order enforced. Standalone STANCE required. At least one CONDITION or BLOCK. All-APPROVE reopens Phase 2 (implied). |
| C-07 | PASS | "PRINT: TALLY — count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose." OUTCOME declared from TALLY. |
| C-08 | PARTIAL | CONSTRAINTS rule 3 addresses coupling integrity, not voice distinctiveness. Phase 0 fill: "PRINT: Committee Type ... Participants." No orientation phrase format. Phase 3: "WRITE: 2-4 sentences per participant from their charter orientation." Weak structural forcing same as baseline. Phase 5 specificity: dissent cites INERTIA-FINDING-* label, resolution path, named authority — good. Partial credit. |
| C-09 | MISS | No ORIENTATION-LENS. No ROLE-DISTINCTIVENESS RULE. |
| C-10 | MISS | STANCE MANIFEST skeleton: `[___] ___` list. ACTION ITEMS: `___ -- ___ -- ___` list. No tables. |
| C-11 | MISS | CONSTRAINTS rule 7 frames YES/NO symmetrically. No injection-as-default, no motivational rationale. |
| C-12 | PASS | `## CONSTRAINTS -- READ BEFORE PRINTING SKELETON` block with 7 numbered rules precedes skeleton. Rules cover commit placement, INERTIA sealing, coupling integrity, gate loop rewrite, STANCE MANIFEST, ACTION ITEMS, bridge. ENFORCE/VALIDATE framing throughout. |
| C-13 | PASS | `*** REWRITE PROTOCOL ***` in Phase 1 fill rules: "STOP immediately. Do not write ## INERTIA RECORD. Do not proceed past Phase 1. Discard all four findings from the current attempt entirely. They do not carry forward. Write: ### INVESTIGATION-ATTEMPT-[N+1]. Rewrite all four findings completely from scratch — different workflow, different surface, different team, different switching cost. Not revised. Not extended. Replaced." STOP explicit. Scope: "all four findings." Downstream gate: "## INERTIA RECORD" named. CONSTRAINTS rule 4 pre-activates this: "If a gate answers NO, halt and fully rewrite all four findings from scratch before proceeding." |
| C-14 | PASS | CONSTRAINTS rule 3: "COUPLING INTEGRITY: PHASE-1-COMMIT carries both coupling directions for INERTIA RECORD. PHASE-3-COMMIT carries both coupling directions for STANCE MANIFEST. One direction only fails. Both commits require this treatment." "Both commits require this treatment" is an explicit annotation that Phase-3-COMMIT mirrors Phase-1-COMMIT in kind. Pattern name "COUPLING INTEGRITY" is recognizable. Positioned in pre-skeleton rule block. PASS — same mechanism as V-01 rule 3. |

**Aspirational pass count:** 0.5(C-08) + 0 + 0 + 0 + 1(C-12) + 1(C-13) + 1(C-14) = 3.5
**Score: 60 + 30 + (3.5/7 × 10) = 60 + 30 + 5.0 = 95.0**

---

### V-05 — Full Integration (C-12 + C-13 + C-14)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 0 standard skeleton. CONSTRAINTS rule 1 covers terminal commits. PHASE-0-COMMIT terminal. |
| C-02 | PASS | All six PHASE-N-COMMIT markers. CONSTRAINTS rule 1 pre-activates commit placement across all phases. |
| C-03 | PASS | Four INERTIA-FINDING-* slots. CONSTRAINTS rule 2: both elements of INERTIA INVARIANT required. Fill rules name FAILS (a)/(b)/(c) axes. SYMMETRY DECLARATION references INERTIA RECORD coupling for PHASE-1-COMMIT. |
| C-04 | PASS | All three Phase 5 sections. Fill rules: Owner + Trigger required when not APPROVED; "Rewrite failing voices before proceeding to STANCE MANIFEST" pattern protects Phase 5 structural completeness downstream. Action items: three fields required. |
| C-05 | PASS | CONSTRAINTS rule 7: "YES requires a qualifying participant named. YES without a qualifying participant is a distinct failure from structural absence." Bridge fill: "YES -- qualifying participant: ___" in skeleton; NO path: "Inertia-Advocate INJECTED." |
| C-06 | PASS | Fill rules: tier order enforced. Standalone STANCE required. VALIDATE: at least one CONDITION or BLOCK. STANCE MANIFEST complete. |
| C-07 | PASS | "PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose." Table counting removes prose-reparse risk. |
| C-08 | PARTIAL | No ORIENTATION-LENS at Phase 3 voice level. Phase 3: "WRITE: 2-4 sentences per participant from their charter orientation." SYMMETRY DECLARATION improves commit integrity but does not address voice distinctiveness. Phase 5 fill: "specific objection citing INERTIA-FINDING-* label, resolution path, named authority, concrete trigger" — specificity instruction present. Partial credit for Phase 5 but voice forcing absent. |
| C-09 | MISS | No ORIENTATION-LENS. No ROLE-DISTINCTIVENESS RULE. V-05 does not inherit R2 V-05's orientation-anchoring mechanism. |
| C-10 | MISS | Skeleton STANCE MANIFEST: `[___] ___` list. ACTION ITEMS: `___ -- ___ -- ___` list. SYMMETRY CHECK is not a table for these sections. |
| C-11 | MISS | CONSTRAINTS rule 7 symmetric framing. Bridge skeleton shows INJECTED on NO path but does not frame NO as the default. No injection-as-default declaration, no motivational rationale. |
| C-12 | PASS | `## CONSTRAINTS -- READ BEFORE PRINTING SKELETON` block with 7 numbered rules before skeleton. CONSTRAINTS rule 3 explicitly references SYMMETRY DECLARATION: "see SYMMETRY DECLARATION in Step 2." All mechanisms primed before any phase content. |
| C-13 | PASS | `*** REWRITE PROTOCOL ***` in Phase 1 fill: "STOP immediately. Do not write ## INERTIA RECORD. Discard all four findings... Rewrite all four findings completely from scratch... Replaced. Write GATE-[N+1] and evaluate. If NO again — execute REWRITE PROTOCOL again from the top. Repeat until YES." STOP explicit. Scope: "all four findings." Gate target: "## INERTIA RECORD." Strongest C-13 implementation across all five variations. |
| C-14 | PASS | Triple-layered C-14 implementation: (1) CONSTRAINTS rule 3: "COUPLING INTEGRITY SYMMETRY: PHASE-1-COMMIT and PHASE-3-COMMIT each carry bilateral coupling clauses... Both commits must carry this treatment identically." Uses exact pattern name "COUPLING INTEGRITY SYMMETRY." (2) SYMMETRY DECLARATION in fill rules: COUPLING PAIR A and COUPLING PAIR B explicitly named with forward+reverse for each. SYMMETRY RULE: "satisfying Pair A and omitting Pair B fails coupling integrity." (3) SYMMETRY CHECK in skeleton: three ticked checkboxes gate Phase 4. Phase 3 fill: "PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION." Strongest C-14 implementation. |

**Aspirational pass count:** 0.5(C-08) + 0 + 0 + 0 + 1(C-12) + 1(C-13) + 1(C-14) = 3.5
**Score: 60 + 30 + (3.5/7 × 10) = 60 + 30 + 5.0 = 95.0**

---

## Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Score | Golden? |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|---------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PART | MISS | MISS | MISS | PASS | MISS | PASS | **93.57** | YES |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PART | MISS | MISS | MISS | MISS | PASS | MISS | **92.14** | YES |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PART | MISS | MISS | MISS | MISS | MISS | PASS | **92.14** | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PART | MISS | MISS | MISS | PASS | PASS | PASS | **95.0** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PART | MISS | MISS | MISS | PASS | PASS | PASS | **95.0** | YES |

**Ranking: V-04 = V-05 (95.0) > V-01 (93.57) > V-02 = V-03 (92.14)**

V-05 is designated top variation due to the stronger C-14 implementation (triple-layered: CONSTRAINTS + SYMMETRY DECLARATION + SYMMETRY CHECK skeleton gate vs V-04's single CONSTRAINTS rule). Both score identically because the rubric measures PASS/MISS, not implementation thoroughness.

---

## Key Findings

**All essential criteria pass across all five variations.** The base skeleton and phase structure are sound in all R3 prompts.

**All recommended criteria pass across all five variations.** C-05, C-06, C-07 are stable. This confirms the R2 foundation held through the R3 rewrites.

**C-09, C-10, C-11 are all MISS across R3 variations.** These mechanisms (ORIENTATION-LENS, table format, injection-default) were not included in any R3 variation. The R3 design was intentional: test the three new v3 criteria in isolation. The cost is a ceiling of 95.0 rather than 100. This is acceptable — the open target for R4 is combining C-12/C-13/C-14 with C-09/C-10/C-11.

**V-01 earns C-14 as a side effect of C-12.** The pre-skeleton CONSTRAINTS block that names bidirectionality for both PHASE-1-COMMIT and PHASE-3-COMMIT in the same rule naturally satisfies C-14's symmetry annotation requirement. This is the key finding from R3.

**C-13 requires explicit gate-target naming.** V-01 and V-03 both have imperative rewrite instructions ("rewrite all four findings") but MISS C-13 because neither names the downstream section ("## INERTIA RECORD") that the gate blocks. V-02/V-04/V-05 pass because they explicitly say "Do not proceed to ## INERTIA RECORD."

**Single-axis variations (V-02, V-03) underperform V-01.** V-01 earns two aspirational passes (C-12 + C-14) from one mechanism; V-02 and V-03 each earn one aspirational pass from their mechanism alone. C-12 + C-14 coupling makes V-01 the most efficient single-axis variation.

---

## Excellence Signals from V-04 / V-05

**1. C-12 + C-14 natural coupling — pre-skeleton CONSTRAINTS rule naming both commits earns both criteria simultaneously.** A rule that says "PHASE-1-COMMIT [bidirectionality]. PHASE-3-COMMIT [same]. Both commits require this treatment" satisfies C-14's symmetry annotation within the C-12 block. This means C-14 is free once C-12 is implemented correctly. Demonstrated by V-01 (which targeted only C-12 and co-earned C-14 without intending to).

**2. STOP-DISCARD gate-target naming is the critical element for C-13.** "Rewrite all four findings" without naming where execution stops is insufficient (V-01, V-03). "STOP. Do not proceed to ## INERTIA RECORD. Discard..." with the section named is the pass condition. The REWRITE PROTOCOL delimiter (`*** REWRITE PROTOCOL ***` ... `*** END REWRITE PROTOCOL ***`) plus the explicit named gate makes the correction path unambiguous.

**3. V-05 SYMMETRY CHECK in skeleton creates a hard visual gate.** Unlike V-03's SYMMETRY DECLARATION in fill rules only, V-05 embeds the three checkboxes in the skeleton itself between Phase 3 and Phase 4. The fill rules say "All three checkboxes must be ticked. Any unticked box halts Phase 4." This makes symmetry verification a structural gate rather than an advisory check — the model cannot procedurally proceed to Phase 4 without ticking the checkboxes.

---

## R3 Open Targets (for R4)

| Open target | What's needed |
|-------------|--------------|
| C-09 PASS | Add ORIENTATION-LENS + ROLE-DISTINCTIVENESS RULE from R2 V-04/V-05 to a V-05 base |
| C-10 PASS | Add Markdown tables for STANCE MANIFEST and ACTION ITEMS |
| C-11 PASS | Add injection-as-default framing + motivational rationale to CONSTRAINTS rule 7 |
| C-08 PASS | Flows from C-09 — ORIENTATION-LENS at Phase 3 elevates from PARTIAL to PASS |

A V-06 combining all R2 V-05 + R3 V-05 mechanisms should earn 100.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["C-12 and C-14 naturally couple — a pre-skeleton CONSTRAINTS block that names bidirectionality for both PHASE-1-COMMIT and PHASE-3-COMMIT in the same numbered rule simultaneously earns C-14 symmetry annotation as a side effect; C-14 is free once C-12 is implemented correctly", "C-13 requires explicit downstream gate naming — imperative rewrite language alone (rewrite all four findings) is insufficient; the pass condition requires explicitly naming the section blocked ('Do not proceed to ## INERTIA RECORD') so the correction path has a named gate target, not just a rewrite scope"]}
```
