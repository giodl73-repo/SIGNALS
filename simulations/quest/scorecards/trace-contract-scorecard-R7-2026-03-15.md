## trace-contract R7 Scoring — Rubric v7

### Rubric Reference

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 – C-05 | 12 pts each = 60 |
| Recommended | C-06 – C-08 | 10 pts each = 30 |
| Aspirational | C-09 – C-22 | 1 pt each = 14 |
| **Max** | | **104** |

---

## V-01 — Skeleton-First (C-22 isolation)

**Mechanism:** Full artifact skeleton (all section headers + template slots in final position) before Phase 1. Unified finding template. Prose gate. Phase 1 / Phase 3 role headings.

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 1 explicitly names Connectors contract expert; "You have not run the operation. You write from the spec alone." Role boundary is unconditional. |
| C-02 | **PASS** | "Elements present in § 2 but absent from § 4 are silent omissions — the trace fails C-02 regardless of finding quality." Coverage obligation stated by name. |
| C-03 | **PASS** | "Fill § 5 — Findings. For each deviation from § 4" — one finding per deviation. |
| C-04 | **PASS** | Skeleton pre-prints `spec: [clause from §2 that this finding violates — must match]`; "An expected element without a spec citation is not a valid contract entry." |
| C-05 | **PASS** | Template field: "hypothesis: [causal mechanism — the process, mapping, serialization path, or condition that produced the wrong output; not a restatement of what differed]" — explicit disqualifier for symptom restatements. |

**Essential subtotal: 60 / 60**

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **FAIL** | Stock roles include Connectors contract expert, but the finding template carries no `connector-impact` slot. No structural mandate for integration callout. |
| C-07 | **PASS** | Skeleton pre-prints §6 Summary with severity count table and "Verdict: [Contract violated / Contract satisfied]". |
| C-08 | **PASS** | "If no deviations: replace § 5 with `## 5. Findings — none. Contract satisfied.`" — affirmative statement, not silence. |

**Recommended subtotal: 20 / 30**

### Aspirational (C-09–C-22)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `recommendation: [amend-spec \| fix-impl \| needs-discussion] — [one sentence rationale]` in template; instruction mandates it for breaking/degraded. |
| C-10 | **PASS** | §7 Patterns pre-printed in skeleton with three-branch handling instructions; "This section may not be silently omitted." |
| C-11 | **PASS** | Labeled block format; absence of a field produces a visible gap. |
| C-12 | **PASS** | Explicit gate: `[EXPECTED SEALED — Phase 1 complete. Contract Author role ends. Automate begins after this line.]` |
| C-13 | **FAIL** | Gate is a prose statement — not a structured parseable token with `clauses:{N}`, `date:`, `author:`, `phase:` fields. |
| C-14 | **FAIL** | Finding template has no `connector-impact` slot. No per-finding integration obligation. |
| C-15 | **FAIL** | Unified template; `recommendation` conditioned on severity ("Include for breaking and degraded. Omit for cosmetic") — not an unconditional slot in a breaking-specific template. |
| C-16 | **FAIL** | Unified template. No severity-stratified architecture. |
| C-17 | **FAIL** | C-15 fails (no breaking-tier template with unconditional `recommendation` slot); C-17 presupposes C-15 architecture. |
| C-18 | **FAIL** | Criterion text not in v7 rubric prompt; scoring conservative FAIL. |
| C-19 | **PASS** | Skeleton preamble includes behavioral commitment: "No section may be added, removed, or reordered after the skeleton is written" — behavioral rules precede Phase 1. |
| C-20 | **FAIL** | §7 Patterns is a top-level section after §6 Summary. C-20 requires the Patterns block embedded within the Phase 5 summary template — not a standalone section. |
| C-21 | **PASS** | Explicit role headings: `### Phase 1 — Connectors Contract Expert` and `### Phase 3 — Automate`. |
| C-22 | **PASS** | Complete artifact skeleton (§1 through §7, all headers and template slots) appears as a named structural declaration before Phase 1 begins. |

**Aspirational subtotal: 7 / 14** (C-09, C-10, C-11, C-12, C-19, C-21, C-22)

### V-01 Total: **87 / 104** — All essential PASS

---

