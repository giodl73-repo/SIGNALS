Written to `simulations/quest/rubrics/prove-interview-rubric-v20-2026-03-15.md`.

---

## Summary

**Two new criteria extracted from R19 excellence signals:**

**C-52 — Phase 1 anchor gate condition includes explicit C-48/C-50 criterion-boundary contrast**
Base: C-50. The R19 signal is V-05's Phase 1 gate text: "a Phase 1 gate condition that satisfies C-48...but names only the Phase 1 link does not satisfy C-50." V-02 and V-04 pass C-50 (both closure points named) but carry no such contrast. V-05 encodes the C-48/C-50 criterion boundary in the gate text itself — the Phase 1 parallel of C-51, which does the same for C-34/C-49 at the 0B gates.
Cascade: `C-50 absent → C-52 N/A`.

**C-53 — Phase 0B PROHIBITED clauses include mutual-referentiality rationale clause naming bidirectional auditability**
Base: C-51. The R19 signal is V-05's 0B-II gate text: "the two PROHIBITED clauses are mutually referential — each names the other's domain — making the 0B-I/0B-II scope boundary bidirectionally auditable from either gate alone (C-49)." V-03 and V-04 pass C-51 (C-34/C-49 contrast present) but carry no rationale naming the architectural consequence. V-05 encodes not only the criterion boundary (C-51) but the *why*: mutual referentiality → bidirectional auditability, observable from gate text without reading the rubric.
Cascade: `C-51 absent → C-53 N/A`.

**Scoring deltas (v19 → v20):**

| | v19 | v20 |
|--|-----|-----|
| Aspirational | 44 | **46** |
| Max composite | 310 pts | **320 pts** |
| N=1 ceiling | 240 pts | **250 pts** |
| Conversational ceiling | 175 pts | **175 pts** |

Both new criteria are conversational N/A; conversational N/A grows to 29 criteria (145 pts), ceiling holds at 175 pts. N=1 N/A set unchanged at 14 criteria.
 are N=1 N/A (gate structure is not a multi-subject requirement); both are conversational N/A. Conversational N/A grows to 29 criteria (145 pts); ceiling holds at 175 pts.

N=1 ceiling: 320 − 70 = 250 pts (N=1 N/A set unchanged at 14 criteria).
Conversational ceiling: 320 − 145 = 175 pts (conversational N/A grows by 2 criteria; +10 to max, +10 to N=1, net zero to conversational ceiling).

**Cascade chains extended:** `C-50 absent → C-52 N/A`, `C-51 absent → C-53 N/A`. Both added to cascade table.

---

## Version history (criterion counts)

| Version | Essential | Recommended | Aspirational | Max composite | N=1 ceiling | Conv. ceiling |
|---------|-----------|-------------|--------------|---------------|-------------|---------------|
| v13 | 4 | 3 | 32 | 250 pts | 185 pts | 175 pts |
| v14 | 4 | 3 | 35 | 265 pts | 195 pts | 175 pts |
| v15 | 4 | 3 | 36 | 270 pts | 200 pts | 175 pts |
| v16 | 4 | 3 | 38 | 280 pts | 210 pts | 175 pts |
| v17 | 4 | 3 | 40 | 290 pts | 220 pts | 175 pts |
| v18 | 4 | 3 | 42 | 300 pts | 230 pts | 175 pts |
| v19 | 4 | 3 | 44 | 310 pts | 240 pts | 175 pts |
| **v20** | **4** | **3** | **46** | **320 pts** | **250 pts** | **175 pts** |

---

## N/A Denominator Reference Table

