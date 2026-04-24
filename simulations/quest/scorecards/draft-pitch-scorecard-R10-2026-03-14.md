## draft-pitch — Round 10 Scorecard

**Ranking (all Golden band):**

| Rank | Variation | Score | New criteria | Regressions |
|------|-----------|-------|--------------|-------------|
| 1 | V-01 | **99.4** | C-41 PASS | None |
| 2 | V-05 | **99.2** | C-41+C-42+C-43 PASS | C-25+C-26+C-27 FAIL |
| 3 | V-04 | **98.9** | C-41+C-42 PASS | C-25+C-26+C-27 FAIL |
| 4 | V-02 | **98.6** | C-42 PASS | C-25+C-26+C-27+C-41+C-43 FAIL |
| 4 | V-03 | **98.6** | C-43 PASS | C-25+C-26+C-27+C-41+C-42 FAIL |

**The R10 structural paradox**: V-05 (the intended golden candidate) gains C-41+C-42+C-43 but loses C-25+C-26+C-27 by stripping the BINDING DECLARATION — a net zero. V-01 gains only C-41 but preserves everything, netting +1.

**Key finding**: V-02 through V-05 all use a stripped BINDING DECLARATION that drops the C-25/C-26/C-27 text present in V-01. These three criteria — exhaustiveness closure, access prohibition, meta-purpose auditability statement — were R5/R6 achievements. The stripping is not intentional regression; it's isolation-probe simplification. But it scores as regression.

**R11 target**: One synthesis variation — V-01's full Phase 2 BINDING DECLARATION + V-05's Phase 5 changes. Expected score: **100.0** (36/36 aspirationals).

```json
{"top_score": 99.4, "all_essential_pass": true, "new_patterns": ["Declaration-site colocation is compound not sequential: both pattern citation and auditability intent must appear in the PHASE 5 STRUCTURE heading line itself — body sentences immediately following are inside the block not at the declaration site", "Targeted variation scoping preserves prior-phase precision: changing only Phase 5 header while leaving Phase 2 BINDING DECLARATION intact nets higher score than closing three new criteria while stripping three established ones — minimum change zero regression beats maximum change with regression"]}
```
A inertia references." The meta-purpose auditability statement (C-27), exhaustiveness closure (C-25), and access prohibition (C-26) are all absent.

All other inherited criteria (C-01 through C-24, C-28 through C-40) PASS across all five variations.

---

### C-41 — Phase structure block cites prior pattern + declares auditability at declaration site

Pass condition: PHASE 5 STRUCTURE heading must contain BOTH (a) explicit citation of the prior-phase pattern by name and (b) an explicit auditability intent statement — both at the heading (the declaration site), not distributed across the block body.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Heading: "applies the Phase 2 **BINDING DECLARATION** pattern at the phase level; Phase 5 is auditable from skill structure alone" — both elements in the heading line. |
| V-02 | FAIL | Heading: "(read before any drafting step):" only. Pattern citation in first body sentence; auditability declaration at end of block, 8+ lines later. Not at declaration site. |
| V-03 | FAIL | Same PHASE 5 STRUCTURE heading as V-02. C-41: FAIL. |
| V-04 | PASS | Heading identical to V-01: "applies the Phase 2 **BINDING DECLARATION** pattern at the phase level; Phase 5 is auditable from skill structure alone." |
| V-05 | PASS | Heading identical to V-01/V-04. Both elements at declaration site. |

---

### C-42 — Draft-order integrity scope names all prior-phase locked outputs by canonical identifier

Pass condition: The draft-order integrity statement must name all prior-phase locked outputs by their canonical identifiers (AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE), not by phase number.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | "does not change any locked output from Phases 2, 3, or 4" — set-scope form (C-39 passes) but uses phase numbers, not canonical names. |
| V-02 | PASS | "does not change **AUDIENCE BELIEF MAP** [Phase 2 locked output], **POSITIONING LOCK** [Phase 3 locked output], or **EXEC OPENING SENTENCE** [Phase 4 locked output]. All three prior-phase locked outputs are unaffected by draft order." |
| V-03 | FAIL | "does not change any locked output from Phases 2, 3, or 4" — phase numbers. |
| V-04 | PASS | Same canonical-name enumeration as V-02. All three named explicitly. |
| V-05 | PASS | Same canonical-name enumeration as V-02/V-04. |

---

### C-43 — Gate YES/NO questions carry inline advisory citations using exact canonical names

Pass condition: Each gate question carries an inline citation naming the source advisory using its EXACT canonical text as it appears in the skill body. Descriptive phrases or paraphrases fail. All three questions must cite.

R9 V-05 form (carried into V-01, V-02, V-04): descriptive phrases.
V-03 and V-05: exact verbatim advisory text.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | Q1: "Enforces Core Belief distinctness advisory in Phase 2 Core Belief column definition." Q2: "zero-acronym advisory in Maker Version Hook and Why-It-Matters instructions." Q3: "scenario-hook advisory in Dev Version Hook instruction." All descriptive phrases. |
| V-02 | FAIL | Same descriptive-phrase citations as V-01. |
| V-03 | PASS | Q1 cites verbatim: "Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience." Q2: "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology." Q3: "A scenario the developer is in right now -- the moment before Signal changes what happens next." All three cite exact instruction text at the cite site. |
| V-04 | FAIL | Same descriptive-phrase citations as V-01/V-02. |
| V-05 | PASS | Same exact-text citations as V-03. All three gate questions cite verbatim advisory text. |