## V-02 — Severity-Stratified Templates (C-16 isolation)

**Mechanism:** Three distinct tier templates (BREAKING 6 fields, DEGRADED 5 fields, COSMETIC 3 fields). Prose gate `[CONTRACT COMMITTED]`. Step-based flow without role headings or skeleton.

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "Write the `## Expected Output` section from the spec alone. Do not run or simulate the operation before this section is complete." |
| C-02 | **PASS** | "Every element must appear. A missing element is a silent omission — the trace fails C-02 regardless of finding quality." |
| C-03 | **PASS** | Tier template selection per deviation; instructions mandate one finding block per flagged deviation. |
| C-04 | **PASS** | `spec: [clause from Expected Output that this finding violates]` in all three templates. |
| C-05 | **PASS** | "Hypothesis rule (applies to all tiers): The hypothesis names a causal mechanism. It does not restate the deviation. If your hypothesis could be written without knowing anything about the system under test — only from reading the deviation line — it is a symptom restatement, not a mechanism." Strongest hypothesis enforcement of any variation. |

**Essential subtotal: 60 / 60**

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | BREAKING template has `connector-impact` unconditionally; DEGRADED template has `connector-impact` unconditionally. Both higher tiers structurally guarantee integration callout. |
| C-07 | **PASS** | Step 6 Summary template with severity count table and verdict line. |
| C-08 | **PASS** | "If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 6." Summary verdict then confirms `Contract satisfied`. |

**Recommended subtotal: 30 / 30**

### Aspirational (C-09–C-22)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `recommendation` slot in BREAKING template (unconditional); DEGRADED also has `recommendation`. |
| C-10 | **FAIL** | No Patterns section in Step 6 or anywhere in the variation. |
| C-11 | **PASS** | Three labeled tier templates with named fields; missing field produces a visible gap. |
| C-12 | **PASS** | "`[CONTRACT COMMITTED]` — Do not proceed to Step 3 before writing this line." Explicit prose gate acknowledgment. |
| C-13 | **FAIL** | `[CONTRACT COMMITTED]` is prose — no `clauses:N`, `date:`, `author:` parseable fields. |
| C-14 | **FAIL** | COSMETIC template has only 3 fields: `deviation`, `spec`, `hypothesis`. No `connector-impact`. Not all finding blocks carry integration-impact field. |
| C-15 | **PASS** | BREAKING template includes `recommendation: [amend-spec \| fix-impl \| needs-discussion]` as an unconditional labeled slot — the template cannot be filled without it. |
| C-16 | **PASS** | Three distinct templates per severity tier, each with unconditionally mandatory fields and no conditional language. |
| C-17 | **PASS** | BREAKING template carries both `recommendation: [vocab choice]` and `rationale: [which side of the contract is wrong and why — one sentence]` as separate labeled fields. |
| C-18 | **FAIL** | Unknown criterion text; conservative FAIL. |
| C-19 | **FAIL** | No named preamble behavioral protocol before Phase 1. Step instructions begin immediately. |
| C-20 | **FAIL** | No Patterns section at all. |
| C-21 | **FAIL** | "Stock roles: Connectors contract expert + Automate" listed in header but steps carry no explicit per-phase role headings. |
| C-22 | **FAIL** | No artifact skeleton preamble. |

**Aspirational subtotal: 6 / 14** (C-09, C-11, C-12, C-15, C-16, C-17)

### V-02 Total: **96 / 104** — All essential PASS

---

## V-03 — Machine-Readable Gate Token (C-13 isolation)

**Mechanism:** Structured parseable gate token `[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]` with closure echo `[TRACE-COMPLETE | ... | gate-clauses:{N}]`. Unified finding template. Step-based flow.

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "Write the `## Expected Output` section from the spec alone." Token asserts Phase 1 completed by a role that had not observed runtime output. |
| C-02 | **PASS** | "Every element must appear." |
| C-03 | **PASS** | Finding entry per deviation from §4. |
| C-04 | **PASS** | `spec: [spec clause violated — must match a clause cited in Expected Output]` |
| C-05 | **PASS** | "the causal mechanism — name the process, mapping, serialization path, or condition that produced the wrong output; not what differed." |

