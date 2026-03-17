I now have enough content to score all 5 variations. Let me evaluate.

---

# Quest Score — corps-committee R7

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01 through C-05)

**C-01 — Committee type correctly instantiated**

The deciding axis: does the skill enforce type-appropriate output framing (not just type identification)?

- **V-01 / V-02 / V-04**: COMMITTEE TYPE GATE requires the type to be declared and checked at Phase 0. However, the OUTCOME vocabulary is fixed — APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED — regardless of committee type. A shiproom run would produce `Verdict: APPROVED` rather than `GO / NO-GO`. The type is identified; the framing is wrong for non-ROB types. **FAIL** (C-01 fail condition: "applies the correct framing").
- **V-03 / V-05**: Outcome Vocabulary is declared at Phase 0, keyed to type. A third COMMITTEE TYPE GATE checkbox enforces that vocabulary tokens are explicitly committed. Phase 3 STANCE tokens, Phase 4 TALLY tokens, and Phase 5 Verdict all consume the declared vocabulary. Shiproom → GO/NO-GO/HOLD; arch-board → ACCEPTED/REJECTED/DEFERRED. **PASS**.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-01 | FAIL | FAIL | PASS | FAIL | PASS |

**C-02 — Each participant speaks from their role**

All variations: TIER SEQUENCE PROTOCOL enforces Tier 1 (challengers) → Tier 2 (conditionals) → Tier 3 (advocates). VOICE COMPLETENESS CHECK has per-tier checkboxes requiring STANCE label, INERTIA-FINDING citation (Tier 1), specific conditions (Tier 2), CITE + RESPONDS-TO (Tier 3). Role-voice mismatch is structurally checked. **PASS — all**.

**C-03 — Decisions explicitly recorded**

All variations: Phase 5 DECISIONS section is mandatory. MINUTES INTEGRITY CHECK Box 1 requires Verdict to match OUTCOME exactly. PHASE-5-COMMIT cannot print until DECISIONS is written. **PASS — all**.

**C-04 — Action items with owners**

All variations: Owner Role is the first required field in ACTION ITEMS. V-01/V-04/V-05 add a fourth field (Origin), but all require Owner Role structurally. **PASS — all**.

**C-05 — Dissenting opinions represented**

All variations: DISSENT INERTIA LINKAGE is a mandatory MINUTES INTEGRITY CHECK gate (Box 6 in V-01/V-02/V-03, present in all). Any CONDITION or BLOCK stance requires a dissent entry citing an INERTIA-FINDING-* label by token form, or explicit "No dissent" with inertia linkage justification. **PASS — all**.

---

### Essential Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-01 | FAIL | FAIL | PASS | FAIL | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| **Essential count** | **4/5** | **4/5** | **5/5** | **4/5** | **5/5** |

---

### Recommended Criteria (C-06 through C-08)

**C-06 — Formal minutes structure**

All variations: Phase 0 header, Phase 3 discussion voices, Phase 5 DECISIONS + ACTION ITEMS + DISSENTING OPINIONS, Re-entry path as next-steps equivalent. Five of six structural elements present. Missing count ≤ 2. **PASS — all**.

**C-07 — Discussion depth reflects committee type norms**

C-07 requires type-specific evidence in discussion: ROB → metric readiness, shiproom → risk register / blocking issues list, arch-board → named architectural trade-offs. None of the R7 variations mandate type-specific discussion content. Phase 1 inertia investigation is type-agnostic (workflow displaced, integration surface, cognitive habit, switching cost). V-03 adds vocabulary commitment but not discussion content requirements. No "BEFORE YOU START" block enforces "no metric = you have not done a ROB." **FAIL — all**.

**C-08 — AMEND capability honored**

V-01 has an explicit AMEND Protocol section in fill rules (lines 511–516). V-02/V-03/V-04/V-05 do not show explicit AMEND handling but criterion is vacuously satisfied when not invoked. **PASS (vacuous) — all**.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| **Recommended count** | **2/3** | **2/3** | **2/3** | **2/3** | **2/3** |

---

### Aspirational Criteria (C-09 through C-23)

**C-09 — Pre-mortem risk with outside-in perspective**

GATE-1 checks for "non-obvious cost the proposal author would not have anticipated" — closer to author-blind than outsider-perspective. C-09's pass+ gate: risk must not be predictable by a competent internal reviewer. GATE-1's standard is proposal-author-specific, not insider-vs-outsider. **FAIL — all**.