---

### Per-Variation Aspirational Summary (C-08 through C-43, denominator 36)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 through C-24 (17 criteria) | PASS | PASS | PASS | PASS | PASS |
| C-25 Exhaustiveness closure | PASS | FAIL | FAIL | FAIL | FAIL |
| C-26 Downstream access prohibition | PASS | FAIL | FAIL | FAIL | FAIL |
| C-27 Meta-purpose auditability statement | PASS | FAIL | FAIL | FAIL | FAIL |
| C-28 through C-40 (13 criteria) | PASS | PASS | PASS | PASS | PASS |
| C-41 Phase structure cites + declares at site | PASS | FAIL | FAIL | PASS | PASS |
| C-42 Integrity scope names canonical set | FAIL | PASS | FAIL | PASS | PASS |
| C-43 Gate cites exact canonical names | FAIL | FAIL | PASS | FAIL | PASS |
| **Aspirational pass count** | **34/36** | **31/36** | **31/36** | **32/36** | **33/36** |

Failures by variation:
- V-01: C-42, C-43 (2 failures)
- V-02: C-25, C-26, C-27, C-41, C-43 (5 failures)
- V-03: C-25, C-26, C-27, C-41, C-42 (5 failures)
- V-04: C-25, C-26, C-27, C-43 (4 failures)
- V-05: C-25, C-26, C-27 (3 failures)

---

### Scores

```
Score = (essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/36)*10
```

All variations: essential 4/4 = 60.0, recommended 3/3 = 30.0.

| Rank | Variation | Aspirational | Total |
|------|-----------|--------------|-------|
| 1 | V-01 | (34/36)*10 = 9.44 | **99.4** |
| 2 | V-05 | (33/36)*10 = 9.17 | **99.2** |
| 3 | V-04 | (32/36)*10 = 8.89 | **98.9** |
| 4 | V-02 | (31/36)*10 = 8.61 | **98.6** |
| 4 | V-03 | (31/36)*10 = 8.61 | **98.6** |

Band: All variations Golden (all essential pass, score >= 80).

---

### Excellence Signals (from V-01, top scorer)

**E-01: Declaration-site colocation is compound, not sequential.**

V-01 puts both the pattern citation ("applies the Phase 2 BINDING DECLARATION pattern at the phase level") and the auditability declaration ("Phase 5 is auditable from skill structure alone") in the PHASE 5 STRUCTURE heading. A reader verifies both claims at the heading line without entering the block body. V-02 and V-03 distribute these claims: pattern citation in the first body sentence, auditability at the end of the block. C-41's "at the declaration site" means the heading itself — body sentences immediately following are inside the block, not at the declaration site.

**E-02: Targeted variation scoping preserves prior-phase precision text.**

V-01's scope is Phase 5 header only. Because Phase 2 is unchanged, it retains the full C-25/C-26/C-27 BINDING DECLARATION text. V-02 through V-05 all strip the binding declaration to a table + authority statement. Each gains one or two new criteria but drops three previously-established ones. V-01 nets the highest score by changing the minimum: one heading line, zero regressions.

R10 structural paradox: V-05 closes C-41+C-42+C-43 (gain 3) but loses C-25+C-26+C-27 (lose 3), netting zero aspirational improvement over R9 V-05. V-01 closes C-41 only (gain 1) and loses nothing, netting +1. The true R11 golden must carry both sides simultaneously.

---

### R10 Structural Finding

V-05 is the intended golden candidate (closes C-41 + C-42 + C-43) but introduces regression on C-25 + C-26 + C-27 via a stripped BINDING DECLARATION. A true R10 golden requires synthesizing:

- V-01's Phase 2 BINDING DECLARATION (C-25 + C-26 + C-27 text preserved in full)
- V-05's PHASE 5 STRUCTURE heading (C-41)
- V-05's draft-order integrity canonical-name enumeration (C-42)
- V-05's gate exact-text citations (C-43)

That synthesis would pass 36/36 aspirationals and score 100.0.

The parallel: just as R5/R6 required C-25/C-26/C-27 to fully mature the BINDING DECLARATION, R10 requires those same criteria to remain intact while adding the Phase 5 structural analogs (C-41/C-42/C-43). A stripped binding declaration paired with a Phase 5 declaration with full precision is structurally inconsistent — the standard applied at Phase 2 does not match the standard applied at Phase 5.

---

### Next Round Setup

R11 target: one variation. Full Phase 2 BINDING DECLARATION (V-01 text, no stripping) + Phase 5 STRUCTURE heading with compound declaration (V-05 heading) + canonical draft-order integrity (V-05) + exact gate citations (V-05). No stripped sections.

R11 aspirational denominator: **36** (no new criteria needed — the gap is synthesis fidelity, not discovery).

Expected top score if synthesis is correct: **100.0**.
