# Quest Score — `topic:echo` Round 3

**Rubric:** v3 | **Max:** 120 | **Date:** 2026-03-16
**Trace artifact:** placeholder — scoring structural enforcement properties of each prompt design

---

## Scoring Method

No output artifact exists yet. Each variation is scored on its probability of satisfying each criterion given the prompt's structural enforcement mechanisms. PASS = high structural probability; PARTIAL = moderate (instruction-dependent); FAIL = low or blocked by applicability gate.

---

## Criterion Evaluation — All Variations

### Essential Criteria (12 pts each)

**C-01 — Named surprises present**
All five variations open with "every entry is a surprise" and require departure framing. All PASS.

**C-02 — Signal tracing per surprise**
All five include a `Source:` field (labeled in V-02/V-04/V-05 schema; listed in V-01; instruction-required in V-03). All PASS.

**C-03 — Design impact per surprise**
All five include an `Impact: {confirming|redirecting|destabilizing} -- {named decision}` field with an explicit failure example ("'This changes things' without naming what changes fails"). All PASS.

**C-04 — Synthesis not summary**
All five open with "Not a summary of signals. Every entry is a surprise." V-03/V-05 reinforce this through role separation (Archivist and Signal Reader cannot co-produce a summary). All PASS.

**C-05 — Surprise specificity**
All five include the generic-discard rule and the "could it appear in any investigation?" handle test. V-03/V-05 add the role boundary, which structurally prevents the Archivist from framing generic beliefs as topic-specific. All PASS.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| **Essential** | **60** | **60** | **60** | **60** | **60** |

---

### Recommended Criteria (10 pts each)

**C-06 — Expectation counterfactual**
All five include an `Expected:` field citing the PBI entry, and all five require "A reader new to the topic must be able to reconstruct the prior assumption from this entry alone." All PASS.

**C-07 — Institutional framing**
All five include an explicit "Institutional forward" step addressed to the next team. V-05 is most explicit: "Frame the echo as: 'things you would not predict by reading today's materials alone.'" All PASS.

**C-08 — Cross-signal pattern identification**
All five include a Cross-Signal Patterns step requiring either a named pattern with design implication, or an explicit independence statement with rationale. All PASS.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| **Recommended** | **30** | **30** | **30** | **30** | **30** |

---

### Aspirational Criteria (5 pts each)

**C-09 — Surprise hierarchy by design impact**
All five include a Surprise Ranking step with an explicit argument requirement ("A sorted list without argument fails"). All PASS.

**C-10 — Riskiest surprise flagged**
All five include a Risk Escalation step naming assumption at risk, source artifact, and survival condition. All PASS.

**C-11 — Pre-committed PBI**
- V-01: Hard phase gate ("Phase 1 complete. PBI is frozen at {timestamp}. Opening signal artifacts now. Do not revise the PBI after this point.") — temporal boundary is structural. **PASS (5)**
- V-02: Instruction only ("Before reading any signal artifact, commit the beliefs"). No gate, no freeze declaration. Section exists with addressable PB-NN identifiers, but pre-signal ordering is on model discipline. **PARTIAL (4)**
- V-03: Archivist role scope ("No signal artifacts. No file reads.") + freeze declaration ("Archivist complete. PBI is frozen.") — role boundary enforces pre-commitment. **PASS (5)**
- V-04: Hard phase gate identical in strength to V-01. **PASS (5)**
- V-05: Role boundary + phase gate + freeze declaration. **PASS (5)**

**C-12 — Named surprise handles**
All five include: a 2–5 word handle specificity requirement, the "could it appear in any investigation?" test, and a Handle Ledger section. V-05 adds an explicit independence test for handle language in Echo Author Step 2. All PASS.

**C-13 — Dual phase-locked pre-commitment integrity**
*Applicability gate: C-11 and C-12 must both pass.*

