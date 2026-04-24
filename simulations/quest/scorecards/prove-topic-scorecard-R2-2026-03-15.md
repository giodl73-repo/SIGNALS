## prove-topic — Round 2 Scoring

---

## V-01 — Inertia Framing

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 All five sub-skills | PASS (10) | SESSION OPEN + Stages 1–5 all present, labeled by sub-skill |
| C-02 Hypothesis grounded in scout | PASS (10) | Scout load in SESSION OPEN; Stage 1 requires named slug before Claim field |
| C-03 Artifact written per stage | PASS (10) | Every stage ends "Confirm artifact written. Proceed to STAGE N." |
| C-04 Synthesis terminal and complete | PASS (10) | Stage 5 last; Inertia Verdict / Confidence / Key Evidence / Counter-Evidence / Caveats / Handoff all present |
| C-05 Topic prefix consistent | PASS (10) | Each "Write to:" names `{topic}-{stage}-{date}.md` in situ; Completion Check repeats all five |
| C-06 Stage order enforced | PASS (10) | "Five stages execute in order. Each stage writes its artifact before the next begins." |
| C-07 Scout handoff explicit | PASS (10) | Stage 1 requires `[slug] — [finding]` field; frontmatter lists `scout_anchor` |
| C-08 Synthesis signals topic-story | PASS (10) | Handoff: `ready_for_topic_story: true`, `Recommended next skill: /topic:story` |
| C-09 Thin-evidence propagates | PARTIAL (2) | Stage 4 flags "thin-evidence" if UNCLEAR; Stage 5 says "if any stage returned thin." Stages 2–3 have no explicit flag field — propagation implicit |
| C-10 Progress narrated per stage | PARTIAL (2) | "Confirm artifact written. Proceed to STAGE N." is a structural command, not a verbal narrative signal |
| C-11 Hypothesis hard-gated on scout | FAIL (0) | No GATE block or blocking checkpoint before Stage 1; inertia registration is ordered before scout but no gate enforces it |
| C-12 Comparator anchored at session open | PASS (4) | SESSION OPEN registers `current_practice` before any evidence; each stage carries "Inertia anchor (carry forward)" field; synthesis names it in first sentence |
| C-13 Per-artifact path enforcement | PASS (4) | Every "Write to:" instruction includes full `{topic}-{stage}-{date}.md` path; Completion Check repeats all five |

**V-01 Score: 92 / 100** — all essential PASS

---

## V-02 — Phrasing Register (conversational)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 All five sub-skills | PASS (10) | "Before you start" (load) + Acts 1–5 map to all five sub-skills |
| C-02 Hypothesis grounded in scout | PASS (10) | "Before you start" loads scout; Act 1 requires "Name your scout anchor — the specific artifact" before claim |
| C-03 Artifact written per stage | PASS (10) | Each act provides write path and advance token ("Say 'X artifact written' before moving to Act N") |
| C-04 Synthesis terminal and complete | PASS (10) | Act 5 is last; all six required sections present including handoff with `ready_for_topic_story: true` |
| C-05 Topic prefix consistent | PASS (10) | Every act's write instruction names `{topic}-{stage}-{date}.md`; Quick check list repeats abbreviated forms |
| C-06 Stage order enforced | PASS (10) | "each act produces one artifact, and the next act can't begin until the current one is written" |
| C-07 Scout handoff explicit | PASS (10) | Act 1: "Name your scout anchor — the specific artifact and finding"; frontmatter `scout_anchor (slug or 'none')` |
| C-08 Synthesis signals topic-story | PASS (10) | Handoff block: `ready_for_topic_story: true`, `Recommended next skill: /topic:story` |
| C-09 Thin-evidence propagates | PARTIAL (2) | Act 4 introduces thin-evidence flag for UNCLEAR verdict; Act 5 "if any stage came back thin." Acts 2–3 have no explicit flag |
| C-10 Progress narrated per stage | PASS (4) | "Say 'hypothesis artifact written' before moving to Act 2" — instructs model to emit verbal confirmation at each stage boundary; natural-language signal |
| C-11 Hypothesis hard-gated on scout | FAIL (0) | "Now that you know what the scout found" is narrative continuity, not a structural gate; no checkpoint blocking hypothesis work |
| C-12 Comparator anchored at session open | PASS (4) | "That's your inertia anchor — you'll come back to it at every stage" established before Act 1; each act references it; synthesis "name the status quo" in first sentence |
| C-13 Per-artifact path enforcement | PASS (4) | Every act names full path in write instruction; Quick check repeats all five |

