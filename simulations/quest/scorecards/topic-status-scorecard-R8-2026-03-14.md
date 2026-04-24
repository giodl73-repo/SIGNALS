Now I have all the information needed. Let me evaluate all five variants against the full v8 rubric.

---

## Scorecard: `topic:status` — Round 8, Rubric v8 (max 210)

### Evaluation Strategy

R7 V-02 baseline against v8 = **205/210** — C-29 PASS, C-31 PASS, C-30 FAIL (combined branch). All five R8 variants inherit the full R7 V-02 body with modifications to C-30 axis. Criteria C-01 through C-28 are stable across all variants; scoring focuses on Tier 7 differential.

---

### Common Baseline Assessment (C-01 – C-28, all variants)

| ID | Criterion | Evidence (shared) | All 5 |
|----|-----------|-------------------|-------|
| C-01 | Signal discovery | `Glob: simulations/**/{topic}-*` → DISK_SIGNALS; zero-result handled: "No signals found for {topic}" | PASS |
| C-02 | Coverage percentage | `percent = VERIFIED / PLANNED * 100`; consistency guard: if UNVERIFIED non-empty and percent=100%, halt and recompute | PASS |
| C-03 | Gap identification | UNVERIFIED signals surfaced by name in COMMIT DECISION ("Committing now means shipping without: {list}"); not just counted | PASS |
| C-04 | Display-only behavior | "DISPLAY ONLY. Write no files." header + "Write no files." in DISPLAY GATE phase | PASS |
| C-05 | Readiness verdict | `Readiness: READY \| PARTIAL \| NOT READY` in COMMIT DECISION, threshold-qualified | PASS |
| C-06 | Namespace breakdown | COMMIT RISK BY NAMESPACE table with all 9 namespaces (scout through topic) | PASS |
| C-07 | Strategy cross-reference | `simulations/strategy.md` named in PHASE 2; missing case handled with explicit message | PASS |
| C-08 | Recency awareness | STALE EVIDENCE section with date and days-old count | PASS |
| C-09 | Actionable next step | HIGHEST PRIORITY RISK: `/{namespace}:{signal} {topic}` — concrete skill invocation form | PASS |
| C-10 | Structural namespace completeness | All 9 namespaces in table; zeros shown as `0 \| 0 \| --` | PASS |
| C-11 | Phase-gated execution | Four named phases; DISPLAY GATE with pre-display invariant | PASS |
| C-12 | Gap-first output ordering | [LAYER 1 -- STRUCTURAL] COMMIT RISK REGISTER precedes EXPOSURE SUMMARY in template | PASS |
| C-13 | Triple-redundancy ordering guard | [LAYER 1 STRUCTURAL], [LAYER 2 SEMANTIC], [LAYER 3 EXECUTION] with `ordering invariant` declared in [LAYER 3] | PASS |
| C-14 | Template-first structural absorption | `== OUTPUT TEMPLATE ==` section precedes `== EXECUTION PHASES ==` section | PASS |
| C-15 | Per-signal assertion chain | "Assert each signal individually. No batch evaluation." + per-planned-signal loop | PASS |
| C-16 | Consequence-framed readiness verdict | "Committing now means shipping without: {list of UNVERIFIED signals}" | PASS |
| C-17 | Labeled redundancy layers | All three `[LAYER N -- TYPE]` labels present at mechanism locations in template | PASS |
| C-18 | Assertion table pre-seeded in template | COMMIT RISK REGISTER table with VERIFIED\|UNVERIFIED column headers in OUTPUT TEMPLATE section | PASS |
| C-19 | Consequence vocabulary saturation | COMMIT RISK REGISTER, COMMIT RISK BY NAMESPACE, EXPOSURE SUMMARY, COMMIT DECISION, STALE EVIDENCE, HIGHEST PRIORITY RISK — all consequence-domain | PASS |
| C-20 | Assertion table as primary gap artifact | `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]` — exact required phrase present | PASS |
| C-21 | Execution phase names in consequence vocabulary | SIGNAL ACQUISITION / PER-SIGNAL COMMITMENT ASSERTION / EXPOSURE COMPUTATION / DISPLAY GATE — zero neutral or ordinal names | PASS |
| C-22 | Missing baseline as epistemic consequence | File-absent branch: "No planned baseline -- commit exposure is unquantifiable." — exact canonical form | PASS |
| C-23 | Phase name as compressed criterion statement | `PER-SIGNAL COMMITMENT ASSERTION` — granularity-scope term + decision-stake noun phrase | PASS |
| C-24 | Cross-layer vocabulary coherence | `[LAYER 3 -- EXECUTION: DISPLAY GATE render order:]` — layer label uses phase vocabulary, not ordinal | PASS |
| C-25 | Template field inline consequence annotation | `strategy.md: [FOUND \| NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]` — inline `if absent:` clause in field format string | PASS |
| C-26 | Granularity-prefix left-edge declaration | `PER-SIGNAL` is the leftmost token; COMMITMENT ASSERTION follows | PASS |
| C-27 | Full compressed phase name in C-24 layer labels | `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` — full granularity-prefix form present | PASS |
| C-28 | Field annotation phase-attribution | "if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute" — names specific C-21 phase; not generic epistemic language | PASS |