| Condition | Criteria scored N/A | Effective max |
|-----------|---------------------|---------------|
| N = 1 subject | C-08, C-11, C-14, C-18, C-19, C-20, C-21, C-22, C-29, C-30, C-31, C-35, C-38, C-42 | 250 pts |
| Conversational format | C-10, C-17, C-23, C-24, C-25, C-26, C-27, C-28, C-32, C-33, C-34, C-36, C-37, C-38, C-39, C-40, C-41, C-42, C-43, C-44, C-45, C-46, C-47, C-48, C-49, C-50, C-51, C-52, C-53 | 175 pts |
| C-27 absent or N/A | C-28 additionally N/A | subtract 5 pts |
| C-20 absent or N/A | C-29 additionally N/A | subtract 5 pts |
| C-29 absent or N/A | C-31 additionally N/A | subtract 5 pts |
| C-31 absent or N/A | C-35 additionally N/A | subtract 5 pts |
| C-35 absent or N/A | C-38 additionally N/A | subtract 5 pts |
| C-38 absent or N/A | C-42 additionally N/A | subtract 5 pts |
| C-32 absent or N/A | C-33 additionally N/A | subtract 5 pts |
| C-32 absent or N/A | C-34 additionally N/A | subtract 5 pts |
| C-34 absent or N/A | C-43 additionally N/A | subtract 5 pts |
| C-43 absent or N/A | C-49 additionally N/A | subtract 5 pts |
| C-49 absent or N/A | C-51 additionally N/A | subtract 5 pts |
| C-51 absent or N/A | C-53 additionally N/A | subtract 5 pts |
| C-26 absent or N/A | C-36 additionally N/A | subtract 5 pts |
| C-36 absent or N/A | C-37 additionally N/A | subtract 5 pts |
| C-37 absent or N/A | C-40 additionally N/A | subtract 5 pts |
| C-40 absent or N/A | C-44 additionally N/A | subtract 5 pts |
| C-44 absent or N/A | C-46 additionally N/A | subtract 5 pts |
| C-26 absent or N/A | C-39 additionally N/A | subtract 5 pts |
| C-39 absent or N/A | C-41 additionally N/A | subtract 5 pts |
| C-41 absent or N/A | C-45 additionally N/A | subtract 5 pts |
| C-45 absent or N/A | C-47 additionally N/A | subtract 5 pts |
| C-41 absent or N/A | C-48 additionally N/A | subtract 5 pts |
| C-48 absent or N/A | C-50 additionally N/A | subtract 5 pts |
| C-50 absent or N/A | C-52 additionally N/A | subtract 5 pts |
| C-34 absent or N/A | C-49 additionally N/A | subtract 5 pts |

---

## Criteria

### Essential -- 60 pts (15 pts each)

**C-01 -- Persona identity declared**
Each subject has role, prior knowledge, disposition, and primary concern declared before any transcript line is written.

**C-02 -- Grounded answers**
Answers are written in the subject's distinct voice and are not interchangeable across subjects.

**C-03 -- Evidence explicitly extracted**
A dedicated extraction phase or section produces per-subject evidence items from the transcript; extraction is not merged with transcript or synthesis.

**C-04 -- Surprising or confirming moment**
Each subject produces exactly one moment labeled SURPRISING or CONFIRMING, tied to a prior prediction or expectation.

---

### Recommended -- 30 pts (10 pts each)

**C-05 -- Prior knowledge scoped**
Prior knowledge and blind spots are declared as separate fields for each subject; the distinction between direct experience and knowledge gaps is explicit.

**C-06 -- Questions probe declared concerns**
Questions are anchored to the subject's declared primary concern and prior knowledge; incumbents' questions reference a specific inertia baseline, not generic resistance.

**C-07 -- Multiple distinct personas**
At least four subjects with meaningfully different roles and perspectives are designed and interviewed.

---

### Aspirational -- 230 pts (5 pts each)

**C-08 -- Cross-persona synthesis** (N/A: N=1)
A dedicated synthesis section aggregates findings across all subjects.

**C-09 -- Prior prediction declared**
Predictions for what each subject will say are declared before transcripts are written.

