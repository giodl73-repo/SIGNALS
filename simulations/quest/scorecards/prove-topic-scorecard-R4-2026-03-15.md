## prove-topic — Round 4 Score Report

---

### Rubric Reference

| Band | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01 to C-05 | 10 | 50 |
| Recommended | C-06 to C-08 | 10 | 30 |
| Aspirational | C-09 to C-17 | 4 | 36 |
| **Total** | | | **116** |

PARTIAL scores: Essential=5, Recommended=4 (C-07/C-08), Aspirational=2.

---

### V-01 — Adversarial Escalation Protocol

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Five stages in fixed sequence | PASS (10) | STAGE 0–5, "advance to STAGE N" enforced |
| C-02 | Hypothesis grounded in scout signals | PASS (10) | `scout_anchor: [slug from GATE S]`, claim derived from scout record |
| C-03 | Artifact written per stage | PASS (10) | Write instruction at every stage |
| C-04 | Final synthesis terminal and complete | PASS (10) | "Terminal stage," Findings + Confidence + Handoff present |
| C-05 | Topic prefix consistent | PASS (10) | All paths `{topic}-*` |
| C-06 | Stage order enforced | PASS (10) | "Do not open Stage 1 without GATE S confirmed" |
| C-07 | Scout signal handoff explicit | PASS (10) | Named slug in hypothesis frontmatter |
| C-08 | Synthesis signals readiness for topic-story | PASS (10) | `next: topic-story`, `status: [Ready / Escalated]` |
| C-09 | Thin-evidence acknowledgment propagates | FAIL (0) | No per-stage quality labels; no thin-evidence flag |
| C-10 | Progress narrated per stage | PASS (4) | Natural-language confirm at every stage |
| C-11 | Hypothesis hard-gated on scout | PASS (4) | "Do not open Stage 1 without this gate confirmed" |
| C-12 | Status-quo anchor at open | PASS (4) | CAMPAIGN OPEN section; mandatory before Stage 0 |
| C-13 | Per-artifact path in each write | PASS (4) | Full `simulations/prove/{topic}/...` paths in every Write |
| C-14 | Counter-evidence mandatory | PASS (4) | MANDATORY Part B at S2, S3, S4; null fallback at each |
| C-15 | gate_s_cleared in artifact frontmatter | PASS (4) | `gate_s_cleared: true` in Stage 1 frontmatter |
| C-16 | Null CE triggers adversarial escalation | PASS (4) | Named reviewer at CAMPAIGN OPEN; ADVERSARIAL ESCALATION ACTIVATED block; promotion blocked |
| C-17 | Confidence mechanically capped | PARTIAL (2) | Verbal rule ("cannot be rated HIGH") — no numeric formula; cap is a prose instruction, not a computed value |

**V-01 Total: 110 / 116**

---

### V-02 — Mechanical Counter-Evidence Cap

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Five stages in fixed sequence | PASS (10) | STAGE 0–5, sequential advance |
| C-02 | Hypothesis grounded in scout signals | PASS (10) | `scout_anchor: [slug from GATE S]`; claim derived from scout |
| C-03 | Artifact written per stage | PASS (10) | Write at every stage |
| C-04 | Final synthesis terminal and complete | PASS (10) | Formula Computation + Findings + Counter-Evidence + Handoff |
| C-05 | Topic prefix consistent | PASS (10) | All paths `{topic}-*` |
| C-06 | Stage order enforced | PASS (10) | GATE S blocks Stage 1; sequential confirms |
| C-07 | Scout signal handoff explicit | PASS (10) | Named slug in Stage 1 frontmatter |
| C-08 | Synthesis signals readiness for topic-story | PASS (10) | `next: topic-story` in Handoff |
| C-09 | Thin-evidence acknowledgment propagates | PARTIAL (2) | Stage scores flow numerically through formula but no explicit "Thin" quality label or named flag in synthesis |
| C-10 | Progress narrated per stage | PASS (4) | "Score rationale: One sentence" + Confirm at each stage |
| C-11 | Hypothesis hard-gated on scout | PASS (4) | "Do not open Stage 1 without this gate confirmed" |
| C-12 | Status-quo anchor at open | PARTIAL (2) | Comparator first appears in Stage 1 frontmatter — no CAMPAIGN OPEN section registering it before Stage 0 |
| C-13 | Per-artifact path in each write | PASS (4) | Full paths in all Write instructions |
| C-14 | Counter-evidence mandatory | PASS (4) | Null fallback at S2, S3, S4 |
| C-15 | gate_s_cleared in artifact frontmatter | PASS (4) | `gate_s_cleared: true` in Stage 1 |
| C-16 | Null CE triggers adversarial escalation | FAIL (0) | No adversarial reviewer; no escalation state; null path records CE-score but does not block promotion |
| C-17 | Confidence mechanically capped | PASS (4) | Fixed formula; CE-score = -2 if all null; "Verbal override is not permitted" |

