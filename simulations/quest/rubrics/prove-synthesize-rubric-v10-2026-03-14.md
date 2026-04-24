Reading the R9 scorecard carefully before extracting signals.

**Excellence signals identified:**

1. **V-02 C-35 signal — Concurrent role execution with seamless output** — `"Roles run concurrently in your reasoning; the output produced afterward is a single document, not three labeled sections."` — Prior variations named roles for sequencing; V-02 specifies concurrent reasoning that produces no visible role seams in output. The roles inform the synthesis without generating labeled sections or sequential role-produced blocks. This is structurally distinct from named roles (C-11) and role failure-mode naming (C-30) — it governs output shape, not role definition.

2. **V-02 C-36 signal — Dual-exemplar adversarial gate** — ADVERSARY gate provides both a negative case (`"'confidence could be higher with more data' applies to every synthesis"`) and a positive case (`"'the three key signals all measure stated preference, not observed behavior — the synthesis has no revealed-preference signal in key evidence'"`) inside the same constraint. C-32 requires one inline exemplar; V-02 provides two — negative instantiation of the failure mode and positive instantiation of the valid alternative — co-located inside the gate instruction.

3. **V-02 C-37 signal — Slot-indexed self-containment check** — `"Self-containment check maps five reader questions to the five-paragraph structure (verdict/confidence → key evidence → counter-evidence → principles → open questions). Slot-to-check correspondence is explicit."` — C-10 requires a self-contained mandate; V-01's check maps to output requirements without naming slots; V-02's check names the specific output slot each question verifies. A reader can determine which structural element satisfies which comprehension requirement.

4. **V-02 C-38 signal — Role-to-output closure attribution** — `"If the question was raised by the ADVERSARY challenge, acknowledge that"` — the open questions slot includes a role attribution instruction, creating a traceability link from output elements back to the generating role. Named roles (C-30) define failure modes; C-38 closes the loop — open questions in output carry their generating role as provenance.

**Calibration preview:** V-01 earns 0 of 4 new criteria (sequenced not concurrent; no gate-bound exemplars; implicit not slot-indexed check; no closure attribution). V-02 earns all 4.

---

