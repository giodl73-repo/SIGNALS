---

# Round 4 Scorecard — flow-resilience (Rubric v4)

**Scoring basis**: Prompt-template evaluation. Each variation is scored as a structural guarantee — i.e., does following this template reliably produce criterion-satisfying output? The trace artifact is a placeholder; no executed output is available.

---

## C-01 Baseline Recovery

C-01 requires at least one scenario per degradation class. Confirmed from v1 rubric: "At least one scenario exists per degradation class, each clearly labeled." All five variations require ≥2 per class by template mandate — C-01 PASS is guaranteed structurally for all.

---

## Criterion-by-Criterion Evaluation

### Essential Tier (C-01 through C-05)

All five variations: **PASS** on all five essential criteria.

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-01 Scenario Coverage | PASS | Templates require ≥2 scenarios per class (Offline / Partial-Failure / Eventual-Consistency), exceeding the ≥1 threshold |
| C-02 Four-Field Structure | PASS | All templates mandate State / Capability / Data at risk / Recovery path for every Include entry with explicit non-trivial content requirements |
| C-03 Gap Identification | PASS | All have three labeled sections (OEG-NN / DCV-NN / MRF-NN) with explicit nil-statement formats |
| C-04 DS Accuracy | PASS | All reference correct DS constructs (CAP, idempotency, conflict strategies); no invented protocols appear in templates |
| C-05 Commerce Grounding | PASS | All anchor to named commerce operations; V-05 explicitly enumerates checkout, inventory reservation, payment processing, cart state, order fulfillment, loyalty redemption |

**Essential sub-total: 60/60 for all five.**

---

### Recommended Tier (C-06 through C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Severity + Blast Radius | FAIL | FAIL | FAIL | FAIL | FAIL | No variation includes a severity label or blast-radius field in the scenario template. The Capability field uses "available / degraded / blocked" but that is not a separate severity annotation, and blast radius is never mentioned. |
| C-07 Actor-Labeled Recovery | PASS | PASS | PASS | PASS | PASS | All templates mandate `[client]` / `[server]` / `[operator]` / `[user]` prefixes per recovery step with trigger condition and success signal. |
| C-08 Conflict Resolution | PASS | PASS | PASS | PASS | PASS | All have a dedicated CR adequacy phase; verdict `no` or `undefined` feeds a DCV-CR-NN finding. |

**Recommended sub-total: 20/30 for all five.**

---

### Aspirational Tier (C-09 through C-18)

#### V-01 — Named Gate-State Vocabulary

| C | Result | Evidence |
|---|--------|----------|
| C-09 Chaos Engineering | FAIL | Not mentioned. |
| C-10 Observability | FAIL | Not mentioned. |
| C-11 Confidence Catalog | **PARTIAL** | Template uses three named dispositions (Include / BARRED / Argued-Impossible) with explicit basis per entry and TRIAGE GATE: OPEN/CLOSED. However, C-11 requires "confidence ratings (high / medium / low / impossible)" — V-01 omits the explicit confidence-level label field; disposition encodes confidence implicitly but not by name. |
| C-12 Nil-Finding Norm | **PASS** | Phase 3 provides nil format for all three gap sections: `OEG-NIL: No offline experience gaps identified for this deployment pattern — [scope rationale]`. Scope rationale explicitly required; bare "none found" not valid. |
| C-13 Coverage Roster | FAIL | No pre-analysis roster. Minimum coverage enforced by Phase 2 instruction ("return to Phase 1 and expand") but not as a standalone commitment table. |
| C-14 CR→DCV Source | **PASS** | Phase 4 explicitly states: "If the verdict is `no` or the strategy is `undefined`, the scenario generates an additional DCV finding. Append to the Data Consistency Violations list with label `DCV-CR-NN`." |
| C-15 DS Primitive | **PASS** | Impossibility Register template includes: `DS Primitive cited:`, `Architecture argument:`, `VALID impossibility argument:`, `INVALID impossibility argument:` — all four fields. Satisfies the strengthened C-15. |
| C-16 Named Vocab | **PASS** | Template explicitly prohibits "Flagged", "Uncertain", "Needs investigation" by name. Three-label vocabulary defined in a table. TRIAGE GATE: OPEN/CLOSED declaration required; gate cannot close with free-text qualifiers. |
| C-17 BARRED→CG | FAIL | No mechanism to harvest permanently BARRED entries into a coverage gap registry. BARRED entries are excluded from Phase 2 with a named basis but produce no downstream artifact. |
| C-18 Entry/Exit | **PARTIAL** | "Do not proceed to Phase 2 until the Triage Gate is CLOSED" — implicit entry condition. No formal "Entry condition:" / "Exit condition:" headers per phase; closure is declared only at the Triage Gate, not at each phase boundary. |