**V-02 Score: 94 / 100** — all essential PASS

---

## V-03 — Per-Artifact Path Enforcement

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 All five sub-skills | PASS (10) | Stage 0 (scout) + Stages 1–5 covering all five sub-skills |
| C-02 Hypothesis grounded in scout | PASS (10) | Stage 0 loads scout; Stage 1 requires "Scout anchor (from STAGE 0 — name the slug)" before Claim |
| C-03 Artifact written per stage | PASS (10) | Every stage has "WRITE ARTIFACT: Path: …" block with "Confirm: '{topic}-{stage}-{date}.md written.' Proceed to STAGE N only after confirming." |
| C-04 Synthesis terminal and complete | PASS (10) | Stage 5 labeled SYNTHESIS; all required prose sections present; `ready_for_topic_story=true` in frontmatter |
| C-05 Topic prefix consistent | PASS (10) | Every "WRITE ARTIFACT: Path:" specifies `{topic}-{stage}-{date}.md`; ARTIFACT REGISTRY table repeats all five full paths |
| C-06 Stage order enforced | PASS (10) | "Prove evidence campaign. Five stages. One artifact per stage. Forward only." Each stage: "Proceed to STAGE N only after confirming." |
| C-07 Scout handoff explicit | PASS (10) | Stage 1 "Scout anchor (from STAGE 0 — name the slug)"; frontmatter `scout_anchor=[slug or "none"]` |
| C-08 Synthesis signals topic-story | PASS (10) | Stage 5 Handoff: `ready_for_topic_story: true`, `Recommended next skill: /topic:story` |
| C-09 Thin-evidence propagates | PASS (4) | Explicit `thin_evidence_flag` in Stage 2 verdict and frontmatter; Stage 3 Summary; Stage 4 flag; Stage 5 assembles "Thin-evidence flags from all stages: Stage 2 / Stage 3 / Stage 4" with per-stage effect on Confidence |
| C-10 Progress narrated per stage | PARTIAL (2) | "Confirm: '{topic}-{stage}-{date}.md written.'" is a structured token, not a verbal narrative; ARTIFACT REGISTRY provides end-of-session verification but not per-stage narrative |
| C-11 Hypothesis hard-gated on scout | FAIL (0) | Stage 0 has scout load and status-quo anchor but no GATE block or "do not proceed until" checkpoint before Stage 1 |
| C-12 Comparator anchored at session open | PASS (4) | Stage 0 establishes `current_practice` anchor; "This anchor carries forward to every stage"; Stages 1–5 each open with "Status-quo anchor (copy from STAGE 0)" |
| C-13 Per-artifact path enforcement | PASS (4) | Primary axis of this variation; every WRITE ARTIFACT block names full `Path: simulations/prove/{stage}/{topic}-{stage}-{date}.md`; ARTIFACT REGISTRY repeats all five |

**V-03 Score: 94 / 100** — all essential PASS

---

