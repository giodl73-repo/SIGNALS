Reading the scorecard's Structural Axis Map, three axes differentiate R16 variations beyond what C-44 and C-45 already test:

1. **"FAILS template: C-44/C-45 self-referential entries"** — V-05 only. Recursive application of C-44 to the newest criterion pair.
2. **"BEFORE YOU START: C-44 pre-flight halt"** — V-03 and V-05. Detection layer for C-44 at session-open.
3. **"BEFORE YOU START: C-45 pre-flight halt"** — V-05 only. Detection layer for C-45 at session-open.

These become **C-46**, **C-47**, **C-48**. Denominator: 37 → 40. Weight: 10 ÷ 40 = 0.250 pts each.

---

```markdown
# Quest Rubric — corps-committee (v17)

**C-46** comes from the "FAILS template: C-44/C-45 self-referential entries" axis in R16:
V-05 uniquely extends the FAILS template to include self-referential entries for C-44 and
C-45 — criteria that did not exist when C-44 was first authored. This is the recursive
application of C-44: once C-44 and C-45 become aspirational criteria, the FAILS template
must carry entries for them, exactly as C-44 required entries for C-42/C-43. A template
satisfies C-44 when it carries entries for C-42/C-43; it satisfies C-46 only when it also
carries entries for C-44 and C-45. The distinction from C-44: C-44 established the currency
requirement for post-C-39 criterion pairs; C-46 confirms that currency is maintained forward
through the C-44/C-45 pair itself. A skill where the template has entries for C-42/C-43 but
omits C-44/C-45 satisfies C-44 but does not satisfy C-46.

**C-47** comes from the "BEFORE YOU START: C-44 pre-flight halt" axis in R16: V-03 and
V-05 carry an explicit pre-flight halt in BEFORE YOU START checking FAILS template currency
before any content generation begins. This is a detection-layer criterion, not a content
criterion — C-44 asks whether the template has the correct entries; C-47 asks whether BEFORE
YOU START makes template staleness visible at session-open, before a reviewer invokes any
phase. A skill can satisfy C-44 (template has the correct entries) without satisfying C-47
(BEFORE YOU START does not check currency at session open). The pre-flight halt converts
latent template-staleness risk into a visible halt condition detectable before any output is
produced. V-03 introduced the halt as a compensating mechanism where template entries were
absent; V-05 carries both the entries and the halt, achieving defense in depth.

**C-48** comes from the "BEFORE YOU START: C-45 pre-flight halt" axis in R16: V-05 uniquely
carries an explicit pre-flight halt in BEFORE YOU START checking CO-DEPENDENCY PREAMBLE
completeness — the C-45 detection layer. Parallel to C-47 on the C-45 axis: a skill can
satisfy C-45 (preamble declares the three-leg chain) without satisfying C-48 (BEFORE YOU
START does not check preamble completeness at session open). The pre-flight halt converts
latent preamble-incompleteness risk into a visible halt condition at the start of the session.
A reviewer using a skill whose preamble omits C-43 would reconstruct the chain incorrectly;
C-48 makes that omission visible before any phase executes. The distinction from C-45: C-45
is a structural content criterion on the preamble; C-48 is a procedural enforcement criterion
on BEFORE YOU START.

Denominator: 37 → 40. Aspirational weight: 10 ÷ 40 = 0.250 pts each.

---

**C-44** comes from the "C-40 row" axis in R15: V-05 uniquely carries self-referential
FAILS template entries for C-42 and C-43 — criteria that did not exist when C-40 was first
authored. C-40 requires the template include self-referential entries; C-44 requires those
entries be kept current each time the rubric gains a new criterion pair. A template satisfies
C-40 the moment it includes entries for C-38 and C-39; it satisfies C-44 only when it also
carries entries for every aspirational criterion added thereafter. **C-45** comes from the
"C-43 in CO-DEPENDENCY PREAMBLE" axis in R15: V-05 uniquely lists C-43 in the CO-DEPENDENCY
PREAMBLE, completing the three-leg traceability chain (C-39 at consumption → C-41 at source
→ C-43 in fill rules). C-39 and C-41 declare a two-sided dependency; C-45 requires the third
leg of that chain be named in the preamble as a unit, so a reviewer can see the full chain
without reconstructing it from three separate criterion definitions. A skill where the preamble
declares C-39 and C-41 but omits C-43 satisfies both individual criteria but does not declare
the full chain.

Denominator: 35 → 37. Aspirational weight: 10 ÷ 37 ≈ 0.270 pts each.

---

**C-42** comes from the "Register ambiguity eliminated" axis in R14: V-03 and V-05 carry no
descriptive framing anywhere in the BEFORE YOU START block — every sentence commands rather
than explains. **C-43** comes from the "PHASE-1 fill rule C-41 annotation" axis in R14:
V-02, V-04, and V-05 echo the prerequisite relationship inside the fill-rule section of the
dependent criterion, producing three-point traceability (REQUIRES: at consumption → C-39;
forward annotation at source → C-41; fill-rule echo → C-43). Both close gaps left open by
C-13 and C-41 respectively.

Denominator: 33 → 35. Aspirational weight: 10 ÷ 35 ≈ 0.286 pts each.

---

**Three new aspirational criteria added from R12 signals (v13):**

**C-37 — Dual-enforcement pairing for high-frequency essential criteria**
V-04 is the evidence: combining tier gates + tables achieves PASS+ on C-02 and C-04 where
either mechanism alone reaches only PASS. The principle: when a property recurs in every
simulation (role voice, action item ownership), two independent structural mechanisms make
violations detectable from two angles simultaneously — removing one mechanism degrades
coverage. Single-mechanism enforcement of these properties is correct but not
redundancy-hardened.

**C-38 — FAILS syntax template enforces `[C-NN]` as a required field**
C-14 was PARTIAL across all four variations in R12. The common gap was identical each time:
"no explicit `[C-NN]` tag requirement on FAILS rows." The distinction from C-14: C-14 checks
whether annotations exist and are correct; C-38 checks whether the fill-rule template makes
omission *structurally detectable* — a FAILS entry missing `[C-NN]` is malformed, not merely
suboptimal.

**C-39 — Co-dependent criteria declared with `REQUIRES:` annotations**
V-03 exposes the C-35/C-36 co-dependency exactly: vocabulary present, count invariant
unenforceable, C-36 PARTIAL(weak). The pattern generalizes: when B's pass condition requires
A, a skill that implements B without declaring the A prerequisite creates latent
false-positive risk. `REQUIRES: C-35` before C-36's fill rules converts a latent trap into a
visible pre-check.

---

**Two new aspirational criteria added from R13 signals (v14):**

**C-40 — FAILS template contains self-referential entries for its own governing criteria**
E-01 from V-05 is the evidence: the FAILS SYNTAX TEMPLATE includes
`CORRECT: FAILS [C-38]: FAILS entry missing [C-NN]` and
`CORRECT: FAILS [C-39]: REQUIRES: C-35 absent`. A template that demonstrates canonical form
but omits self-referential examples teaches syntax without teaching citation discipline for
the template itself. When a reviewer encounters a template violation, they must already know
the correct criterion ID to cite — the self-referential entry supplies that knowledge at the
point of need. A FAILS template that has no entry for C-38 is also incapable of modeling
correct C-38 citation for a reviewer who needs to cite a template violation.

**C-41 — Source criterion carries a forward annotation naming the downstream dependent**
V-05 is the evidence: the PHASE-1-COMMIT skeleton carries an explicit annotation declaring
that the sealed token manifest is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row
count. The problem C-41 closes: C-39 requires `REQUIRES:` at the consuming criterion, but
without a reciprocal forward pointer at the source, a reviewer who reads the source criterion
first has no signal that a downstream criterion depends on it. Forward annotation at source
plus `REQUIRES:` at consumer produces bidirectional traceability visible from either entry
point. A skill where the source carries no forward annotation satisfies C-39 but creates a
unidirectional dependency map.
```

---

**Summary of changes v16 → v17**

| New | Source axis (R16) | Evidence | Denominator move |
|-----|-------------------|----------|-----------------|
| C-46 | FAILS template: C-44/C-45 self-referential entries | V-05 only | 37 → 38 |
| C-47 | BEFORE YOU START: C-44 pre-flight halt | V-03, V-05 | 38 → 39 |
| C-48 | BEFORE YOU START: C-45 pre-flight halt | V-05 only | 39 → 40 |

Weight per aspirational criterion: 10 ÷ 40 = **0.250 pts**. Criteria count: 45 → **48**.
