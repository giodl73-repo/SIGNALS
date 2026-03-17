Now I have all the information needed to score. Let me produce the full scorecard.

---

# flow-throttle Score — Round 16

**Rubric:** v16 (C-01–C-41) | **Max composite:** 255 | **Baseline:** R15 best = 250/255 (C-41 FAIL)

---

## Scoring Basis

All five R16 variations are built on R15's best variant (V-04 R15), which scored PASS on C-01–C-40. The delta this round is exclusively C-41: whether each variation's gate mechanism structurally prevents Phase 1 from opening when the annotation inventory count is below 7, rather than merely noting the discrepancy as a readable item inside the entry condition.

C-01–C-40 evidence is inherited from R15 analysis and confirmed by inspection of each variation's full text (Section A, B, C structures are identical; analysis steps 1A–2H + Audit block preserved in all five variations, either fully written or explicitly marked "identical structure to V-01").

---

## Criteria Scorecard

### Essential (5 criteria × 12 pts = 60 pts max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Primary bottleneck with causal reason | PASS | PASS | PASS | PASS | PASS |
| **C-02** Backpressure trace ≥2 hops w/ mechanism + observable effect | PASS | PASS | PASS | PASS | PASS |
| **C-03** ≥2 tiers with enforcing component and scope | PASS | PASS | PASS | PASS | PASS |
| **C-04** UX at each throttle tier | PASS | PASS | PASS | PASS | PASS |
| **C-05** At least one concrete mitigation per binding tier | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 all five variations.**

Evidence (all): TABLE A with Binding?+mechanism, TABLE B ≥2 hops with permitted-set Mechanism values, TABLE C one row per tier with error code/signal, TABLE F with Setting or API parameter. All structures fully present in V-01 body; marked "identical structure to V-01" in V-02–V-05 with explicit confirmation that all columns are preserved.

---

### Recommended (3 criteria × 10 pts = 30 pts max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** Load-shape comparison with numeric differential | PASS | PASS | PASS | PASS | PASS |
| **C-07** Cascade scenario ≥3 tiers with causal chain | PASS | PASS | PASS | PASS | PASS |
| **C-08** Retry-After gap assessment naming failure mode | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 all five variations.**

Evidence: Step 2G present with UNIFORM/BURST arrival pattern comparison and numeric differential requirement; Step 2E present with T-NN identifiers and explicit causal links, minimum three tiers; Step 2F present with retry storm vs. quota exhaustion distinction.

---

### Aspirational (33 criteria × 5 pts = 165 pts max)

For space efficiency: C-09–C-40 PASS all five variations (identical to R15 best). Detail below for C-09–C-40 block, then full per-variation analysis for C-41.

#### C-09–C-40 Block (all five variations: PASS)