**Baseline: 200/210 across all five variants before Tier 7.**

---

### Tier 7 Differential Assessment (C-29, C-30, C-31)

#### C-29 — Multi-site phase-attributed annotation

All five variants carry the STALE EVIDENCE template field:
```
{signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
```
Phase name attributed (`PER-SIGNAL COMMITMENT ASSERTION`). Verb is `may rest on expired evidence` — degraded-not-blocked semantics, satisfying the required verb downgrade from `cannot execute`. C-28 and C-05 both pass (prerequisite satisfied).

**C-29: PASS — all five variants. +5 pts each.**

---

#### C-30 — Absent-topic early exit

| Variant | PHASE 2 structure | Verdict |
|---------|------------------|---------|
| V-01 | Two **numbered sequential** stop conditions: `1. If strategy.md absent → "No planned baseline..."` and `2. If strategy.md present but contains no entry for {topic} → "topic not registered: no planned signals for {topic}"` followed by `Stop before PHASE 3.` Structurally distinct branches, topic-specific message | **PASS** |
| V-02 | Combined: `If absent or no entry for {topic}: Output: "No planned baseline -- commit exposure is unquantifiable." Stop.` Single message, no distinction between axes, no topic-specific stop message | **FAIL** |
| V-03 | Formal GUARD block with two numbered entries: `(1) strategy.md absent → ...unquantifiable... and stop` and `(2) strategy.md present but {topic} not registered → "topic not registered: no planned signals for {topic}" and stop before PHASE 3`. Two-entry GUARD block; scorer cannot interpret as combined | **PASS** |
| V-04 | Named exits: `Exit A -- file absent: ... Stop.` and `Exit B -- topic not registered: If strategy.md present but contains no entry for {topic}: Output: "topic not registered: no planned signals for {topic}" Stop before PHASE 3.` Plus preamble declaration explicitly naming C-30 as architectural invariant | **PASS** |
| V-05 | GUARD block identical structure to V-03 with two numbered entries. Preamble declares: `"PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct stop conditions with distinct messages"`. Note: preamble labels dual-axis rule as `(C-31)` — this is a transcription error (should be C-30) but the GUARD block implementation is structurally correct and unambiguous | **PASS** |

**C-30: V-01 PASS, V-02 FAIL, V-03/V-04/V-05 PASS.**

---

#### C-31 — Per-register-row commit-consequence annotation

All five variants carry the register row template:
```
| 1 | {ns} | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |
```
Inline `if absent: ships without this signal on commit` in the row format string. Commit-framed vocabulary (`ships without...on commit`), not phase-execution-framed. C-09 and C-25 both pass (prerequisite satisfied). V-05 additionally declares this in the PHASE 2 OUTPUT block: `if UNVERIFIED: ships without this signal on commit` — multi-site.

