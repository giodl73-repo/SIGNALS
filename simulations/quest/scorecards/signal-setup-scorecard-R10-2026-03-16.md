## Quest Scorecard — signal-setup Round 10 (v9 Rubric)

**Skill**: signal-setup | **Rubric**: v9 | **Denominator**: E=5 R=3 A=19 | **Date**: 2026-03-16
**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/19 × 10)`
**Scoring**: PASS=1 | PARTIAL=0.5 | FAIL=0

---

## V-01 — Axis A: Single Detection Parent (GATE 1A/1B)

**Gate structure**: GATE 1 (detect, parent) → GATE 1A (missing), GATE 1B (configured) → GATE 2 (preview) → GATE 3 (confirm) → GATE 4 (write) → GATE 5 (Copilot, parent) → GATE 5A (already configured) → GATE 6 (done)

**Key structural facts**:
- GATE 1 parent routing: plain prose — "Three cases follow. See GATE 1A (missing file), GATE 1B (already configured), or continue to GATE 2" — no bold
- GATE 5: GATE 5A is a named sub-gate (heading-delimited). After GATE 5A, confirmation is inline prose: "If no Signal section in copilot-instructions.md: ask the confirmation below." — not headed
- Heading outline: GATE 1, GATE 1A, GATE 1B, GATE 2, GATE 3, GATE 4, GATE 5, GATE 5A, GATE 6 (9 entries)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | PASS | GATE 1 reads and checks CLAUDE.md |
| C-02 | Preview before writing | PASS | GATE 2 |
| C-03 | Confirmation required | PASS | GATE 3 |
| C-04 | Signal section with skill advertising | PASS | GATE 4 appends full section |
| C-05 | Idempotent re-run | PASS | GATE 1B detects and stops |
| C-06 | Inertia rule included | PASS | In Signal section preview |
| C-07 | Copilot instructions offered | PASS | GATE 5 |
| C-08 | User feedback on outcome | PASS | GATE 6 status table |
| C-09 | Preview matches written output | PASS | GATE 4 appends "exactly as shown in GATE 2" |
| C-10 | Handles missing CLAUDE.md gracefully | PASS | GATE 1A: "Signal will create one" |
| C-11 | Named gate checkpoints | PASS | All phases named and sequenced |
| C-12 | Edge-case paths as first-class gates | PASS | GATE 1A and GATE 1B are heading-delimited sub-gates |
| C-13 | Motivational preamble | PASS | Adversary framing opens the spec |
| C-14 | Decline path names consequence | PASS | GATE 1A decline: "Signal not configured. At the planning stage..." |
| C-15 | Already-configured path affirms positive | PASS | GATE 1B: "Inertia already has a named opponent here." |
| C-16 | Inertia as adversary | PASS | "There is a force that wins every feature decision when no one intervenes: inertia." |
| C-17 | Preamble explains temporal persistence | PASS | "not a one-time action. It is a permanent presence." |
| C-18 | Decline anchored to future moment | PASS | "before the next feature topic is named and the team decides whether to build" |
| C-19 | Arguments threaded through all Signal-absent exits | PASS | GATE 1A and GATE 3 both carry planning-stage future-moment framing |
| C-20 | Already-configured names persistence mechanism | PASS | "the load itself keeps the question present, not you remembering to ask." |
| C-21 | Secondary optional gates: path-specific consequence | PASS | GATE 5 decline: "At the implementation stage — while Copilot is generating function bodies..." |
| C-22 | Consequence anchors phase-indexed | PASS | "planning stage / spec committed" vs. "implementation stage / function bodies and endpoint scaffolding" — non-overlapping vocabulary |
| C-23 | Explicit phase label at each decline | PASS | "At the planning stage" and "At the implementation stage" as explicit labels |
| C-24 | Secondary already-configured paths: tool-local | PASS | GATE 5A: "Copilot Chat loads workspace instructions at session start" |
| C-25 | Sub-gate identifiers encode parent lineage | PASS | GATE 1A (parent=1, pos=A), GATE 1B (parent=1, pos=B), GATE 5A (parent=5, pos=A) |
| C-26 | Optional confirmation as first-class sub-gate | **FAIL** | Copilot confirmation is inline prose after GATE 5A — no named sub-gate |
| C-27 | Gate boundaries by document-structure markers | **PARTIAL** | No bold used anywhere; but Copilot confirmation branch is invisible to heading navigation — heading outline misses a significant decision path |

**Scores**: E=5/5 | R=3/3 | A=17.5/19 (C-26 FAIL, C-27 PARTIAL)
**Composite**: 60 + 30 + (17.5/19 × 10) = 60 + 30 + **9.21** = **99.21**

---

## V-02 — Axis B: Copilot Dual Sub-Gates (GATE 6A + GATE 6B)

**Gate structure**: GATE 0 (detect) → GATE 1 (missing) → GATE 1A (decline) → GATE 2 (configured) → GATE 2A (skip) → GATE 3 (preview) → GATE 4 (confirm) → GATE 5 (write) → GATE 6 (Copilot, parent) → GATE 6A (already configured) → GATE 6B (confirm) → GATE 7 (done)

**Key structural facts**:
- GATE 0 routing uses bold: `**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).` / `**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).` / `**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).`
- GATE 6A and GATE 6B are both heading-delimited sub-gates under GATE 6
- Heading outline: 12 entries — all gates and sub-gates discoverable

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | **All PASS** | Identical base behaviors from R9 |
| C-09–C-24 | Aspirational carry-forward | **All PASS** | Phase labels, adversary framing, persistence mechanism, consequence anchors all present |
| C-25 | Sub-gate lineage | PASS | GATE 1A (parent=1), GATE 2A (parent=2), GATE 6A (parent=6), GATE 6B (parent=6) |
| C-26 | Optional confirmation as first-class sub-gate | PASS | GATE 6B = "Confirm Copilot Append" — dedicated heading, full ask/decline/write treatment |
| C-27 | Document-structure markers as gate delimiters | **PARTIAL** | GATE 0 uses `**bold**` routing (`**If CLAUDE.md does not exist:** proceed to GATE 1`) — matches the syntactic pattern the rubric flags; all routed-to gates ARE heading-delimited, but the bold introduces a prohibited typographic layer |

**Scores**: E=5/5 | R=3/3 | A=18.5/19 (C-27 PARTIAL)
**Composite**: 60 + 30 + (18.5/19 × 10) = 60 + 30 + **9.74** = **99.74**

---

## V-03 — Axis C: Heading-Only Gate Routing (No Bold Anywhere)

**Gate structure**: GATE 1 (detect file) → GATE 1A (missing) → GATE 2 (detect Signal presence) → GATE 2A (already configured) → GATE 3 (preview) → GATE 4 (confirm) → GATE 5 (write) → GATE 6 (Copilot, parent) → GATE 6A (confirm) → GATE 7 (done)

**Key structural facts**:
- GATE 1 routing: plain prose bullet list — "CLAUDE.md does not exist — see GATE 1A below." / "CLAUDE.md exists with Signal section — see GATE 2A below." / "CLAUDE.md exists without Signal section — continue to GATE 2"
- GATE 2 routing: plain prose — "Two outcomes: Signal section found — see GATE 2A below. No Signal section — continue to GATE 3"
- GATE 6: Copilot already-configured handled as plain prose inside GATE 6 body (not a sub-gate): "(no sub-gate needed — this is a skip path)" with complete affirm content. GATE 6A = Confirm (the C-26 mandatory case)
- GATE 6 routing: "Two outcomes follow: Signal section found in copilot-instructions.md — affirm and skip to GATE 7. No Signal section — proceed to GATE 6A (Confirm)." — plain prose
- Zero `**bold**` formatting anywhere
- Heading outline: GATE 1, GATE 1A, GATE 2, GATE 2A, GATE 3, GATE 4, GATE 5, GATE 6, GATE 6A, GATE 7 (10 entries)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | **All PASS** | Identical base behaviors |
| C-09–C-24 | Aspirational carry-forward | **All PASS** | All behaviors present |
| C-25 | Sub-gate lineage | PASS | GATE 1A (parent=1, A), GATE 2A (parent=2, A), GATE 6A (parent=6, A) |
| C-26 | Optional confirmation as first-class sub-gate | PASS | GATE 6A = "Confirm Copilot Append" — dedicated heading, full treatment. The already-configured Copilot case is a detection path (C-12 territory), not a confirmation point (C-26 territory) — inline prose is valid for it |
| C-27 | Document-structure markers | PASS | No bold anywhere. Heading outline complete. All routing is plain prose with no typographic markers. Reader navigating by headings sees all 10 gates. |

**Scores**: E=5/5 | R=3/3 | A=19/19
**Composite**: 60 + 30 + (19/19 × 10) = 60 + 30 + **10.00** = **100.0**

---

## V-04 — Axes A+B: Consolidated Detection + Copilot Dual Sub-Gates

**Gate structure**: GATE 1 (detect, parent) → GATE 1A (missing), GATE 1B (configured) → GATE 2 (preview) → GATE 3 (confirm) → GATE 4 (write) → GATE 5 (Copilot, parent) → GATE 5A (already configured), GATE 5B (confirm) → GATE 6 (done)

**Key structural facts**:
- GATE 1 parent routing uses bold: `**If CLAUDE.md does not exist:** see GATE 1A.` / `**If Signal section found:** see GATE 1B.` / `**If CLAUDE.md exists, no Signal section:** proceed to GATE 2 (Preview).`
- GATE 5 parent routing: "Two sub-gates follow. See GATE 5A if already configured; otherwise GATE 5B." — plain prose ✓
- Both GATE 5A and GATE 5B are heading-delimited sub-gates
- Heading outline: 10 entries — all gates discoverable

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | **All PASS** | Identical base behaviors |
| C-09–C-24 | Aspirational carry-forward | **All PASS** | All behaviors present |
| C-25 | Sub-gate lineage | PASS | GATE 1A/1B (parent=1), GATE 5A/5B (parent=5) — full lineage across both parent phases |
| C-26 | Optional confirmation as first-class sub-gate | PASS | GATE 5B = "Confirm Copilot Append" — dedicated heading, full treatment |
| C-27 | Document-structure markers | **PARTIAL** | GATE 1 parent body uses `**If CLAUDE.md does not exist:** see GATE 1A.` — routing-only bold, no content block, and all routed-to gates ARE heading-delimited. Heading outline remains complete. But the typographic pattern matches what the rubric flags: bold inline labels (`**If not found**:` style) inside a step body. |

**Scores**: E=5/5 | R=3/3 | A=18.5/19 (C-27 PARTIAL)
**Composite**: 60 + 30 + (18.5/19 × 10) = 60 + 30 + **9.74** = **99.74**

---

## V-05 — Axes A+B+C: Full Structural Precision

**Gate structure**: GATE 1 (detect, parent) → GATE 1A (missing), GATE 1B (configured) → GATE 2 (preview) → GATE 3 (confirm) → GATE 4 (write) → GATE 5 (Copilot, parent) → GATE 5A (already configured), GATE 5B (confirm) → GATE 6 (done)

**Key structural facts**:
- GATE 1 parent routing: plain prose — "Three outcomes follow. See GATE 1A if the file is missing. See GATE 1B if Signal is already configured. If CLAUDE.md exists and has no Signal section, continue to GATE 2." — no bold
- GATE 5 parent routing: "Two sub-gates follow. See GATE 5A if Signal is already present; proceed to GATE 5B otherwise." — no bold
- GATE 5A opens with plain prose condition label: "Signal is already present in .github/copilot-instructions.md." — no bold
- GATE 5B opens with plain prose condition label: "Signal is not yet present in .github/copilot-instructions.md." — no bold
- GATE 1B enhanced C-20: "not because you open it, but because Claude Code reads it before the first message of every session."
- Zero `**bold**` formatting anywhere in parent gate routing
- Heading outline: GATE 1, GATE 1A, GATE 1B, GATE 2, GATE 3, GATE 4, GATE 5, GATE 5A, GATE 5B, GATE 6 (10 entries) — complete

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | **All PASS** | Identical base behaviors |
| C-09–C-24 | Aspirational carry-forward | **All PASS** | All behaviors present; C-20 enhanced with sharper mechanism statement |
| C-25 | Sub-gate lineage | PASS | GATE 1A/1B (parent=1), GATE 5A/5B (parent=5) — all sub-gates encode parent + position |
| C-26 | Optional confirmation as first-class sub-gate | PASS | GATE 5B = "Confirm Copilot Append" — GATE 5A = "Copilot Already Configured" — both first-class; both in heading outline |
| C-27 | Document-structure markers | PASS | Zero bold anywhere. Heading outline complete — reader enumerates all 10 gates/sub-gates from outline alone. Plain prose condition labels at sub-gate openings achieve routing clarity without typographic markers. |

**Scores**: E=5/5 | R=3/3 | A=19/19
**Composite**: 60 + 30 + (19/19 × 10) = 60 + 30 + **10.00** = **100.0**

---

## Summary

| Var | Axes | C-25 | C-26 | C-27 | Asp | Composite | Rank |
|-----|------|------|------|------|-----|-----------|------|
| V-03 | C | PASS | PASS | PASS | 19/19 | **100.0** | 1 |
| V-05 | A+B+C | PASS | PASS | PASS | 19/19 | **100.0** | 1 |
| V-02 | B | PASS | PASS | PARTIAL | 18.5/19 | **99.74** | 3 |
| V-04 | A+B | PASS | PASS | PARTIAL | 18.5/19 | **99.74** | 3 |
| V-01 | A | PASS | FAIL | PARTIAL | 17.5/19 | **99.21** | 5 |

---

## Excellence Signals (V-03 and V-05)

**1. Plain prose routing is strictly superior to bold routing** — Both 100.0 scorers use only plain prose for parent gate routing ("See GATE 1A if the file is missing."). V-02 and V-04 score lower because their bold routing (`**If CLAUDE.md does not exist:**`) syntactically matches the prohibited pattern, even though it's routing-only with no content blocks.

**2. Two valid architectures reach the same ceiling** — V-03 (two-parent detection: GATE 1 for file existence, GATE 2 for Signal presence) and V-05 (single-parent detection: GATE 1 → GATE 1A/1B) both achieve 100.0. C-25 does not privilege architectural consolidation over separation; it only requires lineage encoding within chosen sub-gates.

**3. Minimum C-26 interpretation is sufficient** — V-03's design proves that only the confirmation checkpoint needs to be a named sub-gate (GATE 6A). The Copilot already-configured detection case can remain inline plain prose because it is a C-12/C-24 case (detection, not confirmation). Both C-12 and C-24 are satisfied by complete content in plain prose without a heading.

**4. Plain prose condition labels at sub-gate openings (V-05 addition)** — V-05 opens each sub-gate with a plain prose condition statement ("Signal is already present in .github/copilot-instructions.md." / "Signal is not yet present..."). This pattern replaces bold routing without sacrificing conditional clarity — a C-27-safe alternative to `**If X:**` labels.

**5. C-27's true target is content-bearing bold pseudo-gates, not routing-only bold** — The PARTIAL calls for V-02/V-04 reflect the typographic pattern, but their heading outlines remain complete. This confirms the practical gap: routing-only bold is a cosmetic violation, not a structural one. V-03/V-05's zero-bold approach is cleaner but the structural difference is smaller than the point gap suggests.

---

## Carry-Forward for R11

**Recommended baseline**: V-05 (maximum precision, fewest ambiguities). V-03 is a valid alternative if minimalism is preferred.

**Residual question resolved**: C-27 PARTIAL applies to bold routing-only labels in parent gate bodies. The criterion's typographic example (`**If not found**:`) encompasses routing-only uses.

**New rubric candidate**: C-28 could target **plain prose condition labels at sub-gate openings** — "When a sub-gate is entered only when a specific condition holds, the sub-gate opening sentence states that condition in plain prose before any action is taken." V-05 instantiates this; it is not yet formalized.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Routing-only bold in parent gate bodies scores PARTIAL on C-27 even when all routed-to gates are heading-delimited — the prohibited typographic pattern applies regardless of whether bold labels enclose content or just contain routing pointers; zero-bold plain prose is the only path to full C-27 compliance", "Two-parent detection (separate GATE 1 for file existence, GATE 2 for Signal presence) achieves the same 100.0 as single-parent consolidated detection (GATE 1 with GATE 1A/1B sub-gates) — C-25 requires lineage encoding within chosen sub-gates but does not require architectural consolidation"]}
```
