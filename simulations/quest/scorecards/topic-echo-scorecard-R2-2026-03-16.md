Scorecard written to `simulations/quest/scorecards/topic-echo-scorecard-R2-2026-03-16.md`.

---

**Round 2 summary:**

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | V-05 (PBI + Handle Ledger) | 100/110 | PASS |
| 2 | V-01 (Lifecycle Emphasis) | 97/110 | PASS |
| 3 | V-02 (Output Format) | 85/110 | PASS |
| 4 | V-04 (Role Sequence + Lifecycle) | 75/110 | FAIL |
| 5 | V-03 (Phrasing Register) | 72/110 | FAIL |

**Key finding:** V-05 wins because C-11 and C-12 are structurally non-competing. V-01's phase checkpoint and V-02's Handle Ledger operate at different lifecycle positions (Phase 0 vs. Phase 2) on different artifact types (prior beliefs vs. exit handles), so they compose without tradeoffs.

**V-04 and V-03 fail** on the same gap as previous rounds — C-02 (source traceability) and C-03 (design impact specificity) are not primary axes for either and fall to PARTIAL without explicit field definitions and negative specification.

**C-12 gap in V-01:** The portability test is the missing piece. V-01 enforces specificity (pass/fail example pair) but doesn't require a committed Handle Ledger or the explicit portability question. One targeted addition to V-01 would close this.
rtifact name or skill type...Traceable to one artifact, not 'the signals.'" |
| C-03 | **PASS** (12) | "Design impact: The specific component, flow, or decision that must change...One sentence. 'This affects the design' does not pass — name the thing." Negative specification present. |
| C-04 | **PASS** (12) | Phase 0 PBI + Phase 2 SURPRISE/CONFIRMATION gate makes summary content architecturally impossible. Confirmations are explicitly routed to `topic-story`. |
| C-05 | **PASS** (12) | Handle specificity requirement: "'API Complexity Surprise' applies to every investigation and fails. 'Competitors-Treated-Throttle-As-Solved' is falsifiable against this artifact set and passes." |
| C-06 | **PASS** (10) | PBI Reference field: "PB-NN — [the prior belief this finding overturns, verbatim or close summary]." PBI supplies the "expected" half structurally; cannot be post-hoc if PBI was frozen at Phase 0. |
| C-07 | **PASS** (10) | Phase 5 Forward Guidance: "If you are about to build X, the beliefs we held about Y (PB-NN) did not survive contact with Z — before you commit, verify ___. Must be derivable only from these surprises, not generic advice." Explicit addressee register. |
| C-08 | **PASS** (10) | Phase 4 Synthesis: "do two or more surprises overturn PBI entries in the same namespace or reveal the same gap...If the surprises are independent, say so explicitly." Absence of pattern also required to be named. |
| C-09 | **FAIL** (0) | No ranking step. Entries ordered by phase, not by design impact. |
| C-10 | **FAIL** (0) | No riskiest-surprise flagging mechanism. |
| C-11 | **PASS** (5) | Phase 0 produces PB-01 through PB-0N before Phase 1. Checkpoint: "PBI frozen at [N] entries: PB-01 through PB-0N." PBI locked; revisions prohibited. Each Phase 3 entry requires "PBI Reference: PB-NN" field. (a) discrete section ✓ (b) addressable by number ✓ (c) each entry cites identifier ✓. |
| C-12 | **PARTIAL** (2) | Handles are required to be investigation-specific with pass/fail example pair. No Handle Ledger committed before entries; portability test ("could a teammate cite the handle without re-reading the entry?") is not explicitly stated. Specificity bar is present; portability bar is absent. |

**Essential: 60/60 — ALL PASS**
**Recommended: 30/30**
**Aspirational: 7/20** (C-11 PASS + C-12 PARTIAL)
**Total: 97/110**
**Golden threshold: PASS** (all essential + composite ≥ 80)

---

## V-02 — Output Format (Handle Ledger)

