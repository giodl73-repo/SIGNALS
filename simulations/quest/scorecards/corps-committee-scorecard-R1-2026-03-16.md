## corps-committee — R1 Scoring Report

---

### Per-Variation Evaluation

---

#### V-01 — Role Sequence

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | `Committee Type: ___` skeleton + explicit VALIDATE rule: "`Committee Type: ROB` is acceptable, `product review` fails." |
| C-02 | PASS | All 6 PHASE-N-COMMIT markers present with `ENFORCE: terminal position` on each. |
| C-03 | PASS | INERTIA RECORD has four labeled slots; fill rule specifies exact INERTIA INVARIANT text with both contract elements; `[one-phrase anchor]` in skeleton is overridden by fill rule "not bare labels, not placeholder text." |
| C-04 | PASS | DECISIONS/ACTION ITEMS/DISSENTING OPINIONS all in skeleton; fill rule: "Owner Role — specific action — deadline"; Owner/Trigger required if not APPROVED. |
| C-05 | **PARTIAL** | Bridge format is correct (YES/NO with injection logic). But no explicit guard against incorrect YES: "maps to switching-cost analysis" is vague — no "YES without qualifying participant is an incorrect affirmation and fails" statement. |
| C-06 | PASS | ORDERING RULE foregrounded ("READ BEFORE ANYTHING ELSE"), 3–4 vs 2 sentence rule, standalone STANCE: required, "all-APPROVE reopens Phase 2." |
| C-07 | PASS | Fill rule: "TALLY: count tokens in ## STANCE MANIFEST only. Do not re-parse Phase 3 prose." OUTCOME derivation rule present. |
| C-08 | **PARTIAL** | Charter Source in Phase 0, Phase 5 specificity guidance present, but no explicit "voices must be visibly distinct per role orientation" instruction. |

**Score: 60 + (0.5+1+1)/3×30 + 0.5×10 = 60 + 25 + 5 = 90**

---

#### V-02 — Lifecycle Emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 0 CONTRACT: "VALIDATE: Committee Type must use recognized label — `ROB` not `product review`." |
| C-02 | PASS | INPUT/OUTPUT/COMMIT block structure makes commit terminal nature maximally explicit; all 6 markers present. |
| C-03 | PASS | Phase 1 CONTRACT explicitly states: "INERTIA RECORD: one-phrase anchors — no bare labels, no `[one-phrase anchor]` placeholders." Both INERTIA INVARIANT elements: "(1) `sealed at PHASE-1-COMMIT` AND (2) `findings may not be added…` — Omitting either fails." |
| C-04 | PASS | Phase 5 CONTRACT: "all three fields on every row." Dissent handles BLOCK/CONDITION holders. |
| C-05 | **PARTIAL** | Bridge CONTRACT says "YES → name that participant" but no "YES without qualifying participant is an incorrect affirmation" warning. Failure mode is still present. |
| C-06 | PASS | Phase 3 CONTRACT: "standalone `STANCE:` line BEFORE any prose" + "at least one BLOCK or CONDITION; all-APPROVE → reopen Phase 2." |
| C-07 | PASS | Phase 4 CONTRACT: "TALLY: count tokens in ## STANCE MANIFEST only — do not re-parse Phase 3 prose" + OUTCOME RULE explicit. |
| C-08 | **PARTIAL** | Same as V-01 — charter loading present but no role-distinctness mandate. |

**Score: 60 + (0.5+1+1)/3×30 + 0.5×10 = 60 + 25 + 5 = 90**

---

#### V-03 — Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Fill rules: recognized label required; "product review" fails. Phase 0 skeleton standard. |
| C-02 | PASS | All 6 commits with ENFORCE markers; PHASE-1-COMMIT adds bidirectionality clause in skeleton body. |
| C-03 | PASS | **INERTIA INVARIANT fully hardcoded in skeleton**: `sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.` No placeholder — model reproducing skeleton already passes this clause. Fill rules: "Both contract elements required — omitting either fails." |
| C-04 | PASS | Fill rules: "Conditions: specific artifacts, recipients, deadlines." Owner (named role, not team) + Trigger (artifact + recipient + authority) when not APPROVED. Dissent cites INERTIA-FINDING-*. |
| C-05 | PASS | Bridge has **"Purpose" line** + explicit: "YES only if Tier 1/Tier 2 participant's orientation explicitly covers switching-cost or status-quo analysis — not assumed from general 'risk' orientation. YES without a qualifying participant is an incorrect affirmation and **fails**." Injection fully specified including STANCE MANIFEST appearance. |
| C-06 | PASS | Tier 1→2→3 order in fill rules. Standalone STANCE: required. At least one BLOCK/CONDITION required. |
| C-07 | PASS | "TALLY = count ## STANCE MANIFEST tokens. Do not re-parse Phase 3 prose." OUTCOME rule explicit. |
| C-08 | **PARTIAL** | Charter loading + Phase 5 artifact/authority specificity strong. Still no explicit "voices must reflect distinct charter orientation" instruction for role-shaped voices. |

**Score: 60 + (1+1+1)/3×30 + 0.5×10 = 60 + 30 + 5 = 95**

---

