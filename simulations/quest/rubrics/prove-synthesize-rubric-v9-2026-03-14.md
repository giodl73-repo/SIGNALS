Reading the R8 scorecard carefully before extracting signals.

**Excellence signals identified:**

1. **V-02 C-11/C-32 pass mechanism** — `ADVERSARY: "name the exact vulnerability (e.g., 'all three top signals come from the same source type')"` — C-11 fires when a named anti-pattern gate exists; what V-02 adds is a *parenthetical instantiation* of the failure mode inline at the gate — a concrete worked case bound to the abstract name. The exemplar is not in commentary; it is inside the gate instruction itself, making the abstract failure mode recognizable on first encounter.

2. **V-02 C-13/C-33 pass mechanism** — `NOT: table format for this section. The 'Why not the rank below:' sub-item is required...` — C-13 fires when NOT: precedes a success condition; what V-02 adds is a NOT: clause that simultaneously names the *positive structural requirement* in the prohibited format's place. The prohibition and the structural slot it protects are bound in a single constraint — bypassing the format prohibition and bypassing the structural slot are identified as the same violation.

3. **V-02 C-05/C-34 pass mechanism** — `"supersedes every individual signal — it does not summarize them"` / `"This synthesis is self-contained and supersedes all underlying investigation signals."` — C-05 fires when the synthesist commits to a verdict; C-10 fires when a self-contained mandate exists; what V-02 adds is an explicit *supersession assertion* — the synthesis does not integrate or aggregate the signals, it displaces them as the authoritative record. This is a stronger claim than self-containment: C-10 says a reader without artifacts can understand the answer; C-34 says the synthesis actively replaces the signal inventory.

**Calibration preview:** V-01 earns 0 of 3 new criteria (no inline exemplar, no format-prohibition coupling, no supersession claim). V-02 earns all 3 (inline exemplar at adversarial gate, NOT:-plus-slot coupling at C-12 constraint, supersession assertion at opening mandate and SYNTHESIST role instruction).

---

