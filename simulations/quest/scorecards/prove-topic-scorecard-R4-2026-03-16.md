## Quest Score — prove-topic Round 4 (Rubric v14)

**Scoring note**: Rubric criteria C-04 (pass condition truncated) and C-05 through C-10 are not fully shown. Criteria C-05–C-10 are inferred from variation content and the rubric scoring formula. V-02 is truncated (only SETUP visible); V-03–V-05 are absent from input. Scoring proceeds on available material.

---

### Inferred Criteria (C-04–C-10)

| ID | Weight | Inferred Pass Condition |
|----|--------|------------------------|
| C-04 | essential | Synthesis stage explicitly names `/topic-story` as the downstream consumer |
| C-05 | essential | Counter-hypothesis framed in Stage 1 and resolved in Stage 5 with a typed verdict |
| C-06 | recommended | Incumbent named and displacement framing threads through all stages |
| C-07 | recommended | Numerical confidence chain tracked per stage with final derivation in synthesis |
| C-08 | recommended | Minimum evidence counts stated (≥ 3 per stage) |
| C-09 | aspirational | Campaign blocking gate: hard stop when scout artifact not found |
| C-10 | aspirational | Stage boundary announce line after each stage completion |

---

### V-01 — Phrasing Register: Conversational + Imperative

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 — Five stages in sequence | **PASS** | Stage 1→2→3→4→5 fully present in order, named Hypothesis / Web Search / Intelligence / Analysis / Synthesis |
| C-02 — Scout artifact named before hypothesis | **PASS** | Setup step 2 names `{topic}-scout-record-{date}.md`, gate blocks on missing file; Stage 1 entry requires `scout_artifact` path already recorded; Stage 1 copies `source_scout_artifact: [path from Setup — copy, do not infer]` |
| C-03 — Progressive artifact writes | **PASS** | Five separate Write instructions: hypothesis / websearch / intelligence / analysis / synthesis — one per stage, in stage body |
| C-04 — Synthesis signals /topic-story readiness | **PASS** | Stage 5 Announce: *"Evidence brief ready for /topic-story. Campaign complete."* — names downstream skill explicitly |
| C-05 — Counter-hypothesis resolved | **PASS** | Stage 1 frames `counter_hypothesis`; Stage 5 has explicit "Counter-hypothesis resolution" section with verdict options REFUTED / PARTIALLY REFUTED / OPEN RISK and citation requirement |
| C-06 — Displacement framing throughout | **PASS** | Setup records `incumbent_strength` + `incumbent_vulnerability`; each stage has displacement check; Stage 4 produces `Aggregate displacement verdict` |
| C-07 — Confidence chain with derivation | **PASS** | `confidence_prior` in S1; `confidence_delta_s2/s3/s4` per stage; S5 shows explicit derivation formula `prior + s2 + s3 + s4 ± risk_adj = final` |
| C-08 — Minimum evidence counts | **PASS** | S2: "at least 3 external sources"; S3: "at least 3 relevant internal references" |
| C-09 — Blocking gate for missing scout | **PASS** | "If not found: stop. CAMPAIGN BLOCKED — no scout artifact." |
| C-10 — Stage boundary announce lines | **PASS** | Each stage ends with Announce line naming stage, key value, and "Stage N ready" |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 2/2 → 10  
**V-01 Composite: 100/100** — Golden threshold met ✓

---

### V-02 — Lifecycle Emphasis: Stage-Body-First

Only the SETUP block is visible in the input. Stage bodies 1–5 are absent.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | UNKNOWN | Sequence listed in header but bodies not present |
| C-02 | PARTIAL | SETUP contains `scout_artifact:` field; stage 1 gate cannot be confirmed |
| C-03–C-10 | UNKNOWN | Stage bodies absent |

**V-02 Score: Not scoreable — input truncated.** Cannot reach a composite.

---

### V-03 through V-05

**Not provided in input.** Cannot score.

---

