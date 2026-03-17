## Scoring: `topic:echo` — Round 12

**Rubric:** v11 | **Formula:** `(essential/4 × 60) + (recommended/3 × 30) + (aspirational/24 × 10)`

---

## Variation Profiles (Structural Baselines)

| Variation | Base | C-11 | C-12 | C-14 | C-24 | C-25 | C-30 | C-31 |
|-----------|------|------|------|------|------|------|------|------|
| V-01 | R11 V-05 (all 24 active) | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| V-02 | R11 V-01 | FAIL | FAIL | PARTIAL | FAIL | FAIL | PASS | PASS |
| V-03 | R11 V-01 | FAIL | FAIL | PARTIAL | FAIL | FAIL | PASS | PASS |
| V-04 | R11 V-03 (C-24+C-25 active) | FAIL | FAIL | PARTIAL | PASS | PASS | PASS | PASS |
| V-05 | R11 V-05 (all 24 active) | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

---

## V-01 — Phrasing Register (Declarative/Contractual)

All R11 V-05 structural features retained exactly. Register shift only: imperatives become contract declarations, scope boundaries become exclusion violations.

**Essential (all PASS):**
- C-01 PASS — ≥3 entries enforced via step structure
- C-02 PASS — `[CROSS: {artifact-A} × {artifact-B}]` in entry template
- C-03 PASS — `We believed: {falsifiable pre-investigation assumption}` schema slot
- C-04 PASS — `If the next team carries the old assumption: {specific concrete mis-design}` schema slot

**Recommended (all PASS):**
- C-05 PASS — Step 1 reads all namespaces; ≥3 floor stated
- C-06 PASS — T-1..T-4 in Step 9 with citable source requirement
- C-07 PASS — Step 4 triage precedes Step 7 expansion; TRACE-CHECK-VERDICT in Step 10

**Aspirational (24/24 PASS):**

| # | Verdict | Evidence |
|---|---------|----------|
| C-08 | PASS | Step 8: WORD BUDGET ≤120 words; ≥2 entries cited; independence constraint explicit in SCOPE |
| C-09 | PASS | `If the next team carries:` schema slot present |
| C-10 | PASS | Discard log contract: route, reason, downstream destination; non-empty required |
| C-11 | PASS | Stage 2 non-derivability sub-test: `Spec + full CB-ID register prediction` vs `Actual finding`; CONFIRMED/FAILED commit |
| C-12 | PASS | Step 7: `### Defeats CB-{n}:` group headers; ≥2 distinct CB-ID groups required |
| C-13 | PASS | Step 1 records namespace coverage (≥3 floor) before entry expansion |
| C-14 | PASS | Step 3b: CB-ID Redundancy Audit block; same-CB-ID entries flagged; REDUNDANCY-AUDIT-VERDICT token |
| C-15 | PASS | Stage 2: `INVALID → candidate fails Stage 2 → return to discard log as topic-report` (return semantics, not validation flag) |
| C-16 | PASS | Step 8: CATEGORY DECLARATION block with misunderstanding-class taxonomy |
| C-17 | PASS | Step 9: T-1..T-4 slots with named schema and citable source requirement |
| C-18 | PASS | Step 10: named per-field TRACE-CHECK-VERDICT with tier-match, orphan check, one-rule-per-surprise, {CATEGORY}: presence |
| C-19 | PASS | Step 8 SCOPE: "Pattern unreachable from any single entry alone; a pattern reachable from a single entry is not within scope" |
| C-20 | PASS | PHASE CONTRACT blocks on every step with explicit SCOPE exclusions stated as contract violations |
| C-21 | PASS | All stages carry INPUT:/OUTPUT: declarations in PHASE CONTRACT headers |
| C-22 | PASS | Step 8: "Hedged verdict language ('may suggest,' 'seems to indicate') is a contract violation" — explicit prohibition |
| C-23 | PASS | Step 0 BC: ≥3 falsifiable beliefs, source, confidence level; FLOOR GATE; CB-ID FREEZE token |
| C-24 | PASS | Step 4: triage rank = tier severity × CB-ID confidence level; HIGH-confidence defeats first |
| C-25 | PASS | Step 9: SURVIVING BELIEF REGISTER block with status and future-round confirmation requirement |
| C-26 | PASS | Step 6: `RETURN GATE: Either field INVALID → return to Step 5`; Stage 2: `INVALID → return to discard` |
| C-27 | PASS | All PHASE CONTRACT blocks carry INPUT: and OUTPUT: type declarations |
| C-28 | PASS | Step 10: `(encodes: {SURPRISE NAME} → {CATEGORY}: {taxonomy-label})` in audit row schema |
| C-29 | PASS | Step 8: `WORD BUDGET: Taxonomy declaration lines (not counted) + synthesis paragraph ≤120 words` as formal contract field |
| C-30 | PASS | Step 7: `defeats: CB-{n}` as named schema slot alongside `We believed:` and `Actionability:` fields |
| C-31 | PASS | Step 0: "CB-ID FREEZE: The register above is now locked. Adding, modifying, or removing a CB-ID after Step 1 begins is a contract violation. The beliefs declared here constitute the fixed epistemic baseline for all subsequent steps." |

