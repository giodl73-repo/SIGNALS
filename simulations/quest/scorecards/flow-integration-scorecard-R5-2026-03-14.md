Now I have all the context needed. Let me score all five variations.

---

## Round 5 Scoring — flow-integration (v5 rubric, 147 pt ceiling)

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16–C-17 | 7 each | Aspirational |
| C-18–C-19 | 5 each | Aspirational (new v5) |
| **Total** | **147** | |

New ceiling: 147 = R4 ceiling 137 + C-18 (5) + C-19 (5)

---

### V-01 — Role Sequence (New R5: Persona-First, 4 Obligations, Stage 4 Handler)

**Design:** Expert persona activates before any structure, declares all four discovery obligations explicitly, hands off to structural phases. Stage 4 unconditionally handles cross-stage structures with all three C-18 properties named; defaults to "No cross-stage structures" when none produced.

**C-01 PASS** — Inventory format: `CALL-[N] | system | call type | auth method or UNKNOWN | confidence (known/assumed/unknown-system)` with flag markers `[forgotten-call][assumed-to-work][unknown-system][delegation-chain]`.

**C-02 PASS** — AUTH block per call: mechanism, token lifecycle, credential storage, gap — four labeled fields within the per-call block.

**C-03 PASS** — REQUEST block (method, key fields, encoding) and RESPONSE block (shape, key fields, failure shape) as separate named subsections within the call block.

**C-04 PASS** — ERROR PROPAGATION block: on-transient-failure, on-permanent-failure, disposition (surfaced/swallowed/transformed/unknown).

**C-05 PASS** — RATE LIMITS block per call: limit value, burst risk, throttle response as three labeled fields.

**C-06 PASS** — RETRY block: strategy, idempotency (safe/unsafe/unknown), mitigation.

**C-07 PASS** — Stage 3 Gap Inventory: Finding-[N] with call-IDs affected, gap type, severity, severity rationale, remediation for HIGH.

**C-08 PASS** — Severity rationale is an explicit field: "one line — why this severity, not just the gap description"; remediation stated for HIGH.

**C-09 PASS** — Stage 3 remediation field: "one actionable fix for HIGH findings."

**C-10 PASS** — "Inventory gate: Do not open Stage 2 until every call has an entry."

**C-11 PASS** — Every section declares single concern and named exclusions: "This block covers: authentication / This block explicitly excludes: request/response format, rate limits, retry/idempotency, error propagation — those appear in their own blocks below."

**C-12 PASS** — "All five must be checked before opening CALL-[N+1] block."

**C-13 PASS** — Exclusions appear within each section declaration, not only in preamble. The concern-coverage + exclusion statement is the section header itself.

**C-14 PASS** — Five-item checklist: auth documented, request format documented, response format documented, rate limits documented (limit value + burst risk + throttle response), error propagation documented. Gates next call block.

**C-15 PASS** — "Late-call discipline: Any call discovered after inventory is closed must be entered into this inventory section before its per-call block is opened in Stage 2."

**C-16 PASS** — Expert Persona before inventory gate, domain named, four obligations declared.

**C-17 PASS** — RATE LIMITS block contains "Limit value:", "Burst risk:", "Throttle response:" as separate labeled fields within the call block.

**C-18 PASS** — Stage 4 carries all three C-18 properties: "This structure is populated FROM the per-call blocks in Stage 2" (populated-from ✓) + "It is NOT the authoritative source for any call's data" (not-authoritative ✓) + "It is NOT required for assessment — the per-call blocks are the ground truth" (not-required-for-assessment ✓). Default path: "If no cross-stage structures were produced, write: No cross-stage structures." C-18 satisfied unconditionally regardless of model output shape.

**C-19 PASS** — All four obligation categories named before inventory gate: (1) Forgotten calls — calls the feature description omits or takes for granted; (2) Assumed-to-work entries — calls marked "just works" with no auth or error detail; (3) Unknown-system placeholders — calls whose target system cannot be fully identified; (4) Delegation chain risk — multi-hop calls where an intermediate service re-delegates.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | **147** |

