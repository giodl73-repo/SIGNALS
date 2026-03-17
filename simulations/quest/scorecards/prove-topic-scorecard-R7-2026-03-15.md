Now I have everything needed to score all five variations. Let me analyze them systematically.

---

## prove-topic — Round 7 Scorecard (v7 Rubric)

### Scoring Approach

All five variations are built on the R6 V-05 base (C-01–C-22 fully satisfied). The R7 scoring turns on two criteria: **C-23** (independent `incumbent_defense_closed` boolean in handoff) and **C-24** (role-structural attestation ownership). All other criteria pass uniformly across the round.

---

### V-01 — Axis: Handoff Field Independence

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Five stages with write instructions present |
| C-02 | PASS | ROLE B searches and loads scout; Stage 1 frontmatter requires `scout_anchor` |
| C-03 | PASS | Every stage has Write + Confirm instruction before advancing |
| C-04 | PASS | Stage 5 terminal with findings, confidence, handoff sections |
| C-05 | PASS | All artifact paths use `{topic}-` prefix per write instruction |
| C-06 | PASS | "No step may be skipped or reordered" explicit |
| C-07 | PASS | Named `scout_anchor: [slug]` in ROLE B, echoed in hypothesis frontmatter |
| C-08 | PASS | `next: topic-story` in handoff |
| C-09 | PASS | Thin-evidence flag at Stage 4 required; synthesis qualifies confidence |
| C-10 | PASS | Each stage Confirm line with prose acknowledgment ("Artifact written... Advancing to Stage N") |
| C-11 | PASS | GATE S block with explicit STOP on scout failure; both ROLE A and B must complete before Stage 1 |
| C-12 | PASS | `status_quo_comparator` declared in ROLE A before Stage 1; "Why not [incumbent]?" in hypothesis |
| C-13 | PASS | Every write instruction names full path (`{topic}-hypothesis-{date}.md`, etc.) |
| C-14 | PASS | "Incumbent Defense (MANDATORY)" at each evidence stage; "Incumbent Defense Register (MANDATORY)" in synthesis |
| C-15 | PASS | Hypothesis frontmatter carries `gate_s_cleared: true` and `invariant_registry_confirmed: true` |
| C-16 | PASS | LOCK 1 tasks adversarial reviewer; "Topic-story blocked until challenge addressed" |
| C-17 | PASS | "CE-score = -2. Ceiling: MEDIUM. HIGH not available." CE-score applied in Confidence section |
| C-18 | PASS | ATOMIC DUAL-LOCK fires both locks from single trigger; `co_activation_confirmed: true (must equal dual_lock_fired)` |
| C-19 | PASS | "Cannot be softened, overridden, or bypassed at synthesis" — invariant language for both SESSION INVARIANTS in ROLE A |
| C-20 | PASS | Running tally per stage; "Pre-committed in ROLE A — not a synthesis decision" at each null note |
| C-21 | PASS | Handoff carries `co_activation_confirmed: [must equal dual_lock_fired]` |
| C-22 | PASS | Hypothesis frontmatter has `gate_s_cleared` and `invariant_registry_confirmed` as distinct fields; GATE S requires both |
| C-23 | **PASS** | CAMPAIGN OUTCOME block at Stage 4 computes `incumbent_defense_closed` from `null_tally_final` with explicit `derivation_source: "not derived from dual_lock_fired or co_activation_confirmed"`. Structurally separate from DUAL-LOCK. Handoff labels field "from Stage 4 CAMPAIGN OUTCOME — independent of co_activation_confirmed" |
| C-24 | **PARTIAL** | ROLE A and ROLE B structurally separated and produce distinct fields; `(echoed from ROLE A)` comment in GATE S establishes origin trace. However, no `OWNED ATTESTATION FIELD:` declaration at ROLE header level — ownership is visible only by reading GATE S, not from the ROLE schema alone. An auditor cannot identify the gap from dropping ROLE A without an instruction-level read. 2 pts |

**Score:** 50 (essential) + 30 (recommended) + 15×4 + 2 (aspirational) = **142/144** — Golden

---

