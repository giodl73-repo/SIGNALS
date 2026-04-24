## Quest Score — signal-setup — Round 3

---

### Variation Scoring

> **Note**: V-02 text is truncated mid-Step 4 preview. V-03 through V-05 text was not included in the variate file — scores for those three are estimated from axis descriptions. V-01 is the only fully-scoreable variation this round.

---

### V-01: Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | **PASS** | Gate 1 reads/checks both files. Gate 7 is the first write operation. |
| C-02 | Preview shown before writing | **PASS** | Gate 4 shows fenced preview. Gate 7 writes. |
| C-03 | Confirmation required | **PASS** | Gate 5 explicitly asks "yes / no" and waits before advancing. |
| C-04 | Signal section with skill advertising | **PASS** | Gate 4 specifies full skill list grouped by all 12 namespaces. |
| C-05 | Idempotent re-run | **PASS** | Gate 2 detects existing Signal section and emits "Already configured. No changes needed." then STOPs. |
| C-06 | Inertia rule included | **PASS** | Gate 4 includes verbatim inertia rule: "A topic is ready when /topic-status shows green coverage…" |
| C-07 | Copilot instructions offered | **PASS** | Gate 6 explicitly asks "Would you also like to add a Signal reference to .github/copilot-instructions.md?" |
| C-08 | User feedback on outcome | **PASS** | Gate 8 outputs a structured `SIGNAL SETUP COMPLETE` block with three labeled status lines. |
| C-09 | Preview matches written output | **PASS** | Gate 7 states "byte-for-byte identical to the preview shown in Gate 4." |
| C-10 | Handles missing CLAUDE.md gracefully | **PASS** | Gate 3 presents three options (create CLAUDE.md / standalone signal.md / cancel) and waits. |
| C-11 | Named gate checkpoints as explicit phase boundaries | **PASS** | 8 gates, each numbered and labeled. Explicit STOP at Gate 2, 3, and 5 exits. |
| C-12 | Edge-case paths promoted to first-class gates | **PASS** | Gate 2 (already configured) and Gate 3 (missing file) are dedicated top-level gates, not inline conditionals inside the happy path. |
| C-13 | Skill opens with motivational preamble | **FAIL** | Opens procedurally: "Configure Signal in this workspace after installation. Proceed through the gates below in order." No inertia framing before instructions. |
| C-14 | Decline path names its consequence | **PASS** | Gate 5 decline: "No changes made. Signal not configured. Inertia remains unaddressed." Gate 3 cancel: "Setup cancelled. Signal not configured." |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 5/6 → 8.3

**V-01 Score: 98.3** | All essential: YES | Golden: YES

---

### V-02: Inertia Framing *(text truncated)*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | **PASS** | Step 1 checks for both files and reports EXISTS/MISSING. |
| C-02 | Preview shown before writing | **PASS** | Step 4 shows preview (content cut off but structure confirmed). |
| C-03 | Confirmation required | **PARTIAL** | Text cuts off in Step 4. No confirmation step visible; assumed in unshown steps. |
| C-04 | Signal section with skill advertising | **PASS** | Step 4 references "full skill list grouped by namespace" (list body truncated). |
| C-05 | Idempotent re-run | **PASS** | Step 2 handles already-configured with STOP and message. |
| C-06 | Inertia rule included | **PASS** | Preamble names inertia. Step 4 content includes explicit inertia rule sentence. |
| C-07 | Copilot instructions offered | **PARTIAL** | Not in visible text; assumed in truncated tail. |
| C-08 | User feedback on outcome | **PARTIAL** | Not in visible text; assumed in truncated tail. |
| C-09 | Preview matches written output | **PARTIAL** | No "byte-for-byte" guarantee stated in visible text. |
| C-10 | Handles missing CLAUDE.md gracefully | **PASS** | Step 3 handles missing case with three options. |
| C-11 | Named gate checkpoints | **PARTIAL** | Uses numbered Steps, not named Gates; lacks explicit non-skip enforcement language ("STOP"). |
| C-12 | Edge-case paths as first-class gates | **PARTIAL** | Step 2 and Step 3 handle edge cases but as inline steps, not promoted to dedicated gate-level treatment. |
| C-13 | Skill opens with motivational preamble | **PASS** | Opens with 3 paragraphs: inertia as "silent competitor," Signal's purpose, and why setup matters — before any procedural steps. |
| C-14 | Decline path names its consequence | **PARTIAL** | Step 2: "Inertia already has a named opponent here" (consequence framing on skip-path). Step 3 cancel: "Setup cancelled." — short, consequence not named. |

**Essential**: 4.5/5 (C-03 partial) → 54  
**Recommended**: 2/3 (C-07, C-08 partial) → 20  
**Aspirational**: 4/6 (C-09, C-11, C-12, C-14 partial = 0.5 each) → 6.7

**V-02 Score: 80.7** | All essential: NO (C-03 partial) | Golden: NO *(text truncation may inflate fails)*

---

### V-03: Phrasing Register *(estimated — text not available)*

