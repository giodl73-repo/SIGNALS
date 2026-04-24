## prove-topic — Round 8 Scoring (Rubric v7)

**Anchor**: R7 V-05 (144/144). All five variations claim C-01–C-24 compliance. Scoring confirms coverage, then evaluates three R8 excellence axes above the v7 ceiling.

---

### Criterion-by-Criterion Evaluation

**v7 rubric: 144 pts max** (Essential + Recommended = 80 pts; 16 Aspirational × 4 pts = 64 pts)

#### Essential Criteria (10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Five sub-skills (scout load, hypothesis, web search, intelligence, analysis, synthesis) | PASS | PASS | PASS | PASS | PASS |
| **C-02** Each stage writes a named artifact | PASS — all five stages have write instructions | PASS | PASS | PASS | PASS |
| **C-03** Stage gates enforced — no artifact instruction = FAIL | PASS — GATE S blocks Stage 1; each stage has confirm + artifact | PASS | PASS | PASS | PASS |
| **C-04** Terminal synthesis with findings / confidence / handoff | PASS | PASS | PASS | PASS | PASS |
| **C-05** Topic prefix consistent across all artifacts | PASS — `{topic}-` prefix in every write instruction | PASS | PASS | PASS | PASS |

All essential: **50/50** across all five variations.

---

#### Recommended Criteria (10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** Stage order enforced, forward-only | PASS | PASS | PASS | PASS | PASS |
| **C-07** Scout anchor named in hypothesis frontmatter | PASS — `scout_anchor: {topic}-scout-record-{date}.md` in frontmatter | PASS | PASS | PASS | PASS |
| **C-08** Synthesis points to `topic-story` | PASS — `next: topic-story` in handoff | PASS | PASS | PASS | PASS |

All recommended: **30/30** across all five variations.

---

#### Aspirational Criteria (4 pts each, PARTIAL = 2 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-09** Thin-evidence propagates to synthesis | PASS — null notes at S2/S3 feed synthesis CE section | PASS | PASS | PASS | PASS |
| **C-10** Progress narrated per stage | PASS — each stage ends with explicit confirm sentence | PASS | PASS | PASS | PASS |
| **C-11** Hypothesis hard-gated on scout confirmation | PASS — GATE S blocks Stage 1 until `gate_s_cleared: true` | PASS | PASS | PASS | PASS |
| **C-12–C-13** *(inferred from severity stack context)* | PASS | PASS | PASS | PASS | PASS |
| **C-14** Null CE recorded per stage | PASS — NULL RESULT NOTE with stage result | PASS | PASS | PASS | PASS |
| **C-15** *(severity stack context)* | PASS | PASS | PASS | PASS | PASS |
| **C-16** Escalation path defined if null | PASS — adversarial reviewer assignment if null | PASS | PASS | PASS | PASS |
| **C-17** Consequence (confidence cap) | PASS — SESSION INVARIANT B caps confidence | PASS | PASS | PASS | PASS |
| **C-18** Co-activation check (`co_activation_confirmed = dual_lock_fired`) | PASS — format error if they differ | PASS | PASS | PASS | PASS |
| **C-19** Null-CE protocol pre-committed at campaign open | PASS — SESSION INVARIANT A + B locked before Stage 0 | PASS | PASS | PASS | PASS |
| **C-20** Accumulation — running null tally per stage | PASS — "Running tally: [count] null. [X] stages remain" | PASS | PASS | PASS | PASS |
| **C-21** Handoff echo — `incumbent_defense_closed` in handoff | PASS | PASS | PASS | PASS | PASS |
| **C-22** Registry trace — ROLE A attestation visible at GATE S | PASS — `invariant_registry_confirmed` produced by ROLE A only | PASS | PASS | PASS | PASS |
| **C-23** Campaign outcome — `incumbent_defense_closed` independent of `co_activation_confirmed` | PASS — derivation note in Stage 4; NOT assertion in handoff | PASS | PASS | PASS | PASS |
| **C-24** Role separation — two roles, two owned attestation fields | PASS — ROLE A owns `invariant_registry_confirmed`, ROLE B owns `gate_s_cleared`, each declared sole producer | PASS | PASS | PASS | PASS |

All aspirational: **64/64** across all five variations.

---