The key distinction: a **workflow boundary** (phase gate) separates temporal stages but does not prevent the model from drawing on prior reasoning across phases. An **information boundary** (role scope exclusion) makes signal content structurally unavailable to the PBI-writing role.

- V-01: Phase gate creates temporal separation. Risk: PBI entries could anticipate handle concepts through the model's prior reasoning path ("We assumed the competitor would treat X as solved" — written after the model has internally noted X). Moderate enforcement. **PARTIAL (3)**
- V-02: C-11 is PARTIAL, so C-13 applicability is gated. Even if granted: no independence mechanism. PBI and handles could be co-constructed in a single cognitive pass. **FAIL (0)**
- V-03: Archivist scope ("No signal artifacts. No file reads.") — Archivist literally cannot know what the signals say because Signal Reader has not yet run. This is structural impossibility, not instruction. **PASS (5)**
- V-04: Same phase gate mechanism as V-01. Schema adds nothing for C-13. **PARTIAL (3)**
- V-05: Role boundary (strongest mechanism) + phase gate + Echo Author Step 2 explicit independence test: "does the handle echo PBI entry language verbatim? If yes, the handle was constructed by inverting a prediction rather than naming a finding — rewrite it." Converts C-13 from a property-to-verify into a production step that must be passed. **PASS (5)**

**C-14 — Single-entry audit trail completeness**
*Applicability gate: C-11 and C-12 must both pass.*

- V-01: Output artifact section lists Handle, PBI-Ref, Source as required items per entry, but using a bullet list format without labeled field schema. No explicit "validation" self-check instruction. Omission risk under model drift: moderate. **PARTIAL (3)**
- V-02: Labeled schema (`Handle:`, `PBI-Ref:`, `Source:`, ...) with "All fields are required. Omitting any field is a structural violation." + explicit validation note: "a reviewer reading only this entry must be able to verify three things without navigating elsewhere." Strongest schema enforcement of any single-axis variation. **PASS (5)**
- V-03: Echo Author Step 4 uses named fields with "All three audit pointers (Handle, PBI-Ref, Source) must appear in the entry." Strong instruction, but without the "structural violation" enforcement language or self-check. **PARTIAL (4)**
- V-04: Labeled schema + self-check ("can a reviewer verify all three audit pointers from this entry alone?") + "incomplete and must be corrected." **PASS (5)**
- V-05: Identical schema to V-04 + explicit 3-step self-check listing each verification path: "1. Handle exists in Handle Ledger, 2. PBI-Ref entry exists at the named identifier, 3. Source artifact appears in Signal Findings." **PASS (5)**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-09 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 4 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 3 | 0 | 5 | 3 | 5 |
| C-14 | 3 | 5 | 4 | 5 | 5 |
| **Aspirational** | **26** | **24** | **29** | **28** | **30** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** | All Essential Pass | Golden |
|-----------|-----------|-------------|--------------|---------------|-------------------|--------|
| V-01 | 60 | 30 | 26 | **116** | Yes | Yes |
| V-02 | 60 | 30 | 24 | **114** | Yes | Yes |
| V-03 | 60 | 30 | 29 | **119** | Yes | Yes |
| V-04 | 60 | 30 | 28 | **118** | Yes | Yes |
| V-05 | 60 | 30 | 30 | **120** | Yes | Yes |

---

## Rankings

1. **V-05 — 120/120** — Full synthesis. Only variation achieving perfect score. Role boundary + phase gate + entry schema + explicit C-13 self-check combines all three enforcement mechanisms.
2. **V-03 — 119/120** — Role sequence alone. Best single-axis variation. Strongest C-13 enforcement; C-14 slightly weaker due to instruction-only (no schema validation language).
3. **V-04 — 118/120** — Lifecycle + Output Format. Best no-role variation. Phase gate + schema catches C-14 completely; C-13 is the gap (phase gate is a workflow boundary, not an information boundary).
4. **V-01 — 116/120** — Lifecycle only. Phase gate provides C-13 partial enforcement; C-14 partial because pointer requirement is stated as output structure bullets rather than labeled schema.
5. **V-02 — 114/120** — Output Format only. Best C-14 enforcement of any single-axis variation; C-13 entirely unaddressed and C-11 instruction-only.

