## Round 12 Scoring — prove-topic Rubric v11

**Rubric ceiling:** 184 pts (5×10 essential + 3×10 recommended + 26×4 aspirational)
**Golden threshold:** all essential pass + composite ≥ 80

---

### Baseline

All R12 variations are built on the R11 V-01 v10 foundation (180/180 under v10 = all 33 prior criteria full PASS). The scoring delta across variations is driven by two variables:

- **C-34** (new in v11, 4 pts): named INCUMBENT CHECK block at each evidence stage, Stage 4 displacement verdict explicitly asked
- **C-10** (4 pts): natural-language confirmation per stage — at risk when presentation strips prose

All others assumed PASS unless the axis change introduces a degradation path.

---

### V-01 — Role Sequence (Three-Role Gate)

**Axis:** ROLE C (INCUMBENT THREAT ANALYST) added as blocking gate role; owns `incumbent_threat_locked`; INCUMBENT CHECK blocks at Stages 2–4 reference ROLE C as structural origin.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 through C-08 | 10/10 each | All stages present; ROLE A/B/C + GATE S; progressive writes; scout loaded via ROLE B; `topic-story` handoff |
| C-09 | 4/4 | Thin evidence acknowledged and carried to synthesis |
| C-10 | 4/4 | Stage prose unchanged from R11 V-01 baseline; natural-language confirmation per stage intact |
| C-11 | 4/4 | GATE S blocks Stage 1 until all three roles complete |
| C-12 | 4/4 | `status_quo_comparator` in CAMPAIGN OPEN; ROLE C deepens with `incumbent_name`, `incumbent_strength`, `incumbent_vulnerability`; referenced each evidence stage |
| C-13 through C-33 | 4/4 each | Full v10 stack inherited; ROLE C addition is purely additive |
| **C-34** | **4/4** | Named INCUMBENT CHECK blocks at Stages 2, 3, and 4 cite ROLE C fields by name as structural origin. Stage 4 explicitly asks: "does accumulated evidence make a credible case for displacing {incumbent}?" with required Yes/No/Pending answer. C-12 passes (incumbent anchored by ROLE C at campaign opening). |

**C-34 audit chain strength:** ROLE C's `incumbent_threat_locked` field in GATE S means losing the incumbent analysis creates an immediately auditable structural gap — stronger than R11 V-01 where the incumbent block lived in an open preamble with no gate enforcement.

**Composite:** 50 + 30 + 104 = **184/184** ✓ Golden

---

### V-02 — Scorecard Format

**Axis:** Per-stage rows in a running CAMPAIGN SCORECARD table replace prose notes. Columns: Incumbent displacement signal, CE verdict, null tally, schema count. Stage 4 row includes displacement verdict (Yes/No/Pending). "Not prose notes."

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 through C-08 | 10/10 each | All five stages present; GATE S; artifact writes per stage; scout loaded; `topic-story` handoff |
| **C-10** | **2/4** | Design explicitly specifies "not prose notes" — tabular column values (null, found, counts) are verdict tokens in structured cells, not natural-language confirmation per stage. The scorecard format eliminates the prose confirmation layer that C-10 requires. |
| C-11 | 4/4 | GATE S still blocks Stage 1 |
| C-12 | 4/4 | Incumbent tracked as named column across all evidence stages; anchored at CAMPAIGN OPEN |
| C-19 | 4/4 | SESSION INVARIANTs still pre-committed at CAMPAIGN OPEN |
| C-20 | 4/4 | Null tally column provides per-stage tally accumulation with count language |
| C-29 | 4/4 | Schema count column provides per-stage schema integrity count at all evidence stages |
| C-13 through C-33 (excl. C-10) | 4/4 each | v10 stack maintained; scorecard format is additive presentation |
| **C-34** | **2/4** | Scorecard tracks "Incumbent displacement signal" as a named column at each stage — satisfies the per-stage incumbent reference. Stage 4 row records displacement verdict (Yes/No/Pending) — satisfies the verdict presence. **PARTIAL because:** (1) column label is "Incumbent displacement signal," not a named INCUMBENT CHECK block or equivalent that "poses a stage-specific question"; (2) Stage 4's scorecard cell records the Yes/No/Pending answer but does not explicitly *ask* "does the accumulated evidence make a credible case for displacing {incumbent}" — the column header frames the tracking purpose generically. A scorecard cell value is not a structural question. |

**C-34 gap anatomy:** The scorecard column is an equivalent tracking mechanism for C-12 (presence at each stage) but falls short of C-34's stronger requirement: a named block that explicitly poses the displacement question. Verdict tracking ≠ verdict question.

**C-10 gap anatomy:** "Not prose notes" is the design constraint. Each stage output is a table row. Table cells with values like "null" and "found" are verdict tokens; no natural-language per-stage confirmation layer exists.