**Aspirational total: 24/24 = 10.00**
**Score: 60 + 30 + 10.00 = 100.00**

**Phrasing register hypothesis result:** CONFIRMED NEUTRAL. Declarative/contractual register produces identical scoring to R11 V-05's imperative register. C-20/C-21/C-27 scope contracts become explicitly testable under declarative framing, but were already PASS under imperative phrasing. No degradation to C-04.

---

## V-02 — Inertia Framing (Prominent)

Base: R11 V-01 (BC + CB-IDs; C-11/C-12/C-24/C-25 not activated; C-14 PARTIAL).

**Essential (all PASS):**
- C-01 PASS — entry template present; ≥3 entries enforced
- C-02 PASS — `[CROSS: {artifact-A} × {artifact-B}]` in entry template
- C-03 PASS — `We believed: {falsifiable pre-investigation assumption}` field
- C-04 PASS — both `If the next team carries:` AND new `Without this echo: {specific artifact produced under inertia}` fields

**Recommended (all PASS):**
- C-05 PASS — Step 1 namespace floor ≥3
- C-06 PASS — T-1..T-4 in Step 9; source citable
- C-07 PASS — triage (Step 4) precedes expansion (Step 7); traceability check in Step 10

**Aspirational:**

| # | Verdict | Evidence |
|---|---------|----------|
| C-08 | PASS | Step 8: WORD BUDGET ≤120 words; ≥2 entries by label; independence explicit |
| C-09 | PASS | `If the next team carries:` + `Without this echo:` per entry — dual counterfactual fields; INERTIA COMPARISON in Step 9 |
| C-10 | PASS | Discard log: route, reason, destination; non-empty required |
| C-11 | **FAIL** | Stage 2 has VALID/INVALID contradiction test but no non-derivability sub-test against CB-set — not activated in R11 V-01 base |
| C-12 | **FAIL** | Step 7 uses prose block entries without CB-ID group headers — not activated in R11 V-01 base |
| C-13 | PASS | Step 1 namespace coverage recorded before routing |
| C-14 | **PARTIAL** | Stage 3 single-artifact cuts present; no Step 3b CB-ID redundancy audit |
| C-15 | PASS | `INVALID → return to discard log` in Stage 2; `Either INVALID → return to Step 5` in Step 6 |
| C-16 | PASS | Step 8: CATEGORY DECLARATION block present |
| C-17 | PASS | T-1..T-4 with specific fill requirements and citable source |
| C-18 | PASS | Step 10 TRACE-CHECK-VERDICT with per-field verification |
| C-19 | PASS | Step 8 SCOPE: "Must be unreachable from any single entry" |
| C-20 | PASS | PHASE blocks on all steps with SCOPE declarations |
| C-21 | PASS | PHASE blocks carry INPUT:/OUTPUT: on named stages |
| C-22 | PASS | Synthesis paragraph direction mandates committed verdicts (entries named, independence explicit, category named) |
| C-23 | PASS | Step 0 BC: ≥3 falsifiable beliefs; confidence levels; CB-ID FREEZE irrevocable |
| C-24 | **FAIL** | Step 4: comparative tier assignment but no confidence-weighted ordering function — not activated |
| C-25 | **FAIL** | Step 9: "Forward Handover + Inertia Comparison" only; no Surviving Belief Register block |
| C-26 | PASS | Stage 2: INVALID → return to discard; Step 6: INVALID → return to Step 5 |
| C-27 | PASS | PHASE blocks have INPUT:/OUTPUT: on multiple named stages |
| C-28 | PASS | Step 10: `{CATEGORY}:` field in audit row schema referencing Step 8 taxonomy |
| C-29 | PASS | Step 8: `WORD BUDGET: Synthesis paragraph ≤120 words` as formal field |
| C-30 | PASS | `defeats: CB-{n}` as named schema slot in Step 7 entry template |
| C-31 | PASS | "CB-ID FREEZE: Register is now locked... This freeze is irrevocable." |

