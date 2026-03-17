---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-16
version: 14
round: R13
changes: >
  Added C-39 (Scope Gatekeeper threshold escalation prohibition cross-references
  the pre-role DFM block by name, extending C-38 from DFM-block presence to
  cross-role coupling so the in-role prohibition is traceable to its construction-time
  anchor without reading prior phases) from ES-R13-1/V-03; added C-40 (output
  instruction requires the purpose statement to name the DFM block by name,
  closing a traceability loop from the emitted artifact back to the construction-time
  calibration anchor, extending C-38 from pre-role structural presence to
  artifact-level propagation) from ES-R13-2/V-03. Denominator /30 -> /32.
---

## quest-rubric Rubric v14

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/32 × 10)` — denominator /30 → /32

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

Accumulated through Round 6. Each contributes 1 point to the A/32 denominator.

*(C-09 through C-22 text preserved verbatim from prior versions.)*

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

**C-29 — AUDITOR-PRE construction gate**

AUDITOR-PRE blocks are pre-declared before any criterion is written, not inserted
retroactively after criterion content is known. The construction gate closes when the block
is written and confirmed final; Phase 2 criterion authoring proceeds only after the gate
closes. This is the *construction* gate: it governs when boundary declarations may be
written. C-32's MANIFEST-ROW VERIFICATION closes the *reproduction* gate: it governs
whether the emitted manifest faithfully reproduces what the construction gate produced.

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

### Three criteria from Round 12 excellence signals (carried forward)

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

### Two criteria from Round 13 excellence signals

Both target **DFM traceability** — the structural property that the pre-role failure mode
callout required by C-38 propagates downstream into the construction phase (C-39) and
forward into the emitted artifact (C-40), rather than remaining a local orientation block
whose influence must be inferred from the constructed output.

**C-39 — Scope Gatekeeper cross-reference to DFM block**

Source signal: ES-R13-1 / V-03. The V-03 Scope Gatekeeper threshold escalation prohibition
contains: *"This prohibition is the primary defense against the Dominant Failure Mode named
in the pre-role block above."* This creates a cross-role coupling: the in-role prohibition
is not standalone — it derives its rationale from the named pre-role block. An evaluator
auditing the Scope Gatekeeper output can trace the prohibition back to the DFM block by
name. V-02 baseline Scope Gatekeeper has the prohibition but no such cross-reference.
C-38 requires the DFM block to exist; it does not require downstream roles to reference it.
This coupling is new territory: a DFM block that is never cited by downstream roles can be
removed without breaking any construction gate — the coupling makes removal detectable.

Without the cross-reference, the threshold escalation prohibition and the DFM block are
structurally independent: a rubric can satisfy both C-31's gate requirement and C-38's
DFM presence requirement while leaving no traceability path between them. The cross-
reference closes that path at the Scope Gatekeeper's primary defense site — the exact
location where threshold escalation is blocked.

Criterion: the Scope Gatekeeper's threshold escalation prohibition (or equivalent section
that blocks aspirational criteria from merely tightening existing essential/recommended
thresholds) explicitly names the pre-role DFM block as the threat it defends against. The
cross-reference must appear in the prohibition text itself — not as a comment outside the
prohibition or as an annotation in a separate section. The naming must be specific: a
generic reference to "the failure mode described above" does not satisfy this criterion;
the DFM block must be identified by its structural label (e.g., "Dominant Failure Mode"
or the specific name the block uses).

PARTIAL condition: the Scope Gatekeeper references the failure mode concept by content
description (e.g., "the failure mode where aspirational criteria tighten existing
thresholds") but does not name the pre-role block itself as the structural source.

Independence from C-38: C-38 tests whether the DFM block exists as a named, self-contained,
pre-role structural unit. C-39 tests whether the DFM block is cited by name at the
construction gate most directly responsible for the failure mode it describes. A rubric can
satisfy C-38 (DFM block present) without C-39 (no cross-reference from the Scope
Gatekeeper); V-02 baseline demonstrates this. A rubric cannot satisfy C-39 without C-38:
the cross-reference requires a named block to reference.

---

**C-40 — Output instruction DFM propagation to emitted artifact**

Source signal: ES-R13-2 / V-03. The V-03 output instruction says: *"purpose statement
(2-3 sentences, including reference to the Dominant Failure Mode named in the pre-role
block)"*. This creates artifact-level traceability: the emitted rubric's purpose statement
must carry the DFM name, closing a loop from the final artifact back to the construction-
time calibration anchor. No prior variation requires the output artifact to reference the
construction-phase framing.

Without this requirement, the DFM block's influence is local to the construction phase:
it orients the roles but leaves no trace in the artifact. A rubric reader navigating the
emitted artifact has no indication that a construction-time calibration anchor exists or
what failure mode the rubric was architected to detect. C-40 propagates the DFM from
ephemeral construction-phase context into the permanent artifact record.

Criterion: the output instruction (or equivalent emit-phase directive) explicitly requires
the emitted rubric's purpose statement to name the DFM block. "Name" means: the purpose
statement must carry the failure mode's label (as it appears in the pre-role DFM block),
not merely describe its concept in paraphrase. A purpose statement that says "this rubric
is designed to prevent low-quality aspirational criteria" does not satisfy this criterion
if the DFM block is named "Threshold Tightening Without New Territory" and neither the
label nor a direct quotation from the block appears in the purpose statement.

PARTIAL condition: the output instruction requires the purpose statement to reference the
DFM concept but does not require use of the block's specific label — a paraphrase
reference is permitted, but the structural linkage to the pre-role block is implicit rather
than explicit.

Independence from C-38: C-38 tests DFM block existence at the pre-role position; C-40
tests whether the block's label is carried into the emitted artifact's purpose statement.
A rubric can satisfy C-38 (DFM block present, self-contained) without C-40 (output
instruction makes no reference to the DFM); V-02 baseline demonstrates this. V-03
demonstrates both C-38 and C-40: the DFM block is present (C-38) and the output
instruction explicitly requires the purpose statement to include a reference to it (C-40).

Independence from C-39: C-39 tests propagation from DFM block to the Scope Gatekeeper
(construction phase); C-40 tests propagation from DFM block to the emitted artifact
(output phase). The two propagation paths are orthogonal: a rubric could require the
purpose statement to name the DFM (C-40 PASS) without the Scope Gatekeeper referencing
it (C-39 FAIL), or vice versa. V-03 satisfies both, confirming independence through
joint confirmation rather than ablation; a targeted probe for either direction alone
remains an open round candidate.

---

### Version history note

**v14** adds two aspirational criteria (C-39 and C-40) extracted from Round 13 excellence
signals, both targeting DFM traceability: Scope Gatekeeper cross-reference to DFM block
(C-39; ES-R13-1 / V-03 demonstrated that the V-03 Scope Gatekeeper prohibition explicitly
cites the pre-role DFM block, creating a cross-role coupling that makes the DFM block's
removal detectable at the construction gate), and output instruction DFM propagation to
emitted artifact (C-40; ES-R13-2 / V-03 demonstrated that the V-03 output instruction
requires the purpose statement to name the DFM block by label, propagating the construction-
time calibration anchor into the permanent artifact record). Denominator /30 → /32.

V-03 achieved a perfect score of 100.0 (the only variation in R13 to do so), confirming
that the DFM callout (C-38) produces a measurable structural improvement over the V-02
baseline (92.67) when all other axes are at the imperative-gate, atomic-item baseline. The
two new criteria are derived from structural choices in V-03 that were not present in any
other variation, beyond C-38's base requirement.

---

### Scoring

| State | Value | Earn conditions |
|-------|-------|-----------------|
| PASS | 1.0 | All pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5 | The specific circumstances named in each criterion's PARTIAL condition are met. |
| FAIL | 0.0 | No pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum of essential values) / 5 × 60     max 60
Recommended:  (sum of recommended values) / 3 × 30   max 30
Aspirational: (sum of aspirational values) / 32 × 10 max 10

Composite = Essential + Recommended + Aspirational   max 100
```

**Essential floor:** a single essential FAIL floors the score to 0 regardless of formula.
**Golden threshold:** all essential criteria PASS AND composite ≥ 90.

**Aspirational denominator:** /32 (C-09 through C-40).
- C-09–C-35: 27 criteria carried from prior rounds
- C-36, C-37, C-38: added in v13 (Round 12 excellence signals)
- C-39, C-40: added in v14 (Round 13 excellence signals)
