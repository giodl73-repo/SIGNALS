Written to `simulations/quest/rubrics/quest-rubric-rubric-v13-2026-03-15.md`.

---

**What changed v12 → v13:**

**Two new aspirational criteria promoted from R12 excellence signals:**

**C-37** (`section-content-register-enforces-structural-requirements-independently-of-stop-gates`) — R12 V-03 isolation. C-34 already covered STOP-gate register; V-03 identifies a second independent enforcement-register layer: section-placement and section-content requirements ("must appear before criteria table", "must contain three labeled sub-sections"). When these convert to advisory ("should appear", "it is recommended to include"), C-11 drops to PARTIAL even while all STOP gates remain imperative. The three layers (Contract declarative, STOP-gate, section-content) degrade independently — V-03 confirms this by showing Contract item 3 surviving the ablation at PASS while section-content requirements fail. Each layer must independently maintain imperative phrasing.

**C-38** (`enumeration-only-stop-gate-prevents-criterion-drafting-contamination`) — R12 two-round pattern. V-01 and V-02 both score C-30 PARTIAL because Phase 1 combines a failure-mode column with criterion drafting in the same planning-table step — no dedicated STOP gate separates enumeration from drafting. The STOP gate is the structural mechanism that makes the enumeration phase "explicitly dedicated" per C-30's pass condition: without it, the model can merge both activities inline. Two-round confirmation (same root cause, two independent variation constructions) crosses the threshold.

**Structural updates:**
- Required Sections row 7: C-37, C-38 added to N/A scope list
- Scoring N/A paragraph: C-37, C-38 added
- Notes: C-37 and C-38 N/A scope blocks added; C-32 self-application bumped to version 13
- **v14 Candidates** (renamed from v13 Candidates): `joint-failure-chain-annotation` updated with R12 V-03 7-criterion chain evidence (widest chain observed); two new candidates added: `contract-layer-declarations-are-register-immune` and `inertia-framing-null-result-when-imperative-gates-present`; rejection-log count updated to 30 aspirational criteria