**Aspirational: 19 PASS + 1 PARTIAL (C-14) + 4 FAIL (C-11, C-12, C-24, C-25) = 19.5/24 = 8.13**
**Score: 60 + 30 + 8.13 = 98.13**

**Inertia framing hypothesis result:** PARTIALLY CONFIRMED. C-09 (counterfactual awareness) gains dual field support. C-04 (actionability) strengthened by visible inertia prototype. No synthesis crowding — C-08 holds PASS. Ceiling constrained by R11 V-01 base failures (C-11, C-12, C-24, C-25).

---

## V-03 — Output Format (Table-Centric Entries)

Base: R11 V-01. Step 7 changes to markdown table format with named columns; gate structure, synthesis, and Rules of Thumb remain prose.

**Essential (all PASS):**
- C-01 PASS — table rows are countable entries; ≥3 enforced by "One row per SURPRISE" instruction
- C-02 PASS — dedicated `Cross-Signal` column: `[CROSS: {artifact-A} × {artifact-B}]` mechanically enforced
- C-03 PASS — `We believed` column with `{falsifiable pre-investigation assumption}` placeholder; table row validation explicitly checks falsifiability: "`We believed:` column is a falsifiable claim (not a vague fill)? → VALID / INVALID"
- C-04 PASS — `If carries old assumption` column: `{specific concrete mis-design}`; table validation checks: "names a specific artifact (not abstract consequence)? → VALID / INVALID"

**Recommended (all PASS):**
- C-05 PASS — Step 1 namespace ≥3 floor
- C-06 PASS — T-1..T-4 in Step 9
- C-07 PASS — Step 4 triage before Step 7 table; TRACE-CHECK-VERDICT in Step 10

**Aspirational:**

| # | Verdict | Evidence |
|---|---------|----------|
| C-08 | PASS | Step 8: WORD BUDGET ≤120 words; ≥2 entries by label from table; independence constraint explicit |
| C-09 | PASS | `If carries old assumption:` column present |
| C-10 | PASS | Discard log: route, reason, destination required |
| C-11 | **FAIL** | Stage 2 no non-derivability sub-test; not activated in R11 V-01 base |
| C-12 | **FAIL** | Table is flat (no CB-ID group headers); C-12 requires group headers anchored to CB-IDs |
| C-13 | PASS | Step 1 namespace coverage recorded |
| C-14 | **PARTIAL** | Stage 3 single-artifact cuts; no CB-ID redundancy audit |
| C-15 | PASS | Stage 2 INVALID → return to discard; Step 6 return gate |
| C-16 | PASS | Step 8 CATEGORY DECLARATION block |
| C-17 | PASS | T-1..T-4 schema with source requirement |
| C-18 | PASS | Step 10 TRACE-CHECK-VERDICT; table row validation adds per-field pre-commit check |
| C-19 | PASS | Step 8 SCOPE: unreachable from any single row |
| C-20 | PASS | PHASE blocks on Steps 0-4, 7-8 with SCOPE declarations |
| C-21 | PASS | PHASE blocks with INPUT:/OUTPUT: |
| C-22 | PASS | Synthesis instructions mandate committed verdicts |
| C-23 | PASS | Step 0 BC: ≥3 beliefs, confidence, sources; CB-ID FREEZE |
| C-24 | **FAIL** | No confidence-weighted triage ordering — not activated |
| C-25 | **FAIL** | No surviving belief register in Step 9 |
| C-26 | PASS | Return gate semantics in Step 6 and Stage 2 |
| C-27 | PASS | PHASE blocks with I/O type declarations |
| C-28 | PASS | Step 10: `{CATEGORY}:` in audit row schema |
| C-29 | PASS | Step 8: WORD BUDGET contract field |
| C-30 | PASS | `defeats` named **table column**: mechanically enforced, stronger than prose reference |
| C-31 | PASS | "CB-ID FREEZE: Register locked. No CB-ID may be added or modified after Step 1 begins. This is an immutability constraint — not a preference." |