**Axis:** Handle Ledger committed as the first section of the output artifact, before full entries are written; portability test applied per handle before commitment.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Step 2 prediction test is a structural exclusion gate. "Every entry...must pass the prediction test." Committed Handle Ledger titles enforce named-surprise identity. |
| C-02 | **PASS** (12) | Step 4 field: "Source signal: Specific artifact name or skill type. Traceable to one artifact, not 'the research' or 'the signals.'" Anti-generic attribution explicit. |
| C-03 | **PASS** (12) | Step 4 field: "Design impact: Specific component, flow, or decision affected. Must name something specific. 'This affects the design' or 'this changes things' do not pass." Negative specification present. |
| C-04 | **PASS** (12) | Step 2 gate filters confirmations before Handle Ledger is written. "It is not a summary. It is not a set of findings." Structural gate + explicit declaration. |
| C-05 | **PASS** (12) | Step 2 prediction test targets predictability from pre-investigation materials. Step 3 handle rules: "investigation-specific...cannot describe a finding that would appear in any investigation." |
| C-06 | **PASS** (10) | Step 4 field: "Prior assumption: What was expected before this signal. One sentence." Both halves explicitly required per entry. (Post-hoc risk remains — satisfies C-06 but not C-11.) |
| C-07 | **PARTIAL** (5) | Step 5 (Synthesis) referenced in heading but prompt body cut off. Institutional framing not confirmed in visible content; not a primary axis. |
| C-08 | **PARTIAL** (5) | Step 5 body absent. Cross-signal pattern identification not confirmed in visible content. |
| C-09 | **FAIL** (0) | Not present. |
| C-10 | **FAIL** (0) | Not present. |
| C-11 | **FAIL** (0) | No Phase 0 PBI. "Prior assumption" appears only within Step 4 entries — reconstructed during writing, not pre-committed. Satisfies C-06 but not C-11's minimum bar (no discrete PBI section, no addressable identifiers). |
| C-12 | **PASS** (5) | Handle Ledger is first section of artifact, committed before entries (Step 3). Portability test explicit: "If a teammate dropped this handle in a message with no further context, would the full team know exactly which surprise? If the answer is *no* or *maybe* — revise." Handles may be narrowed but not replaced during entry writing. Investigation-specific requirement enforced. |

**Essential: 60/60 — ALL PASS**
**Recommended: 20/30** (C-07, C-08 PARTIAL — Step 5 cut off)
**Aspirational: 5/20** (C-12 PASS)
**Total: 85/110**
**Golden threshold: PASS** (all essential + composite ≥ 80)

---

## V-03 — Phrasing Register (Analogy-Based)

**Scored from design description only.** Axis: "bet slip" analogy for C-11; "Slack citation test" analogy for C-12. Both criteria targeted via concrete analogy rather than structural phase separation.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Departure-register phrasing inherently requires named departures; the "bet slip" framing casts every entry as a departure from a prior commitment. |
| C-02 | **PARTIAL** (6) | Phrasing register doesn't structurally require artifact-level sourcing; "the investigation revealed" can coexist with vague attribution. Not a primary axis. |
| C-03 | **PARTIAL** (6) | Design impact specificity not a primary axis; no negative specification clause confirmed in design description. |
| C-04 | **PASS** (12) | "Bet slip" analogy frames the artifact as departure-only by construction — bets that paid out (confirmations) are not in a bet slip's notable section. Register enforces the exclusion. |
| C-05 | **PASS** (12) | "Slack citation test" enforces specificity: handle must be citable without context by the full team. Generic handles fail this test structurally. |
| C-06 | **PASS** (10) | "Bet slip" analogy is inherently both-halves: the bet = what was expected; the result = what was found. Counterfactual structure falls out from the analogy without a separate clause. |
| C-07 | **PARTIAL** (5) | Institutional framing not a primary axis; likely present as instruction but not structurally enforced via register choice. |
| C-08 | **PARTIAL** (5) | Synthesis/pattern step likely exists but not confirmed in design description as a primary axis. |
| C-09 | **FAIL** (0) | Not shown. |
| C-10 | **FAIL** (0) | Not shown. |
| C-11 | **PARTIAL** (2) | "Bet slip" analogy motivates pre-commitment (bets are placed before the game) but analogy-based enforcement is softer than structural phase separation. Numbered/addressable identifiers and per-entry citation requirement not confirmed — analogy communicates *why* to pre-commit, not *how* to make it auditable. |
| C-12 | **PARTIAL** (2) | "Slack citation test" is the portability test from C-12's definition — this is the right concept. However, without a committed Handle Ledger section, the test is applied inline during entry writing, not as a pre-committed list. Portability concept is present; structural pre-commitment is absent. |