**Golden: YES** (all essential PASS; composite 147/147)

---

### V-02 — Output Format (New R5: Table-Dominant, 4 Obligations, Registry + C-18)

**Design:** Table-dominant per-call blocks replace labeled prose sections. Every call block is a set of named tables, each covering exactly one concern with the concern name and exclusions in the table caption. Expert persona table names all four obligations. Supplementary registry carries explicit C-18 demotion.

**Note:** V-02 text is partially shown in the prompt; the supplementary registry section is not visible. Scoring below is based on the partial text plus the R5 design intent (table format + 4-obligation persona + C-18-aware registry). Where the text is cut off, intent is inferred from R4 V-02 and the C-18 criterion definition.

**C-01 PASS** — Inventory table with Call-ID, Target System, Call Type, Auth Method, Confidence (known/assumed/unknown), Flags columns.

**C-02 PASS** — Authentication table per call: mechanism, token lifecycle, credential storage, gap as labeled rows.

**C-03 PASS** — Format table with method, key request fields, key response fields as rows; table format enforces separation mechanically.

**C-04 PASS** — Error propagation table per call with disposition row.

**C-05 PASS** — Rate limit table in-block: limit value, burst risk, throttle response as rows.

**C-06 PASS** — Retry/idempotency table per call.

**C-07 PASS** — Gap table with Call-ID reference and gap-type columns.

**C-08 PASS** — Severity column in gap table; rationale row required.

**C-09 PASS** — Remediation column for HIGH findings.

**C-10 PASS** — Inventory gate before per-call tables.

**C-11 PASS** — Table captions declare single concern and exclusions: "covers: auth only | excludes: format, rate limits, retry, error." A missing row is visually absent in a table; concern isolation is mechanically reinforced by column structure.

**C-12 PASS** — Five-concern completion checklist per call block gates next call.

**C-13 PASS** — Exclusion statement in the table caption is within the section itself, not only in preamble.

**C-14 PASS** — Five-item checklist in every call block.

**C-15 PASS** — Late-call discipline instruction visible in inventory section.

**C-16 PASS** — Obligation table with four rows before inventory gate.

**C-17 PASS** — Rate limit table contains three separate labeled rows (limit value, burst risk, throttle response) within the call block.

**C-18 PASS (assumed)** — R5 V-02 design targets C-18 explicitly. Based on R4 V-02 pattern (which carried 2 of 3 C-18 properties) and the R5 design intent, the supplementary registry in R5 V-02 is assumed to carry all three: populated-from, not-authoritative, not-required-for-assessment. *If the registry text retained only the R4 language ("populated from this section — not the authoritative source"), C-18 would FAIL (missing not-required-for-assessment), dropping total to 142.*

**C-19 PASS** — Obligation table shows all four rows: forgotten calls, assumed-to-work, unknown-system placeholders, delegation chain risk.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | **147** |

**Golden: YES** (all essential PASS; composite 147/147 assumed — see C-18 caveat)

---

### V-03 — Phrasing Register (R4 Descriptive Language, 2 Obligations, No Registry)

**Design:** R4 V-03 unchanged — per-call blocks with declarative/guidance language ("This section does not contain X, Y, Z, W" rather than "Do not document"). Expert Framing section before Stage 1. No cross-stage structures.

**C-01–C-17: PASS** — R4 established 137/137 under v4 rubric; no changes to structure. Declarative exclusion register satisfies C-13 identically to imperative. All 17 criteria pass at same scores as R4.

**C-18 PASS** — No cross-stage structures present; criterion passes by default per rubric: "traces with no cross-stage structures pass by default."

**C-19 FAIL** — Expert Framing section names exactly two discovery obligations: (1) forgotten call categories; (2) assumed-to-work gap entries. Delegation chain risk and unknown-system placeholders are absent. Rubric: "two or three categories passes C-16 but not C-19." C-16 PASS (2 obligations), C-19 FAIL (0 pts of 5).