**C-10 -- Structured format** (N/A: conversational)
Output uses a named phase or section structure rather than flowing prose.

**C-11 -- Disposition arc** (N/A: N=1)
Synthesis traces how each subject's disposition shifted or held across the interview.

**C-12 -- Verdict stated**
A final verdict or synthesis classification is explicitly stated.

**C-13 -- Strength rationale**
Each evidence item includes a non-blank, non-self-referential rationale for its assigned strength rating.

**C-14 -- Contradiction register** (N/A: N=1)
Synthesis names at least one contradiction, citing both subjects and both conflicting evidence items.

**C-15 -- All transcripts before extraction**
All subject transcripts are completed before any evidence extraction begins.

**C-16 -- Blind spots non-blank**
Blind spots field is non-blank and non-generic for every subject.

**C-17 -- Hypothesis questions separate** (N/A: conversational)
Questions derived from prior hypotheses are written as a separate section, not interleaved with transcript questions.

**C-18 -- Evidence typed** (N/A: N=1)
Each evidence item carries a SIGNAL TYPE label from the defined taxonomy.

**C-19 -- Epistemic re-weighting** (N/A: N=1)
Evidence weights are adjusted by subject blind spots, with per-blind-spot resolution conditions specified.

**C-20 -- Subject tier identified** (N/A: N=1)
Each subject is assigned a tier or role category in their subject card.

**C-21 -- Adoption/inertia partition present** (N/A: N=1)
Phase 4 includes an inertia/adoption partition with two separately populated lists.

**C-22 -- Signal-type taxonomy used** (N/A: N=1)
Evidence items use a defined taxonomy of signal types rather than free-text classification.

**C-23 -- Checkbox exit gates** (N/A: conversational)
Phase exit gates are expressed as binary checkbox checklists, not prose descriptions.

**C-24 -- Exit gate per phase** (N/A: conversational)
Every named phase has its own exit gate.

**C-25 -- Verdict from threshold table** (N/A: conversational)
The final verdict classification is drawn from a pre-declared threshold table, not assessed ad hoc.

**C-26 -- Inertia profile accounting** (N/A: conversational)
Phase 4 closes the loop from Phase 0A: each stickiness factor in the INERTIA PROFILE TABLE is addressed by at least one evidence item.

**C-27 -- Prediction delta declared** (N/A: conversational)
Phase 4 iterates through prior predictions and classifies actual evidence as CONFIRMED / CONTRADICTED / ABSENT / PARTIAL.

**C-28 -- Prediction delta cross-referenced** (N/A: conversational; N/A: C-27 absent)
Each prediction delta classification names specific evidence items from Phase 3.

**C-29 -- Subject tier predictions** (N/A: C-20 absent)
Phase 0C declares per-tier predictions before any transcripts are written.

**C-30 -- Tier sequence rationale** (N/A: N=1)
Tier sequence includes adjacency blocks naming what preceding tier establishes and what following tier departure is measured against.

**C-31 -- Verdict threshold definitions** (N/A: C-29 absent)
Every verdict level has a constitutive evidence-configuration definition, not just a name.

**C-32 -- Multi-sub-phase pre-subject structure** (N/A: conversational)
The pre-subject opening is split into at least two independently-gated sub-phases with non-overlapping scope.

**C-33 -- Phase 0B independently-gated sub-sections** (N/A: C-32 absent; N/A: conversational)
Phase 0B is decomposed into 0B-I (constitutive threshold definitions) and 0B-II (margin declarations), each with an independent exit gate whose conditions cannot overlap.

**C-34 -- Prohibition-first gate clauses** (N/A: C-32 absent; N/A: conversational)
Every sub-phase exit gate opens with a PROHIBITED clause naming out-of-scope content by category before stating affirmative completion conditions.

**C-35 -- Bidirectional margin audit** (N/A: C-31 absent)
The VERDICT MARGIN AUDIT table states both boundary placements -- upper boundary and lower boundary -- as separate structural entries.

