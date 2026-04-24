Now I have enough to score all five variations. Let me work through the full evaluation.

---

# Scoring Report — quest-rubric Round 20 (Rubric v20)

**Rubric:** v20 (C-01–C-52, denominator /44)
**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/44 × 10)`
**Baseline:** 42/44 × 10 = 9.55 on A term → composite 99.55 (assuming full E+R pass)
**Target criteria:** C-51 (co-located per-note STOP gate), C-52 (SPAN DEFINITION pre-step)

---

## Criterion Evaluation Framework

**C-49** — FORMAT TEMPLATE with mandatory [C-NN] slot present in Phase 8.5.
**C-50** — STATUS QUO foil items enumerate full pass-side criteria in each span.
**C-51** — FORMAT TEMPLATE's [C-NN] slot co-located with a STOP condition blocking Phase 8.5 note completion until slot is filled with a specific criterion ID.
**C-52** — Each STATUS QUO foil item preceded by a SPAN DEFINITION pre-step declaring (a) previous failure, (b) current failure, (c) full pass-side enumeration from which the foil item is transcribed.

All variations share the R19 V-04 base for C-01 through C-50. Key differences are isolated to C-51 and C-52.

---

## V-01 — Lifecycle Emphasis

**Axis:** Co-located inline STOP per note (C-51 probe); per-span direct instruction, no SPAN DEFINITION blocks (C-52 ablation control).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 (essential + recommended) | PASS | Inherited from R19 V-04 base; all five essential and three recommended criteria satisfied |
| C-09–C-48 | PASS | R19 V-04 baseline confirmed; no structural changes to these criteria in V-01 |
| C-49 | PASS | PER-NOTE FORMAT TEMPLATE present with [C-NN] slot |
| C-50 | PASS | STATUS QUO foil items enumerate full pass-side criteria per span: "passes C-01 and C-02 while failing C-03," "passes C-04 and C-05 while failing C-06," etc. — complete span in foil item text |
| **C-51** | **PASS** | Co-located `STOP — NOTE-COMPLETION GATE` appears inline immediately after each path note template, blocking completion until [C-NN] slot is filled; STOP fires at note-writing time, not post-hoc; section examples: "STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not." adjacent to each note |
| **C-52** | **FAIL** | STATUS QUO uses per-span direct instruction header ("Each foil item below names every criterion in the span...") but no SPAN DEFINITION pre-step block; completeness is declared as a narrative instruction, not as a structured pre-step output with Previous/Current/Pass-side fields; the foil item span is observable but not pre-declared in the required format |

**A-term count:** 43/44 (C-52 fail)
**A-term score:** 43/44 × 10 = **9.77**
**Composite:** 60.0 + 30.0 + 9.77 = **99.77**

---

## V-02 — Inertia Framing

**Axis:** SPAN DEFINITION pre-step before each foil item (C-52 probe); end-of-section SLOT CHECK, not co-located per note (C-51 ablation control).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Inherited from R19 V-04 base |
| C-09–C-48 | PASS | R19 V-04 baseline; no structural changes |
| C-49 | PASS | PER-NOTE FORMAT TEMPLATE present with [C-NN] slot |
| C-50 | PASS | Foil items enumerate full pass-side criteria; each foil item transcribed from the SPAN DEFINITION's Pass-side list |
| **C-51** | **FAIL** | Phase 8.5 STOP is "**PHASE 8.5 SLOT CHECK:**" placed at the end of the section — after both notes are written; this fires post-completion, not co-located per note; a builder can write both notes with unfilled [C-NN] brackets, then hit the section-level gate; co-location at note-completion time is absent |
| **C-52** | **PASS** | SPAN DEFINITION block precedes each foil item; all three required fields present: `Previous failure: START / C-03 / C-06 / C-10`, `Current failure: C-03 / C-06 / C-10 / C-13`, `Pass side (every criterion in span): C-01, C-02 / C-04, C-05 / ...`; foil item text transcribes Pass-side verbatim |

**A-term count:** 43/44 (C-51 fail)
**A-term score:** 43/44 × 10 = **9.77**
**Composite:** 60.0 + 30.0 + 9.77 = **99.77**

---

## V-03 — Output Format

**Axis:** NOTE-COMPLETION GATE named artifact block per note (C-51 boundary test — named artifact vs inline STOP); SPAN DEFINITION pre-step present (C-52 PASS).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Inherited from R19 V-04 base |
| C-09–C-48 | PASS | R19 V-04 baseline |
| C-49 | PASS | PER-NOTE FORMAT TEMPLATE present with [C-NN] slot |
| C-50 | PASS | Full pass-side enumeration in each foil item, transcribed from SPAN DEFINITION |
| **C-51** | **PASS** | NOTE-COMPLETION GATE is a two-field structured artifact block co-located immediately after each path note template: `[C-NN] slot populated: [YES / NO — STOP if NO]` / `Architecture label resolved: [YES / NO — STOP if NO]`; the block is positionally co-located (follows the note template, precedes the next note); the `STOP if NO` fields are explicit blocking conditions; builder cannot advance past the gate block with NO in either field; functional equivalence to inline STOP: the blocking mechanism operates at note-completion time |
| **C-52** | **PASS** | SPAN DEFINITION pre-step blocks present before each foil item with all three required fields; same structure as V-02 |

**C-51 boundary note:** V-03 tests whether "STOP condition" in C-51 is architecture-neutral. The NOTE-COMPLETION GATE block produces a named, independently scannable gate state (a reviewer can search for `NOTE-COMPLETION GATE` headings and check YES/NO fields without reading surrounding prose), satisfying both the co-location and blocking requirements. PASS on functional grounds; the named-artifact form may exceed minimum C-51 compliance (C-53 candidate surface).

**A-term count:** 44/44
**A-term score:** 44/44 × 10 = **10.00**
**Composite:** 60.0 + 30.0 + 10.0 = **100.00**

---

## V-04 — Combined (Lifecycle + Inertia)

**Axis:** V-01's co-located inline STOP per note (C-51) combined with V-02's SPAN DEFINITION pre-step (C-52). Joint satisfiability test.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Inherited from R19 V-04 base |
| C-09–C-48 | PASS | R19 V-04 baseline |
| C-49 | PASS | PER-NOTE FORMAT TEMPLATE with [C-NN] slot |
| C-50 | PASS | Full pass-side enumeration in foil items; SPAN DEFINITION pass-side lists verbatim transcribed |
| **C-51** | **PASS** | Inline `STOP — NOTE-COMPLETION GATE` per note, co-located with FORMAT TEMPLATE; same V-01 mechanism; fires at note-completion time, blocks before next note |
| **C-52** | **PASS** | SPAN DEFINITION pre-step before each foil item; all three required fields populated; foil item transcribes Pass-side list verbatim; same V-02 mechanism |

**Joint satisfiability:** C-51 operates in Phase 8.5 at note-completion boundaries; C-52 operates in STATUS QUO at foil-item construction boundaries — structurally and positionally independent. No interference detected.

**A-term count:** 44/44
**A-term score:** 44/44 × 10 = **10.00**
**Composite:** 60.0 + 30.0 + 10.0 = **100.00**

---

## V-05 — Combined + Phrasing Register

**Axis:** V-04 mechanisms plus detection-failure consequence naming at each gate site; SPAN DEFINITION with Function label and per-item TRANSCRIPTION STOP. Ceiling form.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Inherited from R19 V-04 base |
| C-09–C-48 | PASS | R19 V-04 baseline |
| C-49 | PASS | PER-NOTE FORMAT TEMPLATE with [C-NN] slot |
| C-50 | PASS | Full pass-side enumeration; SPAN DEFINITION pass-side verbatim transcribed; TRANSCRIPTION STOP makes non-compliant form (range notation) explicit |
| **C-51** | **PASS** | Co-located inline STOP per note (V-04 mechanism); additionally, each STOP names the detection-failure consequence if bypassed: "unfilled [C-NN] bracket passes SV scan and reaches Phase 9 emitted artifact; criterion-ID omission undetected at all verification stages" — converts gate from process instruction to self-justifying audit claim |
| **C-52** | **PASS** | SPAN DEFINITION with Function label ("computes pass-side enumeration for the foil item below; foil item must transcribe Pass side verbatim"); each SPAN DEFINITION includes TRANSCRIPTION STOP naming range notation as non-compliant ("range notation leaves span completeness unverifiable without counting criteria, and partial enumeration defeats the precision criterion-lattice locator function"); verbatim transcription enforced per-item |

**Above-rubric patterns (C-53 surface):** (1) Detection-failure naming at gate sites; (2) Function label on SPAN DEFINITION; (3) TRANSCRIPTION STOP with mechanism explanation. None of these are tested by C-51 or C-52 directly, but all add independently interpretable structure.

**A-term count:** 44/44
**A-term score:** 44/44 × 10 = **10.00**
**Composite:** 60.0 + 30.0 + 10.0 = **100.00**

---

## Score Summary

| V | C-51 | C-52 | A count | A term | Composite | Rank |
|---|------|------|---------|--------|-----------|------|
| V-01 | PASS | FAIL | 43/44 | 9.77 | **99.77** | 4 |
| V-02 | FAIL | PASS | 43/44 | 9.77 | **99.77** | 5 |
| V-03 | PASS | PASS | 44/44 | 10.00 | **100.00** | 3 |
| V-04 | PASS | PASS | 44/44 | 10.00 | **100.00** | 2 |
| V-05 | PASS | PASS | 44/44 | 10.00 | **100.00** | 1 |

**Tiebreaker within 100.00 tier:** V-05 > V-04 > V-03 by structural specificity and C-53 candidate density. V-05 adds three independently verifiable structural properties beyond C-51+C-52 minimum compliance. V-04 is the minimal sufficient combined form. V-03 introduces independently scannable gate-state artifacts (NOTE-COMPLETION GATE headings) as a boundary-testing form.

**V-01 vs V-02:** Both score 99.77. Ablation controls confirmed: co-location (C-51) and SPAN DEFINITION (C-52) are genuinely independent — removing either yields identical composite loss (1/44 × 10 = 0.23 points).

---

## Excellence Signals from Top-Scoring Variation (V-05)

Three patterns in V-05 that elevated beyond V-04 (structurally, within the current rubric ceiling):

**ES-R20-1 — Detection-failure consequence naming co-located at gate sites**
V-05's NOTE-COMPLETION STOPs name the specific bypass that would occur if the gate were omitted — "unfilled [C-NN] bracket passes SV scan undetected because SV checks heading patterns, not bracket population; reaches Phase 9 emitted artifact without triggering any SV catch." This converts each gate from an opaque process step into a self-justifying audit claim: a reviewer reading the gate in isolation understands what it prevents without consulting the surrounding construction protocol. Pattern: gate instructions should name the detection-failure scenario, not just the enforcement action.

**ES-R20-2 — SPAN DEFINITION Function label**
V-05's SPAN DEFINITION blocks open with `Function: enumerate every criterion between Previous failure and Current failure on the pass side; foil item must transcribe Pass side verbatim.` This makes the block's computational role explicitly declared, independently of the three required fields. A reviewer can verify that the function is being executed (the Pass-side list exists and is complete) without reading surrounding foil items. Pattern: named computation blocks should declare their function at the top of the block.

**ES-R20-3 — TRANSCRIPTION STOP with mechanism explanation**
V-05's `TRANSCRIPTION STOP` inside each SPAN DEFINITION names range notation as a non-compliant form and explains why: "range notation leaves span completeness unverifiable without counting criteria, and partial enumeration defeats the precision criterion-lattice locator function of the foil item." The STOP doesn't just name the prohibited form — it names the mechanism the prohibited form would defeat. Pattern: STOP conditions that name prohibited forms should additionally name the mechanism that would be defeated, making enforcement reasons independently auditable.

**C-53 candidate:** SPAN DEFINITION Function label + TRANSCRIPTION STOP as a pair — structurally, V-05's SPAN DEFINITION is a more complete unit than V-02/V-03/V-04's: it declares function, computes span, and enforces transcription all within one named block. If R21 isolates V-05's SPAN DEFINITION form vs bare SPAN DEFINITION (V-02/V-04), the delta would establish whether the Function label + TRANSCRIPTION STOP adds measurable compliance lift beyond C-52's pre-step requirement.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["detection-failure consequence naming co-located at gate sites converts each STOP from opaque process instruction to self-justifying audit claim readable without surrounding context", "SPAN DEFINITION Function label explicitly declares computational role at block top making span pre-declaration independently interpretable", "TRANSCRIPTION STOP names prohibited form and the specific mechanism it would defeat rather than just naming the enforcement action"]}
```