**Essential: 48/60** (C-02, C-03 PARTIAL)
**Recommended: 20/30**
**Aspirational: 4/20** (C-11 PARTIAL + C-12 PARTIAL)
**Total: 72/110**
**Golden threshold: FAIL** (C-02, C-03 not full PASS)

*Note: Analogy-based enforcement correctly identifies the C-11/C-12 mechanisms but cannot match structural pre-commitment. "Bet slip" and "Slack citation test" are high-value orientation devices that augment structural enforcement in V-01 and V-02 — their best role is additive to structure, not a substitute for it.*

---

## V-04 — Role Sequence + Lifecycle Emphasis (Registrar + Chronicler)

**Scored from design description only.** Axis: Registrar pre-role produces numbered PBI and draft handles before Chronicler reads signals; Chronicler gates findings and writes entries with PBI citations.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Chronicler gate: only findings that contradict PBI entries survive. Role boundary enforces structural surprise identity. |
| C-02 | **PARTIAL** (6) | Not a primary axis for either role. Chronicler likely requires source attribution but it is not described as a defining Chronicler constraint. |
| C-03 | **PARTIAL** (6) | Not a primary axis for either role; design description emphasizes PBI + handle pre-commitment, not design-impact field specification. |
| C-04 | **PASS** (12) | Registrar → Chronicler role boundary is architecturally stronger than prose instruction: content that doesn't contradict a PBI entry cannot appear in Chronicler output. |
| C-05 | **PASS** (12) | Registrar's PBI entries must be specific enough to be falsifiable; Chronicler entries that contradict them inherit specificity structurally. Generic findings cannot contradict a specific PBI entry. |
| C-06 | **PASS** (10) | Chronicler entries cite Registrar's PBI, which supplies the "expected" half. The role boundary makes the prior belief structurally prior. |
| C-07 | **PARTIAL** (5) | Not a primary axis for either role. Institutional framing likely present as closing step but not a defining role constraint. |
| C-08 | **PARTIAL** (5) | Not a primary axis. Synthesis step likely exists but not described as a role-defined constraint. |
| C-09 | **FAIL** (0) | Not shown. |
| C-10 | **FAIL** (0) | Not shown. |
| C-11 | **PASS** (5) | Registrar's defining purpose: produce numbered PBI before Chronicler reads signals. Role separation is structurally stronger than phase checkpoint — the Registrar *cannot* read signals (it precedes them by role definition). (a) discrete section ✓ (b) numbered entries ✓ (c) Chronicler cites identifiers ✓. Registrar's output is a datable artifact predating Chronicler's. |
| C-12 | **PARTIAL** (2) | Registrar produces "draft handles" before entries — pre-commitment is present. Design description does not confirm an explicit portability test applied by the Registrar. Handles exist as pre-committed artifacts; portability bar not confirmed. |

**Essential: 48/60** (C-02, C-03 PARTIAL)
**Recommended: 20/30**
**Aspirational: 7/20** (C-11 PASS + C-12 PARTIAL)
**Total: 75/110**
**Golden threshold: FAIL** (C-02, C-03 not full PASS)

---

## V-05 — Lifecycle Emphasis + Output Format (Phase 0 PBI + Phase 2 Handle Ledger)

**Scored from design description only.** Axis: PBI lock at Phase 0 (before signal reading) + Handle Ledger committed at Phase 2 (before prose entries); two pre-commitments at structurally separate lifecycle moments. Inherits V-01's full prompt structure plus V-02's Handle Ledger mechanism.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Inherits V-01's Phase 2 gate (SURPRISE/CONFIRMATION verdict); structural exclusion of confirmations. |
| C-02 | **PASS** (12) | Inherits V-01's explicit source field: "Traceable to one artifact, not 'the signals.'" |
| C-03 | **PASS** (12) | Inherits V-01's design impact field with negative specification: "'This affects the design' does not pass — name the thing." |
| C-04 | **PASS** (12) | Phase 0 PBI + Phase 2 gate architecture makes summary content structurally impossible. Inherits V-01's strongest enforcement mechanism. |
| C-05 | **PASS** (12) | PBI citation mechanism (V-01) requires each surprise to contradict a specific PBI entry; Handle Ledger investigation-specificity requirement (V-02) provides redundant enforcement. |
| C-06 | **PASS** (10) | Inherits V-01's PBI Reference field. PBI is frozen at Phase 0; "expected" half is structurally prior, not reconstructed. |
| C-07 | **PASS** (10) | Inherits V-01's Phase 5 Forward Guidance with explicit addressee register. |
| C-08 | **PASS** (10) | Inherits V-01's Phase 4 Synthesis with required pattern identification and explicit "surprises are independent" declaration when applicable. |
| C-09 | **FAIL** (0) | Not present in either source mechanism. |
| C-10 | **FAIL** (0) | Not present in either source mechanism. |
| C-11 | **PASS** (5) | Phase 0 PBI lock (V-01 mechanism): numbered PBI frozen before Phase 1. Positioned at structurally separate moment from Phase 2 — PBI cannot anticipate handle names, handles cannot be rationalized from PBI entries. Minimum bar fully met. |
| C-12 | **PASS** (5) | Handle Ledger committed at Phase 2 (V-02 mechanism): first section of artifact, committed after surprise set is identified but before prose is written, with explicit portability test. Phase-locked at a structurally distinct moment from PBI. |

