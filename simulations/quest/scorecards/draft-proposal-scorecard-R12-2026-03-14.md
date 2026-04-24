Now I have everything needed. Let me score all 5 variations against the v12 rubric.

---

# draft-proposal Variate Scoring — Round 12

**Rubric:** v12 · Formula: composite = 90 + (passes/28 × 10) · New criteria: C-34, C-35

---

## V-01 — Architect-First (Role Sequence axis)

| Criterion | Status | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | Role sequence declared; four anatomy fields present; matrix built; recommendation with rationale |
| R-01..R-03 | PASS | Risk register (R-NN, P, I, P×I, mitigation); prerequisites verified; coverage table and 4-step finalization |
| C-01..C-21 | PASS | General criteria satisfied |
| C-22 | PASS | CLOSED BY column present in coverage table |
| **C-23** | **FAIL** | RISK fields use "P:[n] × I:[n] = [score]" inline notation — no R-NN register linkage anywhere |
| C-24 | PASS | Amendment table: 35 rows (T-01..T-35) |
| C-25 | PASS | Finalization Phase 10 is explicitly numbered four-step list |
| **C-26** | **FAIL** | No Phase 9b authored — C-23 cascade: no R-NN usage means nothing to back-fill |
| C-27..C-30 | PASS | PHASE column present (C-29); findings use "Finding N: T-NN" format (C-30) |
| **C-31** | **FAIL** | Phase 2 RISK uses direct P×I notation — no `[R-NN pending]` placeholder |
| **C-32** | **FAIL** | No Phase 9b → no structural-domain enumeration possible |
| **C-33** | **FAIL** | No prohibition adjacent to placeholder — no placeholder exists |
| **C-34** | **FAIL** | No Phase 9b domain entries to carry index prefixes |
| **C-35** | **FAIL** | No Phase 9b citation sites to show `[R-NN pending] → [R-NN entries]` transition |

**Open triggers:** T-23, T-26, T-31, T-32, T-33, T-34, T-35 (7)  
**Findings:** Finding 1: T-23 … Finding 7: T-35 (ordinal-labeled, C-30 PASS)  
**Score: 21/28 → composite 97.50**

---

## V-02 — PM-First, Compact Tables (Output Format axis)

| Criterion | Status | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | All essential anatomy criteria satisfied |
| R-01..R-03 | PASS | All required criteria satisfied |
| C-01..C-21 | PASS | General criteria satisfied |
| **C-22** | **FAIL** | Coverage table omits CLOSED BY column — compact format emits CRITERION \| STATUS only |
| C-23 | PASS | Phase 9b back-fills R-NN into RISK fields |
| C-24 | PASS | 35 rows |
| C-25 | PASS | Numbered 4-step finalization |
| C-26 | PASS | Phase 9b present with explicit header `[GATE: C-26]` |
| C-27..C-31 | PASS | C-31 PASS: "Do not compute P×I in Phase 2 RISK fields. Declare `[R-NN pending]` to reserve the slot." |
| C-32 | PASS | Phase 9b names "Domain 1 — Option RISK fields (by option label)" and "Domain 2 — Comparison matrix risk column" |
| C-33 | PASS | "Do not compute P×I in Phase 2 RISK fields" prohibition is adjacent to `[R-NN pending]` directive |
| C-34 | PASS | "Domain 1 —" / "Domain 2 —" numeric index prefixes on every domain entry |
| C-35 | PASS | Per-site: "`[OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]`" arrow notation |

**Open triggers:** T-22 (1)  
**Finding 1: T-22**  
**Score: 27/28 → composite 99.64**

---

## V-03 — Lifecycle-Heavy (Lifecycle Emphasis axis)

| Criterion | Status | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | All essential criteria satisfied |
| R-01..R-03 | PASS | All required criteria satisfied |
| C-01..C-21 | PASS | General criteria satisfied |
| C-22 | PASS | CLOSED BY column present |
| C-23 | PASS | `[R-NN pending]` placeholder at Phase 2, back-filled in Phase 9b |
| **C-24** | **FAIL** | Amendment table built from C-01..C-31 → 31 rows; expected 35. T-24 fires at PRE-DOCUMENT |
| C-25 | PASS | Numbered 4-step finalization |
| C-26 | PASS | Phase 9b present |
| C-27..C-31 | PASS | C-31 PASS: `[R-NN pending]` placeholder present in Phase 2 RISK |
| **C-32** | **FAIL** | Phase 9b: "Enumerate each citation site visited by option label" — comparison matrix not named as second structural domain |
| **C-33** | **FAIL** | Phase 2 RISK: "`[R-NN pending]` — placeholder for register linkage, resolved in Phase 9b" — no adjacent "Do not compute P×I" prohibition |
| **C-34** | **FAIL** | No domain-index prefixes — no structural domain headers, only per-option-label enumeration |
| **C-35** | **FAIL** | No `[R-NN pending] → [R-NN IDs]` transition notation — only confirms "R-NN formula applied at comparison matrix risk column" |

**Note:** T-32..T-35 absent from 31-row table → behavioral fails not captured as trigger findings. One finding only: Finding 1: T-24.  
**Score: 23/28 → composite 98.21**

---

## V-04 — Conversational Register + C-35 Isolation (Phrasing Register axis)

