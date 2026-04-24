## trace-skill — Scoring Round 2 (v2 Rubric)

### Criterion Evaluation by Variation

#### V-01 — Phrasing register (formal/imperative, canonical labels locked)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | **PASS** | Phase Label Schema table locks all four headers upfront |
| C-02 | Gather enumerates inputs by name with source | **PASS** | Gather table with Source column described explicitly |
| C-03 | Bind maps every input to resolved value | **PASS** | Bind table with RESOLVED/UNRESOLVED Status column |
| C-04 | Execute produces artifact | **PASS** | Implied by complete trace design |
| C-05 | Verdict declares PASS/FAIL with rationale | **PASS** | Compliance ledger structure described |
| C-06 | Exact schema labels | **PASS** | Immutable Phase Label Schema table enforces headers |
| C-07 | Verdict cites criterion IDs | **PASS** | "criterion-ID column" explicitly described |
| C-08 | Artifact complete, no elision | **PARTIAL** | Not addressed; completeness not guaranteed by design |
| C-09 | Coverage Matrix | **FAIL** | Not mentioned |
| C-10 | Execute relay carry | **FAIL** | Not mentioned |
| C-11 | Spec-first Gather | **FAIL** | Flat Gather table, no tier separation |
| C-12 | BLOCKED gate | **FAIL** | Not mentioned |
| C-13 | Artifact delimiters | **FAIL** | Not mentioned |

**Score**: (5.0/5 × 60) + (2.5/3 × 30) + (0/5 × 10) = 60 + 25 + 0 = **85**

---

#### V-02 — Gather ordering (spec-first two-tier enumeration)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | **PASS** | All phases implied; conflict rule references Bind explicitly |
| C-02 | Gather enumerates inputs by name with source | **PASS** | Tier 1 + Tier 2 with gap flags cover all inputs |
| C-03 | Bind maps every input to resolved value | **PASS** | Conflict rule stated explicitly → C-03 in Bind |
| C-04 | Execute produces artifact | **PASS** | Implied |
| C-05 | Verdict declares PASS/FAIL with rationale | **PARTIAL** | Verdict not structurally designed; no PASS/FAIL structure described |
| C-06 | Exact schema labels | **PARTIAL** | Only Gather phase designed; Verdict/Bind/Execute labels not locked |
| C-07 | Verdict cites criterion IDs | **FAIL** | No criterion-ID mention |
| C-08 | Artifact complete, no elision | **PARTIAL** | Not addressed |
| C-09 | Coverage Matrix | **FAIL** | Not mentioned |
| C-10 | Execute relay carry | **FAIL** | Not mentioned |
| C-11 | Spec-first Gather | **PASS** | Tier 1 spec-only before Tier 2 invocation is the axis |
| C-12 | BLOCKED gate | **FAIL** | Not mentioned |
| C-13 | Artifact delimiters | **FAIL** | Not mentioned |

**Score**: (4.5/5 × 60) + (1.0/3 × 30) + (1/5 × 10) = 54 + 10 + 2 = **66**

---

#### V-03 — Bind as resolution ledger

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | **PASS** | All phases implied |
| C-02 | Gather enumerates inputs by name with source | **PASS** | Implied by "one row per Gather input" in Bind |
| C-03 | Bind maps every input to resolved value | **PASS** | Ledger with three-value Status is the axis; one row per input |
| C-04 | Execute produces artifact | **PASS** | Implied |
| C-05 | Verdict declares PASS/FAIL with rationale | **PARTIAL** | Verdict not designed; BLOCKED/CONTINUED decision is in Bind |
| C-06 | Exact schema labels | **PARTIAL** | Bind phase designed; Verdict/Execute not locked |
| C-07 | Verdict cites criterion IDs | **FAIL** | Not mentioned |
| C-08 | Artifact complete, no elision | **FAIL** | "Artifact section gap-marked with B-NN" — gap markers are elision markers, explicitly violates C-08 |
| C-09 | Coverage Matrix | **FAIL** | Not mentioned |
| C-10 | Execute relay carry | **FAIL** | Not mentioned |
| C-11 | Spec-first Gather | **FAIL** | Not mentioned |
| C-12 | BLOCKED gate | **PARTIAL** | BLOCKED halt is in Bind (UNRESOLVED-BLOCKED), not a pre-Gather gate; C-12 requires gate before Gather runs |
| C-13 | Artifact delimiters | **FAIL** | Not mentioned |

**Score**: (4.5/5 × 60) + (0.5/3 × 30) + (0.5/5 × 10) = 54 + 5 + 1 = **60**

---

