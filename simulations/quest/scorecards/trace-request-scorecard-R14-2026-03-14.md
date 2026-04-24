Now I have everything I need to score R14. Let me evaluate all five variations.

---

# trace-request Rubric v13 — Round 14 Scorecard

**Scale:** 240 pts (Essential 60 + Recommended 30 + Aspirational 150)
**Golden threshold:** all 4 essential PASS AND composite ≥ 80% (192/240)

---

## Scoring Basis

All variations carry forward identical structure for:
- **Essential tier (C-01–C-04):** no variation modifies these surfaces — all PASS for all runs
- **Recommended tier:** no variation modifies these surfaces — all PASS for all runs
- **Aspirational C-08–C-36 (prior criteria):** all stable and unmodified — PASS for all runs

All R14 variations preserve:
- VT-N: "..." quoted format + TOKEN-COUNT → **C-34 PASS** for all
- Row-Verdict column + CHECK RESULT summary → **C-35 PASS** for all
- C-34 + C-35 simultaneously → **C-36 PASS** for all

The sole differentiating criterion in R14 is **C-37** (Checker algorithm declaration — 5 pts).

**Baseline (C-37 excluded):** 235/240 per variation. C-37 determines whether each variation achieves 235 or 240.

---

## C-37 Test Conditions

All four must hold simultaneously for PASS:
1. CHECKER ALGORITHM block present in Step 8 Header
2. Block appears immediately after TOKEN-COUNT (no intervening content)
3. Declares MATCH-RULE, HALT-RULE, OUTPUT-RULE as named machine-greppable tokens
4. Algorithm declaration is structurally independent of VT-N lines (interpretable from label names alone without reading any VT-N value)

---

## Per-Variation Scoring

### V-01 — Role Sequence · Algorithm Pre-Declaration Contract

**C-37 mechanism:** Algorithm-Declarant produces CHECKER ALGORITHM block at Step A (before Step 0); Step 8 Header reproduces it verbatim.

| C-37 condition | Evidence | Result |
|---|---|---|
| Block present in Step 8 Header | Template shows CHECKER ALGORITHM as a named section in Step 8 Header; GATE-8H: "TOKEN-COUNT must be immediately followed by CHECKER ALGORITHM" | PASS |
| Immediately after TOKEN-COUNT | Template sequence is explicit: TOKEN-COUNT → CHECKER ALGORITHM → MATCH-RULE/HALT-RULE/OUTPUT-RULE; GATE-8H: "No content may appear between TOKEN-COUNT and CHECKER ALGORITHM" | PASS |
| Named machine-greppable tokens | GATE-A enforces: "A combined single-sentence description does not close. Missing any of MATCH-RULE / HALT-RULE / OUTPUT-RULE does not close." Canonical form examples provided (e.g., `MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in this header`) | PASS |
| Independent of VT-N lines | Fill guidance: canonical forms do not reference VT-N values to interpret predicate logic; algorithm phrases are self-contained | PASS |

**Two-phase enforcement analysis:** GATE-A enforces correct production at Step A; GATE-8H enforces verbatim reproduction at Step 8. Same three tokens appear at two independent structural checkpoints. Paraphrase risk is mitigated by canonical form examples that pre-form machine-greppable phrases.

**C-37: PASS**

| Tier | Score |
|---|---|
| Essential (C-01–C-04) | 60/60 |
| Recommended | 30/30 |
| Aspirational C-08–C-36 | 145/145 |
| **C-37** | **5/5** |
| **Total** | **240/240 = 100%** |

**Golden threshold:** PASS

---

### V-02 — Output Format · Pre-Printed CHECKER ALGORITHM Skeleton

**C-37 mechanism:** CHECKER ALGORITHM skeleton pre-printed as three mandatory fill-in fields immediately after TOKEN-COUNT in Step 8 Header template.

| C-37 condition | Evidence | Result |
|---|---|---|
| Block present in Step 8 Header | Skeleton pre-printed in template; model cannot produce visibly complete Step 8 Header without filling all three slots | PASS |
| Immediately after TOKEN-COUNT | Template shows TOKEN-COUNT → CHECKER ALGORITHM in that exact position; GATE-8H: "Content between TOKEN-COUNT and CHECKER ALGORITHM does not close" | PASS |
| Named machine-greppable tokens | Fill guidance: "MATCH-RULE states when Match? = Y. It must be parseable by `grep "MATCH-RULE:"` without reading surrounding text." Same for HALT-RULE and OUTPUT-RULE. GATE-8H: "A prose description in place of a machine-greppable phrase does not close" | PASS |
| Independent of VT-N lines | Explicitly stated: "None of the three fields may depend on reading VT-N lines to interpret the predicate" | PASS |

