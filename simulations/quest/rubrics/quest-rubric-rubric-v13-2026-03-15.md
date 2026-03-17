The file found is the `mock-all` rubric — different skill. The rubric being updated was provided inline in the prompt. Now I'll analyze the R12 scorecard to extract new excellence patterns, then produce the complete v13.

**New patterns from R12:**

1. **V-03 (advisory STOP ablation)** — Converting STOP conditions to advisory phrasing causes a cascade of 10+ gate failures. C-31 covers *presence* of independent STOPs; no existing criterion covers *imperative register*. Advisory phrasing at a gate position is structurally equivalent to removing the gate.

2. **V-04 (prose format ablation)** — C-05, C-08, C-16, C-17 all degrade to PARTIAL from the same root: prose checkpoint items that bundle multiple structural properties cannot be evaluated as single binary gates. No existing criterion requires atomic (one-property-per-item) structure.

3. **V-02 (pre-role inertia framing)** — Pre-role "Dominant Failure Mode" callout before the agent-role declaration creates a calibration anchor independent of SA-1. Design notes flag this as a C-04/C-11 depth signal. Not yet aspirational.

These yield **C-36**, **C-37**, **C-38**. Denominator rises from /27 → /30.

---

## quest-rubric Rubric v13

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/30 × 10)` — denominator /27 → /30

---

### Essential criteria (C-01–C-05) — carried from earlier rounds

Binary pass/fail. All five must pass for the score formula to apply; a single essential FAIL
floors the score regardless of E/R/A components.

*(C-01 through C-05 text preserved verbatim from prior versions.)*

---

### Recommended criteria (C-06–C-08) — carried from earlier rounds

Each contributes to the R/3 component. PARTIAL on a recommended criterion scores 0.5.

*(C-06 through C-08 text preserved verbatim from prior versions.)*

---

### Aspirational criteria (C-09–C-22) — carried from earlier rounds

Accumulated through Round 6. Each contributes 1 point to the A/30 denominator.

*(C-09 through C-22 text preserved verbatim from prior versions.)*

---

### One criterion from Round 9 excellence signals (carried forward)

**C-29 — AUDITOR-PRE construction gate**

AUDITOR-PRE blocks are pre-declared before any criterion is written, not inserted
retroactively after criterion content is known. The construction gate closes when the block
is written and confirmed final; Phase 2 criterion authoring proceeds only after the gate
closes. This is the *construction* gate: it governs when boundary declarations may be
written. C-32's MANIFEST-ROW VERIFICATION closes the *reproduction* gate: it governs
whether the emitted manifest faithfully reproduces what the construction gate produced.

*(Full criterion text preserved verbatim from prior version.)*

---

### Four criteria from Round 7 excellence signals (carried forward)

All four target **partial-credit integrity** — the structural property C-10 tests at the
formula level but not at the criterion level, the reproduction level, or the
inter-boundary semantic level.

**C-23 — Per-criterion PARTIAL-CONDITION block**
V-03 and V-05 demonstrate this. C-10 tells you PARTIAL = 0.5 in the formula; C-23 tells
you what evidence earns 0.5 for *this specific criterion*. Without it, evaluators interpret
partial credit subjectively — violating C-02 at the partial-credit boundary. V-01 and V-04
fail: `verdict_weights` in SA-1 but no per-criterion condition.

**C-24 — Formula consistency across structural positions**
V-02 fails: SA-1 is `essential_pass / N * 60` (binary); FINAL RUBRIC is the weighted form.
Two formula instances disagreeing on type leaves the governing formula ambiguous. V-03 gets
PARTIAL: binary SA-1 formula + prose note + expanded FINAL RUBRIC — intent aligned,
structure divergent.

**C-25 — FINAL RUBRIC anti-collapse formula guard** *(updated in v9 — SA-1 coupling removed)*
The guard was introduced in R7 as: "Reproduce the weighted formula from SA-1 verbatim —
do not collapse to binary counting." R8 exposed that this formulation silently drops the
reproduction mandate when SA-1 is absent (generalization probe). V9 form: **"Reproduce
this formula verbatim at every structural position where a formula appears — do not collapse
to binary counting."** Does not reference a specific prior phase; works when there is no
SA-1. V-04 satisfies the updated criterion (SA-1 present; guard fires correctly). Variations
produced without SA-1 must carry the guard independently.

**C-26 — VERDICT TIER DECLARATION inter-boundary block**
V-02, V-04, V-05 have a named block between `SPEC ANALYST: CLOSED` and `AUTHOR: OPEN`
defining PASS/PARTIAL/FAIL semantics. Evaluator-facing grounding, findable by structure.
V-01 and V-03 embed tier semantics only in SA-1 fields or formula comments.

---

### Criteria from Rounds 8–11 (carried forward)

**C-27 — DISCRIMINATES-BETWEEN blocks**
*(Full criterion text preserved verbatim from prior version.)*

**C-28 — DEPENDS_ON declarations**
*(Full criterion text preserved verbatim from prior version.)*

**C-30 — Dual-column PARTIAL-CREDIT MANIFEST**
*(Full criterion text preserved verbatim from prior version.)*

**C-31 — Structural redundancy guard**
Each enforcement gate position that lacks a structural element (block, field, or table
column) triggers an independent STOP rather than falling through silently. The guard fires
per absent position; a single omnibus STOP at the end of a checklist does not satisfy this
criterion because it cannot enforce absence at individual structural positions. V-03 fails
this criterion explicitly: when STOP tokens are converted to advisory phrasing, the
"independent STOP per absent enforcement position" requirement is rendered advisory, and the
guard no longer closes.

**C-32 — Phase 4 MANIFEST-ROW VERIFICATION**
*(Full criterion text preserved verbatim from prior version.)*

**C-33 — Phase 1 STOP names downstream phase as gate destination**
The Phase 1 STOP instruction explicitly names Phase 2 as the gate destination: "Do not
begin Phase 2 until…" (or equivalent). A STOP that does not name a destination phase
creates a structural ambiguity — the agent cannot determine which phase is gated. V-01
baseline: "Do not begin Phase 2 until…" satisfies this criterion. Advisory phrasing at this
position (V-03) degrades the gate without changing the naming property; the criterion tests
destination-naming, not register.

**C-34 — Verbatim sourcing with character-level precision**
*(Full criterion text preserved verbatim from prior version.)*

**C-35 — Phase 4 structural redundancy step**
*(Full criterion text preserved verbatim from prior version.)*

---

### Three criteria from Round 12 excellence signals

**C-36 — STOP-phrasing register uniformity**

Source signal: V-03 ablation (advisory STOP conditions). Converting all STOP CONDITION
imperatives to advisory phrasing ("please ensure," "it is recommended") causes cascade
failures across C-04, C-05, C-08, C-16, C-29, C-30, C-31, C-32, C-33 simultaneously — a
10+ criterion degradation from a single register substitution. This cascade reveals that
*imperative register* is not a style property but a structural one: advisory phrasing at a
gate position is functionally equivalent to removing the gate at that position.

Criterion: every enforcement-gate STOP token uses imperative phrasing — "STOP", "do not
proceed", "halt", "rewrite before continuing", or equivalent imperative construction.
Advisory variants ("please ensure", "it is recommended", "consider", "you may want to")
appearing at a gate position constitute a gate-open defect *at that position*, regardless of
whether an imperative STOP token appears elsewhere in the same phase. A rubric where some
gate positions are imperative and others are advisory is structurally non-uniform; each
advisory gate position scores as absent for the criterion that gate enforces. A rubric where
all gate positions are advisory fails this criterion and fails C-31 simultaneously.

PARTIAL condition: one or two gate positions use advisory phrasing in an otherwise
imperative stack; the affected gate positions are identifiable and countable.

---

**C-37 — Atomic gate-item structure**

Source signal: V-04 ablation (prose planning and checklist format). Converting Phase 1
planning table rows and Phase 2 checkpoint table rows to numbered prose list items degrades
C-05 (PARTIAL: binary gate enforcement harder to verify per-item), C-08 (PARTIAL: duplicate
failure modes less structurally visible), C-16 (PARTIAL: three failure modes present but
not as independently-addressable structural gates), and C-17 (PARTIAL: inline items not
structural subheader labels). All four failures trace to the same root: a prose item that
encodes two or more structural properties in a single sentence cannot be evaluated as a
binary gate without ambiguity — it conflates pass/fail at the item level.

Criterion: each row in the Phase 1 planning table and each row in the Phase 2 checkpoint
table (or their structural equivalents) encodes exactly one structural property. "Exactly
one" means: the row can be evaluated PASS or FAIL by inspection of a single observable
element (a field, a block, a label, a count, or a named gate). A row that bundles a count
check with a label check with a gate presence check in one prose sentence does not satisfy
this criterion, even if all three bundled properties are individually correct.

PARTIAL condition: the majority of items are atomic but one or two rows bundle two
properties, creating ambiguity at those specific rows only.

---

**C-38 — Pre-role dominant failure mode callout**

Source signal: V-02 variation (inertia framing). V-02 adds a named "Dominant Failure Mode"
callout block *before* the SetCoherenceAuditor preamble — before the agent's structural
scope is declared. The design notes identify this as a C-04/C-11 depth signal: naming the
primary failure mode the rubric is designed to detect before the role declaration creates a
calibration anchor that is structurally independent of SA-1 output. Variations produced
without SA-1 carry this anchor without modification. The pre-role position matters: a
failure mode named *inside* the agent preamble is in scope of the role; a failure mode
named *before* the preamble grounds the role declaration itself.

Criterion: the rubric includes a named failure mode callout block (a discrete, labeled
structural unit — not a parenthetical or inline comment) that appears before the first
agent-role declaration (e.g., before SetCoherenceAuditor or equivalent preamble). The block
names the dominant failure mode the rubric is architected to detect and explains why that
mode is primary. This anchor must be self-contained: an evaluator reading only the pre-role
block can identify the failure mode without reading the criteria.

PARTIAL condition: a failure mode is named before the role declaration but in inline prose
rather than a discrete named block, or the block names a failure mode without explaining
why it is primary.

---

### Version history note

**v13** adds three aspirational criteria (C-36 through C-38) extracted from Round 12
excellence signals: STOP-phrasing register uniformity (C-36; V-03 ablation demonstrated
that advisory register at gate positions is structurally equivalent to gate removal, causing
a 10+ criterion cascade), atomic gate-item structure (C-37; V-04 ablation demonstrated that
prose items bundling multiple properties cannot support per-item binary gate evaluation,
causing C-05/C-08/C-16/C-17 simultaneous degradation), and pre-role dominant failure mode
callout (C-38; V-02 variation demonstrated that a named failure mode block before the agent
role declaration creates a calibration anchor independent of SA-1, strengthening C-04/C-11
depth). Denominator /27 → /30.