#### V-04 — Coverage Matrix + BLOCKED gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | **PASS** | All phases implied |
| C-02 | Gather enumerates inputs by name with source | **PASS** | Gather confirms matrix entries |
| C-03 | Bind maps every input to resolved value | **PASS** | Implied |
| C-04 | Execute produces artifact | **PASS** | Implied |
| C-05 | Verdict declares PASS/FAIL with rationale | **PARTIAL** | Not explicitly designed |
| C-06 | Exact schema labels | **PARTIAL** | Coverage Matrix/Gather structured; Verdict not locked |
| C-07 | Verdict cites criterion IDs | **FAIL** | Not mentioned |
| C-08 | Artifact complete, no elision | **PARTIAL** | Not addressed |
| C-09 | Coverage Matrix | **PASS** | Coverage Matrix with closed-world preamble is the axis |
| C-10 | Execute relay carry | **FAIL** | Not mentioned |
| C-11 | Spec-first Gather | **FAIL** | Not mentioned |
| C-12 | BLOCKED gate | **PASS** | "BLOCKED gate with hard-stop language" before trace runs |
| C-13 | Artifact delimiters | **FAIL** | Not mentioned |

**Score**: (4.5/5 × 60) + (0.5/3 × 30) + (2/5 × 10) = 54 + 5 + 4 = **63**

---

#### V-05 — All aspirationals integrated

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | **PASS** | "Phase headers Gather/Bind/Execute/Verdict" in structural table |
| C-02 | Gather enumerates inputs by name with source | **PASS** | Tier 1 + Tier 2 with gap flags |
| C-03 | Bind maps every input to resolved value | **PASS** | "Bind ledger, one row per Gather input" |
| C-04 | Execute produces artifact | **PASS** | "Artifact sections complete, no elision" → C-04, C-08 |
| C-05 | Verdict declares PASS/FAIL with rationale | **PASS** | "Verdict reads relay table, criterion-ID ledger" |
| C-06 | Exact schema labels | **PASS** | Phase headers locked in structural table |
| C-07 | Verdict cites criterion IDs | **PASS** | Criterion-ID ledger in Verdict |
| C-08 | Artifact complete, no elision | **PASS** | "Artifact sections complete, no elision" explicitly mapped |
| C-09 | Coverage Matrix | **PASS** | "Coverage Matrix with closed-world preamble" |
| C-10 | Execute relay carry | **PASS** | "Relay table in Execute (role/signal/binding/status)" |
| C-11 | Spec-first Gather | **PASS** | "Gather Tier 1 (spec) before Tier 2 (invocation)" |
| C-12 | BLOCKED gate | **PASS** | "BLOCKED gate on Required=YES/Gap=YES" |
| C-13 | Artifact delimiters | **PASS** | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` |

**Score**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = 60 + 30 + 10 = **100**

---

### Ranking

| Rank | Variation | Score | Essential | Notes |
|------|-----------|-------|-----------|-------|
| 1 | V-05 | **100** | 5/5 PASS | All 13 criteria satisfied |
| 2 | V-01 | **85** | 5/5 PASS | Misses all aspirationals; C-08 partial |
| 3 | V-02 | **66** | 4.5/5 | Spec-first Gather but Verdict undesigned |
| 4 | V-04 | **63** | 4.5/5 | C-09+C-12 both pass but Verdict weak |
| 5 | V-03 | **60** | 4.5/5 | C-08 FAIL (gap markers = elision) |

Golden threshold requires all 5 essential PASS + composite ≥ 80. **V-05 and V-01 both meet the threshold.** V-01 is the minimum viable trace; V-05 is the ideal.

---

### Excellence Signals from V-05

**1. Relay-reads-not-reconstructs** — By documenting (role, signal, binding, status) in Execute's relay table, Verdict becomes a reader of already-produced evidence rather than a reconstruction engine. This is architecturally superior: Verdict cannot introduce new claims not grounded in Execute.

**2. Coverage-matrix-as-preflight** — Declaring the full input space before Gather runs inverts the completeness problem. Without the matrix, completeness is only knowable after Gather finishes; with it, any gap is visible before the first Gather row is written.

**3. Integration cascade** — The aspirationals aren't independent add-ons; they form a pipeline: Coverage Matrix declares input space → BLOCKED gate prevents partial execution on required gaps → spec-first Gather anchors inputs before invocation constraints apply → relay table in Execute preserves the evidence chain → Verdict reads that chain with criterion-ID citations. Satisfying all five creates structural guarantees no subset achieves.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["relay-reads-not-reconstructs: Verdict reads relay table from Execute rather than reconstructing from artifact body", "coverage-matrix-preflight: Coverage Matrix declared before Gather runs inverts completeness check from post-hoc to pre-flight", "integration-cascade: aspirationals reinforce each other in pipeline (matrix feeds BLOCKED gate, relay table feeds Verdict reader)"]}
```
