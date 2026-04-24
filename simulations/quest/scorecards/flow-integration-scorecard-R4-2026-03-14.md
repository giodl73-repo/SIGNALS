Now I have everything I need. Let me score all five variations.

---

## Round 4 Scoring — flow-integration (v4 rubric, 137 pt ceiling)

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16 | 7 | Aspirational (new v4) |
| C-17 | 7 | Aspirational (new v4) |
| **Total** | **137** | |

C-16 + C-17 = 14 new points (137 − 123 = 14), split 7+7 as equal-weight new criteria.

---

### V-01: Role Sequence — C-16 Minimal Compliant Expert Persona

**Design:** V-01 R3 structure (per-call blocks, full in-block Section D) unchanged. Prepends a minimal expert persona naming domain + exactly two discovery obligations.

**C-01 PASS** — Inventory table with KNOWN/ASSUMED/UNKNOWN-SYSTEM statuses; call type taxonomy includes token-acquire, health-check, webhook, event-subscribe.
**C-02 PASS** — Section A: auth mechanism, token expiry, credential rotation, security note, gap flag. "Do not skip fields because a system is familiar."
**C-03 PASS** — Section B: method, headers, body, response as four separate labeled lines with "All four fields are required."
**C-04 PASS** — Section C: disposition, transformation detail, gap flag. "A call that 'never fails' is not exempt."
**C-05 PASS** — Section D per block: documented rate limit, burst risk, throttle response, gap flag. Absence = RATE-EXPOSURE gap.
**C-06 PASS** — Section E: strategy, parameters (initial delay / backoff factor / max delay / jitter), max attempts, idempotency guarantee, mitigation, gap flag.
**C-07 PASS** — Stage 3: Finding ID, Call ID, Section, Gap Type, Description. At-minimum requirements for AUTH, RATE, RETRY/IDEMPOTENCY findings.
**C-08 PASS** — Stage 4: "ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale. No row is exempt." HIGH-first ordering.
**C-09 PASS** — Concrete HIGH remediation: exact header name, backoff parameters, specific flow replacement. "Generic advice does not pass."
**C-10 PASS** — "Stage 2 does not begin until this table has a row for every cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1." INVENTORY GATE explicit.
**C-11 PASS** — Every section: "Concern: X only. Do not document Y, Z, A, B here." Five sections, five distinct concerns. Rate limits in Section D, retry/idempotency in Section E, no mixing.
**C-12 PASS** — "Do not open the next call block until all five boxes are checked." + trace completion gate. Both per-block and trace-level gates present.
**C-13 PASS** — Each section carries explicit concern declaration + named exclusion of all four other concerns within the section body. Section A: "Concern: authentication only. Do not document request format, error handling, rate limits, or retry logic here." Four excluded concerns named per section, not preamble-only.
**C-14 PASS** — Five items (A–E) covering all five concerns. Gate: "Do not open the next call block until all five boxes are checked."
**C-15 PASS** — LATE-CALL RULE: "you must STOP, add it here with the next available Call ID, and THEN write its call block. You may not write a call block for a call that has no inventory entry."
**C-16 PASS** — Expert persona appears before the inventory gate. Domain named: "Backend Integration Domain Expert. Your domain: connectors, APIs, and MCP integrations between enterprise systems." Two domain-specific obligations: (1) forgotten-call inventory covering token acquisition, health checks, webhook receipts; (2) assumed-to-work gap entries. Meets minimum threshold exactly.
**C-17 PASS** — Section D: limit value, burst risk, throttle response as three separate labeled fields within the call block. No registry deferral. Absence documented as RATE-EXPOSURE gap in-block.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | **137** |

**Golden: YES** (all essential PASS; composite 137/137)

---

### V-02: Output Format — Hybrid Registry Fixed

**Design:** Section D restored to full in-block rate limit data (all three fields). Stage 3 Rate Limit Registry demoted to supplementary fan-out index, explicitly prohibited from being authoritative. Expert persona with 4 obligations added.