| Criterion | Pass evidence (identical across V-01–V-05) |
|-----------|---------------------------------------------|
| **C-09** 3-volume load projection (1x/2x/5x) | TABLE A has STATUS 1x / 2x / 5x columns |
| **C-10** Numeric limit at every tier (no vague label) | STEP 1A GATE: `Limit` must contain no vague labels; S-01 vague-label substitution annotation at TABLE A `Limit` column |
| **C-11** Named source for every quantified claim | Annotation contract locks Tier-ID threading; T-NN appears verbatim in all downstream sections (Audit Field 1) |
| **C-12** Failure visibility window and recovery time | TABLE A columns `Failure visibility window` and `Recovery time` present; Audit Field 1 checks threading |
| **C-13** T-NN threading across all downstream sections | Audit Field 1 explicitly checks T-NN appears verbatim in all downstream sections |
| **C-14** Binding constraint exclusivity statement | Binding? = Y/N + mechanism; STEP 1A GATE requires at least two distinct `Failure mode` values across rows |
| **C-15** Role-locked sequencing pipeline | Three-phase structure (Role 1 → gate → Role 2 → Role 3); each step has PHASE ENTRY CONDITION |
| **C-16** Load-shape classification at registration | Step 1B deferral prohibition + escape-route frame; STEP 1B GATE blocks Step 2 until classification complete; Audit Field 3 |
| **C-17** Registry gap prohibition stated | REGISTRY GAP PROHIBITION block at top of Role 2; "SHALL NOT assign new T-NN during Step 2" |
| **C-18** Distributed enforcement reminders | Standing reminders at Steps 2A, 2C, 2E, 2G, 2H |
| **C-19** Registry gap prohibition at every discovery site | Stated at Step 2A, 2C, 2E, 2G, 2H individually |
| **C-20** STEP 1A GATE with completeness conditions | STEP 1A GATE present with: all T-NN rows populated, no vague labels, Binding? with mechanism, ≥2 distinct Failure mode values |
| **C-21** STEP 1B GATE blocking Step 2 | STEP 1B GATE: all Load-shape verdict cells filled before Step 2 opens |
| **C-22** Phase entry/exit conditions at each step | PHASE ENTRY CONDITION at each of Steps 1A, 1B, 2A–2H |
| **C-23** Unprotected burst path analysis | Step 2C TABLE D with P-01; at least one path; if none, named controls as evidence |
| **C-24** Tier risk ranking with TYPE classification | Step 2D TABLE E: all TABLE A tiers appear, ordered by business risk, one-sentence rationale |
| **C-25** Top-ranked tier references Failure visibility window + Recovery time | Step 2D: Rank 1 references both fields from TABLE A |
| **C-26** Escape-route frame at Step 1B | Full "STATUS tracks volume thresholds" self-defeating framing argument in V-01; marked "identical" in V-02–V-04; full escape-route frame in V-05 |
| **C-27** Violation-type annotation at every precision site | Section B: 7 column definitions each with `*Violation type:*` and compliance failure condition; 3 non-conflating types at TABLE A group |
| **C-28** Non-conflation count for multi-adjacent group | "Non-conflation count: 3 violation types at TABLE A precision sites. An executor SHALL NOT treat...as variants of a single failure" |
| **C-29** Section A precision-site inventory | 7-row inventory table with Site-ID, Table, Column, Violation type, C-27 hierarchy |
| **C-30** Compliance failure condition per precision site | Each Section B definition has "Compliance failure condition (C-27/S-NN):" |
| **C-31** FORMAT CONTRACT COMPLETE signal | Explicit "FORMAT CONTRACT COMPLETE" statement at Role 1 boundary |
| **C-32** Audit block with per-criterion fields | ROLE 3 — AUDIT with Fields 1–5 and per-section compliance table |
| **C-33** Role-sequence header with three-phase description | Opening paragraph describes three-phase or four-role structure before any section begins |
| **C-34** Observable count stated at Section A path labels | "Count: 7 precision sites" in Section A header |
| **C-35** Format contract as named section | "Section B — Format contract" is a named section |
| **C-36** Observable count at Section A activates Role 3 | Audit Field 1 checks T-NN threading across all downstream sections (count-derived verification gate) |
| **C-37** Annotation inventory as named section | "Section C — Annotation inventory" is a named section |
| **C-38** Annotation count declared in Section C header | "This section declares **7 required annotations**. Count-scan verification: expected rows = 7." |
| **C-39** Inventory closure statement | "This inventory is closed. An annotation not listed here does not exist as a contract requirement." |
| **C-40** PROHIBITED clause physically co-located inside annotation inventory | PROHIBITED clause appears inside Section C body, not in a sibling FORMAT CONTRACT block. V-01: "physically co-located inside the annotation inventory as required." V-02: "Co-located inside annotation inventory per C-40 requirement." V-04: "co-located inside the annotation inventory." V-05: "co-located here inside the annotation inventory per C-40 requirement." V-03: "[PROHIBITED dropout clause co-located inside the inventory]" (confirmed shorthand). |

**C-09–C-40 subtotal: 160/160 all five variations.**

---

#### C-41 — Annotation-inventory count as Phase 1 role-activation gate

Pass condition: A count discrepancy at Section C returns to Role 1 **before Phase 1 opens** — not as a bullet item inside the entry condition, but as a structural gate that prevents the body-construction role from running. The mechanism must block Step 1A, not flag a discrepancy after output is generated.

---

**V-01 — INVENTORY GATE (standalone lifecycle phase)**

Evidence: A named phase "INVENTORY GATE" is positioned as its own section between FORMAT CONTRACT COMPLETE and Role 2. It has its own header, numbered procedure, and an explicit GATE STATUS field: "GATE STATUS: [ CLEARED / BLOCKED ] — fill this field before opening Phase 1. An executor SHALL NOT open Phase 1 until GATE STATUS = CLEARED is explicitly recorded." Row count < 7 → GATE BLOCKED → return to Role 1 procedure. Step 1A PHASE ENTRY CONDITION: "Step 1A SHALL be entered after INVENTORY GATE = CLEARED." Audit Field 5 checks GATE STATUS = CLEARED before Step 1A. A count discrepancy returns to Role 1 before Phase 1 opens — the gate is a named section with an observable state field that cannot remain unfilled.

**C-41: PASS** | 5/5

---

**V-02 — PHASE 1 ACTIVATION TABLE (verification table with Verdict cell)**

Evidence: A 3-row table with columns Check / Expected / Actual / Verdict is positioned between FORMAT CONTRACT COMPLETE and Role 2. Row 1: "Section C Gate-weight=Y row count | 7 | [count them] | PROCEED if actual=7; RETURN TO ROLE 1 if actual<7." ACTIVATION STATUS field: "SHALL be filled before Step 1A begins." Step 1A PHASE ENTRY CONDITION references ACTIVATION STATUS = PROCEED. Section C gains a Gate-weight column (all Y), making the count derivation auditable in the table without traversing annotation content. A blank Verdict cell is itself a detectable compliance failure; a RETURN TO ROLE 1 verdict blocks Step 1A before any analysis output.