### Rankings

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-01 | 100 | ✓ |
| — | V-02 | N/A (truncated) | — |
| — | V-03–V-05 | N/A (absent) | — |

---

### Excellence Signals — V-01

1. **CAMPAIGN BLOCKED gate** — explicit hard stop before Stage 1 when scout artifact is absent; prevents the skill from running on no foundation
2. **incumbent_strength / incumbent_vulnerability in Setup** — displacement framing is anchored before any hypothesis forms, not bolted on at synthesis
3. **Counter-hypothesis as a first-class artifact field** — framed in Stage 1, travels through all stages, resolved with a typed verdict in Stage 5
4. **Confidence chain with explicit arithmetic** — each stage contributes a signed delta; Stage 5 shows the derivation, making confidence reviewable not just asserted
5. **"Copy, do not infer" directive** — `source_scout_artifact: [path from Setup — copy, do not infer]` prevents hallucinated artifact paths downstream

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["CAMPAIGN BLOCKED gate before Stage 1", "incumbent_strength/vulnerability in Setup anchors displacement before hypothesis", "counter-hypothesis as first-class field resolved with typed verdict", "confidence chain with explicit arithmetic derivation", "copy-do-not-infer directive for artifact paths"]}
```
* | SYNTHESIS DECLARATIONS present |
| C-05 | 10 | **PASS** | Stage 4 cross-check; Stage 5 chain confirmation: "S2=[v]+S3=[v]+S4=[v]=[N]. Stage 4=[M]. Match: [T/F]." |
| C-06 | 8 | **PASS** | ROLE B fields declared; CAMPAIGN BLOCKED on false |
| C-07 | 8 | **PASS** | 11 fields + derivations; schema_compliance_confirmed present |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution table with verdicts |
| C-09 | 3 | **PASS** | Lock 1 + Lock 2 with not_triggered else branch |
| C-10 | 3 | **PASS** | Per-stage reads; Stage 5 requires "Stage 4 displacement verdict: [Yes/No/Pending]" and artifact Displacement read citation |
| C-11 | 2 | **PASS** | Mechanical enforcement language throughout |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS block |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS isolation |
| C-14 | 2 | **PASS** | Bidirectional label registry + inline echo |
| C-15 | 2 | **PASS** | CAMPAIGN OPEN + INCUMBENT ANCHOR before SESSION INVARIANTS |
| C-16 | 2 | **PASS** | Per-stage Displacement read fields in Stages 2/3/4 |
| C-17 | 2 | **PASS** | Explicit prohibition: "Invariant F -- SYNTHESIS FORMAT ERROR if in prose" |
| C-18 | 2 | **FAIL** | SESSION INVARIANTS E uses "FORMAT ERROR" not "Invariant E checkpoint -- FAIL"; no canonical label registered |
| C-19 | 2 | **FAIL** | Invariant D uses {status_quo_comparator} literal, no `[incumbent from CAMPAIGN OPEN]` binding |
| C-20 | 2 | **PASS** | Write confirmations explicitly describe artifact content: "Artifact includes: Displacement read: [value]" for websearch, interview, prototype; confirm write echoes value |

**V-03 Score: 96 / 100** — All 5 essential PASS

---

### V-04 — Combo: Invariant E + Invariant D Binding (C-18 + C-19)

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs in order |
| C-02 | 10 | **PASS** | All 6 artifacts |
| C-03 | 10 | **PASS** | Templates use `[incumbent from CAMPAIGN OPEN]`; verbatim at Stages 2/3/4 |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS present |
| C-05 | 10 | **PASS** | Stage 4 + Stage 5 chain confirmation; "S2=[v]+S3=[v]+S4=[v]=[N]. Stage 4=[M]. Match: [T/F]." |
| C-06 | 8 | **PASS** | ROLE B explicit; CAMPAIGN BLOCKED stated |
| C-07 | 8 | **PASS** | 11 fields + derivations; schema_compliance_confirmed echoes "Invariant E checkpoint -- FAIL" verbatim |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution |
| C-09 | 3 | **PASS** | Dual-lock with both locks; not_triggered path |
| C-10 | 3 | **PASS** | Per-stage reads; Stage 5 cites Stage 4 verdict; `[incumbent from CAMPAIGN OPEN]` by bound name |
| C-11 | 2 | **PASS** | Mechanical language throughout |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS block |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS isolation |
| C-14 | 2 | **PASS** | Bidirectional: "Drift in either direction = self-incriminating"; all failure modes (D, A, B, C, E, F) registered |
| C-15 | 2 | **PASS** | CAMPAIGN OPEN + INCUMBENT ANCHOR |
| C-16 | 2 | **PASS** | Per-stage Displacement reads |
| C-17 | 2 | **PASS** | SYNTHESIS DECLARATIONS prohibition |
| C-18 | 2 | **PASS** | SESSION INVARIANTS E: canonical "Invariant E checkpoint -- FAIL" registered; ROLE A confirms label at Step 3; Stage 0 EXIT echoes it; schema_compliance_confirmed echoes verbatim |
| C-19 | 2 | **PASS** | `[incumbent from CAMPAIGN OPEN]` binding in all three Invariant D templates; "Deviation or literal re-establishment = FORMAT ERROR" |
| C-20 | 2 | **FAIL** | Write confirmations do not describe Displacement read as artifact file content — field appears in stage output only |

**V-04 Score: 98 / 100** — All 5 essential PASS

---

### V-05 — Full Integration (C-18 + C-19 + C-20 + gap fixes)

| ID | Pts | Result | Evidence |
|----|-----|--------|---------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs in order; Stage 0 EXIT text names Invariant D binding + Invariant E label + ARTIFACT DISPLACEMENT RULE |
| C-02 | 10 | **PASS** | All 6 artifacts written; write confirmations include displacement read values |
| C-03 | 10 | **PASS** | `[incumbent from CAMPAIGN OPEN]` binding throughout Stages 2/3/4; "Template deviation = FORMAT ERROR. Naming incumbent as literal string = FORMAT ERROR" |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS with all three fields; Invariant F checkpoint stated |
| C-05 | 10 | **PASS** | Stage 4: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]." Stage 5 chain confirmation with S2+S3+S4 reconstruction; "null_tally_final confirmed: [N]" |
| C-06 | 8 | **PASS** | "ROLE B execution (declare all fields by name -- required output)": scout_artifact with explicit not-found format, scout_loaded, gate_s_cleared |
| C-07 | 8 | **PASS** | 11 fields + derivations; schema_compliance_confirmed echoes "Invariant E checkpoint -- FAIL"; Invariant C enforced inline |
| C-08 | 8 | **PASS** | Counter-hypothesis resolution table; OPEN RISK triggers one-tier reduction before ATOMIC DUAL-LOCK |
| C-09 | 3 | **PASS** | "DUAL-LOCK EVALUATION (DUAL-LOCK ERROR if conditions met but locks not declared)"; Lock 1 names adversarial_reviewer_type; Lock 2 shows before/after cap values; not_triggered path present |
| C-10 | 3 | **PASS** | Per-stage reads; Stage 5 must cite "Stage 4 displacement verdict" and Displacement read from Stage 4 artifact |
| C-11 | 2 | **PASS** | All enforcement uses mechanical labels; "Cannot be softened or overridden" |
| C-12 | 2 | **PASS** | Standalone SESSION INVARIANTS block before Stage 0 |
| C-13 | 2 | **PASS** | SYNTHESIS DECLARATIONS with explicit prohibition and Invariant F label |
| C-14 | 2 | **PASS** | "All failure modes (D, A, B, C, E, F) are bidirectionally detectable (registry + inline echo)" |
| C-15 | 2 | **PASS** | CAMPAIGN OPEN + INCUMBENT ANCHOR; "All displacement checks across Stages 2, 3, and 4 bind to the incumbent declared here" |
| C-16 | 2 | **PASS** | Displacement read in Stages 2/3/4; Stage 5 ENTRY CONDITIONS confirm all three reads written |
| C-17 | 2 | **PASS** | "Do not embed these values in prose sentences... Invariant F checkpoint -- SYNTHESIS FORMAT ERROR" |
| C-18 | 2 | **PASS** | SESSION INVARIANTS E: "Invariant E checkpoint -- FAIL" registered; ROLE A confirms; Stage 0 EXIT names it; schema_compliance_confirmed echoes verbatim |
| C-19 | 2 | **PASS** | `[incumbent from CAMPAIGN OPEN]` in all three templates; binding resolves to incumbent_name above; literal string = FORMAT ERROR in ROLE A confirmation |
| C-20 | 2 | **PASS** | Each write confirmation: "Artifact content includes: Displacement read: [copy — written to file]"; Stage 5 ENTRY CONDITIONS: "All three evidence artifacts confirmed written with Displacement read fields" |

**V-05 Score: 100 / 100** — All 5 essential PASS

---

## Ranking

| Rank | Variation | Score | All Essential PASS | New criteria |
|------|-----------|-------|-------------------|--------------|
| 1 | V-05 (Full integration) | **100** | Yes | C-18 + C-19 + C-20 |
| 2 | V-04 (C-18 + C-19) | **98** | Yes | C-18 + C-19 |
| 3 | V-01 (C-18 only) | **96** | Yes | C-18 |
| 3 | V-02 (C-19 only) | **96** | Yes | C-19 |
| 3 | V-03 (C-20 only) | **96** | Yes | C-20 |

Single-axis variations tie at 96 — each gains 2 pts on its target criterion, misses 4 pts on the other two. V-04 gains 4, misses 2. V-05 gains all 6 new pts plus inherits R3 full score.

---

## Excellence Signals from V-05

**Pattern 1 — ARTIFACT DISPLACEMENT RULE as a locked campaign-level rule alongside SESSION INVARIANTS.**
V-05 places the rule in the pre-stage registration section ("ARTIFACT DISPLACEMENT RULE (locked): ...") with ROLE A confirming it alongside the six invariant rows. This makes artifact displacement portability architecturally equivalent to Invariant D compliance — not a per-stage reminder but a campaign-registered invariant. V-01 through V-04 either omit this or add it as a loose annotation.

**Pattern 2 — Stage 5 ENTRY CONDITIONS gate on artifact displacement reads.**
"All three evidence artifacts confirmed written with Displacement read fields" appears as an explicit entry precondition for Stage 5. This creates backward accountability: the synthesis stage cannot begin until artifact portability is confirmed, closing the gap where a model might produce stage-level Displacement reads without writing them to files.

**Pattern 3 — Stage 0 EXIT SIGNAL as a deployment receipt for the full enforcement architecture.**
V-05 Stage 0 EXIT text names all three active controls: "Invariant D bound to [incumbent from CAMPAIGN OPEN]. Invariant E checkpoint -- FAIL registered. ARTIFACT DISPLACEMENT RULE active." This turns the gate exit into a structural assertion about the full enforcement state — any missing control is self-incriminating at the first checkpoint after campaign open.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["ARTIFACT DISPLACEMENT RULE registered as a locked campaign-level rule in the pre-stage SESSION INVARIANTS section with ROLE A confirmation — elevates artifact displacement portability to the same architectural status as Invariant D compliance", "Stage 5 ENTRY CONDITIONS gate on all three evidence artifact Displacement reads confirmed written — ties portability accountability to synthesis stage entry, blocking the gap where stage-level reads are not written to artifact files", "Stage 0 EXIT SIGNAL text declares all three active enforcement contexts as a deployment receipt — Invariant D binding, Invariant E label, and ARTIFACT DISPLACEMENT RULE named together, making any missing control self-incriminating at the first post-open checkpoint"]}
```