**V-01 aspirational raw**: 0+0+1+2+0+2+2+2+0+1 = **10** → capped at 10
**V-01 composite: 60 + 20 + 10 = 90**

---

#### V-02 — Barred-Entry Lifecycle to Coverage Gaps

| C | Result | Evidence |
|---|--------|----------|
| C-09 Chaos Engineering | FAIL | Not mentioned. |
| C-10 Observability | FAIL | Not mentioned. |
| C-11 Confidence Catalog | **PASS** | Phase 1 explicitly requires `Confidence: [High | Medium | Low]` per entry AND a named disposition derived from it. High/Medium → Include; Low → BARRED. TRIAGE GATE: CLOSED with BARRED list. Every entry has an explicit confidence rating with a stated basis. |
| C-12 Nil-Finding Norm | **PASS** | Phase 3a provides nil formats: `OEG-NIL: [scope rationale]`, `DCV-NIL: [scope rationale]`, `MRF-NIL: [scope rationale]`. Scope rationale required. |
| C-13 Coverage Roster | FAIL | No pre-analysis roster committing to per-class coverage before analysis. |
| C-14 CR→DCV Source | **PASS** | Phase 4: "Verdict `no` or strategy `undefined` → append `DCV-CR-NN` to the Data Consistency Violations list." |
| C-15 DS Primitive | **PARTIAL** | Phase 3b Source 2 has `DS Primitive cited:` and `Architecture argument:` fields — but **no `VALID:`/`INVALID:` counter-example fields**. The strengthened C-15 requires inline annotated examples. Half-satisfied. |
| C-16 Named Vocab | **PASS** | "Named dispositions (use exactly these labels)" — Include / BARRED / Argued-Impossible. TRIAGE GATE: [OPEN | CLOSED] with BARRED list. |
| C-17 BARRED→CG | **PASS** | Phase 2 defines two resolution paths: (1) reclassify to Include, (2) permanently BARRED → Phase 3b Coverage Gap Registry. `CG-NN` format with Source, Entry, Class, Unresolved basis, Impact fields. |
| C-18 Entry/Exit | **PARTIAL** | Phase 2 states "Entry condition: Triage Gate CLOSED" — one entry condition is explicit. Phase 3 entry condition: "Phase 2 complete AND BARRED Resolution Gate CLOSED" — a second entry condition with gate reference. But exit conditions are not labeled per phase; BARRED RESOLUTION GATE: CLOSED is an explicit closure but not framed as an exit condition template field. Two entry conditions present, zero explicit exit conditions. |

**V-02 aspirational raw**: 0+0+2+2+0+2+1+2+2+1 = **12** → capped at 10
**V-02 composite: 60 + 20 + 10 = 90**

---

#### V-03 — Explicit Phase Entry and Exit Conditions

