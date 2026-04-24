Now I have all five variations fully read. Let me score each one.

---

# trace-permissions Round 10 — Scoring (rubric v9)

**Baseline entering R10:** V-04-R9 = 195/200 (C-28 + C-29 pass; one aspirational criterion failing at 5 pts; gap candidate: activation-point enumeration specificity in Per-Stage body block).

---

## Criterion-by-Criterion Evaluation

### Essential (15 pts each — C-01 through C-04)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01: Roles by Dataverse system names + record scope | PASS — Phase 1b table requires "Dataverse system names required" + Record Scope column | PASS | PASS | PASS | PASS |
| C-02: FLS per every sensitive entity | PASS — FLS ENTRY block format per sensitive field, section close counts all blocks + CLOSED markers | PASS | PASS | PASS | PASS |
| C-03: OWD per entity with scope distinction | PASS — Phase 1a table "OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row." | PASS | PASS | PASS | PASS |
| C-04: At least one gap or risk flagged | PASS — LIVE GAPS REGISTER with 6 gap types; inertia threats I-1–I-6 with reactive markers; negative-check evidence required in Phase 3 | PASS — blind-spot framing pre-names escalation threat classes, anchoring gap hunt to concrete patterns | PASS | PASS | PASS |

All essential criteria: **PASS for all five variations.**

---

### Recommended (10 pts each — C-05 through C-07)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05: Sharing rule conflicts with specific named rule | PASS — Phase 1d table has Rule Name column; "Conflicts = YES → register SHARING-CONFLICT" | PASS | PASS | PASS | PASS |
| C-06: Team membership gap in non-obvious scenario | PASS — Phase 2a: "Finding: [Role] → [Team X] → [elevated access] -- mechanism: [how]" | PASS | PASS | PASS | PASS |
| C-07: Privilege escalation path end-to-end | PASS — Phase 3 per-role: Team Write / Role Assignment Write / Assign scope / BU Write → ESCALATION-PATH FOUND / RULED OUT | PASS | PASS | PASS | PASS |

All recommended: **PASS for all five variations.**

---