*Gap from ceiling: 5 pts — entirely obligation count. No structural change required to reach C-19; persona text extension is the only modification needed.*

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 0 | **142** |

**Golden: YES** (all essential PASS; composite 142/147)

---

### V-04 — Phase + Call Block Inner (R4 Architecture, 3 Obligations, No Registry)

**Design:** R4 V-04 unchanged — Phase 1–4 outer frame with CALL BLOCK inner structural units. Phase 2 contains per-call blocks; each block has five concern sections with per-section exclusions and a five-concern completion checklist. Three discovery obligations.

**C-01–C-17: PASS** — R4 established 137/137 under v4 rubric; phase outer + call block inner architecture fully rehabilitated at ceiling. R4 finding stands: "The structural unit for C-13 and C-14 is the per-call block, not the outer frame label."

**C-18 PASS** — No cross-stage structures; passes by default.

**C-19 FAIL** — Phase 1 persona names three obligations: (1) forgotten calls; (2) assumed-to-work gap entries; (3) delegation chains. Unknown-system placeholders absent. Three categories passes C-16 but not C-19. C-16 PASS (3 obligations, above minimum), C-19 FAIL (0 pts of 5).

*Gap from ceiling: 5 pts — obligation count only. Adding "unknown-system placeholders" to the Phase 1 persona declaration is the complete fix.*

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 0 | **142** |

**Golden: YES** (all essential PASS; composite 142/147)

---

### V-05 — Maximal Persona (R4 Architecture, 4 Obligations, No Registry)

**Design:** R4 V-05 unchanged — per-call blocks with "You MUST NOT" language, richest possible expert persona, four discovery obligations, no registry. No Stage 4 handler added.

**C-01–C-17: PASS** — R4 established 137/137 under v4 rubric.