```markdown
# prove-synthesize-rubric-v10-2026-03-14.md

## prove-synthesize — Rubric v10

**Version**: v10 (2026-03-14)
**Predecessor**: v9 (2026-03-14)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 165.0

---

## New in v10 — Four Aspirational Criteria from R9 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-35 | Concurrent role execution with seamless output | C-11, C-30 | The skill instruction specifies that cognitive roles execute concurrently in reasoning and that the output is a single document with no labeled role sections or visible role seams. The roles inform the synthesis without producing separate outputs or sequential role-labeled blocks in the result. NOT: instruction that names roles for a defined execution sequence (e.g., verdict-first, analyst-first) without specifying concurrent reasoning. NOT: output instruction that retains labeled role sections or role-produced blocks, even if the roles are named in the instruction. NOT: concurrent execution stated only for reasoning when the output instruction still partitions by role. |
| C-36 | Dual-exemplar adversarial gate | C-32 | The adversarial gate includes both a negative exemplar (a concrete instance of a generic or invalid challenge — what the failure mode looks like) and a positive exemplar (a concrete instance of a specific or valid challenge — what the non-failure alternative looks like), co-located inside the gate instruction. Both cases are instantiated at the gate; a reader can distinguish the invalid case from the valid case at the point of the constraint. NOT: gate with only a negative exemplar (what to avoid) without a positive case. NOT: gate with only a positive exemplar (what to aim for) without a negative case. NOT: both cases present but separated into different instructions rather than co-located inside the gate. |
| C-37 | Slot-indexed self-containment check | C-10 | The self-containment check maps each reader verification question to a named output slot — a paragraph, section, or explicitly labeled structural element. The correspondence is explicit: each question names the slot it verifies. A reader can determine which part of the output satisfies which comprehension requirement without inference. NOT: self-containment check that lists verification questions without mapping them to named output slots. NOT: self-containment check that maps to output requirements in general terms (e.g., "maps to output requirements") without identifying the specific structural element each question verifies. NOT: slot names present elsewhere in the instruction but not referenced inside the self-containment check. |
| C-38 | Role-to-output closure attribution | C-11, C-30 | The open questions or counter-evidence output slot includes an instruction to attribute the source role that raised the question or challenge. The output carries traceability from each open question or counter-evidence item back to the generating role (ADVERSARY, ANALYST, SYNTHESIST, or equivalent). NOT: open questions slot without source role attribution requirement. NOT: role attribution required for a different slot than where open questions or counter-evidence are placed. NOT: attribution instruction present in the role definition but absent from the output slot instruction where questions appear. |

---

## Scoring Delta

| | v8 | v9 | v10 |
|-|----|----|-----|
| Aspirational | 57.5 pts / 23 criteria | 65.0 pts / 26 criteria | **75.0 pts / 30 criteria** |
| Max composite | 147.5 | 155.0 | **165.0** |
| Golden threshold | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## New in v9 (Carried Forward) — Three Aspirational Criteria from R8 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-32 | Inline exemplar at anti-pattern gate | C-11, C-30 | The anti-pattern gate for a cognitive role includes a parenthetical or inline instantiation — a concrete worked case — of the named failure mode, bound inside the gate instruction itself. The exemplar names a specific instance (e.g., a signal-count pattern, a concrete form of generic challenge, a specific hedging phrase) rather than restating the abstract description. The exemplar appears at the point of gate definition, not in separate commentary. NOT: failure mode described only in abstract terms at the gate, with no concrete case. NOT: exemplar provided only in commentary or output instructions separate from the gate instruction where the failure mode is defined. |
| C-33 | Format-prohibition names the positive structural requirement | C-12, C-13 | A NOT: clause that prohibits a specific formatting method (e.g., table) simultaneously names the structural element that must appear in the permitted format. The prohibition and the structural requirement are stated in a single constraint, so that bypassing the format prohibition and bypassing the structural requirement are visible as the same violation. NOT: format prohibition without statement of what structure is required in the permitted format. NOT: structural requirement stated in a separate instruction, leaving the prohibition and the slot requirement unconnected. |
| C-34 | Supersession assertion in synthesis mandate | C-05, C-10 | The synthesis mandate includes an explicit supersession claim — the synthesis is stated to supersede, override, or replace the underlying signals, not merely to summarize, integrate, or aggregate them. The claim asserts that the synthesis is the authoritative statement; the signal inventory is subordinate to it. NOT: synthesis mandate that describes the output as a summary, integration, or aggregation of signals without a supersession claim. NOT: self-contained mandate (C-10) present without supersession claim — C-10 asserts reader comprehension without artifacts; C-34 asserts the synthesis displaces the artifacts as the record. |

---

## R9 Calibration Under v10

| Variation | v9 score | C-35 | C-36 | C-37 | C-38 | v10 score |
|-----------|----------|------|------|------|------|-----------|
| V-01 Role-Sequence | ~119.0 | FAIL | FAIL | FAIL | FAIL | **~119.0** |
| V-02 Per-Rank Prose Slot | ~127.5 | **PASS** | **PASS** | **PASS** | **PASS** | **~137.5** |
| V-03 Lifecycle Emphasis | ~0 | FAIL | FAIL | FAIL | FAIL | **~0** |

**V-01 C-35 FAIL**: V-01 uses an explicit verdict-first sequence (SYNTHESIST → ADVERSARY → ANALYST). The instruction defines execution order, not concurrent reasoning. Output structure preserves role sequence logic; no concurrent execution clause present.

**V-01 C-36 FAIL**: V-01's ADVERSARY exemplar appears before the labeled Gate: instruction, not inside it (basis for C-32 FAIL in R9). No gate-bound exemplar exists at all; dual instantiation cannot be assessed. The pre-gate exemplar, if considered, presents only the negative case (what "generic challenge" looks like) with no positive case (what a valid specific challenge looks like).

**V-01 C-37 FAIL**: V-01's self-containment check (four reader questions) maps to output requirements without naming specific output slots. The correspondence is implicit — questions address comprehension requirements without identifying the paragraph or structural element that satisfies each question. Slot-to-check correspondence is absent.

**V-01 C-38 FAIL**: Open questions slot does not include a role attribution instruction. Questions are listed without traceability back to the generating role. No instruction directs the synthesist to identify whether a question originated from the ADVERSARY or ANALYST role.

**V-02 C-35 PASS**: `"Roles run concurrently in your reasoning; the output produced afterward is a single document, not three labeled sections."` Concurrent execution explicitly specified; output instruction prohibits labeled role sections and role-produced seams. All three roles inform the synthesis without generating separate output blocks.

**V-02 C-36 PASS**: ADVERSARY gate provides two co-located exemplars inside the gate instruction. Negative case: `"'confidence could be higher with more data' applies to every synthesis"` — instantiates the generic invalid challenge. Positive case: `"'the three key signals all measure stated preference, not observed behavior — the synthesis has no revealed-preference signal in key evidence'"` — instantiates a specific valid challenge. Both negative and positive cases present inside the same constraint; a reader can distinguish the invalid form from the valid form at the gate.

**V-02 C-37 PASS**: Self-containment check maps five reader questions to the five-paragraph structure explicitly: verdict/confidence → key evidence → counter-evidence → principles → open questions. Each question names its target slot; slot-to-check correspondence is stated, not inferred.

**V-02 C-38 PASS**: `"If the question was raised by the ADVERSARY challenge, acknowledge that."` Open questions slot includes role attribution instruction. Output items in the open questions paragraph carry provenance back to the generating role; traceability link from output to role is closed.

---

## R8 Calibration Under v9 (Carried Forward)

| Variation | v8 score | C-32 | C-33 | C-34 | v9 score |
|-----------|----------|------|------|------|----------|
| V-01 Role-Sequence | 112.5 | FAIL | PASS | PASS | **117.5** |
| V-02 Per-Rank Prose Slot | 117.5 | **PASS** | **PASS** | **PASS** | **125.0** |

**V-01 C-32 FAIL**: Anti-pattern gates name failure modes (ANALYST: "selective collection"; ADVERSARY: "generic challenge"; SYNTHESIST: "hedging") without inline instantiation — no parenthetical worked case at any gate.

**V-01 C-33 PASS**: `"NOT: table format for this section. The 'Why this signal outranks the alternatives:' sub-item is required at each of the three positions."` — single constraint binds the format prohibition (no table) to the structural requirement (per-signal sub-item).

**V-01 C-34 PASS**: `"supersedes all underlying investigation signals"` + `"The synthesis supersedes every individual signal — it does not summarize them. Issue a judgment; the signal inventory is now subordinate to this document."` Two-site supersession assertion.

**V-02 C-32 PASS**: ADVERSARY gate: `"name the exact vulnerability (e.g., 'all three top signals come from the same source type')"` — parenthetical instantiation of the failure mode bound inside the gate instruction.

**V-02 C-33 PASS**: `"NOT: table format for this section. The 'Why not the rank below:' sub-item is required at each rank position."` — prohibition and structural slot stated in single constraint.

**V-02 C-34 PASS**: Opening mandate: `"This synthesis is self-contained and supersedes all underlying investigation signals."` SYNTHESIST role: `"Issue a judgment. The synthesis supersedes every individual signal — it does not summarize them."` Supersession assertion present at two sites.

---

## Criterion Dependency Relationships

### v10 New Criteria

**C-11/C-35**: C-11 requires named anti-pattern gates that foreclose specific failure modes. C-35 requires the named roles execute concurrently in reasoning and produce a single document with no labeled role sections. Named roles with gates satisfy C-11; only concurrent execution with seamless output satisfies C-35. A skill may name roles and define sequences (satisfying C-11) without specifying concurrent reasoning (failing C-35). C-11 is necessary but not sufficient for C-35.

**C-30/C-35**: C-30 requires each cognitive role name its own failure mode at role definition. C-35 requires those roles execute concurrently with no visible output seams. Role failure-mode naming satisfies C-30; concurrent execution with seamless output is an independent structural requirement. C-30 is necessary but not sufficient for C-35.

**C-32/C-36**: C-32 requires the anti-pattern gate include an inline exemplar of the named failure mode — one concrete worked case. C-36 requires the gate include both a negative exemplar (the failure mode instantiated) and a positive exemplar (the valid alternative instantiated), co-located inside the same gate instruction. A gate with one inline exemplar satisfies C-32; only a gate with both negative and positive exemplars co-located satisfies C-36. C-32 is necessary but not sufficient for C-36.

**C-10/C-37**: C-10 requires a self-contained mandate — the synthesis is comprehensible to a reader without access to investigation artifacts. C-37 requires the self-containment check map each verification question to a named output slot. A self-contained mandate with a verification check satisfies C-10; only a check that names the specific structural element each question verifies satisfies C-37. C-10 is necessary but not sufficient for C-37.

**C-11/C-38**: C-11 requires named cognitive roles with anti-pattern gates. C-38 requires the open questions output slot carry role attribution — each question traced back to its generating role. Named roles provide the referents for attribution; C-38 closes the loop from role definition to output provenance. C-11 is necessary but not sufficient for C-38 — roles may be named without an attribution instruction in the output slot.

**C-30/C-38**: C-30 requires each cognitive role name its own failure mode at role definition. C-38 requires open questions in output attribute their source role. Role failure-mode naming (C-30) establishes the roles as identifiable; role attribution in output (C-38) uses those identities as provenance labels. C-30 is necessary but not sufficient for C-38.

### v9 Criteria (Carried Forward)

**C-11/C-32**: C-11 requires named anti-pattern gates that foreclose specific failure modes — gates present somewhere in the skill instruction. C-32 requires that the named gate include an inline concrete instantiation of the failure mode — a worked case inside the gate instruction itself. Named gates without exemplars satisfy C-11; only gates with inline exemplars satisfy C-32. C-11 is necessary but not sufficient for C-32.

**C-30/C-32**: C-30 requires each cognitive role name its own failure mode at role definition. C-32 requires the named failure mode include an inline exemplar at the definition site. C-30 is necessary but not sufficient for C-32 — a role may name its failure mode (satisfying C-30) without providing a concrete case (failing C-32).

**C-12/C-33**: C-12 requires prose format for evidence ranking — tables prohibited, argument construction present. C-33 requires a NOT: clause that prohibits the specific format and simultaneously names the structural element required in its place. Prose evidence that avoids tables satisfies C-12; only a NOT: clause that names both the prohibited format and the required structural slot satisfies C-33. C-12 is necessary but not sufficient for C-33.

**C-13/C-33**: C-13 requires NOT: precede the success condition. C-33 requires the NOT: clause additionally name the positive structural requirement in the prohibited format's place. C-13 is necessary but not sufficient for C-33.

**C-05/C-34**: C-05 requires the synthesist issue a verdict and take a position — no hedging, no summary. C-34 requires the mandate explicitly assert the synthesis supersedes the signal inventory — the synthesis is the authoritative record. A verdict commitment satisfies C-05; only an explicit supersession claim satisfies C-34. C-05 is necessary but not sufficient for C-34.

**C-10/C-34**: C-10 requires a self-contained mandate — the synthesis is comprehensible to a reader without access to investigation artifacts. C-34 requires an explicit supersession claim — the synthesis does not merely describe itself as self-contained but asserts it displaces the underlying signals as the record. C-10 asserts reader independence; C-34 asserts output authority. A self-contained mandate satisfies C-10 without satisfying C-34 unless supersession is stated. C-10 is necessary but not sufficient for C-34.
```