| C | Result | Evidence |
|---|--------|----------|
| C-09 Chaos Engineering | FAIL | Not mentioned. |
| C-10 Observability | FAIL | Not mentioned. |
| C-11 Confidence Catalog | **PARTIAL** | Uses Include / BARRED / Argued-Impossible with Basis field and GATE 1 STATUS: OPEN/CLOSED. No explicit `Confidence: [High | Medium | Low]` rating label per entry — C-11 requires this literal vocabulary. |
| C-12 Nil-Finding Norm | **PASS** | Gate 3 provides nil format for all three sections with scope rationale. |
| C-13 Coverage Roster | FAIL | No pre-analysis roster. Gate 1's exit condition requires ≥2 Include per class — this is a gate closure condition, not an opening commitment table. |
| C-14 CR→DCV Source | **PASS** | Gate 4: "If verdict is `inadequate` or strategy is `undefined`: add `DCV-CR-NN` to Gate 3 DCV list (this reopens Gate 3 for that amendment only; write `GATE 3b: AMENDED`)." |
| C-15 DS Primitive | FAIL | No Impossibility Register with `DS Primitive cited:` field and VALID/INVALID examples. Argued-Impossible entries have only a Basis field in Gate 1 entry format. The strengthened C-15 is not satisfied. |
| C-16 Named Vocab | **PASS** | Gate 1 exit condition requires all entries carry one of the three named dispositions. GATE N STATUS: OPEN/CLOSED for all four gates. |
| C-17 BARRED→CG | FAIL | No BARRED entry lifecycle tracking. BARRED entries from Gate 1 are excluded from Gate 2 but produce no downstream coverage gap record. |
| C-18 Entry/Exit | **PASS** | All four gates have explicit "Entry condition:" and "Exit condition:" headers with gate-ID citations: Gate 2 entry = "Gate 1 CLOSED"; Gate 3 entry = "Gate 2 CLOSED"; Gate 4 entry = "Gate 3 CLOSED". Each gate has GATE N STATUS: [OPEN | CLOSED] with "Reason if OPEN" field. |

**V-03 aspirational raw**: 0+0+1+2+0+2+0+2+0+2 = **9** → 9 (does not reach cap)
**V-03 composite: 60 + 20 + 9 = 89**

---

#### V-04 — Combination: Gate-State Vocabulary + Barred-Entry Lifecycle

| C | Result | Evidence |
|---|--------|----------|
| C-09 Chaos Engineering | FAIL | Not mentioned. |
| C-10 Observability | FAIL | Not mentioned. |
| C-11 Confidence Catalog | **PARTIAL** | Phase 1 table maps Include to "High or Medium confidence", BARRED to "Low confidence" — semantically equivalent. Entry format has Disposition but no explicit `Confidence:` field per entry. Same gap as V-01. |
| C-12 Nil-Finding Norm | **PASS** | Phase 3 has nil formats with scope rationale for all three gap sections. |
| C-13 Coverage Roster | FAIL | No opening commitment roster. |
| C-14 CR→DCV Source | **PASS** | Phase 4: "Verdict `no` or `undefined` → add `DCV-CR-NN` to Phase 3 DCV list." |
| C-15 DS Primitive | **PASS** | Phase 3b Source 2 (Argued-Impossible Register) includes: `DS Primitive cited:`, `Architecture argument:`, `VALID form:`, `INVALID form:` — all four fields including the counter-examples. Strengthened C-15 is satisfied. |
| C-16 Named Vocab | **PASS** | "Flagged is not a disposition. Uncertain is not a disposition. Any label that does not resolve to one of the three above is treated as a missing disposition — the entry is excluded." TRIAGE GATE: CLOSED with explicit BARRED list declaration. |
| C-17 BARRED→CG | **PASS** | Phase 2b explicitly tracks each BARRED entry to resolution or `Permanently BARRED`. BARRED RESOLUTION GATE: CLOSED with permanently BARRED list. Phase 3b Coverage Gap Registry with CG-NN format for every unresolved entry. |
| C-18 Entry/Exit | **PARTIAL** | Phase 2 has "Entry condition: Triage Gate CLOSED". Phase 3 has "Entry condition: Phase 2 complete AND BARRED Resolution Gate CLOSED". Two entry conditions with gate references are present. However, no "Exit condition:" labels per phase; closures are implied by the GATE: CLOSED template fields, not declared as exit conditions. |

**V-04 aspirational raw**: 0+0+1+2+0+2+2+2+2+1 = **12** → capped at 10
**V-04 composite: 60 + 20 + 10 = 90**

---

#### V-05 — Full Formalization (C-15 + C-16 + C-17 + C-18)

