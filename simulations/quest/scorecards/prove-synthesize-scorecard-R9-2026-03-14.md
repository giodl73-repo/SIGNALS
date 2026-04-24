# prove-synthesize — Scorecard R9

**Rubric**: v9 (2026-03-14)
**Variations present**: V-01, V-02, V-03 (incomplete), V-04/V-05 (not provided)
**Golden threshold**: all essential PASS AND composite >= 90

---

## R9-V-01 — Role Sequence (Verdict-First: SYNTHESIST → ADVERSARY → ANALYST)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Verdict commitment | PASS | SYNTHESIST gate: "If your opening sentence does not contain yes / no / maybe and a numeric confidence, the SYNTHESIST role is incomplete." Hard gate enforces commitment. |
| C-10 | Self-contained mandate | PASS | "A reader with no access to the investigation artifacts must be able to understand the answer, the confidence, and the reasoning." Present at mandate level. |
| C-11 | Named anti-pattern gates | PASS | Explicit labeled "Gate:" instruction at every role — SYNTHESIST, ADVERSARY, ANALYST. All three foreclose named failure modes. |
| C-12 | Prose format for evidence ranking | PASS | "Prose only; argument construction required." Tables prohibited, prose enforced. |
| C-13 | NOT: precedes success condition | PASS | "NOT: table format for this section. The 'Why this signal outranks the alternatives:' sub-item is required at each of the three positions." |
| C-30 | Role names its own failure mode | PASS | SYNTHESIST → hedging; ADVERSARY → generic challenge; ANALYST → selective collection. All three named. |

### v9 New Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-32 | Inline exemplar at anti-pattern gate | **FAIL** | Exemplars exist in failure mode paragraphs (e.g., ADVERSARY: "e.g., 'all three key signals come from user interview artifacts…'") but they appear before the labeled Gate: instruction, not inside it. Gate instructions themselves contain no parenthetical instantiation. |
| C-33 | Format-prohibition names positive structural requirement | PASS | Key Evidence: "NOT: table format for this section. The 'Why this signal outranks the alternatives:' sub-item is required at each of the three positions" — prohibition and structural slot bound in one constraint. |
| C-34 | Supersession assertion in synthesis mandate | PASS | Opening: "supersedes all underlying investigation signals" + "The synthesis supersedes every individual signal — it does not summarize them. Issue a judgment; the signal inventory is now subordinate to this document." Two-site assertion. |

### Additional Aspirational Observations

- Self-containment check at end (four reader questions): PASS — maps directly to output requirements.
- Verdict-first sequence (SYNTHESIST runs before ADVERSARY) is structurally novel: commitment precedes adversarial exposure, eliminating pre-hedged synthesis anticipation.
- Open questions and counter-evidence slots present and well-specified.

### V-01 Composite Estimate

| Pool | Max | Earned |
|------|-----|--------|
| Essential | 90.0 | ~84.0 |
| Aspirational v8 (23 criteria) | 57.5 | ~30.0 |
| v9 new (C-32, C-33, C-34) | 7.5 | 5.0 |
| **Composite** | **155.0** | **~119.0** |

All essential: **PASS**. Above golden (>= 90): **YES**.

---

## R9-V-02 — Output Format (Ranked-Argument Paragraphs, No Section Headers)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Verdict commitment | PASS | SYNTHESIST role: "Issue the judgment. Failure mode: hedging (…a sentence that defers commitment is a refusal to synthesize)." Paragraph 1 output: "Open with the verdict (yes / no / maybe) and confidence score in the first sentence." Verdict required at paragraph opening AND in role definition. |
| C-10 | Self-contained mandate | PASS | "A reader with no access to the investigation artifacts must be able to understand the verdict, the confidence, the reasoning, and the limits of the reasoning from this document alone." PASS |
| C-11 | Named anti-pattern gates | PASS | ADVERSARY: "Generic challenges are not permitted (e.g., 'confidence could be higher with more data' applies to every synthesis)" — prohibition gate with inline test. SYNTHESIST: "a sentence that defers commitment is a refusal to synthesize; it is not a synthesis" — gate via categorical rejection. ANALYST: named failure mode with constraint. No explicit "Gate:" labels but gate function fully present. |
| C-12 | Prose format for evidence ranking | PASS | "Produce a single continuous prose document. No section headers. No bullet lists. No tables." Stronger than prior prose instructions — all three format prohibitions explicit. Bridge sentence requirement enforces argument construction. |
| C-13 | NOT: precedes success condition | PASS | Paragraph 2: "NOT: table format for this section. The 'why this signal ranks above the one below it' bridge sentence is required between each pair of ranked signals." |
| C-30 | Role names its own failure mode | PASS | ANALYST → selective collection; ADVERSARY → generic challenge; SYNTHESIST → hedging. All three named at role definition. |