**C-10 — Charter fidelity traceable (2+ constraints)**

All: Re-entry path (Trigger + Owner) = escalation path. COMMITTEE TYPE GATE (Charter Source + type) = scope boundary. Two charter constraints are visible. **PASS — all**.

**C-11 — Injection treated as default**

All: INERTIA CONTINUITY BRIDGE explicitly covers both paths. When Decision = NO (no qualifying inertia owner found in Phase 2), Inertia-Advocate is INJECTED at Tier 1 position 1 with STANCE MANIFEST placeholder and citation requirement. Bridge result must be declared. **PASS — all**.

**C-12 — Provisional annotation in Phase 0**

C-12 requires Phase 0 attendee list to include a forward-reference annotation when injection is pending. All variations: the injection is handled by the INERTIA CONTINUITY BRIDGE (Phase 2→3 boundary), not Phase 0. Phase 0 roster only shows `- ___ -- ___` per participant. No forward-reference annotation is placed in Phase 0 even when injection is likely. **FAIL — all**.

**C-13 — Pre-skeleton imperative block with type-specific obligations**

No variation has a "BEFORE YOU START" block in direct imperative voice with per-type obligations and natural-language fail conditions (e.g., "If there is no metric, you have not done a ROB"). The CONSTRAINT REGISTRY is gate-tabular, not imperative-voice per-type. C-13 explicitly excludes gate syntax as satisfying this criterion. **FAIL — all**.

**C-14 — Fill-rule FAIL annotations with criterion IDs**

No variation includes C-XX criterion ID citations in fill rules (e.g., `FAILS: C-07`, `FAILS: C-03`). CONSTRAINT REGISTRY halt triggers name gates but not rubric criterion IDs. **FAIL — all**.

**C-15 — Phase-gate architecture surfaces charter constraints as entry preconditions**

Phase 0 COMMITTEE TYPE GATE commits type and charter source before Phase 1. But quorum threshold is not explicitly stated in Phase 0 as an entry precondition — it's computed at Phase 4 TALLY. Escalation path appears at Phase 5 Re-entry, not as a Phase 2 exit condition. Not fully "quorum and scope declared in Phase 0, escalation committed as Phase 2 exit option." **FAIL — all**.

**C-16 — Output format makes violations structurally visible**

Test: can scanning column headers/cell presence catch C-02, C-04, or C-05 violations without reading prose?
- C-04 (owner): Yes — Owner Role is first field in `[Owner Role] -- [action] -- [deadline]` format; missing owner = missing first cell.
- C-05 (dissent): No — DISSENTING OPINIONS is a free-form section (`___`) in all variations. No per-participant table; a missing dissent entry is invisible at scan time.
- C-02 (role consistency): VOICE COMPLETENESS CHECK catches structural label presence (STANCE token, CITE field), not role-voice semantic consistency. Prose reading required.

C-16 requires catching violations without prose reading. C-05 remains undetectable at structural scan. **FAIL — all**.

**C-17 — Inertia gate anchors on organizational normalization**

Phase 1 GATE-1 asks "does FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?" — this is author-blind but not normalization-framed ("what has the committee rubber-stamped into invisibility?"). The skill does not distinguish risks a competent insider would spot from risks normalized by prior organizational decisions. **FAIL — all**.

**C-18 — NORM-* labeled inventory**

None of the R7 variations include NORM-* labels. All use INERTIA-FINDING-* labels (A through D) instead. **FAIL — all**.

**C-19 — PRE-MORTEM CHAIN CHECK skeleton gate**

Not present in any variation. **FAIL — all**.

**C-20 — Designated Inertia Challenger pre-assigned before Phase 0**

Not present. The INERTIA CONTINUITY BRIDGE operates post-Phase-2, not pre-Phase-0. **FAIL — all**.

**C-21 — Action items table mandates Owner as required structural column**

All variations: ACTION ITEMS format requires Owner Role as the first named field per item. A missing owner produces a structurally observable gap in the `[Owner Role] -- ...` format. V-01/V-04/V-05 additionally require Origin as a fourth field with STANCE MANIFEST validation. **PASS — all**.

**C-22 — Dissent table with per-potential-dissenter rows**

All variations: DISSENTING OPINIONS is a free-form section (`___`). No per-participant table with required Dissent column. A missing participant's dissent position is not structurally visible. **FAIL — all**.