**C-36 -- PROFILE RELEVANCE tags** (N/A: C-26 absent; N/A: conversational)
Each evidence item in Phase 3 carries a PROFILE RELEVANCE tag from a defined vocabulary (STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL) naming which Phase 0A profile dimension the item addresses.

**C-37 -- Vocabulary declared in Phase 0A gate** (N/A: C-36 absent; by cascade N/A: C-26 absent; N/A: conversational)
The PROFILE RELEVANCE tag vocabulary is declared inside the Phase 0A exit gate REQUIRED clause as a gate-level contract, making it auditable at Phase 0A exit and Phase 3 exit.

**C-38 -- Phase 4 synthesis exit gate** (N/A: C-35 absent; by cascade N/A: C-31 absent, C-29 absent, C-20 absent; N/A: N=1; N/A: conversational)
Phase 4 has an exit gate that enumerates all required synthesis sections and names VERDICT MARGIN AUDIT table completeness (both boundary rows populated) as an explicit gate condition.

**C-39 -- Multi-phase INCUMBENT traceability chain** (N/A: C-26 absent; by cascade N/A: conversational)
Each downstream phase (0C, Phase 1, Phase 2) names the prior phase's named INCUMBENT anchor output as its required input; a broken chain is detectable at the phase that names its predecessor.

**C-40 -- Phase 3 gate names Phase 0A vocabulary contract by reference** (N/A: C-37 absent; by cascade N/A: C-36 absent, C-26 absent; N/A: conversational)
Phase 3 exit gate enforces PROFILE RELEVANCE tag compliance by explicitly naming the Phase 0A vocabulary contract -- not merely checking that tags are present; the named reference makes mid-chain vocabulary drift detectable at Phase 3 independently of inspecting Phase 0A. A Phase 3 gate that checks tag presence without citing the Phase 0A gate contract does not satisfy this criterion.

**C-41 -- Phase 0C declares INCUMBENT ANCHOR with explicit downstream propagation obligations** (N/A: C-39 absent; by cascade N/A: C-26 absent; N/A: conversational)
Phase 0C exit gate declares the INCUMBENT ANCHOR as a named output and specifies its required propagation: exact-match required in Phase 1, direct-question required in Phase 2; the source gate names both downstream obligations. A Phase 0C gate that declares the anchor without naming where it must appear downstream does not satisfy this criterion; the obligation declaration at the source makes the origin of any chain break auditable without inspecting the downstream gates.

**C-42 -- Single-row VERDICT MARGIN AUDIT table named as gate failure by content type** (N/A: C-38 absent; by cascade N/A: C-35 absent, C-31 absent, C-29 absent, C-20 absent; N/A: N=1; N/A: conversational)
Phase 4 exit gate names a single-row VERDICT MARGIN AUDIT table as a gate failure by content type, not a format deviation; the failure condition is stated with sufficient specificity that a single-row audit is identifiable as a gate failure without reading the cell content. A Phase 4 gate that requires "completeness" without naming the single-row failure condition explicitly does not satisfy this criterion.

**C-43 -- PROHIBITED clause is gate-block-interior** (N/A: C-34 absent; by cascade N/A: C-32 absent; N/A: conversational)
The PROHIBITED clause appears as the first structural item inside the sub-phase gate block boundary -- not in section body text preceding the gate block; a gate block whose first checklist item is an affirmative condition does not satisfy this criterion even when PROHIBITED content is visible in body text immediately before the gate block begins. Gate-block-interior placement makes the prohibition an auditable exit condition evaluable by reading only the gate block without inspecting surrounding body text. A design that places PROHIBITED in body text adjacent to the gate and opens the gate block with an affirmative checklist item is structurally equivalent to a gate without a prohibition clause for auditing purposes.