### v9 New Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-32 | Inline exemplar at anti-pattern gate | **PASS** | ANALYST gate: "selective collection (e.g., building the signal set only from one investigation track — e.g., three signals all sourced from user interviews with no instrumentation signal…)" — exemplar inside role definition, bound to failure mode name. ADVERSARY gate: "(e.g., 'confidence could be higher with more data' applies to every synthesis) … (e.g., 'the three key signals all measure stated preference, not observed behavior — the synthesis has no revealed-preference signal in key evidence')" — two-exemplar instantiation, negative and positive case both present inside the constraint. SYNTHESIST: "(e.g., 'the evidence suggests yes but further investigation is warranted' — a sentence that defers commitment is a refusal to synthesize)". All three roles pass. |
| C-33 | Format-prohibition names positive structural requirement | PASS | Paragraph 2: "NOT: table format for this section. The 'why this signal ranks above the one below it' bridge sentence is required between each pair of ranked signals." Prohibition and structural slot (bridge sentence) bound in single constraint, co-located. |
| C-34 | Supersession assertion in synthesis mandate | PASS | Opening: "It does not summarize the signal inventory — it **replaces** the signal inventory as the authoritative record on this hypothesis." SYNTHESIST role: "The synthesis supersedes every individual signal — it does not summarize them." Uses both "supersedes" and "replaces" — strongest supersession language observed in this series. C-34 satisfied at two sites. |

### Additional Aspirational Observations

- **Concurrent role processing**: "Roles run concurrently in your reasoning; the output produced afterward is a single document, not three labeled sections." This eliminates labeled role sections from output entirely — the three roles inform the synthesis but produce no visible seams. Structurally distinct from all prior single-axis variations that retained labeled role output or explicit role ordering.
- ADVERSARY provides both negative exemplar (generic case) and positive exemplar (valid case) inline — double instantiation at the gate, exceeding C-32's minimum requirement.
- Self-containment check maps five reader questions to the five-paragraph structure (verdict/confidence → key evidence → counter-evidence → principles → open questions). Slot-to-check correspondence is explicit.
- Open questions: "If the question was raised by the ADVERSARY challenge, acknowledge that" — closure loop between roles and output.

### V-02 Composite Estimate

| Pool | Max | Earned |
|------|-----|--------|
| Essential | 90.0 | ~87.5 |
| Aspirational v8 (23 criteria) | 57.5 | ~32.5 |
| v9 new (C-32, C-33, C-34) | 7.5 | 7.5 |
| **Composite** | **155.0** | **~127.5** |

All essential: **PASS**. Above golden (>= 90): **YES**.

---

## R9-V-03 — Lifecycle Emphasis (Incomplete)

**Content received**: `# prove-synthesize` (title only)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| All | All criteria | **FAIL** | No instruction body present. Cannot evaluate GATHER → CHALLENGE → COMMIT phase structure, word-count envelopes, or any rubric criterion. |

**Composite**: ~0. Not scoreable. This variation was not authored.

---

## R9-V-04, V-05 — Combined-Axis (Not Provided)

Listed in the variation set header as combined-axis variations. No content provided. Cannot score.

---

## Round Summary

| Variation | Axis | Essential | C-32 | C-33 | C-34 | Composite |
|-----------|------|-----------|------|------|------|-----------|
| V-01 | Role sequence (verdict-first) | ALL PASS | FAIL | PASS | PASS | ~119.0 |
| V-02 | Output format (no headers, prose) | ALL PASS | PASS | PASS | PASS | ~127.5 |
| V-03 | Lifecycle (incomplete) | FAIL | FAIL | FAIL | FAIL | ~0 |
| V-04 | Combined (missing) | — | — | — | — | — |
| V-05 | Combined (missing) | — | — | — | — | — |

**Top variation**: V-02 at ~127.5

---

## Excellence Signals — R9

**Signal 1 — Concurrent role processing produces seam-free synthesis**

V-02 eliminates labeled role sections from the output document entirely: "Roles run concurrently in your reasoning; the output produced afterward is a single document, not three labeled sections." All prior variations retained explicit role boundaries either in output (labeled sections) or execution order (sequential). Concurrent processing means the model must integrate ANALYST evidence selection, ADVERSARY structural challenge, and SYNTHESIST verdict simultaneously before writing anything — the synthesis cannot pre-hedge because role resolution happens before output begins, not during it.

**Signal 2 — Double exemplar at adversarial gate (negative + positive case)**

V-02 ADVERSARY provides both the negative case (what a generic challenge looks like: "confidence could be higher with more data") and the positive case (what a valid challenge looks like: "the three key signals all measure stated preference, not observed behavior") inside the gate constraint. C-32 requires one instantiation; V-02 provides two, bracketing the gate between the failure mode and the target. This eliminates ambiguity about what "specific" means by showing the contrast directly.

**Signal 3 — "Replaces" strengthens supersession over "supersedes"**

V-01 uses "supersedes" twice. V-02 opens with "It does not summarize the signal inventory — it **replaces** the signal inventory as the authoritative record on this hypothesis" and then also uses "supersedes" in the role definition. The verb "replaces" is stronger than "supersedes" — it asserts displacement of the signal inventory rather than subordination of it. The two-verb approach (replaces + supersedes) closes the interpretation gap between C-10 (reader independence) and C-34 (output authority).

---

```json
{"top_score": 127.5, "all_essential_pass": true, "new_patterns": ["concurrent role processing eliminates labeled sections forcing full integration before output begins", "double exemplar at adversarial gate brackets valid and invalid cases creating contrast instantiation"]}
```