| Criterion | Status | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | All essential criteria satisfied |
| R-01..R-03 | PASS | All required criteria satisfied |
| C-01..C-21 | PASS | General criteria satisfied |
| C-22 | PASS | CLOSED BY column present |
| C-23 | PASS | R-NN back-fill via Phase 9b |
| C-24 | PASS | 35 rows |
| **C-25** | **FAIL** | Phase 10: "Walk through coverage verification as a narrative discussion" — explicitly avoids numbered steps |
| C-26 | PASS | Phase 9b present |
| C-27..C-31 | PASS | C-31 PASS: `[R-NN pending]` placeholder present |
| C-32 | PASS | Phase 9b: "(1) Option RISK fields (by option label)" and "(2) Comparison matrix risk column" — both domains explicitly named |
| **C-33** | **FAIL** | Phase 2 RISK: "`[R-NN pending]` — Placeholder for risk register linkage; will be resolved in Phase 9b" — no "Do not compute P×I" prohibition adjacent |
| C-34 | PASS | "(1)"/"(2)" ordinal-numeric prefix form is an accepted C-34 equivalent; both domain entries carry ordinal index |
| **C-35** | **FAIL** | Phase 9b states "the R-NN IDs applied to its RISK field" (outcome only) — no `[R-NN pending] → [R-NN IDs]` before/after transition notation per site |

**Open triggers:** T-25, T-33, T-35 (3)  
**Findings:** Finding 1: T-25, Finding 2: T-33, Finding 3: T-35 (ordinal labels in narrative, C-30 PASS)  
**Score: 25/28 → composite 98.93**

---

## V-05 — Inertia-Forward + Aggregate Phase 9b (Inertia Framing axis)

| Criterion | Status | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | All essential criteria satisfied; inertia framing is additive, not substitutive |
| R-01..R-03 | PASS | All required criteria satisfied |
| C-01..C-21 | PASS | General criteria satisfied |
| C-22 | PASS | CLOSED BY column present |
| C-23 | PASS | R-NN back-fill via Phase 9b |
| C-24 | PASS | 35 rows |
| C-25 | PASS | Numbered 4-step finalization |
| C-26 | PASS | Phase 9b present |
| C-27..C-31 | PASS | C-31 PASS: `[R-NN pending]` placeholder; C-33 PASS: "Do not compute P×I in Phase 2 RISK fields. Declare `[R-NN pending]` to reserve the slot." adjacent prohibition |
| **C-32** | **FAIL** | Phase 9b: "Citation-site enumeration: all `[R-NN pending]` placeholders resolved; R-NN IDs back-filled from register; comparison matrix risk column updated. Back-fill complete." — aggregate form; neither option RISK fields by label nor matrix column named as a structural domain |
| C-33 | PASS | Prohibition instruction adjacent to `[R-NN pending]` directive in Phase 2 |
| **C-34** | **FAIL** | Aggregate Phase 9b has no enumerated domain entries — no entries to carry index prefixes |
| **C-35** | **FAIL** | Aggregate "Back-fill complete" form has no per-site entries to carry `[R-NN pending] → [R-NN IDs]` transition notation |

**Open triggers:** T-32, T-34, T-35 (3)  
**Findings:** Finding 1: T-32, Finding 2: T-34, Finding 3: T-35  
**Score: 25/28 → composite 98.93**

---

## Rankings

| Rank | Variation | Axis | Fails | Score | Composite |
|------|-----------|------|-------|-------|-----------|
| 1 | **V-02** | Output format (compact + PM-first) | C-22 | 27/28 | **99.64** |
| 2 | **V-04** | Phrasing register (conversational) | C-25, C-33, C-35 | 25/28 | **98.93** |
| 2 | **V-05** | Inertia framing + aggregate Phase 9b | C-32, C-34, C-35 | 25/28 | **98.93** |
| 4 | **V-03** | Lifecycle emphasis (stale trigger count) | C-24, C-32, C-33, C-34, C-35 | 23/28 | **98.21** |
| 5 | **V-01** | Role sequence (Architect-first, no register linkage) | C-23+cascade ×7 | 21/28 | **97.50** |

---

## Excellence Signals — V-02 (top scorer)

**Signal 1 — Compact format enforces Phase 9b structural rigor.**  
The `OUTPUT FORMAT: Compact tables throughout` constraint forced each Phase 9b domain to become an explicit, headed block (`Domain 1 —`, `Domain 2 —`) rather than prose-embedded enumeration. This made the C-34 compliance stronger, not weaker. Implication: compact-format prompts are a reliable vehicle for C-34/C-35 because every structural claim must stand alone.

**Signal 2 — Arrow notation as a state-diff operator per citation site.**  
"`[OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]`" is not just a notation choice — it structures Phase 9b as a before/after diff log. Each site entry has a source state and a resolved state. V-04's failure (outcome-only: "R-NN IDs applied to its RISK field") shows that the domain-index structure (C-34 PASS) does not imply state-diff notation (C-35 FAIL). The arrow is the independent discriminator.

**Signal 3 — Prohibition adjacency is the C-33 critical requirement, not prohibition existence.**  
V-03 and V-04 both include placeholder syntax but omit the adjacent "Do not compute P×I" prohibition. V-02's Phase 2 RISK template pairs them in the same instruction line, making them co-located. This confirms that C-33 tests placement, not just presence — a prohibition buried elsewhere in the document does not satisfy C-33.

---

```json
{"top_score": 99.64, "all_essential_pass": true, "new_patterns": ["compact-format constraint enforces stronger Phase 9b structural enumeration than verbose format — compact Phase 9b blocks are tighter C-34+C-35 exemplars", "arrow notation [R-NN pending] → [R-NN entries] is a state-diff operator independent of domain-index structure — C-34 and C-35 can be satisfied independently as shown by V-04 isolation", "prohibition adjacency is the C-33 discriminator — prohibition and placeholder must be co-located in the same Phase 2 RISK template instruction, not merely present somewhere in the document"]}
```