**C-41: PASS** | 5/5

---

**V-03 — Role 1.5 (INVENTORY VERIFIER) standalone role**

Evidence: A named role "ROLE 1.5 — INVENTORY VERIFIER" with single responsibility ("Confirm that Section C annotation inventory row count equals the declared count of 7. This role has no other responsibility and produces no analysis output") sits between Role 1 and Role 2. Two-signal handoff chain: FORMAT CONTRACT COMPLETE activates Role 1.5; INVENTORY VERIFIED or INVENTORY INCOMPLETE is the handoff from Role 1.5. Role 2 activation condition: "INVENTORY VERIFIED has been stated by Role 1.5. An executor SHALL NOT open Step 1A until the Role 1.5 handoff signal is INVENTORY VERIFIED." Count < 7 → INVENTORY INCOMPLETE → return to Role 1, complete Section C, re-state FORMAT CONTRACT COMPLETE, re-enter Role 1.5. A structural gap in the role sequence (no INVENTORY VERIFIED signal present) prevents Role 2 from running. Opening prompt states the four-role sequence; the named role cannot be skipped without a visible structural gap.

**C-41: PASS** | 5/5

---

**V-04 — PHASE 1 ENTRY CONDITION — MANDATORY GATE (phrasing register + lifecycle)**

Evidence: A named mandatory section "PHASE 1 ENTRY CONDITION — MANDATORY GATE (C-41)" positioned between FORMAT CONTRACT COMPLETE and Role 2 has three subsections: (1) Count declaration — expected = 7; (2) Confirmation — "An executor SHALL count the Annot-ID rows in Section C. Actual Section C row count: [fill — required before proceeding]"; (3) Outcome — CLEARED or BLOCKED, with SHALL at every branch point: "An executor SHALL return to Role 1. An executor SHALL complete Section C to the declared count of 7. An executor SHALL re-state FORMAT CONTRACT COMPLETE. An executor SHALL re-enter this PHASE 1 ENTRY CONDITION from Subsection 1. An executor SHALL NOT proceed to Step 1A until Subsection 3 resolves to CLEARED." STATUS field: "An executor SHALL fill this field. An executor SHALL NOT open Step 1A if this field is BLOCKED or unfilled." SHALL density is maximum at every decision branch — the gate is normatively saturated.

**C-41: PASS** | 5/5

---

**V-05 — Role sequence + output format + inertia framing (three-axis)**

Evidence: Three compounding mechanisms:

(1) **Role activation chain table** (upfront, before any content): a 4-row table with columns Role / Activation signal / Handoff signal / Responsibility makes the activation chain legible before content begins. "An executor SHALL NOT activate a role until its activation signal is present." Row for Role 1.5: activation = FORMAT CONTRACT COMPLETE; handoff = INVENTORY VERIFIED or INVENTORY INCOMPLETE. Row for Role 2: activation = INVENTORY VERIFIED only.

(2) **Verification table in Role 1.5**: Check / Expected / Actual / Verdict table. "HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ] — fill before Role 2." Role 2: "An executor SHALL NOT open Step 1A if HANDOFF SIGNAL = INVENTORY INCOMPLETE or if the HANDOFF SIGNAL field is unfilled."

(3) **Inertia frame** (structural proof rejecting the "looks complete" bypass): "The temptation to skip Role 1.5 and proceed directly to Role 2 is the 'looks complete' framing — because FORMAT CONTRACT COMPLETE has been stated and the analysis tables are scaffolded, activating Role 2 appears to miss no required steps. This frame is self-defeating: FORMAT CONTRACT COMPLETE confirms that Role 1's *sections* are present — it does not verify that the annotation inventory is *complete to its declared count*. ... Skipping Role 1.5 converts the Section C count from a verifiable gate into an unverified assertion — a discrepancy is detectable only after Role 2 has produced output, not before." This mirrors the C-26 circular-dependency proof structure, converting the gate from policy requirement to logical necessity.

Additionally, V-05 replaces prose gates at Steps 1A and 1B with STEP 1A GATE TABLE and STEP 1B GATE TABLE (4-row structured tables with Gate check / Required / Status columns), uniformly raising the visibility of all gate boundaries.

**C-41: PASS** | 5/5

---

### Composite Score Summary