**Essential subtotal: 60 / 60**

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **FAIL** | Unified finding template carries no `connector-impact` slot. No structural integration mandate. |
| C-07 | **PASS** | Step 6 Summary with severity counts and verdict. |
| C-08 | **PASS** | "If no deviations: write `## Diff — Contract satisfied. No findings.`" — affirmative. |

**Recommended subtotal: 20 / 30**

### Aspirational (C-09–C-22)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `recommendation: [amend-spec \| fix-impl \| needs-discussion] — [one sentence rationale]` for breaking/degraded. |
| C-10 | **FAIL** | No Patterns section in V-03. |
| C-11 | **PASS** | Labeled block format. |
| C-12 | **PASS** | "Do not run or simulate the operation before writing this token. The token asserts that Phase 1 was completed by a role that had not observed runtime output" — explicit gate confirmation. |
| C-13 | **PASS** | `[EXPECTED-SEALED \| clauses:{N} \| date:{YYYY-MM-DD} \| author:contract-expert \| phase:1-complete]` — structured, parseable, mechanically verifiable; `clauses:{N}` echoed in closure token. |
| C-14 | **FAIL** | No per-finding `connector-impact` slot in unified template. |
| C-15 | **FAIL** | Unified template; `recommendation` conditional on severity. |
| C-16 | **FAIL** | Unified template. |
| C-17 | **FAIL** | C-15 prerequisite fails. |
| C-18 | **FAIL** | Unknown; conservative FAIL. |
| C-19 | **FAIL** | No named preamble behavioral protocol. |
| C-20 | **FAIL** | No Patterns section. |
| C-21 | **FAIL** | No explicit per-phase role headings. |
| C-22 | **FAIL** | No artifact skeleton preamble. |

**Aspirational subtotal: 4 / 14** (C-09, C-11, C-12, C-13)

### V-03 Total: **84 / 104** — All essential PASS

---

## V-04 — Skeleton-First + Stratified Templates (C-22 × C-16)

**Mechanism:** Full artifact skeleton pre-declares all three tier templates in final positions. Prose gate (clause count inline, not token format). Phase 1 / Phase 3 role headings. COSMETIC template has only 3 fields (no `connector-impact`).

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "You are the Connectors contract expert. You have not run the operation. You write from the spec alone." |
| C-02 | **PASS** | "Every element must appear. Missing elements fail C-02." |
| C-03 | **PASS** | "Fill § 5 — Findings. For each deviation from § 4, select the matching severity tier template from the skeleton and fill all fields." |
| C-04 | **PASS** | `spec — must match a clause cited in § 2; findings without a matched clause fail C-04` |
| C-05 | **PASS** | "hypothesis — names the causal mechanism; 'The output did not match' restates the deviation and is not acceptable." |

**Essential subtotal: 60 / 60**

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | BREAKING and DEGRADED tier templates carry `connector-impact` as unconditional fields. |
| C-07 | **PASS** | §6 Summary pre-printed in skeleton with severity count table and verdict. |
| C-08 | **PASS** | "replace § 5 with `## 5. Findings — none. Contract satisfied.`" — affirmative no-findings path. |

**Recommended subtotal: 30 / 30**

### Aspirational (C-09–C-22)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | BREAKING and DEGRADED tier templates have `recommendation` as unconditional top-level field. |
| C-10 | **PASS** | §7 Patterns pre-printed in skeleton; "This section may not be silently omitted." |
| C-11 | **PASS** | Three labeled tier templates; field gaps are structurally visible. |
| C-12 | **PASS** | "[EXPECTED SEALED — Phase 1 complete. All {N} clauses committed. Automate begins after this line.]" — explicit gate acknowledgment with clause count. |
| C-13 | **FAIL** | Gate is prose: "[EXPECTED SEALED — Phase 1 complete. All {N} clauses committed.]" — not a structured parseable token with `key:value` pipe-delimited fields. |
| C-14 | **FAIL** | COSMETIC template in skeleton has only `deviation`, `spec`, `hypothesis` — no `connector-impact`. Not all finding tiers carry integration-impact field. |
| C-15 | **PASS** | BREAKING tier template has `recommendation: [amend-spec \| fix-impl \| needs-discussion]` as unconditional labeled slot. |
| C-16 | **PASS** | Three distinct tier templates in skeleton, each with tier-appropriate unconditional fields, no conditional language. |
| C-17 | **PASS** | BREAKING template carries `recommendation` and `rationale: [which side of the contract is wrong and why — one sentence]` as separate labeled fields. |
| C-18 | **FAIL** | Unknown; conservative FAIL. |
| C-19 | **PASS** | Skeleton preamble: "No section may be added, removed, or reordered after this skeleton is written" — behavioral commitment rules precede Phase 1. |
| C-20 | **FAIL** | §7 Patterns is a top-level section following §6 Summary, not embedded within the Phase 5 summary template. |
| C-21 | **PASS** | `### Phase 1 — Connectors Contract Expert` and `### Phase 3 — Automate` — explicit role-separated authorship headings. |
| C-22 | **PASS** | Complete artifact skeleton with all section headers and three tier templates appears before Phase 1 begins. |