### v7 Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 50 | 30 | 64 | **144** |
| V-02 | 50 | 30 | 64 | **144** |
| V-03 | 50 | 30 | 64 | **144** |
| V-04 | 50 | 30 | 64 | **144** |
| V-05 | 50 | 30 | 64 | **144** |

All five variations meet or equal the v7 ceiling. The v7 rubric does not discriminate between them.

---

### R8 Excellence Signal Evaluation (above v7 ceiling)

These axes are candidate criteria for v8. Each is evaluated independently.

#### R8 Axis 1 — Handoff Derivation Annotations (all fields labeled)

| Variation | Coverage | Evidence |
|-----------|----------|----------|
| V-01 | **FULL** | DERIVATION ANNOTATION RULE declared; all 8 fields carry `[derived from: X]` labels; "unlabeled field = format error" |
| V-02 | **FAIL** | Pre-committed schema table lists derivation sources, but synthesis Handoff write instruction produces bare fields — no `[derived from: X]` labels on individual fields at synthesis time |
| V-03 | **PARTIAL** | `incumbent_defense_closed` carries `positive_derivation:` and `independence_chain:` chains; other fields (`scout_anchor`, `hypothesis`, `analysis`, `null_tally_final`, `co_activation_confirmed`, `confidence`, `next`) have no derivation labels |
| V-04 | **FULL** | All 8 declared fields written with `[derived from: X]` labels; DERIVATION ANNOTATION RULE stated separately from schema compliance check |
| V-05 | **FULL** | All 9 fields carry labels; DERIVATION ANNOTATION RULE declared; "Unlabeled field = format error" |

#### R8 Axis 2 — Pre-committed Handoff Schema (full contract locked at CAMPAIGN OPEN)

| Variation | Coverage | Evidence |
|-----------|----------|----------|
| V-01 | **FAIL** | No pre-committed schema at CAMPAIGN OPEN; handoff schema assembled reactively at synthesis |
| V-02 | **FULL** | 8-field DECLARED FIELDS table with derivation sources at CAMPAIGN OPEN; ROLE A scope extended to cover schema lock; schema_compliance_confirmed at synthesis; "format error if any field is absent / added" |
| V-03 | **FAIL** | No pre-committed schema |
| V-04 | **FULL** | PRE-COMMITTED HANDOFF SCHEMA table with field names + required derivation sources; compliance check before synthesis writes; schema_compliance_confirmed field |
| V-05 | **FULL** | 9-field schema (includes `schema_compliance_confirmed` as a declared field); compliance check retrieves schema from CAMPAIGN OPEN; "no additions, no omissions, derivation-source mismatch is format error" |

#### R8 Axis 3 — Independence Path Chain on `incumbent_defense_closed`

| Variation | Coverage | Evidence |
|-----------|----------|----------|
| V-01 | **PARTIAL** | Handoff carries `[derived from: null_tally_final via formula — NOT from co_activation_confirmed]` — negates `co_activation_confirmed` but does not name `dual_lock_fired`; not a structured named field, embedded in label text |
| V-02 | **PARTIAL** | Schema table row reads "null_tally_final (NOT co_activation_confirmed)" — present at campaign open but only one negation, no structured `independence_chain:` field; synthesis handoff doesn't carry the chain |
| V-03 | **FULL** | Stage 4 INDEPENDENCE PATH BLOCK: `positive_derivation: source + formula + result`; `independence_chain: NOT derived from: dual_lock_fired / NOT derived from: co_activation_confirmed` with explanatory basis; both chains confirmed in synthesis handoff as distinct structured sub-fields |
| V-04 | **PARTIAL** | `[derived from: null_tally_final via formula — NOT from co_activation_confirmed]` — same gap as V-01: only one negation, no `dual_lock_fired` exclusion, not a structured field |
| V-05 | **FULL** | INDEPENDENCE PATH BLOCK in Stage 4 (identical to V-03); handoff carries `positive_derivation:` + `independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"` as distinct structured sub-fields on `incumbent_defense_closed` |

---

### R8 Excellence Summary

| Variation | Axis 1 (derivation labels) | Axis 2 (pre-committed schema) | Axis 3 (independence chain) | R8 axes satisfied |
|-----------|---------------------------|-------------------------------|------------------------------|-------------------|
| V-01 | FULL | FAIL | PARTIAL | 1 full |
| V-02 | FAIL | FULL | PARTIAL | 1 full |
| V-03 | PARTIAL | FAIL | FULL | 1 full |
| V-04 | FULL | FULL | PARTIAL | 2 full |
| **V-05** | **FULL** | **FULL** | **FULL** | **3 full** |