| C | Result | Evidence |
|---|--------|----------|
| C-09 Chaos Engineering | FAIL | Not mentioned. |
| C-10 Observability | FAIL | Not mentioned. |
| C-11 Confidence Catalog | **PARTIAL** | Three-label disposition vocabulary (Include / BARRED / Argued-Impossible) with explicit basis. Gate 1 STATUS shows Include count by class. No explicit `Confidence: [High | Medium | Low]` label per entry. C-11's literal vocabulary not used; disposition encodes the same semantics differently. |
| C-12 Nil-Finding Norm | **PASS** | Gate 3 nil formats: `OEG-NIL: No offline experience gaps identified — [scope rationale: why this gap type does not apply for this deployment pattern]`. Scope rationale required; independently present for all three sections. |
| C-13 Coverage Roster | **PARTIAL** | Gate 1 exit condition requires: "each degradation class has at least two entries with disposition `Include`." Gate 1 STATUS output: "Include entries: [count by class]" — independently checkable. Not a pre-analysis opening roster committing before any analysis begins; the commitment is enforced at gate close rather than declared upfront. Close enough for PARTIAL, not PASS. |
| C-14 CR→DCV Source | **PASS** | Gate 4: "If verdict is `inadequate` or strategy is `undefined`: amend Gate 3 DCV list with `DCV-CR-NN`. Write `GATE 3 AMENDMENT: DCV-CR-NN added` and `GATE 3 REMAINS CLOSED`." Explicit linkage and amendment declaration. |
| C-15 DS Primitive | **PASS** | Gate 1c (Impossibility Register) template: `DS Primitive cited:`, `Architecture argument:`, `VALID impossibility argument:`, `INVALID impossibility argument:`. Explicit note: "'The topic doesn't mention X' is never a valid impossibility argument." All four strengthened-C-15 elements present. |
| C-16 Named Vocab | **PASS** | "Flagged is not a disposition. A gate with no explicit CLOSED declaration is OPEN by definition." All seven gates have STATUS: [OPEN | CLOSED] declarations with "Open condition (if OPEN)" fields. |
| C-17 BARRED→CG | **PASS** | Gate 1b tracks every BARRED entry to `Include (reclassified)` or `Permanently BARRED`. Gate 1b STATUS: CLOSED with separate `Permanently BARRED:` list. Gate 3b Coverage Gap Registry requires CG-NN for every permanently BARRED entry; `CG-NIL` declared when list is empty. |
| C-18 Entry/Exit | **PASS** | All seven gates carry explicit `Entry condition:` (citing prior gate IDs) and `Exit condition:` headers. Entry conditions use conjunctions: Gate 2 entry = "Gate 1 CLOSED AND Gate 1b CLOSED AND Gate 1c CLOSED"; Gate 3b entry = "Gate 3 CLOSED AND Gate 1b CLOSED". Every gate closes with GATE N STATUS: OPEN/CLOSED. |

**V-05 aspirational raw**: 0+0+1+2+1+2+2+2+2+2 = **14** → capped at 10
**V-05 composite: 60 + 20 + 10 = 90**

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational raw | Aspirational (capped) | Composite | Golden? |
|------|-----------|-----------|-------------|------------------|-----------------------|-----------|---------|
| 1 | V-01 Named Vocab | 60 | 20 | 10 | 10 | **90** | YES |
| 1 | V-02 BARRED Lifecycle | 60 | 20 | 12 | 10 | **90** | YES |
| 1 | V-04 C-16+C-17 combo | 60 | 20 | 12 | 10 | **90** | YES |
| 1 | V-05 Full Formalization | 60 | 20 | 14 | 10 | **90** | YES |
| 5 | V-03 Entry/Exit | 60 | 20 | 9 | 9 | **89** | YES |

**Golden threshold**: composite ≥ 80 AND all 5 essential pass. All five clear the threshold. V-03 is the only variation that does not hit the aspirational cap (9/10), dragged by missing C-15 (no Impossibility Register template) and C-17 (no BARRED lifecycle tracking).

---

