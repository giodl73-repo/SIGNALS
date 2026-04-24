## prove-topic — Round R3 Scoring

### Rubric v3 — Criteria Summary

| ID | Tier | Points | Description |
|----|------|--------|-------------|
| C-01 | Essential | 10 | All five stages present |
| C-02 | Essential | 10 | Hypothesis grounded in scout signals |
| C-03 | Essential | 10 | Artifact written per stage |
| C-04 | Essential | 10 | Synthesis terminal and complete |
| C-05 | Essential | 10 | Topic prefix consistent |
| C-06 | Recommended | 10 | Stage order enforced |
| C-07 | Recommended | 10 | Scout handoff explicit |
| C-08 | Recommended | 10 | Synthesis signals topic-story handoff |
| C-09 | Aspirational | 4 | Thin-evidence propagates to synthesis |
| C-10 | Aspirational | 4 | Progress narrated per stage |
| C-11 | Aspirational | 4 | Hypothesis hard-gated on scout |
| C-12 | Aspirational | 4 | Comparator anchored at session open |
| C-13 | Aspirational | 4 | Per-artifact path in every write instruction |
| C-14 | Aspirational | 4 | Counter-evidence unconditionally required |
| C-15 | Aspirational | 4 | Gate clearance in hypothesis artifact |

**Max: 108 · Golden threshold: 80**

---

### V-01 — Evidence Weighting

| Criterion | Verdict | Evidence Note | Pts |
|-----------|---------|---------------|-----|
| C-01 | PASS | All five stages (hypothesis, web search, intelligence, prototype, synthesis) present | 10 |
| C-02 | PASS | STAGE 0 loads scout; `scout_anchor: [slug from GATE S]` in Stage 1 frontmatter | 10 |
| C-03 | PASS | Every stage has explicit `Write:` instruction with named path | 10 |
| C-04 | PASS | "Terminal stage. No further stages follow." Synthesis has Evidence Ledger Final, Findings, Counter-Evidence, Composite Confidence, Handoff | 10 |
| C-05 | PASS | All write instructions: `simulations/prove/{topic}/{topic}-X-{date}.md` — per-artifact naming throughout | 10 |
| C-06 | PASS | "Five stages execute in fixed order. Each stage writes its artifact before the next begins." All confirms say "— then advance to STAGE N" | 10 |
| C-07 | PASS | `scout_anchor: [slug from GATE S]` — named slug in hypothesis frontmatter | 10 |
| C-08 | PASS | Synthesis Handoff: `next: topic-story`; confirm: "Ready for topic-story" | 10 |
| C-09 | PASS | Evidence ledger tracks quality (Strong/Moderate/Thin) per stage; prototype Thin → `thin_evidence_cap: true`; synthesis Evidence Ledger Final reads cap | 4 |
| C-10 | PARTIAL | Confirm tokens ("Artifact written: X — then advance") confirm creation but provide no prose narrative of what was found | 2 |
| C-11 | PASS | "GATE S: Scout record is on file before proceeding. Do not write the hypothesis until this gate is confirmed." Explicit blocking gate | 4 |
| C-12 | PARTIAL | `Status-quo comparator` introduced in Stage 1 body — not at campaign open. Not referenced by name at S2/S3 | 2 |
| C-13 | PASS | Every write instruction names full path; `{topic}-` prefix in every per-stage instruction | 4 |
| C-14 | PASS | Synthesis `### Counter-Evidence` is MANDATORY with explicit null fallback: "uniformity is recorded as a null result, not suppressed. Recommend adversarial review." | 4 |
| C-15 | PASS | Stage 1 frontmatter: `gate_s_cleared: true` — gate clearance traceable from artifact | 4 |

**V-01 Total: 104 / 108**

---

### V-02 — Confidence Calibration