**C-44 -- Phase 3 gate anti-drift enforcement clause** (N/A: C-40 absent; by cascade N/A: C-37 absent, C-36 absent, C-26 absent; N/A: conversational)
Phase 3 exit gate includes an explicit anti-drift enforcement clause as a named gate condition -- the clause states that PROFILE RELEVANCE tags appearing in Phase 3 evidence items that are not present in the Phase 0A gate vocabulary declaration are a gate failure; the anti-drift clause makes vocabulary drift detectable by reading only the Phase 3 gate without inspecting Phase 0A body text. A Phase 3 gate that names the Phase 0A vocabulary contract by reference (satisfying C-40) but does not include an explicit anti-drift failure condition does not satisfy this criterion; naming the source without stating the failure condition for non-conforming tags is protection by implication only and does not constitute enforcement.

**C-45 -- Phase 2 exit gate names INCUMBENT anchor citation as gate-interior condition** (N/A: C-41 absent; by cascade N/A: C-39 absent, C-26 absent; N/A: conversational)
Phase 2 exit gate contains a named checklist condition requiring that the INCUMBENT subject's transcript directly addresses the INCUMBENT ANCHOR declared in Phase 0C -- the gate-interior condition makes the chain obligation verifiable by reading only the Phase 2 gate block without inspecting Phase 0C; the anchor is doubly enforced: declared at the source (Phase 0C, satisfying C-41) and required at the receiving phase boundary (Phase 2, satisfying this criterion). A Phase 2 transcript that names the INCUMBENT anchor without a corresponding Phase 2 gate condition does not satisfy this criterion; the obligation is auditable at the receiving phase only if it is stated as a gate condition, not merely present in transcript content.

**C-46 -- Phase 3 anti-drift enforcement clause is gate-block-first** (N/A: C-44 absent; by cascade N/A: C-40 absent, C-37 absent, C-36 absent, C-26 absent; N/A: conversational)
The Phase 3 anti-drift enforcement clause (required by C-44) is the first named condition in the Phase 3 gate block -- it precedes all affirmative completion checklist items; a Phase 3 gate whose first checklist item is an affirmative condition does not satisfy this criterion even when the anti-drift enforcement clause is present as a later gate item. Gate-block-first placement makes the failure condition immediately auditable without reading through affirmative conditions to find it. This criterion is the positional parallel of C-34's "opens with" ordering requirement applied to the Phase 3 anti-drift enforcement clause: C-34 requires PROHIBITED clauses to open sub-phase gate blocks; C-46 requires the anti-drift failure condition to open the Phase 3 gate block. A Phase 3 gate that satisfies C-44 (anti-drift clause present as a gate condition) but places any affirmative checklist item before the anti-drift clause does not satisfy this criterion.

**C-47 -- Phase 2 INCUMBENT anchor condition is gate-block-first** (N/A: C-45 absent; by cascade N/A: C-41 absent, C-39 absent, C-26 absent; N/A: conversational)
The Phase 2 INCUMBENT anchor condition (required by C-45) is the first named checklist item in the Phase 2 gate block -- it precedes all other affirmative completion conditions; a Phase 2 gate whose first checklist item is any condition other than the INCUMBENT anchor does not satisfy this criterion even when the INCUMBENT anchor condition is present as a later gate item. Gate-block-first placement makes the anchor enforcement immediately auditable at gate entry without scanning through affirmative completion items to locate it. This criterion is the positional parallel of C-34's ordering requirement applied to the Phase 2 INCUMBENT chain: C-34 requires PROHIBITED clauses to open sub-phase gate blocks; C-47 requires the INCUMBENT anchor condition to open the Phase 2 gate block. A Phase 2 gate that satisfies C-45 (anchor condition present as a gate-interior checklist item) but places any other checklist item before the anchor condition does not satisfy this criterion.