**Composite:** 50 + 30 + (104 − 2 − 2) = **180/184** — Golden (threshold met, gaps at C-10 and C-34)

---

### V-03 — Sparse Lifecycle

**Axis:** No ENTER/WORK/CLOSE labels. INCUMBENT CHECK is the dominant section in each evidence stage. Structural tally and schema notes compressed to a single footer line per stage.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 through C-08 | 10/10 each | All five stages present (structural obligations remain); GATE S; progressive writes; scout load; handoff |
| **C-10** | **4/4** | INCUMBENT CHECK is the dominant section — as the dominant section, it carries the evidence content for the stage (what was found regarding incumbent displacement). This provides the natural-language confirmation C-10 requires. Ceremony stripped ≠ prose stripped. The INCUMBENT CHECK section describes findings in natural language even when ENTER/WORK/CLOSE scaffolding is removed. Contrast with V-02 where "not prose notes" explicitly eliminates prose. |
| C-11 | 4/4 | GATE S blocking intact |
| C-12 | 4/4 | Incumbent anchored at CAMPAIGN OPEN; INCUMBENT CHECK as dominant section provides explicit per-stage reference |
| C-20 | 4/4 | Footer line at each stage includes null tally with count language |
| C-29 | 4/4 | Footer line at each stage includes schema integrity count — "compressed to single footer line" ≠ absent |
| C-13 through C-33 (excl. C-10) | 4/4 each | v10 stack maintained; sparse lifecycle strips ceremony not structural content |
| **C-34** | **4/4** | INCUMBENT CHECK is explicitly named as the dominant section at each evidence stage — satisfies "named INCUMBENT CHECK section." Stage 4's INCUMBENT CHECK must include the displacement verdict question (per R12 objective; removing this from Stage 4's dominant section would hollow the core design purpose). C-12 passes. PASS. |

**C-34 strength note:** Making INCUMBENT CHECK the dominant section is the most direct structural implementation of C-34 — the section is not supplementary to the stage but IS the stage. Stage-skipping or implicit tracking is structurally impossible when INCUMBENT CHECK is the entry point.

**Composite:** 50 + 30 + 104 = **184/184** ✓ Golden

---

### V-04 — Role Sequence + Phrasing Register (Combined)

**Axis:** V-01 three-role gate (ROLE C) combined with a phrasing register axis (consistent formal vocabulary / lexical register declared at CAMPAIGN OPEN).

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 through C-08 | 10/10 each | Full structure inherited from V-01 |
| C-10 | 4/4 | Phrasing register is a vocabulary/tone constraint; does not eliminate prose confirmation per stage |
| C-12 | 4/4 | ROLE C incumbent threat analysis inherited |
| C-19 | 4/4 | SESSION INVARIANTS unchanged; register declaration adds a fourth invariant (SESSION INVARIANT D or equivalent) without degrading existing three |
| C-30 | 4/4 | DERIVATION ANNOTATION RULE still pre-committed as SESSION INVARIANT C |
| C-13 through C-33 | 4/4 each | v10 stack + V-01 additive; phrasing register is presentation-only |
| **C-34** | **4/4** | Inherits V-01's ROLE C + named INCUMBENT CHECK blocks. Phrasing register enforces consistent vocabulary in the blocks (e.g., "INCUMBENT CHECK: Does stage evidence indicate a credible displacement signal against {status_quo_comparator}?") — may sharpen the displacement question framing rather than weakening it. |

**Phrasing register + C-34 interaction:** A declared register ensures the INCUMBENT CHECK blocks at all three stages use the same displacement-question framing — strengthening auditable consistency of the criterion across stages. No structural degradation.

**Composite:** 50 + 30 + 104 = **184/184** ✓ Golden

---

### V-05 — All Three + Inertia Score (Combined)