| Criterion tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|------|------|------|------|------|
| Essential (C-01–C-05): 60 max | 60 | 60 | 60 | 60 | 60 |
| Recommended (C-06–C-08): 30 max | 30 | 30 | 30 | 30 | 30 |
| Aspirational C-09–C-40 (32 × 5 = 160 max) | 160 | 160 | 160 | 160 | 160 |
| **C-41** (5 pts) | **5** | **5** | **5** | **5** | **5** |
| **COMPOSITE** | **255** | **255** | **255** | **255** | **255** |
| All 5 essential PASS | ✓ | ✓ | ✓ | ✓ | ✓ |
| Golden threshold met | ✓ | ✓ | ✓ | ✓ | ✓ |

**All five variations: 255/255. All five are golden.**

---

## Variation Ranking

All five reach the max composite. Rank is based on C-41 mechanism strength and structural excellence signals:

| Rank | Variation | C-41 mechanism | Rationale |
|------|-----------|----------------|-----------|
| 1 | **V-05** | Role sequence + output format + inertia framing | Three compounding axes; inertia frame converts the gate from policy to logical necessity; role chain table + gate tables at all boundaries creates uniform structural visibility; most resistant to executor bypass |
| 2 | **V-04** | SHALL-dominant three-subsection gate block | Highest normative saturation at every decision branch; SHALL NOT at every failure path; three subsections enforce sequential completion |
| 3 | **V-03** | Role 1.5 (INVENTORY VERIFIER) | Named role creates the clearest structural gap in the sequence; two-signal handoff chain (FORMAT CONTRACT COMPLETE → INVENTORY VERIFIED) is the most legible activation design |
| 4 | **V-01** | Standalone INVENTORY GATE phase | Clean single-axis lifecycle salience; standalone phase with CLEARED/BLOCKED field; restart procedure explicit |
| 5 | **V-02** | PHASE 1 ACTIVATION TABLE (verification table) | Table format is mechanically visible; Gate-weight column makes count derivation auditable; slightly lower rank because the multi-check table (3 rows, not just count) introduces more filling burden without proportional salience gain over V-01 |

---

## Excellence Signals — V-05

### Signal 1: Inertia frame as structural proof at role boundaries

V-05 introduces a named "looks complete" bypass failure mode inside Role 1.5, structured identically to the C-26 escape-route frame at Step 1B. It does not merely prohibit skipping Role 1.5 — it names the temptation, shows why it is self-defeating, and explains why Role 1.5 closes the gap that FORMAT CONTRACT COMPLETE leaves open. The proof structure: FORMAT CONTRACT COMPLETE verifies section *presence*, not count *completeness* → partial Section C (e.g., 6 of 7 annotations) satisfies Role 1's check while failing C-38 → skipping Role 1.5 makes discrepancy detectable only after Phase 1 output, not before. This converts C-41 from "the prompt tells you to verify" to "the prompt explains why verification is logically necessary here." The pattern — naming the bypass temptation and logically rejecting it at every structural gate — is a generalization of C-26.

### Signal 2: Role activation chain table (upfront, before content)

A 4-row table with Role / Activation signal / Handoff signal / Responsibility at the prompt's opening gives the executor a structural map of the entire role sequence before encountering any section content. The executor can consult this table to verify that each role's activation condition is met before proceeding. This table makes "INVENTORY INCOMPLETE does not activate Role 2" visible as a structural fact rather than a buried constraint — the INVENTORY INCOMPLETE outcome appears in the handoff signal column, making its consequence (Role 2 remains inactive) derivable from the table without reading Role 1.5 or Role 2 body text.

### Signal 3: Uniform gate-table format across all boundaries

V-05 replaces prose gate statements at Steps 1A and 1B with structured GATE TABLE blocks (Gate check / Required / Status columns). Combined with the Role 1.5 verification table and the upfront role chain table, all gate boundaries in the prompt share a single structural format: a table with a fill-in field. An executor cannot skip a gate without leaving a blank Status cell — a uniformly detectable compliance gap at all four boundaries (Role 1.5 handoff, Step 1A, Step 1B, Role 3 audit). This generalizes C-41's table-format gate across the entire prompt architecture.

---

```json
{"top_score": 255, "all_essential_pass": true, "new_patterns": ["inertia-frame-at-role-boundaries: name the bypass temptation, show why it is self-defeating with a structural proof, and prove why the gate closes the specific gap the predecessor signal leaves open — converts gate from policy requirement to logical necessity", "role-activation-chain-table-upfront: place a full Role/Activation-signal/Handoff-signal/Responsibility table before any section content so the executor can derive activation consequences (INVENTORY INCOMPLETE does not activate Role 2) from the table without traversing body text", "uniform-gate-table-format: replace prose gate statements at all phase boundaries with structured fill-in tables (Gate check/Required/Status or Check/Expected/Actual/Verdict) so every gate in the prompt has a uniformly detectable compliance gap (blank Status cell) rather than a skippable paragraph"]}
```