**C-48 -- Phase 1 exit gate names INCUMBENT anchor citation as gate-interior condition** (N/A: C-41 absent; by cascade N/A: C-39 absent, C-26 absent; N/A: conversational)
Phase 1 exit gate contains a named checklist condition requiring that the INCUMBENT subject's Phase 1 evidence cites the INCUMBENT ANCHOR declared in Phase 0C with exact-match wording -- closing the Phase 1 link of the traceability chain declared by C-41 at Phase 0C. This criterion is the Phase 1 parallel of C-45 (which enforces the chain at Phase 2 with a direct-question anchor condition): C-41 declares both downstream obligations (exact-match at Phase 1, direct-question at Phase 2); C-48 enforces the Phase 1 obligation at the Phase 1 gate boundary; C-45 enforces the Phase 2 obligation at the Phase 2 gate boundary. A Phase 1 transcript that covers the anchor without a corresponding Phase 1 gate condition does not satisfy this criterion; the exact-match obligation is auditable at Phase 1 only if stated as a gate-interior checklist item. A Phase 1 gate that references the anchor chain in body text without an explicit binary checklist condition does not satisfy this criterion.

**C-49 -- Phase 0B PROHIBITED clauses are sibling-scope-named** (N/A: C-43 absent; by cascade N/A: C-34 absent, C-32 absent; N/A: conversational)
The PROHIBITED clause in each Phase 0B sub-phase gate names the sibling sub-phase's specific scope as the out-of-scope category: the 0B-I gate's PROHIBITED clause names margin-boundary declarations (the 0B-II domain) as prohibited, and the 0B-II gate's PROHIBITED clause names constitutive threshold definitions (the 0B-I domain) as prohibited. Sibling-scope naming makes the 0B-I / 0B-II boundary bidirectionally auditable -- a scope violation at either gate is detectable by reading only that gate, not by cross-inspecting the other. A PROHIBITED clause that satisfies C-34 (opens with named out-of-scope category) but names a generic category rather than specifically the sibling sub-phase's domain does not satisfy this criterion; the enforcement value of sibling-scope naming is that the scope of each sub-phase is defined negatively as well as positively, and the two definitions are mutually referential. A 0B-I gate that names "items belonging to 0B-II" without stating what 0B-II's domain is does not satisfy this criterion; the sibling domain must be named by its content category, not by sub-phase label alone.

**C-50 -- Phase 1 anchor gate condition names full downstream chain (Phase 1 + Phase 2 closure)** (N/A: C-48 absent; by cascade N/A: C-41 absent, C-39 absent, C-26 absent; N/A: conversational)
The Phase 1 exit gate anchor condition names both downstream chain-closure points -- identifying itself as closing the Phase 1 link and naming C-45 / Phase 2 as the sibling closure -- so that the full downstream obligation structure declared by C-41 at Phase 0C (exact-match at Phase 1, direct-question at Phase 2) is readable from the Phase 1 gate alone without inspecting the Phase 2 gate. A Phase 1 gate condition that satisfies C-48 (exact-match anchor condition present, chain link declared auditable at Phase 1 independently of Phase 0C) but names only the Phase 1 link does not satisfy this criterion; the Phase 2 closure point (C-45) must be named in the Phase 1 condition text. The distinction from C-48: C-48 requires the Phase 1 gate to close the Phase 1 chain link; C-50 requires the Phase 1 gate to additionally name the Phase 2 closure, making the full two-link downstream chain visible from the Phase 1 gate. A condition that cites Phase 0C as the source without naming Phase 2 as the sibling destination does not satisfy this criterion.