| Criterion | Verdict | Evidence Note | Pts |
|-----------|---------|---------------|-----|
| C-01 | PASS | All five stages present | 10 |
| C-02 | PASS | STAGE 0 loads scout; `scout_anchor: [slug from GATE S]` in hypothesis frontmatter | 10 |
| C-03 | PASS | Every stage has `Write:` instruction | 10 |
| C-04 | PASS | "Terminal stage. No further stages follow." Synthesis has Confidence Ledger Final, Findings, Counter-Evidence, Composite Confidence, Status-Quo Comparison, Handoff | 10 |
| C-05 | PASS | All write instructions use `{topic}-` prefixed full paths | 10 |
| C-06 | PASS | "Stages run in fixed sequence. Each stage scores its evidence contribution before the next stage opens." | 10 |
| C-07 | PASS | `scout_anchor: [slug from GATE S]` in hypothesis frontmatter — named | 10 |
| C-08 | PASS | Synthesis Handoff: `next: topic-story` | 10 |
| C-09 | PASS | Per-stage `< 4` cap rule with explicit WARNING text; synthesis Confidence Ledger Final shows cap triggered; "Cap applied: [yes/no]" | 4 |
| C-10 | PARTIAL | Confirm tokens ("Artifact written: X — advance") are structural, no prose summary of what was found | 2 |
| C-11 | PASS | "GATE S: Scout record confirmed. Do not advance to Stage 1 until this gate is confirmed." Blocking gate present | 4 |
| C-12 | PARTIAL | `status_quo_comparator` introduced at Stage 1 frontmatter, not at session open. S3 references it but S2 counter-evidence doesn't explicitly anchor to it | 2 |
| C-13 | PASS | Per-artifact full path in every write instruction | 4 |
| C-14 | PASS | Synthesis Counter-Evidence section MANDATORY with null fallback: "Null result recorded. Confidence composite adjusted: maximum score reduced by 1 point… Recommend adversarial review." | 4 |
| C-15 | PASS | Stage 1 frontmatter: `gate_s_cleared: true` | 4 |

**V-02 Total: 104 / 108**

---

### V-03 — Artifact Chaining

| Criterion | Verdict | Evidence Note | Pts |
|-----------|---------|---------------|-----|
| C-01 | PASS | All five stages present | 10 |
| C-02 | PASS | STAGE 0 loads scout; Stage 1 frontmatter: `prior_artifact: [scout path from GATE S]` + `scout_anchor: [scout slug]` | 10 |
| C-03 | PASS | Every stage has `Write:` instruction; confirms use "Chain link N written:" phrasing | 10 |
| C-04 | PASS | "Terminal stage. This is the last link in the chain." Synthesis frontmatter `chain_complete: true`; sections: Chain Summary, Findings, Counter-Evidence, Confidence, Handoff | 10 |
| C-05 | PASS | All write instructions name full `{topic}-` prefixed paths | 10 |
| C-06 | PASS | "Each artifact names its predecessor in frontmatter." Advance instructions enforce sequence | 10 |
| C-07 | PASS | `scout_anchor: [scout slug]` in Stage 1 frontmatter — named | 10 |
| C-08 | PASS | Synthesis Handoff: `next: topic-story`; frontmatter `next_artifact: topic-story` | 10 |
| C-09 | PASS | `thin_evidence_inherited` propagates S2→S3→S4 via frontmatter chain; Stage 4 sets `thin_evidence_propagated: true`; synthesis Confidence reads propagation flags | 4 |
| C-10 | PARTIAL | "Chain link N written: X" confirms artifact only; no prose narrative of finding | 2 |
| C-11 | PASS | "Confirm scout artifact path before proceeding. Do not open Stage 1 without this confirmation." Blocking gate | 4 |
| C-12 | PARTIAL | `status_quo_comparator` in Stage 1 frontmatter — not registered at session open. S3 counter-evidence references it; S2 does not | 2 |
| C-13 | PASS | Per-artifact full path in every write instruction | 4 |
| C-14 | PASS | Synthesis Counter-Evidence MANDATORY: null fallback — "cannot be rated HIGH without adversarial input." | 4 |
| C-15 | PASS | Stage 1 frontmatter: `gate_s_cleared: true`; also GATE S records `scout_path` which Stage 1 carries as `prior_artifact` | 4 |

**V-03 Total: 104 / 108**

---

### V-04 — Active Counter-Evidence Posture + Gate Trace (C-14/C-15 amplified)