## Discriminating Criterion Analysis

V-03 is the only variation that fails to reach 90. Its single-axis focus on formal gate sequencing (C-18 PASS) comes at the cost of not inheriting the Impossibility Register (C-15 FAIL) or BARRED lifecycle (C-17 FAIL). C-15 and C-17 together add 4 raw aspirational points vs. C-18's 2 — confirming that the BARRED lifecycle + DS Primitive track is structurally more dense than the sequencing track alone.

**Cap analysis**: V-02, V-04, V-05 all have raw=12+; the cap at 10 flattens them to the same composite as V-01 (raw=10, hits cap exactly). The aspirational cap successfully prevents C-09/C-10 absence from being hidden by deep structural work on other criteria. However, the cap means that **V-05's structural superiority (raw=14) is not visible in the composite score.** The true differentiator for V-05 is not composite score but structural guarantee breadth: it is the only variation where C-16 + C-17 + C-18 all PASS simultaneously — the closed-loop formalization the R4 hypothesis sought to achieve.

---

## Excellence Signals from Top Variations

**V-05 — the defining structural move: fork-join sub-gate architecture**

V-05 introduces Gates 1b and 1c as parallel sub-phases: "Gates 1b and 1c may run in parallel. Both must be CLOSED before Gate 2 begins." Gate 2 entry condition is a conjunction: "Gate 1 CLOSED AND Gate 1b CLOSED AND Gate 1c CLOSED." This is qualitatively different from the linear sequencing in V-03 and from the two-entry-condition pattern in V-02. The fork-join pattern:
- Separates BARRED tracking (1b) from impossibility documentation (1c) — two independent sub-problems
- Forces both to complete before the scenario table opens — neither can be skipped
- Makes the dependency graph explicit rather than implied by document position

This pattern is not captured by C-18 (which requires entry/exit conditions but says nothing about parallel sub-phases).

**V-05 — amendment without reopening**

Gate 4's DCV-CR additions use: `GATE 3 AMENDMENT: DCV-CR-NN added` + `GATE 3 REMAINS CLOSED`. This is a distinct pattern from V-03, which "reopens Gate 3 for that amendment only." The V-05 approach avoids the re-open/re-close cycle for amendments that are provably additive — an amendment protocol that preserves gate stability while extending the record. Not captured by any current criterion.

**V-01 and V-04 — inline INVALID form as anti-drift structure**

The Impossibility Register's `INVALID impossibility argument:` field is embedded directly in the output template, not in instructions. The model must fill in its own example of what would fail. This is a structural anti-drift mechanism: the template contains its own negative space, making the distinction between valid and invalid arguments visible without reading the rubric or instructions. Generalizable: any criterion where a specific anti-pattern is the primary failure mode benefits from an inline INVALID form field.

---

## New Patterns (Not Yet Captured in C-09 through C-18)

1. **Fork-join gate architecture**: parallel sub-phases (1b and 1c) that both gate a single downstream phase, with the entry condition as a conjunction over all parallel sub-gate IDs. Linear sequencing (C-18) is a special case; fork-join is the general case.

2. **Amendment-stable gate closure**: a protocol for adding findings to a closed gate (DCV-CR amendments) without declaring it OPEN again — the amendment is labeled, the gate's CLOSED status is explicitly reaffirmed. Prevents spurious re-opens from polluting the audit trail.

3. **Self-documenting INVALID template field**: the output template requires the model to produce its own example of an invalid argument inline, making the anti-pattern part of the artifact rather than the instructions. The analysis document becomes self-auditing on the boundary cases.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Fork-join gate architecture: parallel sub-phases (Gates 1b and 1c in V-05) both gate a single downstream phase via a conjunction entry condition — linear gate sequencing is a special case of this pattern", "Amendment-stable gate closure: DCV-CR additions append to a closed gate with 'GATE 3 REMAINS CLOSED' rather than reopening it — additive amendments do not invalidate prior closure", "Self-documenting INVALID template field: requiring the model to produce its own example of an invalid argument inline makes the anti-pattern part of the artifact, not the instructions"]}
```
