## mock-ns Round 7 Scorecard (rubric v7, max 116)

### Baseline across all variates

All five variates are identical from S-1 through A-5. The only differences are in S-0's preamble gate sentence(s) and CONSTRAINT vocabulary. The baseline below applies to all variates:

| Block | Criteria | Result | Notes |
|-------|----------|--------|-------|
| Essential | C-01--C-05 | PASS × 5 | Header, CATEGORY, FLAG, fidelity warning, skill-specific body all present |
| Recommended | C-06--C-08 | PASS × 3 | S-1 emit lines, write confirmation, next-step line all present |
| Aspirational | C-09 | PASS | topic-plan selected, topic-status excluded |
| | C-10 | PASS (default) | No compliance tags present; criterion fires only on compliance-tag input |
| | C-11 | PASS | FLAG table covers all 5 cases functionally |
| | C-12 | PASS | S-0 completes before S-1 begins |
| | C-13 | PASS | S-2 error guard names unrecognized skill-id, halts |
| | C-14 | PASS | A-1 through A-5 labeled as discrete steps |
| | C-15 | PASS | CONSTRAINT names 5 op types (≥3 required) |
| | C-16 | PASS | `trace-*`, `scout-feasibility`, `listen-*` in FLAG table condition cells |
| | C-17 | PASS | "S-1 must not begin until..." terminal gate present |
| | C-18 | PASS | "Forward the resolved tier to S-2 and S-3" names both consumers |
| | C-19 | PASS | Preamble gate at S-0 opening + terminal gate after bullets |
| | C-20 | PASS | Tier carry in both table column ("Propagates to S-2 and S-3") and standalone sentence |
| | C-21 | PASS | CONSTRAINT names ≥4 ops including body construction |
| | C-22 | PASS | Separate rows for HS-critical tier=1 and HS non-critical in FLAG table |
| | C-23 | PASS | Gate-type content is absolute first sentence in all variates |
| | C-24 | PASS | CONSTRAINT names 5 ops, last closes artifact write phase |

**Shared score: 112/116** (all C-01--C-24 pass). C-25 and C-26 are the discriminators.

---

### V-01 -- Imperative-First Two-Sentence Gate

**Gate**: "Write the TOPICS.md status line before any other work begins. This step emits first."

**CONSTRAINT**: "No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. No artifact path assembly or file output." (R6 V-05 synonym vocabulary)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-23 | PASS | Gate content is S-0 opening -- zero pre-gate surface; CONSTRAINT follows gate |
| C-25 | **FAIL** | Both sentences present but order is reversed: imperative ("Write...") precedes declarative ("This step emits first."). C-25 pass condition specifies (1) declarative first, (2) imperative second. Presence of both necessary but not sufficient -- order is prescriptive |
| C-26 | PASS | All 5 op types use R6 V-05 synonym vocabulary: "lookup of skill categories," "skill-id resolution," "mock content generation," "artifact body construction," "artifact path assembly or file output" -- each lexically distinct from canonical canonical op-type labels |

**Score: 114/116** (C-25 -2 pts)

---

### V-02 -- 4/5 Synonymized, Op-5 Canonical Retained

**Gate**: "This step emits first. Write the TOPICS.md status line before any other work begins." (R6 V-05 form)

**CONSTRAINT**: "No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. **No artifact path construction or file write.**"

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-23 | PASS | "This step emits first." is absolute first sentence -- zero pre-gate surface |
| C-25 | PASS | Declarative identity ("This step emits first.") precedes imperative emit instruction ("Write the TOPICS.md status line before any other work begins.") -- exact R6 V-05 form retained |
| C-26 | **FAIL** | Op types 1--4 use synonym vocabulary (PASS). Op type 5: "No artifact path construction or file write" is the canonical C-24 phrase verbatim. C-26 is all-or-nothing -- a single canonical phrase fails the criterion regardless of synonym coverage for remaining ops |

**Score: 114/116** (C-26 -2 pts)

---

### V-03 -- Three-Sentence Gate (Declarative + Elaboration + Imperative)

**Gate**: "This step emits first. Its single obligation before advancing is to report TOPICS.md status. Write the TOPICS.md status line before any other work begins."

**CONSTRAINT**: "No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. No artifact path assembly or file output." (R6 V-05 synonym vocabulary)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-23 | PASS | "This step emits first." is absolute first sentence -- zero pre-gate surface |
| C-25 | **FAIL** | Three sentences present: (1) declarative identity ✓, (2) elaborative declarative (not required), (3) imperative ✓. C-25 pass condition specifies "consists of two sentences: (1)... and (2)..." with both items numbered -- the count is explicit. Three sentences do not satisfy "consists of two." The elaboration sentence is semantically compatible but structurally violates the count requirement. **Boundary note for v8**: if the scorer interprets "consists of" as type-based (both required types present) rather than count-strict, this would be 116/116. Ruling here: count-strict → FAIL. A rubric clarification ("exactly two sentences" or "at least two sentences with both types present") is warranted in v8. |
| C-26 | PASS | All 5 ops use R6 V-05 synonym vocabulary -- same as V-01, passes as in V-01's C-26 analysis |

**Score: 114/116** (C-25 -2 pts)