**Aspirational subtotal: 10 / 14** (C-09, C-10, C-11, C-12, C-15, C-16, C-17, C-19, C-21, C-22)

### V-04 Total: **100 / 104** — All essential PASS

---

## V-05 — Platinum Combination (C-22 × C-16 × C-13 × C-14)

**Mechanism:** Full skeleton pre-declares all three tier templates + both structured tokens in final positions. COSMETIC template adds `connector-impact` with "write 'none' if not applicable" — all three tiers carry integration-impact field unconditionally. Parseable gate token `[EXPECTED-SEALED | clauses:{N} | ...]` echoed by closure token `[TRACE-COMPLETE | ... | gate-clauses:{N}]`.

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "You are the Connectors contract expert. You have not run the operation. You write from the spec alone." Phase boundary fully role-labeled. |
| C-02 | **PASS** | "Every element must appear. Missing elements fail C-02." |
| C-03 | **PASS** | "For each deviation from § 4, select the matching tier template from the skeleton and fill all fields." |
| C-04 | **PASS** | "`spec` — must match a clause from § 2; findings without a matched clause fail C-04" |
| C-05 | **PASS** | "'The output did not match' is a symptom restatement, not a hypothesis" — explicit disqualifier; hypothesis must name a causal mechanism. |

**Essential subtotal: 60 / 60**

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | All three tier templates carry `connector-impact`. Even COSMETIC has it ("write 'none' if not applicable"). |
| C-07 | **PASS** | §6 Summary pre-printed in skeleton with full count table and verdict. |
| C-08 | **PASS** | "replace § 5 with `## 5. Findings — none. Contract satisfied.` Fill § 6 and write the `[TRACE-COMPLETE ...]` token." |

**Recommended subtotal: 30 / 30**

### Aspirational (C-09–C-22)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `recommendation` unconditional on BREAKING and DEGRADED tier templates. |
| C-10 | **PASS** | §7 Patterns pre-printed in skeleton; "This section may not be silently omitted." |
| C-11 | **PASS** | Three labeled tier templates; structural gaps are visible at write time. |
| C-12 | **PASS** | "Do not run or simulate the operation before writing this token." Explicit phase gate with role assertion. |
| C-13 | **PASS** | `[EXPECTED-SEALED \| clauses:{N} \| date:{YYYY-MM-DD} \| author:contract-expert \| phase:1-complete]` — pre-declared in skeleton, mechanically parseable; clause count echoed in `[TRACE-COMPLETE \| ... \| gate-clauses:{N}]`. |
| C-14 | **PASS** | All three tier templates carry `connector-impact`. COSMETIC: "write 'none' if not applicable" — field is unconditional, never omittable. |
| C-15 | **PASS** | BREAKING tier template has `recommendation` as unconditional labeled slot in tier-specific block. |
| C-16 | **PASS** | Three distinct tier templates with no conditional field language; each tier's mandatory fields are structurally encoded. |
| C-17 | **PASS** | BREAKING template has `recommendation: [vocab choice]` and `rationale: [which side of the contract is wrong and why — one sentence]` as separate labeled fields. |
| C-18 | **FAIL** | Criterion text not provided in v7 rubric prompt; conservative FAIL. |
| C-19 | **PASS** | Skeleton preamble: "The skeleton commits the complete document structure and every mandatory field obligation before the first expected element is written" — behavioral obligation precedes Phase 1. |
| C-20 | **FAIL** | §7 Patterns is a top-level section (after §6 Summary) in the skeleton, not embedded within the Phase 5 summary template. C-20 requires Patterns inside the Phase 5 summary block. |
| C-21 | **PASS** | `### Phase 1 — Connectors Contract Expert` and `### Phase 3 — Automate` — explicit role-separated authorship. |
| C-22 | **PASS** | Complete artifact skeleton with all sections, all tier templates, and both structured token formats in final positions appears before Phase 1 begins. |