### V-02 — Axis: Role Field Ownership

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-22 | PASS | All inherited from R6 V-05 base; ATTESTATION MANIFEST + OWNED ATTESTATION FIELD declarations fully present; FIELD PROVENANCE MAP in hypothesis frontmatter |
| C-23 | **PARTIAL** | `incumbent_defense_closed` present in handoff as `[true if all null, false if any found]` and computed in Stage 5 "CE State" section before DUAL-LOCK. However: (1) computation occurs inside Stage 5, not at a dedicated Stage 4 step structurally prior to synthesis machinery; (2) no explicit `derivation_source` note stating independence from `co_activation_confirmed`. Field is present and independently computable, but independence is implicit — a downstream consumer cannot confirm structural separation without reading Stage 5's sequencing. PARTIAL per C-23 definition ("defining campaign outcome only through the co-activation field is a PARTIAL"). 2 pts |
| C-24 | **PASS** | ATTESTATION MANIFEST at campaign open: "ROLE A owns: invariant_registry_confirmed — Sole structural source. Dropping ROLE A creates an auditable gap." Each ROLE header carries `OWNED ATTESTATION FIELD:`. FIELD PROVENANCE MAP in hypothesis frontmatter with `gate_s_cleared: [ROLE B — sole source]` / `invariant_registry_confirmed: [ROLE A — sole source]`. Dropping either role is an immediately auditable structural gap from schema alone |

**Score:** 50 + 30 + 15×4 + 2 = **142/144** — Golden

---

### V-03 — Axis: Campaign-Open Schema

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-22 | PASS | Full R6 V-05 base; hypothesis frontmatter has both gate fields; GATE S requires both; per-stage running tally with pre-committed references |
| C-23 | **PASS** | HANDOFF SCHEMA declared before Stage 1 opens — declares all fields with derivation sources in a table. `incumbent_defense_closed` row explicitly states: "INDEPENDENT — not derived from dual_lock_fired or co_activation_confirmed. Both are consumers of the same tally; neither derives the other." Independence contract is a pre-declared campaign invariant. Stage 5 handoff references: "per HANDOFF SCHEMA, independent of co_activation_confirmed." Downstream consumer can read the schema at campaign open and verify independence without reading Stage 5 |
| C-24 | **PARTIAL** | No `OWNED ATTESTATION FIELD:` at ROLE A or ROLE B headers. GATE S has `invariant_registry_confirmed: true (echoed from ROLE A)` — the comment establishes source but ownership is instruction-level, not schema-level. Same gap as V-01: an auditor must read GATE S instructions, not ROLE headers, to identify which field loses its source if a role is dropped. 2 pts |

**Score:** 50 + 30 + 15×4 + 2 = **142/144** — Golden

---

### V-04 — Axes: Handoff Field Independence × Role Field Ownership

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-22 | PASS | Full base; ATTESTATION MANIFEST + OWNED FIELD at each ROLE header; FIELD PROVENANCE MAP in hypothesis; CAMPAIGN OUTCOME block at Stage 4 |
| C-23 | **PASS** | CAMPAIGN OUTCOME block at Stage 4 with `null_tally_final` as direct source; `independence_note: "This field is derived from null_tally_final, not from dual_lock_fired or co_activation_confirmed. Computed at Stage 4 before synthesis begins."` Stage 5 confirms: "Independence: confirmed — derived from null_tally_final at Stage 4, not from co_activation_confirmed." Handoff has source annotation on `incumbent_defense_closed`. Two structurally independent derivation paths: both `incumbent_defense_closed` and `co_activation_confirmed` consume the same tally; neither derives from the other |
| C-24 | **PASS** | ATTESTATION MANIFEST at campaign open; ROLE A: `OWNED ATTESTATION FIELD: invariant_registry_confirmed`; ROLE B: `OWNED ATTESTATION FIELD: gate_s_cleared`; hypothesis FIELD PROVENANCE MAP traces each to sole source. Dropping either role drops exactly one attestation field — structurally auditable without reading any stage instructions |

**Score:** 50 + 30 + 16×4 = **144/144** — Golden (v7 ceiling)

---