**V-02 Total: 108 / 116**

---

### V-03 — Stage-Exit Integrity Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Five stages in fixed sequence | PASS (10) | STAGE 0–5; sequential |
| C-02 | Hypothesis grounded in scout signals | PASS (10) | `scout_anchor: [slug from GATE S]`; claim from scout |
| C-03 | Artifact written per stage | PASS (10) | Write at every stage |
| C-04 | Final synthesis terminal and complete | PASS (10) | Campaign Integrity Summary + Findings + Confidence + Handoff |
| C-05 | Topic prefix consistent | PASS (10) | All paths `{topic}-*` |
| C-06 | Stage order enforced | PASS (10) | GATE S; sequential confirms |
| C-07 | Scout signal handoff explicit | PASS (10) | Named slug in Stage 1 frontmatter |
| C-08 | Synthesis signals readiness for topic-story | PASS (10) | `next: topic-story` in Handoff |
| C-09 | Thin-evidence acknowledgment propagates | FAIL (0) | No per-stage quality label; integrity score tracks process, not evidence quality |
| C-10 | Progress narrated per stage | PASS (4) | "Gate SN cleared. Artifact written..." natural-language confirm |
| C-11 | Hypothesis hard-gated on scout | PASS (4) | "Do not open Stage 1 without this gate confirmed" |
| C-12 | Status-quo anchor at open | PARTIAL (2) | Comparator first in Stage 1 frontmatter; no CAMPAIGN OPEN section |
| C-13 | Per-artifact path in each write | PASS (4) | Full paths in Write instructions |
| C-14 | Counter-evidence mandatory | PASS (4) | Exit Gate item 1 requires counter-evidence confirmation at S2, S3, S4 |
| C-15 | gate_s_cleared in artifact frontmatter | PASS (4) | `gate_s_cleared: true` in Stage 1 |
| C-16 | Null CE triggers adversarial escalation | PARTIAL (2) | "Recommend adversarial review before topic-story promotion" — recommendation, not enforced block; no named reviewer type; no promotion block |
| C-17 | Confidence mechanically capped | FAIL (0) | Confidence by judgment with integrity score factor; no CE-score formula |

**V-03 Total: 104 / 116**

---

### V-04 — Combined C-16 + C-17 Severity Stack

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Five stages in fixed sequence | PASS (10) | STAGE 0–5; fixed sequence |
| C-02 | Hypothesis grounded in scout signals | PASS (10) | GATE S (4-checkbox); `scout_anchor` in Stage 1 frontmatter |
| C-03 | Artifact written per stage | PASS (10) | Write at every stage |
| C-04 | Final synthesis terminal and complete | PASS (10) | Two-lock check + Formula + Findings + CE Register + Handoff |
| C-05 | Topic prefix consistent | PASS (10) | All paths `{topic}-*` |
| C-06 | Stage order enforced | PASS (10) | 4-item GATE S; "Do not open Stage 1 until all four are confirmed" |
| C-07 | Scout signal handoff explicit | PASS (10) | Named slug in Stage 1 frontmatter |
| C-08 | Synthesis signals readiness for topic-story | PASS (10) | `next: topic-story`; `status: [Ready / Escalated]`; `escalation_reviewer` field |
| C-09 | Thin-evidence acknowledgment propagates | FAIL (0) | Stage scores tracked but no "Thin" quality label; no thin-evidence propagation mechanism |
| C-10 | Progress narrated per stage | PASS (4) | Stage score + Confirm text at each stage |
| C-11 | Hypothesis hard-gated on scout | PASS (4) | 4-item GATE S; all required before Stage 1 opens |
| C-12 | Status-quo anchor at open | PASS (4) | CAMPAIGN OPEN section; mandatory; "All three registrations mandatory. Do not proceed without filling all three" |
| C-13 | Per-artifact path in each write | PASS (4) | Full paths in all Write instructions |
| C-14 | Counter-evidence mandatory | PASS (4) | MANDATORY Part B at S2, S3, S4; null fallbacks |
| C-15 | gate_s_cleared in artifact frontmatter | PASS (4) | `gate_s_cleared: true` in Stage 1 |
| C-16 | Null CE triggers adversarial escalation | PASS (4) | LOCK 2: ADVERSARIAL ESCALATION TRIGGERED; named reviewer type from CAMPAIGN OPEN; promotion blocked until review complete or deferred with justification; `escalation_state: triggered` |
| C-17 | Confidence mechanically capped | PASS (4) | LOCK 1: CE-score = -2 if all null; formula explicit in synthesis; "Level (from formula — no override)" |

**V-04 Total: 112 / 116**

---