**Aspirational: 19 PASS + 1 PARTIAL (C-14) + 4 FAIL = 19.5/24 = 8.13**
**Score: 60 + 30 + 8.13 = 98.13**

**Table format hypothesis result:** C-01/C-02/C-30 gain mechanical enforcement via column structure; C-03/C-04 do not degrade (table row validation compensates). Ceiling identical to V-02 because the flat table can't satisfy C-12 (requires CB-ID group headers, not column alone). C-12 FAIL prevents score improvement over V-02.

---

## V-04 — Combined: Phrasing Register + Inertia Framing

Base: R11 V-03 (C-24 + C-25 active; C-11/C-12 NOT activated; C-14 PARTIAL). Axes: declarative phrasing + inertia framing.

**Essential (all PASS):**
- C-01 PASS, C-02 PASS, C-03 PASS
- C-04 PASS — `If the next team carries:` + `Without this echo:` inertia field both present

**Recommended (all PASS):**
- C-05 PASS, C-06 PASS, C-07 PASS

**Aspirational:**

| # | Verdict | Evidence |
|---|---------|----------|
| C-08 | PASS | Step 8: WORD BUDGET ≤120 words; SCOPE: unreachable from single entry |
| C-09 | PASS | Both `If carries:` and `Without this echo:` fields in entry template |
| C-10 | PASS | Discard log: empty discard log is a contract violation |
| C-11 | **FAIL** | Stage 2: no non-derivability sub-test visible — not activated in R11 V-03 base |
| C-12 | **FAIL** | Step 7: prose block entries without CB-ID group headers — not activated in R11 V-03 base |
| C-13 | PASS | Step 1 namespace coverage |
| C-14 | **PARTIAL** | Stage 3 single-artifact cuts only; no CB-ID redundancy audit |
| C-15 | PASS | `RETURN GATE: Either INVALID → return to Step 5`; Stage 2 return path present |
| C-16 | PASS | Step 8: CATEGORY DECLARATION block |
| C-17 | PASS | T-1..T-4 with required fields and source citations |
| C-18 | PASS | Step 10 TRACE-CHECK-VERDICT; per-field audit |
| C-19 | PASS | Step 8 SCOPE: pattern must be unreachable from single entry |
| C-20 | PASS | PHASE CONTRACT blocks throughout with SCOPE exclusions as contract violations |
| C-21 | PASS | PHASE CONTRACT blocks with INPUT:/OUTPUT: on all named stages |
| C-22 | PASS | Synthesis direction mandates committed pattern; independence explicitly required |
| C-23 | PASS | Step 0 BC: ≥3 beliefs, confidence, sources; CB-ID FREEZE immutability contract |
| C-24 | PASS | Step 4: `Triage rank is a function of tier severity × CB-ID confidence level`; write order specifies HIGH-confidence defeats first — activated via R11 V-03 base |
| C-25 | PASS | Step 9: SURVIVING BELIEF REGISTER block with CB-ID listing and future-round confirmation — activated via R11 V-03 base |
| C-26 | PASS | `RETURN GATE` in Step 6; Stage 2 return semantics |
| C-27 | PASS | PHASE CONTRACT blocks carry INPUT:/OUTPUT: declarations |
| C-28 | PASS | Step 10: `{CATEGORY}:` field referencing Step 8 taxonomy |
| C-29 | PASS | Step 8: WORD BUDGET contract field |
| C-30 | PASS | `defeats: CB-{n}` as named schema slot in Step 7 entry template |
| C-31 | PASS | "CB-ID FREEZE: This register is now locked and immutable. Adding, modifying, or removing a CB-ID after Step 1 begins is a contract violation." |

