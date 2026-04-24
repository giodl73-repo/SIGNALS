## mock-ns Round 12 — Scorecard

### Scoring Formula (v11)

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)
PARTIAL = 0.5. Denominator: aspirational = 25.
```

---

### Cross-Variant Common Baseline

All 5 variants carry identical structural content for C-01 through C-30. The table below records the shared verdict, then the per-variant section records only the divergent criteria (C-31 through C-33) and any note-worthy nuance.

| Criterion | Weight | All V-01..V-05 verdict | Evidence basis |
|-----------|--------|------------------------|----------------|
| **C-01** | essential | PASS | 6-field header block defined; `[MOCK ARTIFACT -- NOT VERIFIED]` + Skill/Topic/Category/Date/Status/Flag present |
| **C-02** | essential | PASS | 3-category lookup table in S-2; HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED lists complete |
| **C-03** | essential | PASS | A-3 requires golden section headings, tables/gates, enforcement in expected positions |
| **C-04** | essential | PASS | FLAG computed as named variable in S-3; A-1 references `{FLAG from S-3 -- copied verbatim}` |
| **C-05** | essential | PASS | `simulations/mock/{topic}-{namespace}-mock-{date}.md` — namespace segment, not skill-id in path |
| **C-06** | recommended | PASS | Default table has correct 9 mappings including `topic → topic-plan` |
| **C-07** | recommended | PASS | All 3 fidelity-warning variants present including "REAL-REQUIRED at Tier 2+ for critical namespaces" qualifier |
| **C-08** | recommended | PASS | A-5 emits `Next: /mock:review {topic} ...` as final line |
| **C-09** | aspirational | PASS | Case 1 produces `"none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"` |
| **C-10** | aspirational | PASS | Dedicated `> TOPICS.md:` emit line in S-1 |
| **C-11** | aspirational | PASS | S-3 is named discrete step; `FLAG is a named variable`; A-1 references S-3 by name |
| **C-12** | aspirational | PASS | topic-status exclusion note present in default skill table alongside topic row |
| **C-13** | aspirational | PASS | A-2 explicitly positions fidelity warning before mock content with `---` delimiters |
| **C-14** | aspirational | PASS | Prohibition at both S-3 ("Do not re-evaluate or modify") and A-1 ("Copy FLAG verbatim. Do not rederive.") |
| **C-15** | aspirational | PASS | Dedicated `Exclusion constraint` column in default table (not inline annotation) |
| **C-16** | aspirational | PASS | "FLAG MUST NOT be recomputed anywhere in this run" — explicit run-scope |
| **C-17** | aspirational | PASS | `First rule` row is first entry in A-1 prohibition table |
| **C-18** | aspirational | PASS | Named path classes: step, conditional branch, fallback path, regeneration sequence + catch-all + bypass-order clarifier |
| **C-19** | aspirational | PASS | Anti-displacement names field-listing, category lookup, formatting + "or any other instruction in this step" + declarative closure |
| **C-20** | aspirational | PASS | `[A-1:FC]` row: category mismatch invisible to downstream tooling, silently corrupts trust tier, undetectable without manual inspection |
| **C-21** | aspirational | PASS | `Affirmative closure` row + `No-exemption` row — both present as separate table rows |
| **C-22** | aspirational | PASS | "or any other instruction in this step" catch-all in anti-displacement row |
| **C-23** | aspirational | PASS | `Failure consequence` row: corrupted value indistinguishable from correctly-computed one |
| **C-24** | aspirational | PASS | `All-governed` + `No-exemption` rows at A-1 — positive coverage and explicit no-exemption |
| **C-25** | aspirational | PASS | `Guarantee-break` row: "This violation breaks the closure guarantee stated in the Affirmative closure row above" |
| **C-26** | aspirational | PASS | `Cross-site ref [S-3:CS]` row: names `[A-1:FC]` with description of shared failure mechanism |
| **C-27** | aspirational | PASS | Guarantee-break and Cross-site ref are dedicated labeled rows — structurally isolated, not embedded clauses |
| **C-28** | aspirational | PASS | `[A-1:FC] -- the Failure consequence row in step A-1` — location-specific navigation anchor |
| **C-29** | aspirational | PASS | `[Mutual target of S-3:CS -- Cross-site reference row in S-3]` in A-1's Failure conseq row — backward anchor |
| **C-30** | aspirational | PASS | `[S-3:CS]` and `[A-1:FC]` bracket tokens at both sites as structured identifiers |

---

### C-31 through C-33 — Per-Variant Detail

**C-31 (pre-chain preamble):** All variants PASS. V-01's preamble is inside S-3 before all prohibition rows AND all computation cases. V-02–V-05 use P-0, which precedes both S-3 rows (computation and prohibition) and A-1 rows (prohibition chain) — the orientation point is at the earliest possible step in the run.

---

#### V-01 — Lifecycle Emphasis (Top of S-3, 5-Column Table)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-31 | PASS | "Cross-reference protocol: token resolution table." block at very top of S-3, before `FLAG is computed exactly once...` |
| C-32 | PASS | Preamble is the first content of S-3, before Case 1 — matches the rubric evidence example exactly (Round 11 V-01 pattern) |
| C-33 | PASS | Abbreviation key (`:CS`, `:FC`) + 5-column table (Token / Step / Row type / Paired token / Direction) with both rows populated |

**Aspirational: 25/25. Composite: 60 + 30 + 10 = 100.**

---

#### V-02 — Role Sequence (P-0 Step, 5-Column Table)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-31 | PASS | P-0 block is a dedicated, labeled step appearing before S-1 — precedes all prohibition rows and all computation cases |
| C-32 | PASS | P-0 appears before all FLAG computation cases (before S-3 entirely). C-32's explicit fail mode is "between computation cases and prohibition rows" — P-0 does not match that pattern. Semantic condition met: executor has cross-reference map before any FLAG logic is encountered, at an even earlier point than top-of-S-3 |
| C-33 | PASS | Abbreviation key + 5-column table in P-0 (identical structure to V-01) |

*Note: S-3 carries no preamble in V-02 — the cross-reference protocol is established once at P-0 and referenced via bracket tokens in S-3 and A-1. This means a regenerated-context executor entering S-3 directly will not have P-0's table in view — C-32 is structurally satisfied but behaviorally weaker than V-01 for cold-entry scenarios.*

**Aspirational: 25/25. Composite: 100.**

---

#### V-03 — Phrasing Register (P-0 + Imperative Lookup Directive)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-31 | PASS | Same P-0 structure as V-02 |
| C-32 | PASS | Same position as V-02 — P-0 precedes all FLAG computation cases |
| C-33 | PASS | Same 5-column table as V-02 |

*Bonus beyond rubric: (a) Explicit lookup obligation — "look it up in this table before processing the containing row. Do not decode bracket tokens from memory." This converts passive availability to triggered consultation, which the rubric does not yet score but seeds C-34 candidate behavior. (b) P-0 row navigation labels added to S-3 and A-1 bracket-token rows: `(P-0 table, row 1)` and `(P-0 table, row 2)` — forward navigation to the P-0 table from use sites. These exceed current rubric coverage.*

**Aspirational: 25/25. Composite: 100.**

---

#### V-04 — Inertia Framing (P-0 + S-3 Computation Boundary Reminder)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-31 | PASS | P-0 block is the C-31 preamble (identical to V-02) |
| C-32 | PASS | P-0 precedes all FLAG computation cases (same as V-02). Additionally: S-3 opens with "Protocol checkpoint" paragraph before computation cases — a boundary redirect naming the inertia failure mode explicitly: "If you are entering this step from a regenerated context or without P-0 in active memory, read P-0 before proceeding." The full structured table is in P-0; the checkpoint is a redirect, not the preamble. C-32 passes via P-0 positioning; the S-3 checkpoint is supplementary inertia protection beyond what C-32 requires. |
| C-33 | PASS | 5-column table in P-0 |

*Bonus beyond rubric: S-3 boundary checkpoint names the specific tokens used in S-3 (`[S-3:CS]` and `[A-1:FC]`), names the consequence of missing P-0, and explicitly redirects. This addresses the cold-entry gap that V-02 leaves open. Does not yet correspond to a v11 criterion but seeds a candidate C-35 variant: "compute-step boundary reminder naming the inertia failure mode."*

**Aspirational: 25/25. Composite: 100.**

---

#### V-05 — Full Convergence (P-0 + Imperative + Completeness Assertion + Activation Scope)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-31 | PASS | Same P-0 structure as V-02 |
| C-32 | PASS | P-0 precedes all FLAG computation cases |
| C-33 | PASS | Abbreviation key + 5-column table in P-0 |

*Bonus beyond rubric — two v12 seeds:*
- **(C-34 seed)** Protocol completeness assertion: "Protocol completeness: the table above lists ALL bracket tokens active in this run. No bracket token appears in any step that is not listed here. An executor who encounters a bracket token not in this table MUST stop and report: 'Token not in protocol: {token}.'" This closes the open-world assumption — the table is not merely a reference but a constraint. Unknown tokens become protocol violations, not silent unknowns.
- **(C-35 seed)** Activation scope declaration: "Protocol status: ACTIVE from this step (P-0) through step A-5." Names the protocol lifecycle explicitly so a regenerated-context executor can determine whether the protocol covers their current step by checking the declared scope.

**Aspirational: 25/25. Composite: 100.**

---

### Composite Score Summary

| Variant | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Band |
|---------|---------------|-----------------|-------------------|-----------|------|
| **V-01** | 60 | 30 | 10 (25/25) | **100** | Gold |
| **V-02** | 60 | 30 | 10 (25/25) | **100** | Gold |
| **V-03** | 60 | 30 | 10 (25/25) | **100** | Gold |
| **V-04** | 60 | 30 | 10 (25/25) | **100** | Gold |
| **V-05** | 60 | 30 | 10 (25/25) | **100** | Gold |

All variants achieve full criterion saturation across the v11 rubric. This is the **R12 convergence result**: the synthesis of R11's split findings (C-32 pass in V-01, C-33 pass in V-02) was achieved by all five variants.

---

### Ranking

R12 achieves a 5-way tie at 100. The ranking is resolved by beyond-rubric innovation:

| Rank | Variant | Differentiator |
|------|---------|----------------|
| 1 | **V-05** | Closes the open-world assumption (completeness assertion) + explicit activation scope — seeds both C-34 and C-35; the protocol becomes verifiable, not merely consultable |
| 2 | **V-03** | Imperative lookup obligation converts passive reference to triggered consultation; P-0 row navigation links (P-0 table, row 1/2) — seeds partial C-34 |
| 3 | **V-04** | S-3 boundary checkpoint directly protects against regenerated-context cold entry; names the failure mode at the point of encounter — seeds a compute-step inertia reminder candidate |
| 4 | **V-02** | Cleanest P-0 baseline — protocol established before any skill step; simplest form that achieves P-0 + C-33 together |
| 5 | **V-01** | Minimal synthesis form — top-of-S-3 satisfies C-32 most literally; single-step structure with no P-0 overhead |

---

### Excellence Signals from V-05 (Top Variant)

1. **Closed-world token namespace.** V-05's completeness assertion transforms the P-0 table from an open reference (tokens listed for convenience) to a closed constraint (all tokens listed; an unlisted token is a protocol violation requiring stop-and-report). This eliminates silent contextual resolution of unknown bracket tokens — the most dangerous failure mode in regenerated-context runs where new bracket tokens could be silently interpolated.

2. **Explicit activation scope declaration.** "ACTIVE from P-0 through A-5" gives a regenerated-context executor a run-boundary reference that does not require traversal of the entire skill body to answer "does the protocol apply to my current step?" The declaration is machine-checkable: step name appears within P-0–A-5 range → protocol applies.

3. **P-0 as protocol-first step architecture.** V-02–V-05 share this: placing the cross-reference protocol in a first-class numbered step before S-1 means the executor's first action in the skill is protocol registration, not skill logic. This ordering principle — protocol before subject — is more robust to partial execution than embedding protocol context inside the first computation step (V-01's form), because a partial-run restart can re-execute P-0 as a discrete unit without re-entering S-3.

4. **Layered protocol activation (V-03/V-05).** The combination of passive table availability (C-31/C-33) + imperative lookup obligation (V-03/V-05) + completeness assertion (V-05) creates three mutually reinforcing compliance layers: table is available → executor is required to consult it per token → executor is forbidden to process unlisted tokens without halting. Each layer closes a gap the previous one leaves open.

---

### v12 Seeds

| Candidate | Source | Description |
|-----------|--------|-------------|
| **C-34** | V-05 | Protocol completeness assertion: all bracket tokens enumerated at P-0; unlisted token triggers stop-and-report |
| **C-35** | V-05 | Activation scope declaration: explicit "ACTIVE from P-0 through A-5" statement in P-0 as run-boundary reference |
| **C-34 partial** | V-03 | Imperative lookup obligation: per-token triggered consultation rather than passive availability |
| **C-35 variant** | V-04 | Compute-step boundary reminder: inertia failure mode named at the entry point of S-3 as redirect to P-0 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Protocol completeness assertion at P-0 closes the open-world assumption: all bracket tokens explicitly enumerated, unlisted token triggers stop-and-report rather than silent contextual resolution (seeds C-34)", "Activation scope declaration names the protocol lifecycle explicitly ('ACTIVE from P-0 through A-5'), enabling regenerated-context executors to verify protocol applicability without full document traversal (seeds C-35)"]}
```