**C-01 PASS** — Inventory table; INVENTORY GATE; LATE-CALL RULE covering Stage 2 and Stage 3 discovery.
**C-02 PASS** — Section A: all five fields with gap flag.
**C-03 PASS** — Section B: four separate labeled lines. "All four fields are required as separate labeled lines."
**C-04 PASS** — Section C: disposition, gap flag. "Never fails" is not a valid disposition.
**C-05 PASS** — Section D per block: limit value, burst risk, throttle response. "Absence of a documented limit is itself a gap."
**C-06 PASS** — Section E: strategy, parameters, max attempts, idempotency, mitigation, gap flag.
**C-07 PASS** — Stage 4 Gap Inventory (renumbered from R3): Finding ID, Call ID, Section, Gap Type, Description. At-minimum requirements.
**C-08 PASS** — Stage 5: rationale for ALL findings.
**C-09 PASS** — Concrete HIGH remediation with specific examples.
**C-10 PASS** — INVENTORY GATE blocks Stage 2 until complete.
**C-11 PASS** — Each section single-concern with named exclusions within the section body. Rate limit data is fully in Section D of each call block. Stage 3 is explicitly supplementary and prohibited from containing data not already in Section D. A reviewer can locate complete rate limit data within the call block without scanning Stage 3. The scanning-elsewhere violation from R3 V-02 is resolved: the call block is now self-contained. No concern requires crossing to Stage 3 to be complete.
**C-12 PASS** — "Do not open the next call block until all five boxes are checked." Checklist item D explicitly references "in-block."
**C-13 PASS** — Every section carries "Concern: X only. Do not document Y, Z, A, B in this section." within the section body. Section D: "Concern: rate limit exposure for this call's target system only. Do not document authentication, request format, error handling, or retry logic in this section."
**C-14 PASS** — Five items covering all five concerns. Gate for next block and trace completion.
**C-15 PASS** — "If you identify a call during Stage 2 or Stage 3 that is not in this table, you must STOP, add it here with the next available Call ID, and THEN continue."
**C-16 PASS** — Domain: "connectors, APIs, and MCP integrations." Four discovery obligations: forgotten calls, assumed-to-work gap entries, delegation chain risk, unknown systems. Richest persona form. Well above minimum threshold.
**C-17 PASS** — Section D: three separate labeled fields (limit value, burst risk, throttle response) within the call block. Explicit instruction: "Document the actual rate limit data here, inside this block. Do not defer to Stage 3. The Stage 3 registry is a supplementary fan-out index populated from this section — it is not the authoritative source."

**Supplementary registry neutrality confirmed:** Stage 3 registry presence does not trigger C-11 penalty because the pass condition is "complete rate limit data locatable within the call block" — Section D satisfies this fully. The registry is additive convenience for fan-out features, not a concern-contamination risk.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | **137** |

**Golden: YES** (all essential PASS; composite 137/137)

---

### V-03: Phrasing Register — Descriptive/Guidance Style

**Design:** Per-call blocks (same structural guarantees as V-01/V-05), but declarative/guidance language throughout. Concern exclusions use "This section does not contain X, Y, Z, W" rather than imperatives.

**C-01 PASS** — Stage 1 inventory table; "Stage 2 begins when this table has a row for every cross-system call." LATE-CALL RULE with procedure stated.
**C-02 PASS** — Section A: all five fields with gap flag.
**C-03 PASS** — Section B: four separate labeled fields. "A well-formed Section B has four separate labeled lines. A single merged field combining method, headers, body, and response is not a complete Section B."
**C-04 PASS** — Section C: disposition, gap flag. "A call that 'never fails' still requires a disposition."
**C-05 PASS** — Section D per block: limit value, burst risk, throttle response, gap flag. "When the documented limit is unknown or undocumented, that absence is a gap belonging in this section, not an omission."
**C-06 PASS** — Section E: full retry and idempotency fields.
**C-07 PASS** — Stage 3: gap table with at-minimum requirements explicitly stated.
**C-08 PASS** — Stage 4: "Every finding — HIGH, MEDIUM, and LOW — requires a one-line rationale. No finding is exempt, including LOW."
**C-09 PASS** — "A HIGH remediation names the exact header, the exact backoff parameters, or the specific flow replacement. 'Add retry logic' is not a remediation."
**C-10 PASS** — "Stage 2 begins when this table has a row for every cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1." Inventory-first gate present.
**C-11 PASS** — Each section single-concern. Rate limits in Section D of each call block. Sections do not mix concerns.
**C-12 PASS** — "When all five boxes are checked, the next call block may open. Stage 2 is not complete until every Call ID from Stage 1 has a fully checked checklist." Both per-block and trace-completion gates.
**C-13 PASS** — Declarative register satisfies C-13. Section A: "Concern: authentication only. This section does not contain request format, error handling, rate limit data, or retry logic." This is an explicit named exclusion of all four other concerns, within the section body, not merely at a preamble level. R3 finding ("Do not" vs. "You MUST NOT" is aesthetic) extends cleanly: "This section does not contain X, Y, Z, W" names the excluded concerns explicitly — register difference is cosmetic, not structural.
**C-14 PASS** — Five-item checklist within each call block gates next block and trace completion.
**C-15 PASS** — "When a call is identified during Stage 2 that is not in this table, the right procedure is to stop, add the call here with the next available Call ID, and then continue the call block. A call block cannot be written for a call without an inventory row."
**C-16 PASS** — "## Expert Framing" section before Stage 1. Domain: "backend integration domain expert specializing in connectors, APIs, and MCP integrations." Two domain-specific obligations: forgotten call categories; assumed-to-work gap entries. Minimum-viable form; same score as V-05 on C-16 (binary pass/fail at two obligations).
**C-17 PASS** — Section D: "The actual rate limit data — limit value, burst risk, and throttle response — is documented here, in this block." Three separate labeled fields. PASS.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | **137** |