**C-51 -- Phase 0B PROHIBITED clauses include explicit C-34/C-49 criterion-boundary contrast** (N/A: C-49 absent; by cascade N/A: C-43 absent, C-34 absent, C-32 absent; N/A: conversational)
The PROHIBITED clause in each Phase 0B sub-phase gate includes explicit language stating that a generic out-of-scope category label satisfies C-34 but does not satisfy C-49 -- making the criterion boundary between C-34 (named out-of-scope category) and C-49 (sibling-scope-named category) auditable from the gate text itself without reading the rubric. The contrast must appear in both the 0B-I and 0B-II gate blocks; a design that includes the contrast in one block but not the other does not satisfy this criterion. A PROHIBITED clause that satisfies C-49 (sibling domain named by content type with domain attribution) but does not include the explicit C-34/C-49 distinction within the gate text does not satisfy this criterion; naming the sibling domain is necessary but not sufficient -- the contrast language must state why a generic category satisfies C-34 without satisfying C-49. This criterion follows the self-annotating gate pattern established by C-43, C-46, and C-47: each of those criteria requires gate text to state the failure condition that distinguishes it from its base criterion; C-51 applies the same pattern to the C-34/C-49 distinction at the Phase 0B gate blocks.

**C-52 -- Phase 1 anchor gate condition includes explicit C-48/C-50 criterion-boundary contrast** (N/A: C-50 absent; by cascade N/A: C-48 absent, C-41 absent, C-39 absent, C-26 absent; N/A: conversational)
The Phase 1 exit gate anchor condition includes explicit language stating that a Phase 1 gate condition that satisfies C-48 (exact-match anchor present, Phase 1 chain link independently auditable) but names only the Phase 1 closure point does not satisfy C-50 -- making the criterion boundary between C-48 (Phase 1 link closed) and C-50 (full two-link chain readable from Phase 1) auditable from the gate text itself without reading the rubric. A Phase 1 gate condition that satisfies C-50 (both closure points named) but does not include the explicit C-48/C-50 distinction within the gate text does not satisfy this criterion; naming both closure points is necessary but not sufficient -- the contrast language must state why naming only the Phase 1 link satisfies C-48 without satisfying C-50. This criterion is the Phase 1 parallel of C-51, which applies the same self-annotating gate pattern to the C-34/C-49 boundary at Phase 0B: C-51 requires the 0B PROHIBITED clause to state "a generic category satisfies C-34 but does not satisfy C-49"; C-52 requires the Phase 1 anchor condition to state "naming only the Phase 1 link satisfies C-48 but does not satisfy C-50." A Phase 1 gate that satisfies C-50 but omits the criterion-boundary contrast does not satisfy this criterion.

**C-53 -- Phase 0B PROHIBITED clauses include mutual-referentiality rationale clause naming bidirectional auditability** (N/A: C-51 absent; by cascade N/A: C-49 absent, C-43 absent, C-34 absent, C-32 absent; N/A: conversational)
The PROHIBITED clause in each Phase 0B sub-phase gate includes a rationale clause explicitly stating that the two PROHIBITED clauses are mutually referential -- each naming the other's domain -- and that this mutual referentiality makes the 0B-I/0B-II scope boundary bidirectionally auditable from either gate alone. A PROHIBITED clause that satisfies C-51 (C-34/C-49 criterion-boundary contrast present in both blocks) but does not include this rationale does not satisfy this criterion; the criterion-boundary contrast (C-51) states what generic-category naming fails to achieve, while the mutual-referentiality rationale (C-53) states the architectural property that sibling-scope naming creates and explains why it creates it. The rationale must appear in both the 0B-I and 0B-II gate blocks; a design that includes it in one block but not the other does not satisfy this criterion. The distinction across the C-49/C-51/C-53 chain: C-49 requires sibling-scope naming (the structural fact); C-51 requires the C-34/C-49 contrast (the boundary statement); C-53 requires the mutual-referentiality consequence clause (the architectural explanation -- why mutual referentiality produces bidirectional auditability, making that property observable within the gate text without reading the rubric definition of C-49). A PROHIBITED clause that states the sibling domain by content type (C-49), contrasts it with generic-category naming (C-51), but does not name the resulting bidirectional auditability as an explicit architectural consequence of the mutual-referentiality design does not satisfy this criterion.