### V-05 — Full Compound (Role Sequence + Output Format + Inertia Framing + Handoff Field Independence + Role Field Ownership)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-22 | PASS | Complete R6 V-05 base: role sequence (ROLE A before ROLE B), INCUMBENT-DEFENSE TABLE, inertia framing ("incumbent is the status-quo approach you must beat"), per-stage obligation naming |
| C-23 | **PASS** | CAMPAIGN OUTCOME block at Stage 4; `derivation_source: "null_tally_final from INCUMBENT-DEFENSE TABLE — not derived from dual_lock_fired or co_activation_confirmed. Both incumbent_defense_closed and co_activation_confirmed derive from the same underlying tally through separate derivation paths."` Handoff FIELD PROVENANCE lists `incumbent_defense_closed: [Stage 4 CAMPAIGN OUTCOME — derived from null_tally_final]` alongside the other fields. Independence is visible both at the computation step (Stage 4) and the audit trail (FIELD PROVENANCE) |
| C-24 | **PASS** | ATTESTATION MANIFEST + `OWNED ATTESTATION FIELD: invariant_registry_confirmed` at ROLE A header + `OWNED ATTESTATION FIELD: gate_s_cleared` at ROLE B header + hypothesis FIELD PROVENANCE MAP with manifest references. Visual delimiter (`======`) on ATOMIC DUAL-LOCK confirms block boundary. `cap_applied: true` field in LOCK 2 creates additional audit record. Stress-tested in anchor designation: dropping ATTESTATION MANIFEST fails C-24 while retaining C-23; replacing CAMPAIGN OUTCOME block fails C-23 while retaining C-24 — independent failure modes confirmed |

**Score:** 50 + 30 + 16×4 = **144/144** — Golden (v7 ceiling)

---

### Ranking

| Rank | Variation | C-23 | C-24 | Composite | Band |
|------|-----------|------|------|-----------|------|
| 1 (tie) | V-04 | PASS | PASS | 144/144 | Golden |
| 1 (tie) | V-05 | PASS | PASS | 144/144 | Golden |
| 3 (tie) | V-01 | PASS | PARTIAL (2) | 142/144 | Golden |
| 3 (tie) | V-02 | PARTIAL (2) | PASS | 142/144 | Golden |
| 3 (tie) | V-03 | PASS | PARTIAL (2) | 142/144 | Golden |

All five variations are **Golden** (all essential criteria pass; all composites ≥ 80).

---

### Excellence Signals — V-05 (Anchor)

**What V-05 adds beyond V-04 (the other ceiling variation):**

1. **Per-stage obligation naming with specific reviewer** — Stage 2 null note: `"Obligations = A ([reviewer_type]) + B (CE-score = -2) pending if S3+S4 also null."` The specific reviewer type from ROLE A appears at each tally step. An auditor can read Stage 2's note and know which reviewer is committed without looking back at ROLE A. V-04 references "pre-committed obligations" generically; V-05 names them by type.

2. **Visual delimiter on ATOMIC DUAL-LOCK** — The `======` border on the dual-lock block in V-05 makes the activation boundary visually auditable. V-04's DUAL-LOCK has the same content but no visual delimiter — partial parsing is possible.

3. **`cap_applied: true` in LOCK 2** — Explicit named field confirming the confidence cap fired, separate from `co_activation_confirmed`. Creates an additional artifact-level record. C-17 requires the cap to be mechanical; `cap_applied` confirms it actually fired as a named field.

4. **FIELD PROVENANCE at handoff level** — V-05 adds a `FIELD PROVENANCE` block inside the Handoff section that traces three fields (`invariant_registry_confirmed`, `gate_s_cleared`, `incumbent_defense_closed`) to their sole sources. V-04 has a FIELD PROVENANCE MAP at hypothesis frontmatter but not repeated in the handoff. The handoff provenance makes the full audit trail available to downstream consumers without reading the hypothesis artifact.

None of these patterns expose a structural gap not closed by v7 criteria — they are quality refinements within the same 144/144 ceiling. No new rubric-extractable criteria emerge from this round.

---

```json
{"top_score": 144, "all_essential_pass": true, "new_patterns": []}
```