## V-04 — GATE S + Inertia Framing (C-11 + C-12)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 All five sub-skills | PASS (10) | SESSION OPEN + Stages 1–5 all present, labeled by sub-skill |
| C-02 Hypothesis grounded in scout | PASS (10) | REGISTRATION 1 loads scout; Stage 1 requires named slug before Claim |
| C-03 Artifact written per stage | PASS (10) | Every stage: "Write to: simulations/prove/{stage}/{topic}-{stage}-{date}.md / Confirm artifact written. Proceed to STAGE N." |
| C-04 Synthesis terminal and complete | PASS (10) | Stage 5 is terminal; all required sections plus mandatory Counter-Evidence; Handoff with `ready_for_topic_story: true` |
| C-05 Topic prefix consistent | PASS (10) | All "Write to:" instructions name `{topic}-{stage}-{date}.md`; Completion Checklist lists all five paths |
| C-06 Stage order enforced | PASS (10) | "Five stages in order. One artifact per stage." GATE S must clear before Stage 1; each stage advances only after confirmation |
| C-07 Scout handoff explicit | PASS (10) | Stage 1: "Scout anchor (from REGISTRATION 1 — name the slug)"; frontmatter `scout_anchor` |
| C-08 Synthesis signals topic-story | PASS (10) | Stage 5 Handoff: `ready_for_topic_story: true`, "Recommended next skill: /topic:story" |
| C-09 Thin-evidence propagates | PASS (4) | Stage 2: explicit `thin_evidence_flag` with threshold rule; Stage 3: `Thin-evidence check`; Stage 4: collects all prior flags into propagation table; Stage 5: reads from "Thin-evidence flags (from STAGE 4 aggregate)" with per-flag confidence effect |
| C-10 Progress narrated per stage | PARTIAL (2) | "Confirm artifact written. Proceed to STAGE N." is a structural command, not verbal narrative |
| C-11 Hypothesis hard-gated on scout | PASS (4) | Explicit GATE S block with `[ ] Scout record on file` and `[ ] Inertia anchor registered`; "Do not begin Stage 1 until both checkboxes can be checked"; Stage 1 opens "GATE S must be complete before this stage opens." |
| C-12 Comparator anchored at session open | PASS (4) | REGISTRATION 2 at SESSION OPEN names `current_practice`; "must be referenced at each subsequent stage"; each evidence stage opens with "Inertia anchor (copy from SESSION OPEN REGISTRATION 2)"; Stage 5 synthesis first sentence required to name it |
| C-13 Per-artifact path enforcement | PASS (4) | Each "Write to:" names full `simulations/prove/{stage}/{topic}-{stage}-{date}.md`; `gate_s_cleared: true` propagated into hypothesis frontmatter |

**V-04 Score: 98 / 100** — all essential PASS

---

## V-05 — GATE S + Inertia Framing + Per-Artifact Paths (C-11 + C-12 + C-13)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 All five sub-skills | PASS (10) | SESSION OPEN + Stages 1–5, all sub-skills |
| C-02 Hypothesis grounded in scout | PASS (10) | REGISTRATION 1 loads scout; GATE S must clear; Stage 1 requires named slug before Claim |
| C-03 Artifact written per stage | PASS (10) | Every stage: `WRITE: File: …` block with `Confirm: "Written: simulations/prove/{stage}/{topic}-{stage}-{date}.md"` and "Do not open Stage N until write is confirmed." |
| C-04 Synthesis terminal and complete | PASS (10) | "Terminal stage. No further stages follow." All six sections present; Counter-Evidence explicitly mandatory; frontmatter `ready_for_topic_story=true` |
| C-05 Topic prefix consistent | PASS (10) | Every WRITE `File:` uses `{topic}-{stage}-{date}.md`; CAMPAIGN CLOSE ARTIFACT REGISTRY repeats all seven entries (includes both registrations) |
| C-06 Stage order enforced | PASS (10) | "five stages, forward only" declared upfront; GATE S blocks Stage 1; each stage: "Do not open Stage N until write is confirmed." |
| C-07 Scout handoff explicit | PASS (10) | Stage 1: "Scout anchor (from REGISTRATION 1): [Slug] — [one-sentence finding]"; frontmatter `scout_anchor=[slug or "none"]` |
| C-08 Synthesis signals topic-story | PASS (10) | Stage 5 Handoff: `ready_for_topic_story: true`, `Recommended next skill: /topic:story` |
| C-09 Thin-evidence propagates | PASS (4) | Explicit `thin_evidence_flag` in Stage 2 write frontmatter; Stage 3 write frontmatter; Stage 4 propagation table (Stage 2/3/4); Stage 5 reads aggregate, names per-flag effect, adds `thin_evidence_stages` to synthesis frontmatter and Handoff |
| C-10 Progress narrated per stage | PARTIAL (2) | `Confirm: "Written: simulations/prove/…"` is a path-embedded token; "Do not open Stage N until write is confirmed" is a structural gate — structural rather than verbal narrative |
| C-11 Hypothesis hard-gated on scout | PASS (4) | GATE S block with both registration checkboxes; "State both boxes checked. Do not write the hypothesis until you have done so."; Stage 1: "GATE S required before this stage." |
| C-12 Comparator anchored at session open | PASS (4) | REGISTRATION 2: `ANCHOR: [current_practice]` with "This anchor is fixed for the session. Copy it forward verbatim at each stage."; Stages 1–5 all open with "Inertia anchor (copy verbatim from REGISTRATION 2)"; synthesis names it by "exact registered text" |
| C-13 Per-artifact path enforcement | PASS (4) | `WRITE: File: simulations/prove/{stage}/{topic}-{stage}-{date}.md` + `Confirm: "Written: simulations/prove/{stage}/{topic}-{stage}-{date}.md"` — path appears twice per stage; CAMPAIGN CLOSE ARTIFACT REGISTRY repeats all seven; "Protections active: [ ] Every WRITE instruction named the exact {topic}-{stage}-{date}.md path" as explicit check |