**C-31: PASS — all five variants. +5 pts each.**

---

### Per-Variant Scorecard

#### V-01 — Sequential guard, minimum delta

| Tier | Criteria | Points | Pass |
|------|----------|--------|------|
| Essential | C-01–C-04 | 60/60 | 4/4 |
| Recommended | C-05–C-07 | 30/30 | 3/3 |
| Aspirational | C-08–C-12 | 25/25 | 5/5 |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 |
| **Total** | | **210/210** | **31/31** |

Hypothesis confirmed: numbered sequential guards satisfy C-30 with minimum structural change from R7 V-02.

---

#### V-02 — C-30 withheld (isolation test)

| Tier | Criteria | Points | Pass |
|------|----------|--------|------|
| Essential | C-01–C-04 | 60/60 | 4/4 |
| Recommended | C-05–C-07 | 30/30 | 3/3 |
| Aspirational | C-08–C-12 | 25/25 | 5/5 |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 |
| Tier 7 C-29 | C-29 | 5/5 | PASS |
| Tier 7 C-30 | C-30 | **0/5** | **FAIL** |
| Tier 7 C-31 | C-31 | 5/5 | PASS |
| **Total** | | **205/210** | **30/31** |

Isolation confirmed: combined branch (`if absent or no entry for {topic}`) passes C-12 (gap-first ordering) and C-22 (epistemic consequence statement for file-absent) but fails C-30 — no topic-specific stop message, no structural separation of axes. C-12 ⊄ C-30 confirmed.

---

#### V-03 — Lifecycle emphasis, dual GUARD contract

| Tier | Criteria | Points | Pass |
|------|----------|--------|------|
| Essential | C-01–C-04 | 60/60 | 4/4 |
| Recommended | C-05–C-07 | 30/30 | 3/3 |
| Aspirational | C-08–C-12 | 25/25 | 5/5 |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 |
| **Total** | | **210/210** | **31/31** |

Additional redundancy: C-11/C-12 evidence appears in formal INPUT/GUARD/OUTPUT blocks. GUARD block with two named entries makes C-30 distinction auditable from the contract declaration alone, not dependent on reading the execution prose body.

---

#### V-04 — C-30 + vocabulary preamble + inertia framing

| Tier | Criteria | Points | Pass |
|------|----------|--------|------|
| Essential | C-01–C-04 | 60/60 | 4/4 |
| Recommended | C-05–C-07 | 30/30 | 3/3 |
| Aspirational | C-08–C-12 | 25/25 | 5/5 |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 |
| **Total** | | **210/210** | **31/31** |

Additional structural redundancy: vocabulary coherence preamble explicitly declares C-30 dual-axis exit as an architectural invariant. "PHASE 2 implements dual-axis exit" with distinct message descriptions appears at preamble level before the template is even reached. Named Exit A / Exit B pattern differentiates from V-01's numbered sequentials. PRIMARY ADVERSARY framing deepens C-16 consequence verdict (commit-without-evidence as default outcome if status not checked) — potential v9 signal, not scoreable in v8.

---

#### V-05 — Lifecycle + full Tier 7 + inertia framing

| Tier | Criteria | Points | Pass |
|------|----------|--------|------|
| Essential | C-01–C-04 | 60/60 | 4/4 |
| Recommended | C-05–C-07 | 30/30 | 3/3 |
| Aspirational | C-08–C-12 | 25/25 | 5/5 |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 |
| **Total** | | **210/210** | **31/31** |

Note: Preamble contains a transcription error — labels dual-axis exit rule as `(C-31)` instead of `(C-30)`. The PHASE 2 GUARD block implementation is structurally correct (two numbered entries, topic-specific message, stops before PHASE 3). Implementation satisfies C-30; preamble label error is a documentation defect, not a structural failure.