**Aspirational: 21 PASS + 1 PARTIAL (C-14) + 2 FAIL (C-11, C-12) = 21.5/24 = 8.96**
**Score: 60 + 30 + 8.96 = 98.96**

**Combination hypothesis result:** C-24/C-25 (from R11 V-03 base) add +0.83 over V-02. Declarative phrasing confirmed neutral. Inertia framing confirmed independent — adds C-09 depth without displacing synthesis content. Additive composition confirmed: no interference between phrasing register and inertia framing axes.

---

## V-05 — Full Synthesis: All Three R12 Axes

Base: R11 V-05 (all 24 active). Adds: declarative phrasing + inertia framing + table entries organized by CB-ID group headers.

**Essential (all PASS):**
- C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS

**Recommended (all PASS):**
- C-05 PASS, C-06 PASS, C-07 PASS

**Aspirational — critical interference checks:**

| # | Verdict | Evidence |
|---|---------|----------|
| C-08 | PASS | Step 8: WORD BUDGET ≤120 words; "≥2 named entries; independence constraint explicitly stated"; hedging is a contract violation |
| C-09 | PASS | `If carries old assumption:` + `Without this echo:` as named table columns |
| C-10 | PASS | Empty discard log is a contract violation; route, reason, destination required |
| C-11 | PASS | Stage 2 non-derivability sub-test present; `Non-deriv.` column in table enforces per-entry confirmation |
| C-12 | PASS | **Key test:** Step 7 uses `### Defeats CB-{n}: "{belief statement}"` group headers ABOVE table rows — CB-ID grouping preserved in table format. ≥2 distinct CB-ID groups required. |
| C-13 | PASS | Step 1 namespace coverage recorded |
| C-14 | PASS | Step 3b CB-ID Redundancy Audit block with REDUNDANCY-AUDIT-VERDICT token |
| C-15 | PASS | Stage 2: INVALID → return to discard; Step 6 RETURN GATE |
| C-16 | PASS | Step 8: CATEGORY DECLARATION block |
| C-17 | PASS | T-1..T-4 with schema and source |
| C-18 | PASS | Step 10 TRACE-CHECK-VERDICT; table per-row validation also adds pre-commit field checks |
| C-19 | PASS | Step 8 SCOPE: "Pattern unreachable from any single row" |
| C-20 | PASS | PHASE CONTRACT blocks on all steps; scope exclusions as contract violations throughout |
| C-21 | PASS | INPUT:/OUTPUT: on all named pipeline stages |
| C-22 | PASS | "Hedging language is a contract violation" explicit in Step 8 |
| C-23 | PASS | Step 0 BC: ≥3 beliefs, confidence, sources; CB-ID FREEZE immutability |
| C-24 | PASS | Step 4: rank = tier × confidence; salience ordering is a contract violation; write order specified |
| C-25 | PASS | Step 9: SURVIVING BELIEF REGISTER; all three outputs (handover + surviving-belief + inertia comparison) required |
| C-26 | PASS | Multiple RETURN GATE declarations; Stage 2 INVALID → return |
| C-27 | PASS | PHASE CONTRACT blocks with full INPUT:/OUTPUT: declarations |
| C-28 | PASS | Step 10 `{CATEGORY}:` in audit rows; absent → return to Step 8 |
| C-29 | PASS | Step 8: WORD BUDGET formal contract field |
| C-30 | PASS | `defeats` as named table column alongside all other schema fields |
| C-31 | PASS | "Adding, modifying, or removing a CB-ID after Step 1 begins is a contract violation. These beliefs are the fixed epistemic baseline for all subsequent testing." |