### Aspirational (5 pts each — C-08 through C-29)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08: Remediation per finding | PASS — three-field template (Config change / Expected state / Verification step) pre-declared in Phase 0 | PASS | PASS | PASS | PASS |
| C-09: Cross-role interaction | PASS — Phase 1b multi-role matrix (highest-privilege first, CS/SE as deltas) + Phase 4 contrast statement with both names explicit | PASS | PASS | PASS | PASS |
| C-10: Ceiling-floor delta framing | PASS — "Highest-privilege role first; CS and SE as deltas" in Phase 1b | PASS | PASS | PASS | PASS |
| C-11: Trigger-rule auto-escalation | PASS — I-2 "Missing FLS on PII, Financial, Audit/Compliance → MISSING-FLS" is a deterministic trigger; severity CRITICAL/HIGH/MEDIUM column in register | PASS | PASS | PASS | PASS |
| C-12–C-19: v3–v5 criteria (carried forward) | PASS — full inertia threat framework with I-1–I-5 identifiers + reactive markers; chain propagation infrastructure preserved from baseline | PASS | PASS | PASS | PASS |
| C-20: VERDICT-FAIL gate | PASS — "ANTI-SPECULATION MANDATE -- VERDICT-FAIL before the table header. No gate row may record PASS without citing specific evidence." | PASS | PASS | PASS | PASS |
| C-21: Inertia threat list with per-threat identifiers and reactive markers | PASS — I-1 through I-6, each with unique ID, stated violation condition (Fires During), and reactive marker (ESCALATION-PATH / MISSING-FLS / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT-VIOLATION) | PASS | PASS | PASS | PASS |
| C-22: Category drift as I-6 | PASS — "I-6 \| Category drift -- re-derivation downstream of Step 1 \| Phase 1c Step 2 onward \| CATEGORY-DRIFT-VIOLATION" present in all variations | PASS | PASS | PASS | PASS |
| C-23: Chain-verifier gate row with token-swap | PASS — gate row 5 checks: STEP-1-CLOSE-TOKEN anchor [M] RESOLVED, section-close annotation count [M], [M]==[M] YES/NO, PR-1 clean, rows 1-4 PASS | PASS | PASS — V-03 gate row 5 updated to reference REGISTRY IDs | PASS | PASS |
| C-24: Step 1 close token as chain anchor | PASS — STEP-1-CLOSE-TOKEN format records "Category table total rows analyzed: [N]" and "Chain anchor value: [M]"; section close declares "Downstream FLS ENTRY Category annotation count: [M] (Separately declared for gate row 5 comparison)" | PASS | PASS | PASS | PASS |
| C-25: Per-stage chain-reminder at consumption points | PASS — `[Category chain: active -- inherit from Step 1]` required at LIVE GAPS REGISTER header (first activation) and every FLS ENTRY block open | PASS | PASS — `[PR-OBL-02]` reference appended to annotation | PASS | PASS |
| C-26: Phase 0 body-level pre-declaration with PENDING → ACTIVATED lifecycle | PASS — both protocols declared as named Phase 0 body blocks; ACTIVATION STATE LOG carries PENDING/ACTIVE states with activation points and broken-obligation notes; RESOLVED marker fires at Step 1 close referencing Phase 0 declaration | PASS | PASS — PROTOCOL REGISTRY table serves as the named Phase 0 body blocks; all four required fields (named block, state, activation point, broken-obligation note) encoded as explicit columns; RESOLVED marker present in ACTIVATED token format | PASS | PASS |
| C-27: Rubric-verbatim pass-condition language at enforcement sites | PASS — STEP-1-CLOSE-TOKEN protocol definition: "emit a named close token recording the exact count of items analyzed (C-24 rubric phrase)"; chain-reminder annotation appears verbatim at LIVE GAPS REGISTER header and block format | PASS | PASS | PASS | PASS |
| C-28: Protocol-class state-semantic differentiation with activation-class-appropriate broken-obligation semantics | PASS — STEP-1-CLOSE-TOKEN: PENDING, activation class deferred, "unresolved PENDING at trace close = broken obligation" ✓; Per-Stage: ACTIVE, "immediately active," broken-obligation note "absence at any FLS ENTRY block open is a broken state" ✓; state-class semantics match. **GAP (5 pts)**: "Subsequent activation points: every FLS ENTRY block open in Phase 1c" is a class description, not enumeration by individual name — C-28 pass condition requires "all subsequent phase/section activation points by name" | PASS (same gap) | PASS — REGISTRY table encodes activation class explicitly; same enumeration gap | PASS (same gap) | **PASS (gap closed)** — IMMEDIATELY-ACTIVE formal label is embedded in the annotation form at every consumption site: `[PR-OBL-02: IMMEDIATELY-ACTIVE -- absence is a broken state]`; each FLS ENTRY block, at execution time, carries the PR-OBL-02 ID — activation sites are named by their REGISTRY-ID at instantiation; DEFERRED-PENDING/IMMEDIATELY-ACTIVE labels thread from REGISTRY declaration through ACTIVATED token and LOG table, satisfying "by name" requirement via per-site ID embedding rather than static enumeration |
| C-29: Phase-anchored broken-obligation detection point in PENDING protocol declarations | PASS — "A trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor -- detectable without reading gate row 5." Names Phase 5b explicitly | PASS | PASS — Detection Phase column in REGISTRY: "Phase 5b -- a trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor" | PASS | PASS — exact C-29 detection phrase in PR-OBL-01 Broken-Obligation Note cell; Detection Phase column carries "Phase 5b" with C-29 label |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (110) | Total (200) | Notes |
|-----------|---------------|-----------------|-------------------|-------------|-------|
| V-01 | 60 | 30 | 105 | **195** | C-28 activation-enumeration gap (5 pts): "every FLS ENTRY block open" is class description, not named instances |
| V-02 | 60 | 30 | 105 | **195** | Same C-28 gap; CONTEXT preamble strengthens C-04/C-08 but both were already PASS |
| V-03 | 60 | 30 | 105 | **195** | REGISTRY table satisfies C-26/C-28/C-29 content requirements; same C-28 enumeration gap persists (activation points still described as class, not named per-site) |
| V-04 | 60 | 30 | 105 | **195** | V-01+V-02 combined; non-overlapping axes; C-28 gap unchanged |
| V-05 | 60 | 30 | **110** | **200** | C-28 closed: PR-OBL-02 ID embedded in annotation form creates per-site named activation points at execution time; DEFERRED-PENDING/IMMEDIATELY-ACTIVE labels thread from declaration through ACTIVATED token and LOG table |