**Golden: YES** (all essential PASS; composite 137/137)

**V-03 R4 finding:** Declarative exclusion register satisfies C-13 identically to imperative register. "This section does not contain X, Y, Z, W" is an explicit named exclusion. Phrasing preference has no scoring effect.

---

### V-04: Combined — Lifecycle (Phase Frame + Call Block Inner Units) + Role Sequence

**Design:** Phase 1–4 outer frame. Phase 2 contains CALL BLOCK inner structural units — each call block has five concern sections with per-section exclusions and a five-concern completion checklist. This is the definitive test of R3 Open Q3.

**C-01 PASS** — Phase 1 inventory table; PHASE 1 GATE; LATE-CALL RULE.
**C-02 PASS** — Section A: all five fields.
**C-03 PASS** — Section B: "All four fields are required as separate labeled lines."
**C-04 PASS** — Section C: disposition, gap flag. "'Never fails' is not a valid disposition."
**C-05 PASS** — Section D per call block: limit value, burst risk, throttle response, gap flag.
**C-06 PASS** — Section E: full retry/idempotency fields.
**C-07 PASS** — Phase 3 Gap Inventory: Finding ID, Call ID, Section, Gap Type, Description. At-minimum requirements.
**C-08 PASS** — Phase 4: "ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale. No row is exempt."
**C-09 PASS** — "Concrete, call-specific remediation: exact header name, exact backoff parameters, or specific flow replacement. Generic advice does not pass."
**C-10 PASS** — "PHASE 1 GATE: Phase 2 does not begin until every cross-system call has a row in this table. No per-call analysis of any kind appears in Phase 1." Inventory-first gate explicit.
**C-11 PASS** — Each section within each call block: "Concern: X only. Do not document Y, Z, A, B in this section." Five sections, five distinct concerns. Rate limits in Section D within call blocks.
**C-12 PASS** — "Do not open the next call block until all five boxes are checked." + "Phase 2 is not complete until every Call ID from Phase 1 has a call block with a fully checked completion checklist."
**C-13 PASS** — *Definitive answer to R3 Open Q3.* The "PHASE 2 -- PER-CALL ANALYSIS" header contains no concern exclusion statements — it says only to process each call in a dedicated block. Exclusion statements are within "#### Section A" (and B, C, D, E) inside "### CALL BLOCK" — these are per-section units inside call blocks, not phase-level preambles. The C-13 rubric phrase "a phase-level label alone does not pass" refers to structures where the exclusion lives ONLY at the phase header (R3 V-03/V-04 pattern). Here, the "## PHASE 2" header is a structural wrapper only; the actual exclusion statements appear within each section inside each call block. Per-section exclusions within nested call blocks retain full C-13 credit regardless of outer frame label.
**C-14 PASS** — Five-item checklist inside "### CALL BLOCK" with "Do not open the next call block until all five boxes are checked." Checklist gates the next block (not the next phase). All five items present and checkable at the time the gate fires.
**C-15 PASS** — "Any call identified during Phase 2 that is not in this table must be added here with the next available Call ID before its call block is opened."
**C-16 PASS** — Domain: "connectors, APIs, and MCP integrations." Three discovery obligations: forgotten calls, assumed-to-work gap entries, delegation chains. Above minimum threshold (three vs. two required).
**C-17 PASS** — Section D: three separate labeled fields in-block. "Absence of a documented limit is itself a gap — document it here, do not omit it." No registry.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | **137** |