**Axis**: Register change only. Assumes core detection/preview/confirm/write flow is preserved. No structural gate architecture. No motivational preamble.

| Criterion | Result | Rationale |
|-----------|--------|-----------|
| C-01 through C-05 | **PASS** | Register variation doesn't alter detection/confirm/write logic. |
| C-06 | **PASS** | Inertia rule included regardless of register. |
| C-07 | **PASS** | Copilot prompt likely present. |
| C-08 | **PASS** | Outcome feedback standard. |
| C-09 | **PASS** | Preview fidelity independent of register. |
| C-10 | **PASS** | Missing-file handling present. |
| C-11 | **PARTIAL** | No gate structure implied by axis. |
| C-12 | **PARTIAL** | Edge cases inline, not dedicated gates. |
| C-13 | **FAIL** | Register change doesn't imply motivational preamble. |
| C-14 | **PARTIAL** | Register may soften or harden decline phrasing; consequence naming unlikely unless explicitly targeted. |

**Estimated score: 60 + 30 + (3/6 × 10) = 95** | All essential: YES | Golden: YES

---

### V-04: Role Sequence + Output Format *(estimated — text not available)*

**Axis**: Combination of role framing + structured output tables/blocks. Expected strong C-08. Role sequencing may create implicit phase ordering without gate labels.

| Criterion | Result | Rationale |
|-----------|--------|-----------|
| C-01 through C-05 | **PASS** | Core flow intact. |
| C-06 | **PASS** | Inertia rule in output block. |
| C-07 | **PASS** | Copilot offered. |
| C-08 | **PASS** | Structured output format is the axis strength. |
| C-09 | **PASS** | Formatted preview likely has explicit write-fidelity. |
| C-10 | **PASS** | Missing-file path handled. |
| C-11 | **PARTIAL** | Role/output axes don't imply gate labeling. |
| C-12 | **PARTIAL** | Edge cases may appear as table rows, not first-class gates. |
| C-13 | **FAIL** | Output format axis doesn't motivate with preamble. |
| C-14 | **PARTIAL** | Structured output may include consequence but not guaranteed. |

**Estimated score: 60 + 30 + (3.5/6 × 10) = 95.8** | All essential: YES | Golden: YES

---

### V-05: Inertia Framing + Decline Consequence *(estimated — text not available)*

**Axis**: Combination that directly targets C-13 and C-14. Described in the rubric preamble: three-paragraph inertia preamble + decline path says "Signal not configured. Inertia remains unaddressed." Gate structure unclear but likely step-based like V-02.

| Criterion | Result | Rationale |
|-----------|--------|-----------|
| C-01 through C-05 | **PASS** | Core flow assumed intact. |
| C-06 | **PASS** | Inertia rule in appended content; preamble reinforces. |
| C-07 | **PASS** | Copilot present. |
| C-08 | **PASS** | Outcome reporting present. |
| C-09 | **PASS** | Preview fidelity likely explicit. |
| C-10 | **PASS** | Missing-file path present. |
| C-11 | **PARTIAL** | Combination axis targets preamble + decline, not gate architecture. |
| C-12 | **PARTIAL** | Edge cases step-level not gate-level. |
| C-13 | **PASS** | Axis defines this: three-paragraph inertia preamble. |
| C-14 | **PASS** | Axis defines this: "Signal not configured. Inertia remains unaddressed." |

**Estimated score: 60 + 30 + (5/6 × 10) = 98.3** | All essential: YES | Golden: YES

---

### Rankings

| Rank | Variation | Score | All Essential | Golden |
|------|-----------|-------|---------------|--------|
| 1 | V-01 Lifecycle Emphasis | **98.3** | YES | YES |
| 1 | V-05 Inertia + Decline (est.) | **98.3** | YES | YES |
| 3 | V-04 Role + Output (est.) | 95.8 | YES | YES |
| 4 | V-03 Phrasing Register (est.) | 95.0 | YES | YES |
| 5 | V-02 Inertia Framing (truncated) | 80.7 | NO* | NO* |

*V-02 fails C-03 only due to text truncation; likely passes if full text were available.

---

### Excellence Signals

**V-01 distinguisher**: Explicit `STOP` keyword at each non-advancing gate exit. This makes the spec itself model the runtime behavior — the structure of the document enforces sequencing, not prose like "do not proceed." C-11 captures gate structure but not the STOP-as-enforcement pattern specifically.

**V-05 distinguisher**: Consequence naming in the decline path is the axis, not a side effect. When decline consequence is designed-in from the start (vs. added as a criterion), it flows naturally through the entire skill — the preamble names inertia as the enemy, so the decline path can name exactly what the user accepted: inertia remains.

**Cross-variation**: V-01 and V-05 both reach 98.3 — they are complementary, not alternatives. V-01 has the gate architecture; V-05 has the motivational bookending. A V-06 combining both would be the 100-point variation.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["Explicit STOP keyword at each non-advancing gate exit makes the spec enforce sequencing structurally, not just describe it", "Consequence naming in the decline path is strongest when designed from the preamble forward — the same enemy named at open is named at the exit"]}
```