**Ranking:** V-05 (200) > V-01 = V-02 = V-03 = V-04 (195)

---

## Excellence Signals from V-05

**Signal 1 — Criterion-ID-bearing column headers create self-auditing scoring surfaces:**
V-05's PROTOCOL REGISTRY column headers embed criterion identifiers: "Activation Class (DEFERRED-PENDING or IMMEDIATELY-ACTIVE per C-28)", "Broken-Obligation Note (C-28: semantics must match state class)", "Detection Phase (C-29: named phase where broken obligation becomes visible)". A scorer verifies C-28/C-29 compliance by reading the column headers — no rubric cross-reference required. The table is not just a data structure; it is simultaneously an enforcement spec. C-27 makes rubric phrases appear at enforcement sites; this pattern makes criterion IDs appear at the column-header level of the enforcement table itself.

**Signal 2 — Formal activation-class identifiers (DEFERRED-PENDING/IMMEDIATELY-ACTIVE) as traceable first-class tokens:**
V-05 converts activation class from a prose description ("activation class: deferred") to a formal two-value vocabulary (DEFERRED-PENDING, IMMEDIATELY-ACTIVE) that threads as a constant token through four distinct locations: REGISTRY column value, ACTIVATED token suffix `[PR-OBL-01: DEFERRED-PENDING -> RESOLVED]`, annotation form suffix `[PR-OBL-02: IMMEDIATELY-ACTIVE -- absence is a broken state]`, and LOG table column. A reviewer can grep for DEFERRED-PENDING or IMMEDIATELY-ACTIVE and trace the full activation-class lifecycle from declaration to execution. This makes C-28 state-class compliance mechanically verifiable across documents, not just readable in a single prose block.

**Signal 3 — Per-activation-site REGISTRY-ID embedding resolves the activation-point enumeration gap:**
The annotation form `[Category chain: active -- inherit from Step 1] [PR-OBL-02: IMMEDIATELY-ACTIVE -- absence is a broken state]` appears at every FLS ENTRY block open. Each consumption site, when instantiated, carries the PR-OBL-02 identifier — effectively naming every activation site with its REGISTRY-ID at execution time. This satisfies C-28's "all subsequent phase/section activation points by name" requirement without requiring static enumeration of unknown instances in the Phase 0 declaration. The pattern: activation points are named by REGISTRY-ID at instantiation rather than pre-listed at declaration. → **C-30 candidate**.

---

## Summary

| Metric | Value |
|--------|-------|
| Top score | 200/200 (V-05) |
| All essential pass | YES (all five variations) |
| Best baseline | V-01/V-02/V-03/V-04 all at 195/200 |
| Gap closed by V-05 | C-28 activation-enumeration (5 pts) via per-site REGISTRY-ID embedding |
| New patterns | 3 (criterion-ID column headers; formal lexical activation-class tokens; per-site ID embedding resolves enumeration gap) |

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["criterion-ID-bearing REGISTRY column headers create self-auditing scoring surfaces — scorer verifies C-28/C-29 from column header alone without rubric cross-reference", "formal activation-class tokens (DEFERRED-PENDING/IMMEDIATELY-ACTIVE) as first-class identifiers threading from declaration through ACTIVATED token, annotation form, and LOG table — mechanical cross-document traceability", "per-activation-site REGISTRY-ID embedding in annotation format strings resolves activation-point enumeration gap — each FLS ENTRY block carries PR-OBL-02 ID at instantiation, naming activation sites by ID at execution time rather than pre-listing unknown instances at declaration time"]}
```