**Single-stage enforcement note:** No pre-declaration phase (unlike V-01/V-03/V-04). Relies entirely on fill guidance + GATE-8H to enforce machine-greppable phrases. The `grep`-parseable requirement is explicitly spelled out per token, which mitigates the prose-fill risk but provides less pre-commitment than multi-stage mechanisms.

**C-37: PASS**

| Tier | Score |
|---|---|
| Essential (C-01–C-04) | 60/60 |
| Recommended | 30/30 |
| Aspirational C-08–C-36 | 145/145 |
| **C-37** | **5/5** |
| **Total** | **240/240 = 100%** |

**Golden threshold:** PASS

---

### V-03 — Lifecycle Emphasis · ALGORITHM-CONTRACT Phase Gate

**C-37 mechanism:** Phase P-2 (ALGORITHM-CONTRACT) gates Phase P-3 (SCOPE-VERIFICATION) entry. P-2 artifact = CHECKER ALGORITHM block. Step 8 Header in P-3 carries P-2 artifact immediately after TOKEN-COUNT.

| C-37 condition | Evidence | Result |
|---|---|---|
| Block present in Step 8 Header | Phase P-3 gate condition: "Step 8 Header (VT-N schema + TOKEN-COUNT + CHECKER ALGORITHM)"; carry instruction: "carry the Phase P-2 CHECKER ALGORITHM block immediately after TOKEN-COUNT" | PASS |
| Immediately after TOKEN-COUNT | Carry instruction + GATE-8H: "Step 8 Header does not close unless CHECKER ALGORITHM appears immediately after TOKEN-COUNT with all three tokens present" | PASS |
| Named machine-greppable tokens | GATE-P2: "Phase P-2 does not close without all three named tokens. Algorithm logic expressed as prose does not close. A single combined statement does not close." Fill guidance: "Must be greppable by `^  MATCH-RULE:`" etc. | PASS |
| Independent of VT-N lines | P-2 fill guidance: "None of the three fields depends on VT-N values to interpret the predicate logic" | PASS |

**Phase gate enforcement note:** P-2 → P-3 gate creates a hard artifact checkpoint before Step 8 begins. The carry instruction uses "carry" language which is slightly weaker than V-01/V-04's verbatim reproduction contract — but GATE-8H compensates by explicitly testing position and completeness.

**C-37: PASS**

| Tier | Score |
|---|---|
| Essential (C-01–C-04) | 60/60 |
| Recommended | 30/30 |
| Aspirational C-08–C-36 | 145/145 |
| **C-37** | **5/5** |
| **Total** | **240/240 = 100%** |

**Golden threshold:** PASS

---

### V-04 — Role Sequence + Lifecycle Emphasis · Scope-Verifier Role Entry Contract

**C-37 mechanism:** The Scope-Verifier role entry contract IS the CHECKER ALGORITHM declaration. GATE-ENTRY + GATE-8H double-enforce. Role handoff triggers algorithm production; Phase P-3 cannot begin until GATE-ENTRY closes.

| C-37 condition | Evidence | Result |
|---|---|---|
| Block present in Step 8 Header | Role entry contract template pre-prints CHECKER ALGORITHM with three fill slots; Step 8 Header has "carry role entry CHECKER ALGORITHM block" instruction with same template; GATE-ENTRY: "Phase P-3 DOES NOT BEGIN until this entry artifact is complete" | PASS |
| Immediately after TOKEN-COUNT | Step 8 Header template: TOKEN-COUNT → CHECKER ALGORITHM in sequence; GATE-8H: "No content between TOKEN-COUNT and CHECKER ALGORITHM. All three tokens required." | PASS |
| Named machine-greppable tokens | GATE-ENTRY: "Prose description of scope checking does not close"; GATE-8H: "Prose does not close. Role entry paraphrase does not close." Both gates independently require machine-greppable tokens | PASS |
| Independent of VT-N lines | Role entry guidance: "No field depends on reading VT-N values to interpret its predicate logic" | PASS |

**Double-enforcement property:** GATE-ENTRY fires at role entry (before Steps 4–7). GATE-8H fires at Step 8 Header. The algorithm token set must satisfy two independent structural checkpoints at different positions in the trace — a consistency constraint: role entry paraphrase fails GATE-8H, and Step 8 Header prose fails GATE-8H independently of GATE-ENTRY. The algorithm is the definitional condition for the Scope-Verifier role to exist.