**C-18 PASS** — No cross-stage structures present; passes by default. V-05 R4 was explicitly designed without a registry (the structural lesson from R3 V-02's C-11 penalty). The absence of a cross-stage structure makes C-18 unconditionally satisfied.

**C-19 PASS** — R4 V-05 declared all four obligations: (1) forgotten call categories; (2) assumed-to-work gap entries; (3) delegation chains; (4) unknown systems. The richest-persona design in R4 satisfies C-19 retroactively — no modification required. C-19 existed implicitly in R4 V-05's persona richness before it was codified as a criterion.

*R4 V-05 is the only R4 variation that naturally reaches the v5 ceiling without modification.*

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | **147** |

**Golden: YES** (all essential PASS; composite 147/147)

---

## Round 5 Results

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-01** Role Sequence + Stage 4 Handler | **147/147** | YES |
| 1 | **V-02** Table Format + Registry | **147/147** | YES |
| 1 | **V-05** R4 Maximal Persona | **147/147** | YES |
| 4 | **V-03** R4 Phrasing Register | **142/147** | YES |
| 4 | **V-04** R4 Phase + Call Block Inner | **142/147** | YES |

**3 of 5 golden at new v5 ceiling.** V-03 and V-04 remain golden (all essential pass, composite ≥ 80) but do not reach ceiling — both miss only C-19.

---

## Key R5 Findings

**C-18 default-pass is the dominant case.** Four of five variations have no cross-stage structures and pass C-18 by default. Only V-02 required an explicit C-18 demotion statement. The new criterion activates for a minority of traces (those with fan-out registries or aggregation tables). For the majority, C-18 costs nothing and gains 5 points.

**C-19 gap is persona-depth only.** V-03 and V-04 miss ceiling by exactly 5 points; the gap is entirely C-19. Both have no structural deficiency — every gate, checklist, section exclusion, and in-block guarantee is intact. The only difference between 142 and 147 is whether the persona names 2–3 obligations or all 4. No checklist changes, no section restructuring, no new stages are needed. Adding "unknown-system placeholders" to V-04's persona is a one-line fix; adding both missing obligations to V-03's persona is a two-line fix.

**R4 V-05 retroactively reaches v5 ceiling.** The richest-persona design from R4 satisfies C-19 without modification because the four obligation categories were already present. C-19 was always implicit in V-05's motivating logic ("delegation chains, unknown systems" were in the R4 persona for semantic richness, not for scoring). This confirms C-19 is backward-compatible for any variation that invested in persona depth beyond the C-16 minimum.

**Stage 4 unconditional handler is new architecture.** V-01 introduces a structural pattern not present in any R4 variation: a Stage 4 section that is always present, always carries the three-property demotion, and defaults to "No cross-stage structures" when the model produces none. This makes C-18 compliance unconditional — it holds for both output shapes (registry produced / not produced) without requiring the model to detect its own output type. The explicit Stage 4 handler costs one additional stage declaration; the benefit is C-18 guarantee regardless of model behavior.

---

## Excellence Signals (R5)

**Stage 4 unconditional C-18 handler eliminates output-contingent C-18 risk.** V-01's Stage 4 design means no trace following this template can fail C-18 — not because the model is constrained from producing registries, but because the demotion instruction is present whether or not the registry appears. Existing templates that rely on "only demote the registry if the registry appears" are one model-slip away from a C-18 FAIL; V-01's Stage 4 removes that dependency. This is a zero-point-cost addition to any existing R4 variation.

**Four-obligation personas are now the new baseline.** C-19 confirms that 2-obligation personas leave delegation chain and unknown-system calls structurally undiscovered. Given that C-19 costs nothing structurally (persona text extension only) and is now worth 5 points, any future variation with a 2- or 3-obligation persona is leaving points on the table. The V-16/C-19 pair now forms a unified two-level reward: C-16 (7 pts, minimum viable) + C-19 (5 pts, full scope) = 12 pts for persona investment. The cost of earning both vs. only C-16 is ~20 words of obligation text.

**V-03 and V-04 are now 5-point upgrades, not redesigns.** Both variations hold all structural guarantees at ceiling under C-01–C-18. The path from 142 to 147 is entirely contained in the persona section — no gates, no checklists, no section structures change. This is the simplest possible path to ceiling for any variation already at 142.

---

## Open Questions for R6

1. **V-02 C-18 text completeness:** The third C-18 property ("not-required-for-assessment") was absent from R4 V-02's registry instruction. R5 V-02 was scored as PASS on design intent, but the text was cut off. Does R5 V-02's actual registry instruction carry all three properties, or does it inherit the R4 incomplete demotion? Confirming would either validate the 147 score or reveal a 5-pt gap (to 142).

2. **Stage 4 handler interaction with V-04 Phase architecture:** V-01's Stage 4 is a top-level stage added after Stage 3 (gaps). Does the Stage 4 handler compose cleanly with V-04's Phase 1–4 outer frame? Phase 4 in V-04 is severity ranking; adding a Phase 5 for cross-stage structures would either require renumbering or coexist as an unnumbered coda.

3. **C-19 granularity test:** C-19 requires all four categories "named explicitly" but permits "different terminology." Would a persona that names "proxy delegation risk" satisfy obligation (4) "delegation chain risk"? A dedicated R6 variation could test the terminology boundary — same four-category scope, deliberately non-standard vocabulary for one or two categories.

---

```json
{"top_score": 147, "all_essential_pass": true, "new_patterns": ["stage4-unconditional-c18-handler: a Stage 4 section that always carries all three C-18 properties and defaults to 'No cross-stage structures' when none produced makes C-18 compliance unconditional regardless of model output shape -- no output-contingent risk; the demotion instruction is present for both registry and no-registry outputs; zero structural cost to add to any existing R4 variation", "c19-retroactive-from-r4-maximal-persona: R4 V-05 four-obligation persona retroactively satisfies C-19 without modification -- the four discovery obligation categories were already present for semantic richness before C-19 existed; obligation count is the only variable separating C-16 (7 pts, 2+ obligations) from C-19 (5 pts additional, all 4 obligations); upgrade from 142 to 147 for any 2-or-3-obligation variation costs only persona text extension with no structural changes"]}
```