```markdown
# prove-synthesize-rubric-v9-2026-03-14.md

## prove-synthesize — Rubric v9

**Version**: v9 (2026-03-14)
**Predecessor**: v8 (2026-03-14)
**Golden threshold**: all essential pass AND composite >= 90
**Max composite**: 155.0

---

## New in v9 — Three Aspirational Criteria from R8 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-32 | Inline exemplar at anti-pattern gate | C-11, C-30 | The anti-pattern gate for a cognitive role includes a parenthetical or inline instantiation — a concrete worked case — of the named failure mode, bound inside the gate instruction itself. The exemplar names a specific instance (e.g., a signal-count pattern, a concrete form of generic challenge, a specific hedging phrase) rather than restating the abstract description. The exemplar appears at the point of gate definition, not in separate commentary. NOT: failure mode described only in abstract terms at the gate, with no concrete case. NOT: exemplar provided only in commentary or output instructions separate from the gate instruction where the failure mode is defined. |
| C-33 | Format-prohibition names the positive structural requirement | C-12, C-13 | A NOT: clause that prohibits a specific formatting method (e.g., table) simultaneously names the structural element that must appear in the permitted format. The prohibition and the structural requirement are stated in a single constraint, so that bypassing the format prohibition and bypassing the structural requirement are visible as the same violation. NOT: format prohibition without statement of what structure is required in the permitted format. NOT: structural requirement stated in a separate instruction, leaving the prohibition and the slot requirement unconnected. |
| C-34 | Supersession assertion in synthesis mandate | C-05, C-10 | The synthesis mandate includes an explicit supersession claim — the synthesis is stated to supersede, override, or replace the underlying signals, not merely to summarize, integrate, or aggregate them. The claim asserts that the synthesis is the authoritative statement; the signal inventory is subordinate to it. NOT: synthesis mandate that describes the output as a summary, integration, or aggregation of signals without a supersession claim. NOT: self-contained mandate (C-10) present without supersession claim — C-10 asserts reader comprehension without artifacts; C-34 asserts the synthesis displaces the artifacts as the record. |

---

## Scoring Delta

| | v8 | v9 |
|-|----|-----|
| Aspirational | 57.5 pts / 23 criteria | **65.0 pts / 26 criteria** |
| Max composite | 147.5 | **155.0** |
| Golden threshold | >= 90 | >= 90 (unchanged) |

---

## R8 Calibration Under v9

| Variation | v8 score | C-32 | C-33 | C-34 | v9 score |
|-----------|----------|------|------|------|----------|
| V-01 Role-Sequence | 112.5 | FAIL | FAIL | FAIL | **112.5** |
| V-02 Per-Rank Prose Slot | 117.5 | **PASS** | **PASS** | **PASS** | **125.0** |

**V-01 C-32 FAIL**: Anti-pattern gates name failure modes (ANALYST: "selective collection"; ADVERSARY: "generic challenge"; SYNTHESIST: "hedging") without inline instantiation — no parenthetical worked case at any gate.

**V-01 C-33 FAIL**: Format prohibitions not observed in V-01's structure; format-prohibition + structural-slot coupling absent.

**V-01 C-34 FAIL**: Self-contained mandate present ("This synthesis is self-contained... A reader with no access to the investigation artifacts must be able to understand the answer") satisfies C-10; no supersession claim. The mandate addresses reader comprehension without asserting the synthesis displaces the signal inventory.

**V-02 C-32 PASS**: ADVERSARY gate: `"name the exact vulnerability (e.g., 'all three top signals come from the same source type')"` — parenthetical instantiation of the failure mode bound inside the gate instruction. The exemplar names a specific signal-count pattern (C-31-class case), making "generic challenge" recognizable as a concrete instance.

**V-02 C-33 PASS**: `NOT: table format for this section. The 'Why not the rank below:' sub-item is required at each rank position.` — single constraint binds the format prohibition (no table) to the structural requirement (per-rank sub-item). The slot and the prohibition are stated together; absence of the sub-item and use of table format are identified as violations of the same constraint.

**V-02 C-34 PASS**: Opening mandate: `"This synthesis is self-contained and supersedes all underlying investigation signals."` SYNTHESIST role instruction: `"Issue a judgment. The synthesis supersedes every individual signal — it does not summarize them."` Supersession assertion present at two sites — mandate opening and role definition — establishing the synthesis as the authoritative record.

---

## Criterion Dependency Relationships

**C-11/C-32**: C-11 requires named anti-pattern gates that foreclose specific failure modes — gates present somewhere in the skill instruction. C-32 requires that the named gate include an inline concrete instantiation of the failure mode — a worked case inside the gate instruction itself. Named gates without exemplars satisfy C-11; only gates with inline exemplars satisfy C-32. C-11 is necessary but not sufficient for C-32.

**C-30/C-32**: C-30 requires each cognitive role name its own failure mode at role definition. C-32 requires the named failure mode include an inline exemplar at the definition site. C-30 is necessary but not sufficient for C-32 — a role may name its failure mode (satisfying C-30) without providing a concrete case (failing C-32).

**C-12/C-33**: C-12 requires prose format for evidence ranking — tables prohibited, argument construction present. C-33 requires a NOT: clause that prohibits the specific format and simultaneously names the structural element required in its place. Prose evidence that avoids tables satisfies C-12; only a NOT: clause that names both the prohibited format and the required structural slot satisfies C-33. C-12 is necessary but not sufficient for C-33.

**C-13/C-33**: C-13 requires NOT: precede the success condition. C-33 requires the NOT: clause additionally name the positive structural requirement in the prohibited format's place. C-13 is necessary but not sufficient for C-33.

**C-05/C-34**: C-05 requires the synthesist issue a verdict and take a position — no hedging, no summary. C-34 requires the mandate explicitly assert the synthesis supersedes the signal inventory — the synthesis is the authoritative record. A verdict commitment satisfies C-05; only an explicit supersession claim satisfies C-34. C-05 is necessary but not sufficient for C-34.

**C-10/C-34**: C-10 requires a self-contained mandate — the synthesis is comprehensible to a reader without access to investigation artifacts. C-34 requires an explicit supersession claim — the synthesis does not merely describe itself as self-contained but asserts it displaces the underlying signals as the record. C-10 asserts reader independence; C-34 asserts output authority. A self-contained mandate satisfies C-10 without satisfying C-34 unless supersession is stated. C-10 is necessary but not sufficient for C-34.

**C-09/C-29**: C-09 requires comparative language for each rank — "why this signal over the one below it?" present in the output. C-29 requires that comparative question be assigned to a structurally required slot per rank position — the comparison is demanded by structure, not by instruction alone. A prose section with comparative language satisfies C-09; only a design where each rank position has a named comparative slot satisfies C-29. C-09 is necessary but not sufficient for C-29.

**C-11/C-30**: C-11 requires named anti-pattern gates that foreclose specific failure modes — gates present somewhere in the skill instruction. C-30 requires each gate be assigned to the cognitive role that exhibits the failure mode — each role owns its anti-pattern at role definition. Anti-patterns listed centrally satisfy C-11; only role-owned anti-patterns at role definition satisfy C-30. C-11 is necessary but not sufficient for C-30.

**C-17/C-31**: C-17 requires the adversarial challenge be derived from this record's structural properties — a record-specific, not generic, failure mode. C-31 requires the challenge be derived from the aggregate pattern of multiple signals — a distribution property not visible from any single signal. A single-signal structural derivation satisfies C-17; only a pattern-of-N derivation that names the signal count satisfies C-31. C-17 is necessary but not sufficient for C-31.

**C-12/C-29 tension**: C-12 prohibits table formatting for evidence ranking. C-29 rewards a per-rank comparative slot, which can be implemented as a table column (as in R7 V-02) or as a labeled prose subsection per rank entry. Table-column implementation satisfies C-29 while failing C-12; labeled-prose implementation satisfies both. The tension is a feature — the highest-quality artifacts satisfy both via non-table per-rank slots. R8 V-02 resolves this tension: per-rank labeled prose sub-item (`Why not the rank below:`) satisfies C-12, C-29, and C-33 simultaneously.

**C-23/C-26**: C-23 requires named violation categories inline at each fill-window bound — the writer encounters the violation name when reading the constraint. C-26 requires all violation categories be indexed as a named registry block before FRONTMATTER begins — the violation taxonomy is visible before the first constraint is encountered. Inline naming satisfies C-23; front-indexing requires the additional registry block. C-23 is necessary but not sufficient for C-26.

**C-24/C-25/C-27**: C-24 requires arrow-chain field:value notation in RECORD DIAGNOSIS. C-25 requires a named PRE-FLIGHT structural phase between ADVERSARY and JUDGE. C-27 requires the arrow-chain propagate across all three named sites — RECORD DIAGNOSIS creates the chain, PRE-FLIGHT Phase B audits it, JUDGE confidence paragraph applies it. C-24 and C-25 are each necessary but not sufficient for C-27.

**C-25/C-28**: C-25 requires a named PRE-FLIGHT structural phase exist as a sequenced block between ADVERSARY and JUDGE. C-28 requires an explicit anti-skip gate at PRE-FLIGHT entry that names the bypass failure mode (PHASE-ADVANCE VIOLATION or equivalent) before any PRE-FLIGHT phase step is listed. PRE-FLIGHT that begins with its phase steps satisfies C-25; only PRE-FLIGHT that begins with a named entry gate satisfies C-28. C-25 is necessary but not sufficient for C-28.

**C-11/C-12 tension**: Confirmed across R2–R8. Both criteria remain; the tension is a feature.
```