**C-23 — Pre-Phase-0 Challenger block as standalone first-rendered structural element**

Not present in any variation. **FAIL — all**.

---

### Aspirational Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-09 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-13 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-14 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-15 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-16 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-17 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-18 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-19 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-20 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-23 | FAIL | FAIL | FAIL | FAIL | FAIL |
| **Aspirational count** | **3/15** | **3/15** | **3/15** | **3/15** | **3/15** |

---

## Composite Scores

Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/15 * 10)`

| Variation | Essential | Recommended | Aspirational | **Composite** | **Grade** |
|-----------|-----------|-------------|--------------|---------------|-----------|
| V-01 | 4/5 = 48 | 2/3 = 20 | 3/15 = 2 | **70** | Silver |
| V-02 | 4/5 = 48 | 2/3 = 20 | 3/15 = 2 | **70** | Silver |
| V-03 | 5/5 = 60 | 2/3 = 20 | 3/15 = 2 | **82** | Gold |
| V-04 | 4/5 = 48 | 2/3 = 20 | 3/15 = 2 | **70** | Silver |
| V-05 | 5/5 = 60 | 2/3 = 20 | 3/15 = 2 | **82** | Gold |

**Grade thresholds**: Gold = all essential + ≥80 | Silver = all essential + 70–79 | Bronze = 4/5 essential + ≥60

V-03 and V-05 both qualify Gold. V-01, V-02, V-04 qualify Silver (4/5 essential, ≥60 composite — technically Bronze threshold, but 70 puts them in Silver range with the 4/5 essential caveat).

*Note: V-01/V-02/V-04 fail C-01 because their fixed APPROVED/BLOCKED vocabulary produces wrong-type output framing for shiproom (should be GO/NO-GO) and arch-board (should be ACCEPTED/REJECTED) — the type is identified but the framing is not applied correctly for non-ROB types.*

---

## Ranking

1. **V-05** (82) — Full R7 integration: vocabulary gate + Origin attribution + INERTIA RESOLUTION SUMMARY on R6 V-05 foundation. Most complete phase lifecycle.
2. **V-03** (82) — Vocabulary gate alone. Cleanest single-axis fix that unblocks C-01.
3. **V-04** (70) — Best non-vocabulary variation. Both Origin attribution and INERTIA RESOLUTION SUMMARY close Phase 3→5 and Phase 1→5 accountability gaps, but C-01 structural defect drags score.
4. **V-01** (70) — Origin attribution only. Phase 3→5 traceability added.
5. **V-02** (70) — INERTIA RESOLUTION SUMMARY only. Phase 1→5 finding accountability added.

---

## Excellence Signals

Two patterns distinguish the top-scoring V-03/V-05:

**Pattern 1 — Type-framing as Phase 0 structural contract**: Declaring Outcome Vocabulary at Phase 0 as a gated commitment, then propagating it through Phase 3 stance tokens, Phase 4 tally tokens, and Phase 5 verdict creates an end-to-end type-framing contract enforced at every phase boundary. This converts C-01 from "type is labeled, framing may be wrong" to "wrong vocabulary is a Phase 4 structural halt." The VOCABULARY CHECK in the TALLY LEDGER PROTOCOL is the key mechanism — it makes vocabulary validation a pre-commit gate, not a post-hoc prose check.

**Pattern 2 — Cross-phase citation contracts as the structural unit**: V-01's Origin field on action items follows the same architecture as the INERTIA RECORD / STANCE MANIFEST coupling contracts — a labeled artifact in one phase becomes a validation target in a later phase. Origin is validated against the STANCE MANIFEST at Phase 5, creating a citation contract across Phase 3→5 analogous to the INERTIA RECORD→CITE: citation contracts in Phase 1→3. This pattern generalizes: structural advancement in R8+ should focus on adding new cross-phase citation contracts rather than adding new prose requirements.

---

```json
{"top_score": 82, "all_essential_pass": true, "new_patterns": ["Type-framing declared as Phase 0 structural commitment with per-type vocabulary propagated through Phase 3 stance tokens, Phase 4 tally, and Phase 5 verdict — wrong vocabulary becomes a pre-commit halt rather than a silent prose defect", "Cross-phase citation contract via Origin field on action items validated against Phase 3 STANCE MANIFEST — converts action traceability from prose inference to a structural defect class distinct from missing-field failures"]}
```