---

## Discriminating Pair Results

| Pair | Axis isolated | C-13 result | C-14 result | Finding |
|------|--------------|-------------|-------------|---------|
| V-01 vs V-02 | Phase gate vs schema | V-01 > V-02 (3 vs 0) | V-02 > V-01 (5 vs 3) | Each axis hits its target criterion and misses the other — confirmed isolation |
| V-01 vs V-03 | Phase gate vs role boundary | V-03 > V-01 (5 vs 3) | V-03 > V-01 (4 vs 3) | Role boundary outperforms phase gate on C-13; role sequence also improves C-14 as a side effect |
| V-02 vs V-04 | Schema alone vs schema + phase | V-04 > V-02 (3 vs 0) | Equal (5 vs 5) | Schema does the C-14 work in both; phase adds marginal C-13 lift |
| V-03 vs V-05 | Role only vs full synthesis | Equal (5 vs 5) | V-05 > V-03 (5 vs 4) | Schema is the marginal gain in V-05 over V-03 — confirms C-14 needs schema, not role boundary |
| V-04 vs V-05 | Combined vs full synthesis | V-05 > V-04 (5 vs 3) | Equal (5 vs 5) | Role information boundary adds 2 pts on C-13 that the phase gate cannot provide |

**Key R3 finding:** The role information boundary (V-03, V-05) reliably outperforms the workflow phase gate (V-01, V-04) on C-13. V-03 (119) > V-04 (118), confirming the role boundary adds reliability the phase gate alone cannot provide.

---

## Excellence Signals from V-05

**Pattern 1 — Structural impossibility over workflow instruction for C-13.**
The Archivist scope constraint ("No signal artifacts. No file reads.") makes it *impossible* for PBI entries to anticipate handle language — not because the prompt says not to, but because handles are produced by the Echo Author after Signal Reader completes. The information boundary is enforced by role sequencing, not by trust. This is what made V-05's C-13 a PASS where V-04 with an identical phase gate scored PARTIAL: a workflow gate stops the model from *opening files* but not from *reasoning ahead*; a role scope boundary stops the Archivist from having signal content at all.

**Pattern 2 — Naming failure modes as production steps converts verification into prevention.**
V-05 Echo Author Step 2 includes: "does the handle echo PBI entry language verbatim? If yes, the handle was constructed by inverting a prediction rather than naming a finding — rewrite it." This is the C-13 failure mode stated as an in-process check the model must run. V-01 through V-04 only describe what good handles look like; V-05 also describes what bad handles look like and requires a rewrite step. Naming the anti-pattern turns C-13 from a post-hoc reviewer check into a required production gate.

**Pattern 3 — Signal Findings section makes the independence evidence auditable.**
V-03 and V-05 include a `## Signal Findings` section (Signal Reader output). This section provides the *positive* independence evidence: a reviewer can inspect the Signal Reader's findings register and confirm that the Archivist's PBI entries contain no language that anticipates specific finding content. V-01 and V-04 phase gates prevent co-construction but leave no artifact trail that demonstrates independence. V-05's Signal Findings section is the audit residue.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Role information boundary enforces C-13 through structural impossibility -- Archivist scope exclusion makes signal knowledge unavailable before PBI is written, not merely instructed-against; workflow phase gate cannot achieve the same reliability because it controls file access but not the model's prior reasoning", "Naming failure modes as in-process rewrite steps (V-05 Echo Author Step 2: 'does the handle echo PBI entry language verbatim? rewrite it') converts C-13 from a post-hoc reviewer check into a required production gate the model must pass before writing the entry"]}
```