### V-05 — Full Excellence Signal Compound

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Five stages in fixed sequence | PASS (10) | "All five stages in fixed sequence. No stage opens without preceding artifact confirmed." |
| C-02 | Hypothesis grounded in scout signals | PASS (10) | `scout_anchor` + `scout_path` in Stage 1 frontmatter; "Link explicitly to the scout finding. Do not derive from general knowledge." |
| C-03 | Artifact written per stage | PASS (10) | Write at every stage |
| C-04 | Final synthesis terminal and complete | PASS (10) | "Terminal stage. No stages follow." Null check + Evidence Ledger + Findings + CE Register + Composite Confidence + Handoff |
| C-05 | Topic prefix consistent | PASS (10) | All paths `{topic}-*` |
| C-06 | Stage order enforced | PASS (10) | "No stage opens without the preceding artifact confirmed"; 4-item GATE S |
| C-07 | Scout signal handoff explicit | PASS (10) | Both `scout_anchor` (slug) and `scout_path` (full path) in hypothesis frontmatter |
| C-08 | Synthesis signals readiness for topic-story | PASS (10) | `next: topic-story`; `status`; `ready: [true/false — if false, specify blocker]` |
| C-09 | Thin-evidence acknowledgment propagates | PASS (4) | Per-stage `Evidence quality: [Strong/Moderate/Thin]`; Stage 4 `prototype_cap: true` + "WARNING: Final composite capped at 6.9 (MEDIUM max)"; synthesis "Prototype cap applied: [yes/no]" and `Prototype cap: [yes/no]` in Composite Confidence |
| C-10 | Progress narrated per stage | PASS (4) | Stage score + quality update + Confirm text at each stage |
| C-11 | Hypothesis hard-gated on scout | PASS (4) | "Do not open Stage 1 until all four are confirmed" (4-item gate) |
| C-12 | Status-quo anchor at open | PASS (4) | CAMPAIGN OPEN: mandatory `status_quo_comparator`; "All registrations mandatory. Do not proceed without filling all fields." |
| C-13 | Per-artifact path in each write | PASS (4) | Full paths in Write instructions AND in Confirm text (e.g., `Confirm: "Artifact written: simulations/prove/{topic}/{topic}-hypothesis-{date}.md"`) |
| C-14 | Counter-evidence mandatory | PASS (4) | MANDATORY Part B at S2, S3, S4; explicit null fallbacks |
| C-15 | gate_s_cleared in artifact frontmatter | PASS (4) | `gate_s_cleared: true` + `evidence_weights_registered: true` in Stage 1 frontmatter |
| C-16 | Null CE triggers adversarial escalation | PASS (4) | All null → `escalation_state: triggered`; named adversarial reviewer from CAMPAIGN OPEN; ADVERSARIAL ESCALATION TRIGGERED block; "Block: Promotion to topic-story requires adversarial review completion or explicit written deferral" |
| C-17 | Confidence mechanically capped | PASS (4) | CE-score formula registered at CAMPAIGN OPEN; prototype_cap as second ceiling; "Level (from formula — no override)"; synthesis Composite Confidence shows all formula inputs |

**V-05 Total: 116 / 116**

---

### Summary

| Variation | Essential | Recommended | Aspirational | Total | All Essential Pass |
|-----------|-----------|-------------|--------------|-------|--------------------|
| V-05 | 50 | 30 | 36 | **116** | Yes |
| V-04 | 50 | 30 | 32 | **112** | Yes |
| V-01 | 50 | 30 | 30 | **110** | Yes |
| V-02 | 50 | 30 | 28 | **108** | Yes |
| V-03 | 50 | 30 | 24 | **104** | Yes |

All five variations pass all essential criteria. Golden threshold (80) cleared by all.

---

### Excellence Signals — V-05

**1. Prototype-cap as second formula gate (C-09 / C-17 compound)**
V-05 introduces a second mechanical cap orthogonal to CE-score: if prototype quality is Thin, the composite is capped at 6.9 regardless of how high stage scores are. This is more aggressive than CE-score because it fires on evidence quality, not counter-evidence state. A campaign with strong web search and intelligence but a weak prototype cannot escape MEDIUM via a formula that happens to average above 7.0. The cap is registered in CAMPAIGN OPEN, triggered in Stage 4, and shown in the synthesis Composite Confidence section.

**2. Full path in confirm text**
Every Confirm statement in V-05 includes the complete `simulations/prove/{topic}/...` path, not just the filename. This means the audit trail is recoverable from the confirm text alone, without re-reading the Write instruction.

**3. Dual scout reference (slug + path) in hypothesis frontmatter**
`scout_anchor` (slug) and `scout_path` (full path) are both required in Stage 1 frontmatter. The slug provides human-readable identity; the path provides machine-traversable location. Either alone is sufficient for C-15; both together make the scout chain auditable from the artifact.

---

```json
{"top_score": 116, "all_essential_pass": true, "new_patterns": ["prototype-cap as second formula gate: Thin prototype quality (highest-weight stage) caps final composite at MEDIUM independent of CE-score, creating compound mechanical ceiling on HIGH confidence", "full path in confirm text: Confirm statement includes complete artifact path (not just filename), making the audit trail recoverable from confirms alone without replaying Write instructions"]}
```