**Golden: YES** (all essential PASS; composite 137/137)

**V-04 finding (R3 Open Q3 resolved):** Phase outer frame + call block inner units scores C-13/C-14 at full ceiling. The structural unit for C-13 and C-14 is the per-call block, not the outer frame label. Phase architecture is fully rehabilitated when CALL BLOCKs containing per-section concern exclusions and five-concern checklists are nested inside phases. "Phase-level label alone does not pass" applies only when the exclusion statement is at the phase header itself — not when it is within per-section units inside nested call blocks.

---

### V-05: Combined — Expert Persona Maximal (C-16 Richest) + Structural Ceiling (C-17 Explicit)

**Design:** V-05 R3 "You MUST NOT" structure (123/123 under v3) plus richest expert persona (domain named richly, four obligations, gap sensitivity) plus explicit C-17 anchor in Section D naming the three required fields and prohibiting registry substitution.

**C-01 PASS** — Stage 1 inventory; INVENTORY GATE; named LATE-CALL RULE box with 3-step procedure and "no exceptions" language.
**C-02 PASS** — Section A: all five fields. "Concern: authentication only. You MUST NOT document request format, error handling, rate limits, or retry logic in this section."
**C-03 PASS** — Section B: four separate labeled lines. "A merged cell that combines method, headers, body, and response is not acceptable and does not satisfy this section."
**C-04 PASS** — Section C: disposition, transformation detail, gap flag. "'This call never fails' is not a valid disposition."
**C-05 PASS** — Section D per block: three separate labeled fields. Absence = gap.
**C-06 PASS** — Section E: full retry/idempotency fields.
**C-07 PASS** — Stage 3: Finding ID, Call ID, Section, Gap Type, Description. At-minimum requirements.
**C-08 PASS** — "ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale. Rationale is not optional for any row, including LOW findings."
**C-09 PASS** — Three concrete example forms in Stage 4 rules: exact header, exact backoff parameters, specific flow replacement. "Generic advice ('add retry logic', 'implement error handling', 'use idempotency') does not pass."
**C-10 PASS** — INVENTORY GATE + named LATE-CALL RULE box.
**C-11 PASS** — "**Concern: X only. You MUST NOT document Y, Z, A, B in this section.**" in every section. Five sections, five distinct concerns.
**C-12 PASS** — "This checklist gates two things: (1) the next call block — do not open it until all five boxes are checked; (2) trace completion — the trace is not complete until every Call ID from Stage 1 has a call block with all five boxes checked here."
**C-13 PASS** — "**You MUST NOT document [other four concerns] in this section.**" appears within every section in every call block. All four excluded concerns named per section. Not preamble-only.
**C-14 PASS** — Exactly five items (A–E). Dual gate: next block AND trace completion. Checklist item D explicitly: "Section D (Rate limit) — limit value, burst risk, and throttle response each documented as separate labeled fields in-block."
**C-15 PASS** — Named LATE-CALL RULE box, numbered 3-step procedure. "There are no exceptions — a call discovered on the last block is subject to the same rule as a call discovered on the first."
**C-16 PASS** — Richest possible persona. Domain: "enterprise connector and API integration patterns: OAuth delegation chains, MCP tool invocations, Power Automate connector actions, REST and GraphQL APIs, event bus subscriptions, and cross-tenant API access." Four discovery obligations: forgotten call categories, assumed-to-work gap entries, delegation chains, unknown systems. Gap sensitivity: "401 storms, 429 cascades, silent data loss, duplicate writes under retry." Maximum semantic quality — scores same rubric credit as V-01 (C-16 is binary pass/fail).
**C-17 PASS** — Section D: "**The three required fields for this section are: (1) documented rate limit value, (2) burst risk, and (3) throttle response. These are three separate labeled fields. A cross-reference to an external registry is not a substitute for these fields.**" Explicit C-17 anchor, prohibits registry substitution. Checklist item D confirms "as separate labeled fields in-block." Maximum C-17 semantic quality.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | **137** |

**Golden: YES** (all essential PASS; composite 137/137)

---

## Round 4 Results

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-01** Minimal Expert Persona | **137/137** | YES |
| 1 | **V-02** Hybrid Registry Fixed | **137/137** | YES |
| 1 | **V-03** Descriptive Register | **137/137** | YES |
| 1 | **V-04** Phase + Call Block Inner | **137/137** | YES |
| 1 | **V-05** Maximal Persona + C-17 Anchor | **137/137** | YES |