**C-37: PASS**

| Tier | Score |
|---|---|
| Essential (C-01–C-04) | 60/60 |
| Recommended | 30/30 |
| Aspirational C-08–C-36 | 145/145 |
| **C-37** | **5/5** |
| **Total** | **240/240 = 100%** |

**Golden threshold:** PASS

**Excellence signal (V-04 ES-1):** Role entry contract as algorithm declaration — the Scope-Verifier role cannot begin its work without having declared its algorithm. Algorithm production is not a downstream requirement of the role but the condition for role existence. This binds algorithm declaration to role handoff as a single structural event, preventing the R13 failure mode (algorithm logic deferred to Step 8b prose) by making the algorithm a required precondition rather than a header annotation.

---

### V-05 — Output Format + Phrasing Register + Inertia Framing

**C-37 mechanism:** Pre-printed skeleton (output format) + declarative register framing + Status-Quo Reference motivating the CHECKER ALGORITHM block. Step 8 description explicitly names which token drives each computation.

| C-37 condition | Evidence | Result |
|---|---|---|
| Block present in Step 8 Header | Pre-printed skeleton in Step 8 Header template; Status-Quo Reference section motivates production; Step 8 intro prose: "This trace produces that block" | PASS |
| Immediately after TOKEN-COUNT | Template: TOKEN-COUNT → CHECKER ALGORITHM in sequence; GATE-8H: "Step 8 Header is incomplete if TOKEN-COUNT is not immediately followed by CHECKER ALGORITHM ... or if the block appears anywhere other than the Step 8 Header section" | PASS |
| Named machine-greppable tokens | Fill guidance per token: "one machine-greppable phrase encoding Match? = Y condition"; GATE-8H: "if any token value is a prose paragraph rather than a machine-greppable phrase" | PASS |
| Independent of VT-N lines | Explicitly stated in Step 8 Header description: "The CHECKER ALGORITHM block is structurally independent of VT-N values: its three token phrases are interpretable from the label names alone without reading any VT-N line" | PASS |

**Backward traceability property:** Step 8c table prose explicitly names which CHECKER ALGORITHM token drives each cell computation: "Match? is computed from the MATCH-RULE. Row-Verdict is set from the HALT-RULE. CHECK RESULT is computed from the OUTPUT-RULE." This creates a named link from Step 8c execution back to Step 8 Header algorithm tokens — a testable traceability property not present in V-01 through V-04.

**Inertia risk note:** The Status-Quo Reference section expands prompt length. GATE-8H addresses the risk that the block might appear in prose sections but not the Step 8 Header: "if the block appears anywhere other than the Step 8 Header section" — this explicitly anticipates and blocks the failure mode.

**C-37: PASS**

| Tier | Score |
|---|---|
| Essential (C-01–C-04) | 60/60 |
| Recommended | 30/30 |
| Aspirational C-08–C-36 | 145/145 |
| **C-37** | **5/5** |
| **Total** | **240/240 = 100%** |

**Golden threshold:** PASS

**Excellence signal (V-05 ES-1):** Backward execution traceability — Step 8c prose names the CHECKER ALGORITHM token that drives each computation. Match? is not just binary (Y/N) — its computation is attributed to MATCH-RULE; Row-Verdict is attributed to HALT-RULE; CHECK RESULT is attributed to OUTPUT-RULE. Each execution result is traceable to a named algorithm token without reading prose.

---

## Summary Table

| Variation | C-34 | C-35 | C-36 | C-37 | Score | % | Golden |
|---|---|---|---|---|---|---|---|
| V-01 (Role Sequence) | PASS | PASS | PASS | PASS | 240/240 | 100% | PASS |
| V-02 (Output Format) | PASS | PASS | PASS | PASS | 240/240 | 100% | PASS |
| V-03 (Lifecycle) | PASS | PASS | PASS | PASS | 240/240 | 100% | PASS |
| V-04 (Role + Lifecycle) | PASS | PASS | PASS | PASS | 240/240 | 100% | PASS |
| V-05 (Format + Register + Inertia) | PASS | PASS | PASS | PASS | 240/240 | 100% | PASS |

**Ranking:** All five tie at 240/240 = 100%. Differentiated by excellence signal quality.

**Excellence signal tier:**
- **Tier A** (V-04, V-01): Structural double-enforcement with distinct checkpoints at different trace phases
- **Tier B** (V-05): Backward execution traceability introduces a C-38-relevant pattern
- **Tier C** (V-03): Phase gate enforcement, strong but single carry pathway
- **Tier D** (V-02): Skeleton-only, no pre-declaration phase; fills role but weakest structural coupling

