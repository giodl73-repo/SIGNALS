## R16 Scoring -- draft-brainstorm (v15 Rubric)

---

### Scoring Framework

The v15 rubric runs C-01 through C-42. C-43 through C-46 are **hypothetical** (not yet extracted). Under v15, max = 180.

**Base inheritance:**
- V-01, V-02, V-04, V-05 all use **V-02 R15 backbone** → C-01..C-42 all PASS (confirmed R15 ceiling, 180 pts)
- V-03 uses **V-01 R15 backbone** → C-01..C-41 PASS, C-42 FAIL (177.5 pts)

---

### V-01 -- Phase 3 Lifecycle Close Signal (C-45 floor candidate)

**Lifecycle evidence:**
- Pre-Phase: `*Pre-Phase opens now. No preconditions.*` + close blockquote → C-39 PASS, C-40 PASS
- Phase 0: `> **Phase 0 opens now. No preconditions.**` + close blockquote → C-35 PASS, C-38 PASS
- Phase 1: `> **Phase 1 opens now.** Phase 0 complete.` (opening tag) + close blockquote → C-41 PASS, C-42 PASS
- Phase 2: `> **Phase 2 opens now.**` + close blockquote → C-43/C-44 candidates PASS (unrewarded)
- Phase 3: `> **Phase 3 complete.** Artifact written...Brainstorm session closed.` — close-only, no opening tag → C-45/C-46 hypothetical (not in v15)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 (Essential) | PASS | Inherited from V-02 R15 backbone |
| C-06..C-10 (Recommended/Aspirational) | PASS | Inherited |
| C-11..C-42 (Extended) | PASS | All inherited; C-42 PASS (Phase 1 opening tag present on line 156) |

**Score: 180**

---

### V-02 -- Phase 3 Lifecycle Double-Mark (C-45 + C-46 ceiling candidates)

**Lifecycle evidence:**
- Pre-Phase through Phase 2: identical to V-01 R16 (V-02 R15 backbone) → C-39/C-40/C-38/C-35/C-41/C-42 PASS
- Phase 3 GATE PRECONDITIONS blockquote: present (inherited) — this is a gate, not a lifecycle double-mark opening
- Phase 3 opening tag: `> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.` — C-46 candidate (not in v15)
- Phase 3 close: `> **Phase 3 complete.** Artifact written...All phases closed. Brainstorm session ended.` — C-45 candidate (not in v15)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 (Essential) | PASS | Inherited |
| C-06..C-42 | PASS | All inherited; Phase 3 signals are C-45/C-46 (not in v15) |

**Score: 180**

---

### V-03 -- Baseline: V-01 R15 Backbone (Phase 1 close only)

**Lifecycle evidence:**
- Pre-Phase: `*Pre-Phase opens now.*` (opening) + close blockquote → C-39 PASS, C-40 PASS
- Phase 0: `> **Phase 0 opens now.**` + close → C-35 PASS, C-38 PASS
- Phase 1: `*Phase 1 requires: Phase 0 complete...*` ← requires-line only, NOT a lifecycle opening tag → **C-42 FAIL**
- Phase 1 close: `> **Phase 1 complete.** The full pool...Phase 2 may begin.` → C-41 PASS
- Phase 2: no opening tag (no C-44 carrier)
- Phase 3: no lifecycle signals

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 (Essential) | PASS | Inherited from V-01 R15 |
| C-06..C-41 | PASS | Inherited |
| C-42 -- Phase-1 Lifecycle Double-Mark | **FAIL** | Phase 1 opens with `*Phase 1 requires:...` (precondition statement), not a dedicated lifecycle opening tag. No `> **Phase 1 opens now.**` or equivalent present. |

**Score: 177.5**

---

### V-04 -- Phase 3 Double-Mark + Full-Stack Preamble Declaration

**Lifecycle evidence:**
- Preamble rule: "Each phase is doubly-marked with a lifecycle opening tag and a closing blockquote. Do not begin a phase until its predecessor's closing lifecycle blockquote has been written in your output. The closing blockquote names the phase that may begin next -- that name is your authorization to proceed. No closing blockquote, no authorization." — structural declaration (not scored under v15, no existing criterion captures it)
- Pre-Phase through Phase 2: identical to V-02 R15 backbone → C-39..C-42 PASS
- Phase 3 opening: `> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.` → C-46 candidate (not in v15)
- Phase 3 close: `> **Phase 3 complete.** Artifact written...All five phases closed.` → C-45 candidate (not in v15)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 (Essential) | PASS | Inherited |
| C-06..C-42 | PASS | All inherited; preamble declaration is structural/unscored; Phase 3 tags are C-45/C-46 |