| Criterion | Verdict | Evidence Note | Pts |
|-----------|---------|---------------|-----|
| C-01 | PASS | All five stages present | 10 |
| C-02 | PASS | STAGE 0 loads scout with slug/path table; GATE S checks `key_finding: [recorded]`; Stage 1 frontmatter: `scout_anchor: [slug from GATE S]` | 10 |
| C-03 | PASS | Every stage has `Write:` instruction | 10 |
| C-04 | PASS | "Terminal stage." Synthesis: Findings, Counter-Evidence Register, Status-Quo Comparison, Confidence, Handoff — all required sections present | 10 |
| C-05 | PASS | All write instructions use full `{topic}-` prefixed paths | 10 |
| C-06 | PASS | Stages advance via "— advance to STAGE N" in every confirm. "Full prove evidence campaign" opens with fixed-sequence intent | 10 |
| C-07 | PASS | `scout_anchor: [slug from GATE S]` in hypothesis frontmatter — named | 10 |
| C-08 | PASS | Synthesis Handoff: `next: topic-story`; `counter_evidence_status` field in handoff block | 10 |
| C-09 | PASS | Mandatory Part B counter-evidence searches at S2/S3/S4 each produce explicit null-result fallbacks that aggregate into synthesis Counter-Evidence Register; synthesis Confidence field: "Counter-evidence impact: [None found (adjusted)…]" | 4 |
| C-10 | PARTIAL | Confirm tokens ("Artifact written: X — advance") are structural; no prose narrative of what was found | 2 |
| C-11 | PASS | GATE S: 4-checkbox clearance, "Do not open Stage 1 until all four checkboxes are marked." Strongest blocking gate of any variation | 4 |
| C-12 | **PASS** | `status_quo_comparator` and `counter_evidence_target` registered in CAMPAIGN PREAMBLE **before STAGE 0** — anchored before any stage. S2, S3, S4 all `Carry forward from preamble:` and Part B anchors to `status_quo_comparator`. V-04 pattern is the C-12 exemplar | **4** |
| C-13 | PASS | Per-artifact full path in every write instruction | 4 |
| C-14 | PASS | Synthesis Counter-Evidence Register is MANDATORY table; null fallback: "Confidence is not rated HIGH on this basis alone. Adversarial review is required… Confidence adjusted to MEDIUM max." | 4 |
| C-15 | PASS | Stage 1 frontmatter: `gate_s_cleared: true` AND `gate_s_path: [scout path confirmed at GATE S]`; explicit comment: "gate compliance can be audited from the artifact chain without replaying the session" | 4 |

**V-04 Total: 106 / 108**

---

### V-05 — Full Excellence Signal Compound (R1 + R2 + evidence weighting)

| Criterion | Verdict | Evidence Note | Pts |
|-----------|---------|---------------|-----|
| C-01 | PASS | All five stages present | 10 |
| C-02 | PASS | STAGE 0 slug/path table; `scout_anchor` + `scout_path` in hypothesis frontmatter; "Do not derive from general knowledge" | 10 |
| C-03 | PASS | Every stage has `Write:` instruction | 10 |
| C-04 | PASS | "Terminal stage. No stages follow this one." Synthesis: Evidence Ledger Final, Findings, Counter-Evidence Register, Status-Quo Comparison, Composite Confidence, Handoff — most complete synthesis structure of any variation | 10 |
| C-05 | PASS | All write instructions use full `{topic}-` prefixed paths | 10 |
| C-06 | PASS | "No stage opens without the preceding artifact confirmed." Advance sequence enforced | 10 |
| C-07 | PASS | `scout_anchor: [slug from GATE S]` and `scout_path: [path from GATE S]` in hypothesis frontmatter | 10 |
| C-08 | PASS | Synthesis Handoff: `next: topic-story`; `ready: [true/false]` field; `counter_evidence_status` | 10 |
| C-09 | PASS | Evidence ledger (Strong/Moderate/Thin) per stage; prototype Thin → `thin_evidence_cap: true` with WARNING; synthesis reads ledger weights and cap; counter-evidence register additionally tracks adversarial signal quality | 4 |
| C-10 | PARTIAL | Confirm tokens ("Artifact written: X — advance to STAGE N") are structural; final confirm adds "ready for topic-story" but no per-stage prose narrative of findings | 2 |
| C-11 | PASS | GATE S: 4-checkbox compound clearance including scout_path, key_finding, status_quo_comparator, evidence_ledger. "Do not open Stage 1 without all four confirmed." | 4 |
| C-12 | **PASS** | `status_quo_comparator` and `evidence_ledger` registered in CAMPAIGN OPEN before any stage. S2/S3/S4 Part B each reference `status_quo_comparator`. Synthesis Status-Quo Comparison: "Claim evidence vs. [status_quo_comparator from campaign open]" | **4** |
| C-13 | PASS | Per-artifact full path in every write instruction | 4 |
| C-14 | PASS | Synthesis Counter-Evidence Register MANDATORY; null fallback: "Null result recorded — not suppressed. This cannot be treated as confirmation. Confidence is capped at HIGH-with-caveat pending adversarial review." | 4 |
| C-15 | PASS | Stage 1 frontmatter: `gate_s_cleared: true` AND `scout_path: [path from GATE S]` — gate clearance + scout path both traceable from artifact | 4 |