**Axis:** Role sequence (ROLE C) + scorecard format + sparse lifecycle + inertia score. Inertia score quantifies how hard it would be to displace the incumbent; feeds Stage 4 displacement verdict.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 through C-08 | 10/10 each | Full structure; three roles; all stages present |
| **C-10** | **4/4** | Sparse lifecycle's INCUMBENT CHECK as dominant section provides per-stage prose. Scorecard rows provide tabular evidence summary. Combined: dominant-section prose + scorecard structure = C-10 satisfied. The V-02 degradation (prose absent) is mitigated by V-03's dominant-section design. |
| C-12 | 4/4 | ROLE C (role_sequence) + INCUMBENT CHECK dominant section (sparse lifecycle) + scorecard column (scorecard format) — three-mechanism coverage |
| C-17 | 4/4 | Inertia score could add a fourth confidence-capping variable (high inertia → lower confidence even on positive CE) but does not remove the existing CE-score cap formula |
| C-20 | 4/4 | Scorecard null tally column provides per-stage accumulation |
| C-29 | 4/4 | Scorecard schema count column per stage |
| C-13 through C-33 | 4/4 each | Full three-axis combination maintains all v10 obligations; inertia score is additive to confidence mechanism |
| **C-34** | **4/4** | Sparse lifecycle provides named INCUMBENT CHECK as dominant section (resolves V-02's column-vs-block ambiguity). Stage 4 INCUMBENT CHECK includes inertia score as the mechanism for the displacement verdict: "INCUMBENT CHECK: Inertia score = N. Does accumulated evidence (inertia-adjusted) make a credible case for displacing {status_quo_comparator}? [Yes/No/Pending]." Role C provides structural origin; scorecard row records the verdict. Three-mechanism C-34 implementation — strongest in the round. |

**Inertia score + C-34 interaction:** Inertia score makes Stage 4's displacement verdict mechanically grounded — the Yes/No/Pending answer is derived from the inertia score value rather than a qualitative judgment. This extends C-34's displacement verdict the same way C-17 extends C-09: from verbal qualification to structural constraint.

**Composite:** 50 + 30 + 104 = **184/184** ✓ Golden

---

### Round 12 Summary

| Variation | Axis | C-34 | C-10 | Other | Score | Status |
|-----------|------|------|------|-------|-------|--------|
| V-01 | role_sequence | 4/4 PASS | 4/4 | All 4/4 | **184** | Golden |
| V-02 | scorecard_format | 2/4 PARTIAL | 2/4 PARTIAL | All 4/4 | **180** | Golden |
| V-03 | sparse_lifecycle | 4/4 PASS | 4/4 | All 4/4 | **184** | Golden |
| V-04 | role_sequence + phrasing_register | 4/4 PASS | 4/4 | All 4/4 | **184** | Golden |
| V-05 | all_three + inertia_score | 4/4 PASS | 4/4 | All 4/4 | **184** | Golden |

**Rankings:**
1. V-01, V-03, V-04, V-05 — 184/184 (tied)
2. V-02 — 180/184

---

### V-02 Gap Analysis

C-34 and C-10 both fail in the same structural direction: the scorecard format trades prose for structured columns. C-34's "named block that poses a question" becomes a column header that records an answer. C-10's "natural-language confirmation" becomes a table cell value. The scorecard is a strong C-12 and C-20/C-29 implementation but an insufficient C-34 implementation because the incumbent check is tracking-oriented, not question-oriented.

**Fix path:** Promote Stage 4's scorecard row from a column entry to a named INCUMBENT CHECK block with an explicit displacement question, then record the answer as a cell in the scorecard. This preserves the scorecard's audit benefits while satisfying C-34's "explicitly ask" requirement.

---

### Excellence Signals

**From V-01 (top + highest new C-34 chain strength):**
- `incumbent_threat_locked` as gate attestation field: moving INCUMBENT THREAT BLOCK from open preamble to a dedicated role closes the "gate doesn't verify incumbent analysis was done" gap. GATE S now requires `invariant_registry_confirmed` (ROLE A) + `gate_s_cleared` (ROLE B) + `incumbent_threat_locked` (ROLE C) — making all three session preconditions auditable as owned fields before Stage 1 opens.

**From V-03:**
- INCUMBENT CHECK as sole dominant section under sparse lifecycle: demonstrates C-34 is structurally self-sustaining without ceremony scaffolding. When ENTER/WORK/CLOSE labels are stripped, the incumbent displacement argument IS the stage — the most direct possible expression of C-34's intent.

**From V-05:**
- Inertia score as mechanical Stage 4 displacement verdict: extends C-34 the same way C-17 extended C-09. Yes/No/Pending answers a qualitative question; an inertia-adjusted score derives the verdict computationally, making Stage 4's INCUMBENT CHECK output auditable from the score value.

**From V-04:**
- Phrasing register as C-34 consistency enforcer: a declared register ensures all three INCUMBENT CHECK blocks use the same displacement-question framing — prevents criterion drift between Stage 2, Stage 3, and Stage 4 blocks in long or multi-turn sessions.

---

```json
{"top_score": 184, "all_essential_pass": true, "new_patterns": ["incumbent_threat_locked as gate attestation field makes ROLE C incumbent analysis auditable from GATE S — closes preamble-provenance gap not addressed by C-34 alone", "INCUMBENT CHECK as dominant section under sparse lifecycle demonstrates C-34 obligation is ceremony-independent and structurally self-sustaining", "inertia score as Stage 4 displacement verdict mechanism grounds Yes/No/Pending in a computable value — extends C-34 the way C-17 extended C-09"]}
```