**Aspirational: 24/24 = 10.00**
**Score: 60 + 30 + 10.00 = 100.00**

**Full synthesis hypothesis result:** CONFIRMED. All three R12 axes compose without interference. Critical finding: table format + CB-ID group headers are compatible — the group headers above each table section preserve C-12 while the table columns enforce C-30 mechanically. No criterion degraded.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Score** | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 | 60.00 | 30.00 | 10.00 | **100.00** | 1 (tied) |
| V-01 | 60.00 | 30.00 | 10.00 | **100.00** | 1 (tied) |
| V-04 | 60.00 | 30.00 | 8.96 | **98.96** | 3 |
| V-02 | 60.00 | 30.00 | 8.13 | **98.13** | 4 (tied) |
| V-03 | 60.00 | 30.00 | 8.13 | **98.13** | 4 (tied) |

---

## Discriminating Pair Analysis

| Pair | Isolated variable | Result |
|------|-------------------|--------|
| V-01 vs R11 V-05 | Phrasing register | **Neutral** — 100.0 = 100.0; declarative/contractual register adds no scoring value over imperative |
| V-01 vs V-05 | Phrasing register when inertia+table also active | **Neutral** — 100.0 = 100.0; all three axes compatible |
| V-02 vs V-04 | Declarative phrasing when inertia held constant | **Neutral** — 98.13 → 98.96 delta comes from R11 V-03 base (C-24/C-25), not phrasing |
| V-03 vs V-05 | Table format value when full structural stack active | **Neutral** — table composites cleanly at 100.0; interference hypothesis (C-12 disruption) falsified |
| V-02 vs V-03 | Inertia framing vs table format on identical base | **Tied** — 98.13 = 98.13; neither axis unlocks any of the four FAIL criteria (C-11/C-12/C-24/C-25) |

---

## Excellence Signals

**Top-scoring variations:** V-01 and V-05 (both 100.0)

**Pattern 1 — Phrasing register is a scoring-neutral axis.**
V-01 confirms: when the full R11 V-05 structural stack is present, converting all instructions from imperative ("Recover the team's prior belief set") to declarative contract ("The CB-ID register is the Belief Cartographer's sole deliverable; signal artifact read is a phase contract violation") produces no score change. Scope exclusion contracts are as testable as inclusion mandates. The phrasing change adds legibility and enforcement _vocabulary_ but the structural features already encoded the requirements.

**Pattern 2 — Table entries with CB-ID group headers resolve the C-12/C-30 co-requirement.**
V-05 demonstrates a non-obvious composition: C-30 (schema propagation: `defeats` as named slot) and C-12 (root-cause grouping: entries organized under CB-ID group headers) were previously satisfied by having the field in a prose entry template and using `### Defeats CB-{n}:` group headers. In table format, both criteria are satisfied simultaneously by placing the `defeats` column inside rows that appear under `### Defeats CB-{n}:` group headers. The schema-column approach (C-30) and the grouping-header approach (C-12) compose without collision.

**Pattern 3 — Inertia framing adds a second dimension to C-09 without crowding belief framing.**
V-02, V-04, V-05 all include `Without this echo: {specific wrong artifact the next team produces under inertia}` as an additional entry field alongside `If the next team carries the old assumption: {specific concrete mis-design}`. These two fields are distinct dimensions of the same concept (C-09 counterfactual awareness): the first names the wrong action, the second names the wrong artifact produced. Neither crowds C-03 (belief framing) or C-08 (synthesis) — confirmed by all variations holding essential and synthesis PASS.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Declarative contract register is scoring-neutral: converting imperative instructions to contractual declarations preserves all criterion passes when structural features are identical", "Table-plus-CB-ID-group-headers compose: table rows organized under group headers satisfy C-30 (schema column) and C-12 (root-cause grouping) simultaneously without collision", "Inertia Without-this-echo field adds second C-09 dimension without crowding belief framing or synthesis criteria"]}
```