**V-05 Score: 98 / 100** — all essential PASS

---

## Round 2 Composite

| Variation | Score | All Essential | C-09 | C-10 | C-11 | C-12 | C-13 |
|-----------|-------|---------------|------|------|------|------|------|
| V-01 Inertia Framing | 92 | YES | PARTIAL | PARTIAL | FAIL | PASS | PASS |
| V-02 Phrasing Register | 94 | YES | PARTIAL | PASS | FAIL | PASS | PASS |
| V-03 Per-Artifact Paths | 94 | YES | PASS | PARTIAL | FAIL | PASS | PASS |
| V-04 GATE S + Inertia | **98** | YES | PASS | PARTIAL | PASS | PASS | PASS |
| V-05 GATE S + Inertia + Paths | **98** | YES | PASS | PARTIAL | PASS | PASS | PASS |

**Ranking**: V-04 = V-05 (98) > V-02 = V-03 (94) > V-01 (92)

The single-axis variations confirm the axis isolation: C-12 is now baseline (all five pass), C-13 and C-09 complement each other (V-03 wins C-09; V-01/V-02 win neither), and C-11 is the only differentiator requiring the combined variations.

---

## Excellence Signals from Top Scorers (V-04, V-05)

**Signal 1 — Dual-registration GATE S.** Combining both prerequisites (scout load + inertia anchor) into a single GATE block with two checkboxes is more robust than ordering them sequentially in prose. A single gate clears both dependencies before Stage 1, with Stage 1 explicitly declaring "GATE S required" — the blocking point is unambiguous and auditable.

**Signal 2 — Stage 4 as thin-evidence aggregation point.** Rather than having Stage 5 synthesize thin-evidence flags from memory, Stage 4 (prototype) explicitly collects flags from Stages 2, 3, and its own outcome into a propagation table. Stage 5 then reads from Stage 4's aggregate. This two-step chain reduces the synthesis burden and makes thin-evidence signals structurally impossible to drop in Stage 5.

**Signal 3 — `gate_s_cleared: true` in artifact frontmatter.** Propagating the gate status into the hypothesis artifact's frontmatter creates a machine-readable audit trail. The artifact itself carries evidence that the structural prerequisite was satisfied — not just the session that produced it.

**C-10 remains the ceiling blocker.** Both 98-scoring variations use structural confirmation tokens rather than verbal narrative. A variation targeting 100 would need to combine V-02's "Say 'X artifact written'" verbal token pattern with V-05's GATE S + inertia + per-path enforcement.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["Dual-registration GATE S clears both scout-load and inertia-anchor prerequisites in a single checkpoint block before Stage 1 opens, making both blocking conditions structurally auditable", "Stage 4 collects thin-evidence flags from Stages 2 and 3 into a propagation aggregate table, so Stage 5 reads from that aggregate rather than reconstructing from memory", "gate_s_cleared: true propagated into hypothesis artifact frontmatter creates a machine-readable audit trail confirming the gate was satisfied"]}
```