**V-05 Total: 106 / 108**

---

### Ranking

| Rank | Variation | Score | Delta from Max |
|------|-----------|-------|----------------|
| **1 (tie)** | **V-04** | **106** | -2 (C-10 partial) |
| **1 (tie)** | **V-05** | **106** | -2 (C-10 partial) |
| 3 (tie) | V-01 | 104 | -4 (C-10, C-12 partial) |
| 3 (tie) | V-02 | 104 | -4 (C-10, C-12 partial) |
| 3 (tie) | V-03 | 104 | -4 (C-10, C-12 partial) |

**Binding gap:** V-01/V-02/V-03 all score 104 because C-12 is PARTIAL (2 pts) — the status-quo comparator is introduced at Stage 1, not at session open, and is not carried forward by reference at every evidence stage. V-04/V-05 resolve this by registering the comparator in a mandatory CAMPAIGN PREAMBLE / CAMPAIGN OPEN block before Stage 0, then explicitly carrying it forward at every evidence stage via Part B searches. The C-12 fix adds 2 points and pushes the score from 104 → 106.

**Why C-10 remains PARTIAL in all variations:** Every variation uses structural confirm tokens ("Artifact written: X — advance to STAGE N") rather than natural-language narration of what was found. A full C-10 PASS would require: after gathering evidence and writing the artifact, producing a 1–2 sentence prose summary of the key finding before the advance token fires.

---

### Excellence Signals from Top Variations (V-04, V-05)

**Signal 1 — Compound GATE S with campaign anchor registration**
V-04/V-05 expand GATE S from a scout-confirmation gate (C-11) into a 4-item compound clearance that also requires `status_quo_comparator` and (in V-04) `counter_evidence_target` to be registered. This means it's impossible to clear the gate without the campaign's anchor frame in place. C-11 only checks "does a blocking gate exist"; this pattern checks "does the gate enforce anchor setup." The GATE S becomes the campaign's initialization contract, not just a scout check.

**Signal 2 — `ready: boolean` in synthesis handoff**
V-05 introduces `ready: [true / false — if false, specify blocker]` in the synthesis Handoff block. This is distinct from the confidence level — it's a binary promotion gate. A HIGH confidence synthesis can still set `ready: false` with a blocker (e.g., "adversarial review required before topic-story"). This makes the topic-story entry decision machine-readable and auditable from the artifact, not just advisory. No current rubric criterion captures this.

---

```json
{"top_score": 106, "all_essential_pass": true, "new_patterns": ["Compound GATE S requiring status_quo_comparator (and counter_evidence_target) as mandatory gate checkboxes alongside scout confirmation — makes campaign anchor setup a hard prerequisite for hypothesis formation, extending C-11 from scout-gate to full campaign-initialization gate", "Synthesis handoff ready: boolean field — machine-readable binary promotion gate distinct from confidence level, allowing HIGH-confidence syntheses to block topic-story entry when adversarial review is required"]}
```