**Aspirational subtotal: 12 / 14** (C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-19, C-21, C-22)

### V-05 Total: **102 / 104** — All essential PASS

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | All Essential |
|-----------|-----------|-------------|--------------|-------|---------------|
| **V-05** | 60 | 30 | 12 | **102** | ✓ |
| **V-04** | 60 | 30 | 10 | **100** | ✓ |
| **V-02** | 60 | 30 | 6 | **96** | ✓ |
| **V-01** | 60 | 20 | 7 | **87** | ✓ |
| **V-03** | 60 | 20 | 4 | **84** | ✓ |

**Ranking: V-05 > V-04 > V-02 > V-01 > V-03**

All five variations pass all essential criteria (60/60). No variation regresses the essentials despite increasing structural overhead.

---

## Gap Analysis

Two criteria block V-05 from a perfect 104:

| Missing | Why all variations fail it |
|---------|--------------------------|
| **C-18** | Criterion text absent from v7 rubric prompt; unable to evaluate |
| **C-20** | Requires `## Patterns` embedded *within* the Phase 5 summary template; all R7 variations place §7 Patterns as a top-level section after §6 Summary — structurally correct for C-10 but positionally wrong for C-20. Recovering C-20 requires collapsing §7 into the §6 Summary block, which conflicts with the skeleton's section-per-phase architecture |

The C-20 conflict is structural: the skeleton enforces §6 (Summary) and §7 (Patterns) as separate sections, which satisfies C-10 and C-22 but violates C-20's "embedded within Phase 5" requirement. Resolving this in R8 would require either merging §6+§7 or redefining the skeleton's section boundaries.

---

## Excellence Signals — V-05

**Why V-05 scores highest:**

1. **`connector-impact` on COSMETIC tier ("write 'none' if not applicable")** — the decisive move over V-04. Making integration-impact unconditional on all three tiers transforms C-14 from a per-tier exception into a universal structural obligation. The "write none if not applicable" pattern preserves correctness without creating silence: COSMETIC findings that have no integration impact explicitly confirm the absence rather than omitting the field.

2. **Both structured tokens pre-declared in skeleton** — `[EXPECTED-SEALED | ...]` and `[TRACE-COMPLETE | ...]` appear in the skeleton before Phase 1. The model sees the exact token format as a structural slot to fill, not as an instruction to construct mid-workflow. This reduces token format errors: the obligation is visible from document open, not encountered at a moment of cognitive pressure.

3. **Four orthogonal mechanisms with zero redundancy** — skeleton (document shape), tier templates (finding field completeness), gate token (phase boundary assertion), per-finding integration slot (depth coverage) — each addresses a distinct failure dimension. Adding C-14 to V-04's C-22+C-16 base costs zero points elsewhere: V-05 retains all 10 aspirational points from V-04 and adds C-13 (1 pt) and C-14 (1 pt) without dropping any.

---

```json
{"top_score": 102, "all_essential_pass": true, "new_patterns": ["connector-impact on COSMETIC tier with write-none-if-not-applicable converts integration coverage from at-least-one to universally structural — C-14 achieved by making every tier carry the field rather than restricting it to higher tiers", "both structured tokens (EXPECTED-SEALED and TRACE-COMPLETE) pre-declared as skeleton slots before Phase 1 — format obligation is visible at document open rather than introduced mid-workflow under cognitive pressure", "four orthogonal mechanisms (skeleton shape, tier templates, gate token, per-finding integration slot) are simultaneously achievable without essential regression — each covers a distinct failure dimension with zero overlap"]}
```