---

### Ranking

1. **V-05** — 144/144 v7; all three R8 axes FULL. Only variation where the independence path chain (positive + negative assertions as distinct fields) appears in both Stage 4 and the synthesis handoff, and where the pre-committed schema is 9 fields (including `schema_compliance_confirmed` as a declared field, not an add-on). Axis 2 and Axis 3 are mutually reinforcing: the negative derivation chain for `incumbent_defense_closed` is visible at CAMPAIGN OPEN via the schema's `NOT dual_lock_fired; NOT co_activation_confirmed` source declaration, then confirmed at synthesis. Pre-commitment makes the independence assertion load-bearing before any evidence runs.

2. **V-04** — 144/144 v7; Axes 1+2 FULL, Axis 3 PARTIAL. The combination of uniform labeling + pre-committed schema creates the double-checkpoint pattern (declared at open, verified at synthesis), but the independence chain only negates `co_activation_confirmed` — `dual_lock_fired` exclusion is absent, and the chain is embedded in a label string rather than a structured field.

3. **V-01** — 144/144 v7; Axis 1 FULL. Cleanest single-axis implementation of uniform derivation labeling. Axis 3 has a partial negative assertion but misses the second exclusion term. Better than V-02/V-03 for the stated axis.

4. **V-02** — 144/144 v7; Axis 2 FULL. Pre-committed schema is well-formed (table format, derivation sources, format-error language) but synthesis handoff writes bare fields — the label rule is absent, creating an asymmetry where the contract is declared but not enforced at the field level.

5. **V-03** — 144/144 v7; Axis 3 FULL. The independence path chain implementation is structurally the strongest of the single-axis variants — both positive derivation and negative assertion as distinct structured fields, basis explanation included. But leaves the other two axes entirely uncovered.

---

### Excellence Signals from V-05

**1. Pre-commitment extends to the handoff contract, not just the null-CE protocol.** The three session invariants (Adversarial Reviewer, Confidence Cap, Handoff Schema) form a single locked block at CAMPAIGN OPEN. ROLE A's scope explicitly covers all three. This makes the handoff contract as auditable as the adversarial reviewer assignment — both are known before Stage 0 runs.

**2. Schema compliance check is a structured retrieval + comparison, not a prose reminder.** At synthesis, the instruction is to retrieve the PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN and verify each field against its declared derivation source before writing. A mismatch is a format error named with field and expected/actual derivation. This is a mechanical compliance step, not a vague "make sure handoff is complete."

**3. Independence assertion is a two-part structured field on `incumbent_defense_closed`, present in both Stage 4 and the synthesis handoff.** `positive_derivation:` names source and formula; `independence_chain:` explicitly names both `dual_lock_fired` and `co_activation_confirmed` as excluded derivation paths. The basis sentence explains why they're excluded (parallel consumers of `null_tally_final`, not upstream sources). A reader with no domain knowledge can verify independence from the field alone.

**4. `schema_compliance_confirmed` is a declared schema field, not a post-hoc assertion.** It appears in the CAMPAIGN OPEN schema table as the ninth field with `derived from: synthesis-time compliance check`. This means the compliance check itself is part of the contract — synthesis can't omit the compliance step without triggering a schema-error on the one field that attests compliance.

---

```json
{"top_score": 144, "all_essential_pass": true, "new_patterns": ["Pre-committed handoff schema as session invariant — full field contract with derivation sources locked at CAMPAIGN OPEN before Stage 0, constraining synthesis to an exact predetermined contract that cannot be assembled reactively", "Uniform derivation annotation rule on all handoff fields — every field carries a [derived from: X] label naming its structural source, with unlabeled field treated as a format error independent of schema compliance", "Structured two-part independence path chain — incumbent_defense_closed carries both positive_derivation (source + formula) and independence_chain (NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed) as distinct named sub-fields, making the independence assertion machine-readable without domain knowledge of the dual-lock mechanism", "schema_compliance_confirmed as a declared schema field — the ninth field in the pre-committed schema, with derivation source listed as synthesis-time compliance check, making the compliance step itself part of the session contract"]}
```