*V-03 surfaces the C-25 count-interpretation open question. Calling FAIL on strict-count reading; v8 should add "exactly two sentences" clarification to C-25 pass condition.*

---

### V-04 -- Output-Primacy Declarative (Step-Role Boundary)

**Gate**: "The first observable output of this step is the TOPICS.md status line. Write it before any other work begins."

**CONSTRAINT**: "No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. No artifact path assembly or file output." (R6 V-05 synonym vocabulary)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-23 | PASS | "The first observable output of this step is the TOPICS.md status line." is absolute first sentence -- zero pre-gate surface |
| C-25 | **FAIL** | Two sentences, declarative first -- but the declarative asserts OUTPUT POSITION ("the first observable output of this step is X"), not STEP IDENTITY ("this step emits first" -- what the step IS). C-25 requires a "declarative identity sentence asserting the step's emit primacy as a statement of the step's ROLE." Output-ordering declaration names what comes out first; step-role declaration names what the step fundamentally is. The distinction: identity ("S-0 is the emit step") vs output-sequence ("output #1 is X"). Both are two-sentence with declarative-first structure, so C-23 passes; only C-25 catches the semantic mismatch. |
| C-26 | PASS | Same R6 V-05 synonym CONSTRAINT as V-01, V-03 -- PASS |

**Score: 114/116** (C-25 -2 pts)

---

### V-05 -- Convergent: Zero-Lexeme Synonym Depth

**Gate**: "This step emits first. Write the TOPICS.md status line before any other work begins." (R6 V-05 verbatim)

**CONSTRAINT**: "No classification of skill registries. No routing of input identifiers to skill records. No synthesis of simulated content. No composition of artifact sections. No filesystem path formation or file emission."

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-23 | PASS | "This step emits first." is absolute first sentence |
| C-25 | PASS | Declarative identity ("This step emits first.") first, imperative ("Write the TOPICS.md status line before any other work begins.") second -- exact R6 V-05 two-sentence form |
| C-26 | PASS | All 5 op types use deepened synonym vocabulary with zero shared content words vs canonical: "classification of skill registries" ≠ "category lookup"; "routing of input identifiers to skill records" ≠ "skill selection"; "synthesis of simulated content" ≠ "mock generation"; "composition of artifact sections" ≠ "body generation"; "filesystem path formation or file emission" ≠ "artifact path construction or file write." Semantic equivalence preserved at concept level despite zero lexical overlap. C-26 has no implicit proximity bound -- deepest valid synonymization still passes. |

**Score: 116/116**

---

### Round Summary

| Variate | C-25 | C-26 | Aspirational pts | Total |
|---------|------|------|-----------------|-------|
| V-01 | FAIL (order reversed) | PASS | 34/36 | **114/116** |
| V-02 | PASS | FAIL (op-5 canonical) | 34/36 | **114/116** |
| V-03 | FAIL (count = 3) | PASS | 34/36 | **114/116** |
| V-04 | FAIL (output-primacy) | PASS | 34/36 | **114/116** |
| V-05 | PASS | PASS | 36/36 | **116/116** |

**All essential criteria pass across all variates.**

Rank: V-05 alone at 116. V-01, V-02, V-03, V-04 tied at 114.

---

### Excellence Signals (V-05)

**Signal 1 -- Zero-lexeme synonym depth has no proximity bound**
V-05 replaces R6 V-05's first-level synonyms ("No lookup of skill categories") with zero-lexeme paraphrase ("No classification of skill registries"). No shared content words between any canonical phrase and its replacement. C-26 passes: the criterion requires lexical distinctness and semantic equivalence, not lexical proximity. Deep paraphrase is not "too abstract" -- if it names the same prohibited concept, it satisfies C-26 regardless of distance from canonical vocabulary.

**Signal 2 -- Step-role declarative is definitionally prior to the imperative**
V-05 retains "This step emits first. Write the TOPICS.md status line before any other work begins." The declarative establishes that the emit is the step's definitional behavior (identity), not a precondition imposed from outside. The imperative then directs the specific action. This two-layer structure -- identity before command -- is what C-25 encodes. V-01 shows that having both sentences but in reversed order (command then identity) fails; V-04 shows that having two sentences in the right order but with a weaker declarative (output-position, not step-role) also fails. V-05 gets both layers right.

---

### New patterns to carry into rubric v8

**From V-03**: C-25 sentence-count ambiguity surfaced. "Consists of two sentences" may need explicit clarification as "exactly two sentences" to close the gap between count-based and type-based interpretation. A three-sentence gate with both required types (declarative + imperative) plus an intermediate elaboration is the boundary case. Recommend adding: "exactly two sentences; additional sentences between the declarative and the imperative do not satisfy this criterion."

**From V-05**: C-26 zero-lexeme synonym depth confirmed. No proximity bound exists. The criterion is purely about semantic equivalence + lexical distinctness -- any valid paraphrase at any distance from canonical satisfies it. No C-27 needed.

---

```json
{"top_score": 116, "all_essential_pass": true, "new_patterns": ["Zero-lexeme synonym depth satisfies C-26 without proximity bound -- any semantically equivalent paraphrase passes regardless of lexical distance from canonical", "Three-sentence gate fails C-25 strict count -- 'consists of two sentences' means exactly two; an elaboration sentence between declarative and imperative still fails even when both required sentence types are present"]}
```