**Essential: 60/60 — ALL PASS**
**Recommended: 30/30**
**Aspirational: 10/20** (C-11 PASS + C-12 PASS)
**Total: 100/110**
**Golden threshold: PASS** (all essential + composite ≥ 80)

---

## Ranking Summary

| Rank | Variation | Total | All Essential | Golden |
|------|-----------|-------|---------------|--------|
| 1 | V-05 (PBI + Handle Ledger) | **100** | YES | PASS |
| 2 | V-01 (Lifecycle Emphasis) | **97** | YES | PASS |
| 3 | V-02 (Output Format) | **85** | YES | PASS |
| 4 | V-04 (Role Sequence + Lifecycle) | 75 | NO | FAIL |
| 5 | V-03 (Phrasing Register) | 72 | NO | FAIL |

---

## C-11 / C-12 Discriminator Analysis

| Variation | C-11 | C-12 | Combined | Mechanism |
|-----------|------|------|----------|-----------|
| V-01 | PASS (5) | PARTIAL (2) | 7 | Phase lock for PBI; no Handle Ledger |
| V-02 | FAIL (0) | PASS (5) | 5 | Handle Ledger; no PBI pre-commitment |
| V-03 | PARTIAL (2) | PARTIAL (2) | 4 | Analogy for both; no structural enforcement |
| V-04 | PASS (5) | PARTIAL (2) | 7 | Role separation for PBI; draft handles without portability test |
| V-05 | PASS (5) | PASS (5) | 10 | Phase lock for PBI + Handle Ledger at separate phases |

**Finding:** C-11 and C-12 are satisfied by different structural mechanisms operating at different lifecycle positions (Phase 0 vs. Phase 2). V-01 and V-04 show C-11 is achievable without C-12; V-02 shows C-12 is achievable without C-11. V-05 demonstrates they are non-competing and combinable without degrading any essential criterion.

---

## Excellence Signals from V-05

**Pattern 1: Dual pre-commitment at structurally separate lifecycle moments**
V-05 positions each pre-commitment at a distinct phase boundary — PBI at Phase 0 (before signal reading) and Handle Ledger at Phase 2 (before prose writing). The temporal separation is load-bearing: PBI entries cannot anticipate handle names (Phase 0 precedes Phase 2), and handles cannot be rationalized from PBI entries (Phase 2 is post-gate but pre-entry). Each pre-commitment is made with different information available, forcing two genuinely independent prior commitments. This is the mechanism that produces C-11 PASS + C-12 PASS together without either contaminating the other.

**Pattern 2: C-11 and C-12 are structurally non-competing**
V-01 achieves C-11 without adding Handle Ledger; V-02 achieves C-12 without adding PBI. Neither mechanism degrades the other when combined in V-05 — all essential criteria scores are preserved, both aspirational criteria are achieved. The combination introduces no tradeoffs. The two mechanisms target different artifact types (prior beliefs vs. exit handles) at different temporal positions and compose cleanly. Future rounds can extend V-05 toward C-09 and C-10 without disrupting this foundation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dual pre-commitment at structurally separate lifecycle moments: PBI locks at Phase 0 before signal reading and Handle Ledger commits at Phase 2 before prose writing — temporal separation forces two genuinely independent prior commitments that cannot rationalize each other", "C-11 and C-12 are structurally non-competing: they operate at different phases on different artifact types (prior beliefs vs. exit handles) and combine without degrading any essential criterion — the combination is additive with no tradeoffs"]}
```