---

## Excellence Signals

### ES-1 (V-04) — Algorithm declaration as role entry contract

The Scope-Verifier role cannot accept the role handoff from Platform Expert without producing the CHECKER ALGORITHM block as its entry artifact. The algorithm is not a requirement downstream of role entry — it is the structural pre-condition for role entry itself. This prevents the R13 failure pattern (algorithm deferred to Step 8b prose or embedded as a single combined sentence) by making algorithm production occur before boundary traversal begins, not during Step 8 authorship. GATE-ENTRY and GATE-8H are independent checkpoints: satisfying GATE-ENTRY at role entry and GATE-8H at Step 8 Header creates a consistency requirement that the same machine-greppable tokens appear at both positions.

### ES-2 (V-01) — Two-phase declaration-carry consistency contract

Algorithm declared at Step A with explicit canonical form examples + GATE-A enforcement; algorithm reproduced verbatim at Step 8 Header with carry instruction + GATE-8H enforcement. The same three machine-greppable token phrases appear at two structural positions in the trace. GATE-A prevents loose Step A formation (no combined sentences, no missing tokens) and GATE-8H prevents carry drift (no paraphrase, no reference without reproduction). The two-phase structure makes algorithm consistency verifiable: token values in Step 8 Header should exactly match Step A declaration, creating a structural consistency check property as a C-38 surface.

### ES-3 (V-05) — Backward execution traceability from Step 8c to CHECKER ALGORITHM

Step 8c table prose explicitly names which CHECKER ALGORITHM token drives each cell computation: Match? ← MATCH-RULE, Row-Verdict ← HALT-RULE, CHECK RESULT ← OUTPUT-RULE. Each execution result has a named algorithm token as its source. This closes the declaration-execution gap: the algorithm is declared in Step 8 Header, and its execution is attributed by token name in Step 8c. A checker can verify not only that the algorithm block is present (C-37) but that each Step 8c computation references the correct token — execution attribution as a C-38-eligible property.

---

## C-38 Design Surfaces Opened

**From ES-1 (V-04) — Algorithm-role binding:** If V-04 produces consistent evidence across rounds that the Scope-Verifier role entry contract reliably generates CHECKER ALGORITHM blocks with stable machine-greppable phrases across variation axes, C-38 specification becomes: "The scope-verification role's entry artifact is the CHECKER ALGORITHM block; role presence in the output implies algorithm presence; role handoff without algorithm production is a structural gate failure." Requires multi-round stability evidence from V-04 before freezing.

**From ES-2 (V-01) — Declaration-carry consistency:** If V-01 produces consistent evidence that Step A tokens carry verbatim to Step 8 Header (no paraphrase drift), C-38 specification becomes: "The CHECKER ALGORITHM token values in Step 8 Header exactly match the declared values at Step A (or Phase P-2 artifact); algorithm declaration consistency is a verifiable structural property; any drift between declaration and header is a consistency violation detectable without semantic reading."

**From ES-3 (V-05) — Execution attribution:** If V-05 produces consistent evidence that the Step 8c attribution language ("Match? is computed from the MATCH-RULE") appears reliably across variation axes, C-38 specification becomes: "Each Step 8c computation (Match?, Row-Verdict, CHECK RESULT) carries a named reference to the CHECKER ALGORITHM token that produces it; execution attribution is a machine-readable property of the Step 8c table prose."

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Role entry as algorithm contract: the scope-verification role entry artifact IS the CHECKER ALGORITHM block — algorithm declaration is not downstream of role entry but is the pre-condition for role entry itself; GATE-ENTRY and GATE-8H create independent checkpoints that require the same machine-greppable token set at two structural positions, making consistency between role declaration and Step 8 Header verifiable (V-04)", "Two-phase declaration-carry consistency: algorithm declared at Step A with canonical form examples + GATE-A enforcement, reproduced verbatim at Step 8 Header with carry instruction + GATE-8H enforcement — same three tokens appear at two independent structural checkpoints; paraphrase drift between Step A and Step 8 Header becomes a detectable consistency violation (V-01)", "Backward execution traceability: Step 8c table prose explicitly names the CHECKER ALGORITHM token that drives each cell computation (Match? from MATCH-RULE, Row-Verdict from HALT-RULE, CHECK RESULT from OUTPUT-RULE) — each execution result has a named algorithm source, closing the declaration-execution gap and creating per-cell algorithm attribution as a C-38-eligible structural property (V-05)"]}
```