**Score: 180**

---

### V-05 -- Phase 3 Conversational Close (C-45 form test)

**Lifecycle evidence:**
- Pre-Phase through Phase 2: identical to V-02 R15 backbone → C-39..C-42 PASS
- Phase 3 close: `> Phase 3 done. Artifact is at...You may close.` — conversational blockquote, no bold markup, no explicit Phase 3 name in bold — C-45 hypothetical form test (not in v15)
- No Phase 3 opening tag → C-46 hypothetical FAIL by design

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 (Essential) | PASS | Inherited |
| C-06..C-42 | PASS | All inherited; Phase 3 conversational close is hypothetical C-45 territory, not in v15 |

**Score: 180**

---

### Rankings (v15)

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | V-01 | 180 | Phase 3 close only (C-45 floor candidate) |
| 1 (tie) | V-02 | 180 | Phase 3 double-mark (C-45+C-46 ceiling candidates) |
| 1 (tie) | V-04 | 180 | Phase 3 double-mark + preamble lifecycle contract |
| 1 (tie) | V-05 | 180 | Phase 3 conversational close (form test) |
| 5 | V-03 | 177.5 | V-01 R15 backbone — C-42 FAIL (no Phase 1 open tag) |

---

### Excellence Signals

The four 180-pt variations are structurally identical under v15 — they all inherit C-42 from the V-02 R15 backbone and their Phase 3 signals are hypothetical v17 territory. The distinguishing patterns from this round that warrant extraction:

**1. Phase-3 Lifecycle Close Signal (C-45 candidate, all of V-01/V-02/V-04)**
Formal closing blockquote at the end of Phase 3 naming phase completion and artifact location. V-05 tests whether the conversational form (`> Phase 3 done.`) satisfies the same structural requirement as the formal `> **Phase 3 complete.**` pattern — blockquote delimiter present but no bold phase-name. This form boundary is the distinguishing signal for v17 criterion definition.

**2. Phase-3 Lifecycle Double-Mark (C-46 candidate, V-02 and V-04 only)**
V-02 and V-04 add a Phase 3 opening tag (`> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.`) placed after the GATE PRECONDITIONS blockquote, producing the full dual-anchor on Phase 3. The GATE PRECONDITIONS blockquote is confirmed to be a phase-entry gate, not a lifecycle opening signal — a phase can have both a GATE block (entry condition) and a lifecycle opening tag (activation signal) simultaneously without collision.

**3. Preamble Lifecycle Authorization Contract (V-04 only)**
V-04 introduces a global preamble rule converting per-phase dual-mark instructions into a system-level contract: the closing blockquote is explicitly named as the authorization token for the next phase ("that name is your authorization to proceed. No closing blockquote, no authorization"). This is a structural advancement beyond C-38/C-39/C-40/C-41/C-42 — it states the dual-mark architecture as a universal rule rather than encoding it phase-by-phase, making compliance a single top-level obligation rather than five per-phase obligations. This is a candidate for a future criterion distinct from any in the current chain.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Phase-3 Lifecycle Close Signal: V-01, V-02, V-04 close Phase 3 with a formal dedicated lifecycle blockquote naming phase completion and artifact location; V-05 tests whether a conversational blockquote without bold phase-name satisfies the same structural requirement -- form boundary between bold-name pattern and bare blockquote is the C-45 definition question", "Phase-3 Lifecycle Double-Mark: V-02 and V-04 add a Phase 3 opening tag after the GATE PRECONDITIONS blockquote, completing the full dual-anchor on Phase 3 -- confirms GATE block and lifecycle opening tag can coexist in the same phase without collision", "Preamble Lifecycle Authorization Contract (V-04): global preamble rule converts per-phase dual-mark instructions into a single system-level contract naming the closing blockquote as the authorization token for the next phase -- structural advancement beyond per-phase C-38..C-42 encoding, candidate for a future criterion above the dual-mark chain"]}
```