Additional structural density: each Tier 7 criterion appears at ≥ 2 structural sites simultaneously — (C-29) STALE EVIDENCE template field + PHASE 2 OUTPUT declaration; (C-30) vocabulary preamble + PHASE 2 GUARD block; (C-31) register row template + PHASE 2 OUTPUT declaration. A scorer can verify all Tier 7 criteria from contract declarations alone without reading the execution prose.

---

### Ranking

| Rank | ID | Score | Differentiator |
|------|----|-------|----------------|
| T-1 | V-01 | 210/210 | Minimum delta — numbered sequential guards |
| T-1 | V-03 | 210/210 | Formal GUARD block — structural unambiguity for C-30 |
| T-1 | V-04 | 210/210 | Preamble invariant declaration + named exits (Exit A/B) |
| T-1 | V-05 | 210/210 | Multi-site Tier 7 evidence + GUARD block + preamble + inertia |
| 5 | V-02 | 205/210 | C-30 withheld — confirms C-12 ⊄ C-30, combined branch insufficient |

V-05 is the auditability champion: all three Tier 7 criteria are verifiable from contract declarations without reading execution prose, and criteria appear at multiple structural sites. V-01 is the minimally-compliant champion: smallest structural change to close C-30 from R7 V-02 baseline.

---

### Excellence Signals (from top-scoring variants)

**Signal 1 — GUARD-block dual-entry as structural contract for multi-axis exits (V-03, V-05)**
A formal `GUARD: (1) ... (2) ...` block inside a phase contract declaration makes multi-axis stop conditions structurally named invariants. A two-entry GUARD block cannot be misread as a combined branch; it is auditable at the contract level before the execution prose is read. Minimum-delta approaches (V-01 numbered sequential prose, V-04 named Exit A/B) satisfy C-30 but leave the distinction auditable only by reading the prose. GUARD blocks elevate the distinction to the contract declaration level.

**Signal 2 — Criterion-tagged preamble as pre-execution specification (V-04, V-05)**
Declaring each structural invariant in a vocabulary coherence preamble with explicit criterion references (e.g., `(C-30)`, `(C-26, C-27)`) converts the preamble into a compressed specification: any implementation that diverges from a declared invariant is a detectable error. This pattern is distinct from execution documentation — the preamble is audited first; the implementation is verified against it, not the other way around. V-05's transcription error (labeling C-30 dual-axis rule as `(C-31)`) is the only defect, confirming that preamble accuracy is independently load-bearing.

**Signal 3 — Multi-site Tier 7 criterion evidence propagation (V-05)**
Each Tier 7 criterion appears at ≥ 2 structural sites: (C-29) in STALE EVIDENCE template field AND PHASE 2 OUTPUT declaration; (C-31) in register row template AND PHASE 2 OUTPUT declaration. This cross-site redundancy means the criterion is scoreable from either the template section or the contract block alone — neither site is necessary; both are sufficient. The pattern suggests a Tier 8 candidate: criteria whose evidence appears in n ≥ 3 structurally independent sites (template, preamble, execution phase contract).

---

### C-30 Isolation Confirmed

V-02 scores 205 and V-01 scores 210 — a clean 5-point gap. The combined `if absent or no entry for {topic}` branch satisfies C-12 (gap-first ordering) and C-22 (epistemic consequence statement) but fails C-30 regardless of the message text. The combined branch is structurally insufficient: structural separation of the two axes — not message content — is the criterion gate.

---

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["GUARD-block dual-entry pattern elevates multi-axis stop conditions to structural contracts auditable before execution prose — distinct from numbered-prose or named-exit approaches", "Criterion-tagged preamble as pre-execution specification converts invariant declarations into checkable contracts; implementation verified against preamble, not the reverse", "Multi-site Tier 7 evidence propagation: each criterion present in template field AND phase contract OUTPUT declaration simultaneously, making criteria verifiable from contracts alone without reading execution prose"]}
```
