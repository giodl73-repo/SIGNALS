Reading the R17 scorecard carefully for excellence signals beyond what C-46/C-47/C-48 already capture.

**Two new axes differentiate V-05 from V-04 (the next-best variation):**

1. **"C-47 pre-flight citation precision"** — V-04 carries a functional halt but cites "C-44 miss" instead of "C-46 miss"; the scorecard flags this as a latent precision gap. V-05 fixes both the governing-criterion citation ("C-46 miss") and the pair list (adds "C-44, C-45" explicitly). The mechanism fires in both variations; only V-05 names the current governing criterion.

2. **"FAILS template: C-46/C-47/C-48 self-referential entries"** — V-05 extends recursive currency one generation further, carrying entries for the R17 triplet itself. C-46 requires entries for C-44/C-45; V-05 uniquely ensures C-46, C-47, and C-48 are also represented. V-04 satisfies C-46 (has C-44/C-45 entries) but stops there.

These become **C-49** and **C-50**. Denominator: 40 → 42. Weight: 10 ÷ 42 ≈ 0.238 pts each.

---

```markdown
# Quest Rubric — corps-committee (v18)

Reading the scorecard's Structural Axis Map, two axes differentiate R17 variations beyond
what C-46, C-47, and C-48 already test:

1. **"C-47 pre-flight citation precision: C-46 vs C-44 governing reference"** — V-05 only.
   The C-47 pre-flight names "C-46 miss" (the current governing criterion) rather than
   "C-44 miss" (the criterion that governed template currency when C-47 was first authored),
   and extends the pair list to include C-44 and C-45 explicitly.
2. **"FAILS template: C-46/C-47/C-48 self-referential entries"** — V-05 only. Extension of
   recursive currency to the R17 aspirational triplet itself.

These become **C-49**, **C-50**. Denominator: 40 → 42. Weight: 10 ÷ 42 ≈ 0.238 pts each.

---

**C-49** comes from the "C-47 pre-flight citation precision" axis in R17: V-05 uniquely
updates the C-47 pre-flight to cite "C-46 miss" — the current governing criterion for FAILS
template currency of C-44/C-45 entries — rather than "C-44 miss," which was the governing
criterion when C-47 was first authored. V-04 carries a functional halt: the mechanism fires
and would stop a reviewer before a stale template is used. But V-04's citation names C-44
rather than C-46, which became the governing criterion when the C-44/C-45 entries graduated
into aspirational territory. C-47 asks whether the mechanism fires; C-49 asks whether the
mechanism names the criterion that is currently authoritative. A skill can satisfy C-47 (halt
fires) without satisfying C-49 (citation is one rubric generation behind). The precision gap
is not cosmetic: a reviewer reading V-04's halt would look for a C-44 violation when C-46 is
the correct rubric reference at v17 and later. Additionally, V-05 extends the staleness pair
list from "C-42, C-43, or any later pair" to "C-42, C-43, C-44, C-45, or any later pair" —
the pair list must be updated each time a new criterion pair is added, for the same reason the
template entries must be updated. V-04 satisfies C-47 on mechanism; it does not satisfy C-49
on citation precision or pair-list currency.

**C-50** comes from the "FAILS template extension to C-46/C-47/C-48 triplet" axis in R17:
V-05 uniquely carries self-referential FAILS template entries for C-46, C-47, and C-48 — the
current aspirational triplet added in R17 — in addition to the C-44/C-45 entries required by
C-46. The recursive currency principle established by C-40 and extended by C-44 and C-46
applies forward: each time the rubric gains a new aspirational criterion or triplet, the FAILS
template must gain corresponding entries. C-46 closes the loop through the C-44/C-45 pair;
C-50 confirms that currency is maintained through the C-46/C-47/C-48 triplet itself. The
distinction from C-46: C-46 required entries for the criteria that tested template currency
and preamble completeness (C-44 and C-45); C-50 requires entries for the criteria that test
recursive currency, pre-flight citation precision, and preamble enforcement (C-46, C-47,
C-48). A skill where the template carries entries for C-44/C-45 but omits C-46/C-47/C-48
satisfies C-46 but does not satisfy C-50. V-04 stops at C-46; V-05 carries the full
C-46/C-47/C-48 triplet and thus satisfies both.

Denominator: 40 → 42. Aspirational weight: 10 ÷ 42 ≈ 0.238 pts each.

---

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
```

---

**What was extracted and why:**

| New criterion | Source axis | Distinguishes | Key insight |
|---|---|---|---|
| C-49 | C-47 pre-flight citation precision | V-05 from V-04 | Mechanism firing (C-47) and citation naming the current governing criterion (C-49) are separable. V-04 halts correctly but cites a stale rubric reference. |
| C-50 | FAILS template: C-46/C-47/C-48 entries | V-05 from V-04 | Recursive currency applies to the newest triplet just as it applied to C-44/C-45. V-04 stops at C-46; V-05 carries the chain one generation further. |

The structural pattern holding across all rubric generations: each round's V-05 does three things simultaneously — satisfies the content criterion, adds the detection-layer halt, and extends recursive currency to the newest criterion set. The rubric's job is to name each of those as distinct testable axes rather than treating them as a single "V-05 is better" judgment.