#### V-04 — Output Format + Phrasing Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Fill rule: recognized label required; "product review" fails. |
| C-02 | PASS | **Strongest C-02 guard**: "Nothing comes after it within that phase. Not a note, not a clarification, nothing. If you write content after a commit line, the simulation is invalid." |
| C-03 | PASS | Fill rules: both INERTIA INVARIANT elements required on same line; explicit failure condition for partial invariant. `[one-phrase anchor]` placeholder in skeleton overridden by fill rule. (INERTIA INVARIANT itself still `___` in skeleton — slight weakness vs V-03.) |
| C-04 | PASS | **ACTION ITEMS is a table** with Owner Role / Action / Deadline columns. Fill rule: "no empty cells." Structural format enforces all-three-fields compliance. |
| C-05 | PASS | Fill rule: "Check whether any Tier 1/Tier 2 participant's charter orientation explicitly covers switching-cost analysis or status-quo defense." Explicit: "Don't claim YES without a qualifying participant — that's an incorrect affirmation." Injection fully specified. |
| C-06 | PASS | "Run voices in Tier 1 → Tier 2 → Tier 3 order. Standalone `STANCE:` line before any prose — not embedded in text." At least one BLOCK/CONDITION required. |
| C-07 | PASS | **STANCE MANIFEST is a table** — structural format makes token counting explicit. Fill rule: "Count the stance tokens in the STANCE MANIFEST table. Don't re-read Phase 3 prose." Table-based counting is less error-prone than list-based. |
| C-08 | **PARTIAL** | Phase 5 artifact/authority specificity strong. Charter loading mentioned. Still no role-distinctness mandate for Phase 3 voices. |

**Score: 60 + (1+1+1)/3×30 + 0.5×10 = 60 + 30 + 5 = 95**

---

#### V-05 — Role Sequence + Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Fill rule: recognized label; fallback to Signal defaults. |
| C-02 | PASS | All 6 commits. PHASE-2-COMMIT: "challenger-first ordering confirmed." PHASE-3-COMMIT: "All voices complete in Tier 1 → Tier 2 → Tier 3 order." Double commit-level reinforcement of structure. |
| C-03 | PASS | **INERTIA INVARIANT fully hardcoded in skeleton** (same as V-03). PHASE-1-COMMIT includes bidirectionality clause in skeleton body. Fill rules require both elements. |
| C-04 | PASS | Fill rules: Owner (named role, not team), Trigger (artifact + recipient + authority), action item all-three-fields. Dissent with INERTIA-FINDING-* citation. |
| C-05 | PASS | **Strongest C-05 guard**: RULE 2 frames injection as DEFAULT ("Inertia-Advocate is a default Phase 3 participant"); YES requires named qualifying evidence. Bridge skeleton contains YES/NO conditions verbatim. Fill rules add motivation: "Incorrect YES is a harder failure than injection; it silences the inertia voice without surfacing it." |
| C-06 | PASS | **RULE 1 foregrounded** ("READ BEFORE ANYTHING ELSE"). PHASE-3-COMMIT explicitly confirms "All voices complete in Tier 1 → Tier 2 → Tier 3 order." Fill rules: "Complete all Tier 1 before any Tier 2; complete all Tier 2 before any Tier 3." Standalone STANCE: required; qualified token (`BLOCK (pending)`) explicitly named as failure. |
| C-07 | PASS | Fill rules: count STANCE MANIFEST tokens only, OUTCOME derivation rule. (List format — no structural table advantage vs V-04.) |
| C-08 | **PARTIAL** | Phase 5 artifact/authority specificity strong. RULE 2 framing makes inertia structurally salient. Still no explicit "voices must reflect distinct role orientation" mandate. |

**Score: 60 + (1+1+1)/3×30 + 0.5×10 = 60 + 30 + 5 = 95**

---

### Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | Score |
|-----------|------|------|------|------|------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | PARTIAL | **90** |
| V-02 | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | PARTIAL | **90** |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | **95** |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | **95** |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | **95** |

**Ranking: V-05 ≈ V-03 ≈ V-04 (95) > V-01 ≈ V-02 (90)**

V-05 edges V-03 and V-04 for the top position because:
- It foregrounds **both** RULE 1 (challenger order) and RULE 2 (inertia default) as co-equal pre-read contracts — the only variation that addresses two structural failure modes simultaneously at the prompt's opening
- RULE 2's motivation ("Incorrect YES silences the inertia voice") gives the model a reason to care, not just a rule to follow
- INERTIA INVARIANT hardcoded in skeleton (same advantage as V-03 for C-03 reliability)

V-04's table format for STANCE MANIFEST is the only structural advantage targeting C-07 specifically (vs all other variations' list format + instruction), making it the strongest single-axis improvement for tally reliability — but it doesn't combine axes. V-03's hardcoded INVARIANT is the strongest single-criterion structural guarantee.

The C-05 failure mode (incorrect YES without qualifying participant) is confirmed as the primary differentiator between 90 and 95. All variations passed all essential criteria.

---

### Excellence Signals from Top Variation (V-05)

1. **Hardcode invariant text in the skeleton** — writing `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.` directly in the skeleton (not `___`) makes a model reproducing the skeleton structurally pass C-03 before the fill step begins

2. **Frame injection as default, YES as the exception requiring evidence** — flipping the presumption from "decide YES or NO" to "default is injection; YES requires a named qualifying participant" eliminates the ambiguity that produces incorrect-YES affirmations

3. **Provide a consequence rationale alongside each rule** — "Incorrect YES is a harder failure than injection; it silences the inertia voice without surfacing it" gives the model motivation to evaluate the YES condition rigorously, not just satisfy the syntax

4. **Foreground multiple structural contracts as co-equal numbered RULES before any phase content** — RULE 1 (challenger-first) and RULE 2 (inertia default) established before the skeleton means both contracts are active constraints throughout execution, not fill-step reminders

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["Hardcode invariant text in skeleton rather than using placeholder — model reproducing skeleton already passes the criterion before the fill step", "Frame injection as the default with YES requiring named qualifying evidence — flips presumption to prevent incorrect-affirmation failures", "Provide consequence rationale alongside structural rules — explaining why a violation is worse than compliance increases adherence beyond rule-following", "Foreground multiple co-equal structural RULES before phase instructions — challenger-order and inertia-default established as simultaneous contracts, not sequential reminders"]}
```