**5 of 5 golden.** First round where every variation reaches the new 137-point ceiling.

---

## Key R4 Findings

**V-04 resolves R3 Open Q3 definitively.** Phase outer frame + call block inner units scores C-13/C-14 at full ceiling. The hard prerequisite for C-13 and C-14 is per-call block structural units with per-section concern exclusions — not the absence of an outer phase label. "Phase-level label alone does not pass" applies only when the exclusion statement lives at the phase header, not when per-section exclusions exist within nested call blocks. Phase architecture is fully rehabilitated at ceiling.

**C-16 is binary pass/fail at two obligations.** V-01 (minimum-viable: domain + 2 obligations) and V-05 (maximal: domain named richly, 4 obligations, gap sensitivity) score identically on C-16. Persona richness beyond the minimum enriches semantic quality of call discovery and auth depth but produces no additional rubric credit. The minimum-viable persona holds ceiling.

**V-02 supplementary registry is C-11 neutral.** A supplementary fan-out index that is explicitly prohibited from containing data not already in Section D does not trigger a C-11 scanning-elsewhere violation. The call block is self-contained; the registry is additive. V-02 R4 reaches ceiling while preserving the fan-out readability benefit.

**Declarative register satisfies C-13.** "This section does not contain X, Y, Z, W" satisfies C-13 identically to "Do not document X, Y, Z, W here." The phrasing register (descriptive vs. imperative vs. "You MUST NOT") has no scoring effect as long as the excluded concerns are named within the section body.

---

## Excellence Signals (R4)

**Phase outer + call block inner is a ceiling-safe hybrid architecture.** Teams building lifecycle-oriented templates (Phase 1: Inventory, Phase 2: Analysis, Phase 3: Gaps, Phase 4: Severity) can preserve the phase framing for readability while achieving C-13/C-14 ceiling by nesting CALL BLOCK structural units inside Phase 2. The call block is the analysis atom; the phase is the organizational frame. Both coexist at full score.

**Minimum-viable expert persona holds ceiling on C-16.** Two domain-specific discovery obligations satisfy C-16 fully. No pressure to invest in persona enrichment for rubric purposes; invest in persona richness only for output quality (richer call inventories, deeper auth analysis).

**Supplementary registry is a free readability win in fan-out features.** A rate limit registry demoted to supplementary status (Section D authoritative, registry = convenience index) preserves C-11 PASS and C-17 PASS. V-02 R4 demonstrates the architecture that captures both the fan-out consolidation benefit and the in-block completeness guarantee simultaneously — resolving the R3 quantified trade-off.

---

## Open Questions for R5

1. **C-16 semantic differentiation unmeasured:** V-01 and V-05 tie at 137 on the structural rubric. A semantic-quality rubric for call discovery richness (does the trace catch more forgotten calls with the richer persona?) and auth depth (do delegation chain notes appear more reliably?) would differentiate. R5 could test this by scoring actual trace outputs, not just template structures.

2. **V-04 Phase architecture generalization:** Phase outer + call block inner reaches ceiling. Does the inverse also work — multiple call blocks nested inside a single CALL BLOCK super-structure (for fan-out scenarios with grouped calls)? Or does nesting a call block inside another call block collapse C-13/C-14?

3. **Supplementary registry positive score:** V-02's Stage 3 supplementary registry is neutral (no penalty). Could a well-structured supplementary registry earn positive credit under a potential C-18 criterion rewarding cross-call concern synthesis (e.g., system-level rate limit totals, auth token sharing patterns)?

---

```json
{"top_score": 137, "all_essential_pass": true, "new_patterns": ["phase-outer-call-block-inner-c13-c14-ceiling: Phase outer frame with nested call block inner units scores C-13/C-14 at full ceiling -- the per-call block architecture is the hard prerequisite, not the absence of a phase label; exclusion statements within per-section units inside nested call blocks retain full structural credit regardless of outer frame; phase architecture fully rehabilitated when call blocks carry all structural requirements", "c16-binary-pass-minimum-viable-sufficient: C-16 is binary pass/fail at domain + two domain-specific obligations; minimum-viable persona (V-01, 2 obligations) and maximal persona (V-05, 4 obligations + gap sensitivity) score identically; persona richness beyond the threshold enriches semantic output quality (call discovery, auth depth) but produces no additional rubric credit within the pass band"]}
```
