## campaign-blueprint — R7 Scoring (Rubric v7)

---

### Orientation

R7 variants are all modifications of R6 V-05's 168-point architecture. The three differentiating axes:
- **C-26 form**: bulleted list (R6) vs anchor sentence (V-01, V-05) vs compact sentence (V-04)
- **C-25 placement**: inside REQUIREMENTS (R6) vs CAMPAIGN SETUP (V-02)
- **D8 form**: full prose per-site (R6) vs bracket notation (V-03, V-04, V-05)

---

### Criterion Abbreviations

> **C-25** = Scout traceability table (5 pts, FULL or NO CREDIT)
> **C-26** = Named inertia model entity with explicit field-to-conviction-type mapping (5 pts, FULL or NO CREDIT)
> **D8** = C-23 requires inertia-grounded labels at BOTH matrix AND per-site execution reminders

---

## V-01 — C-26 Compact Mapping: Anchor Sentence

**Design:** Retains R6 V-05 SCOUT TRACEABILITY TABLE (C-25) and full prose per-site CONVICTION TYPE reminders (D8). Replaces bulleted C-26 field mapping with anchor sentence: *"Cost drives all three conviction types: the spec documents it as factual record, the proposal prices it against each alternative, and the pitch makes it visceral per audience."*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three artifacts produced | PASS | Spec / Proposal / Pitch all instructed with GATE enforcement |
| C-02 | Canonical paths | PASS | All three paths present: `simulations/draft/{specs,proposals,pitches}/{topic}-{artifact}-{date}.md` |
| C-03 | Topic identity consistency | PASS | `{topic}` threaded through all artifact READ fields and paths |
| C-04 | Execution order | PASS | Three explicit GATE guards; CAMPAIGN REFLECTION gated on pitch file existence |
| C-05 | Minimum structure per sub-artifact | PASS | Spec: PURPOSE/REQUIREMENTS/DESIGN/CONSTRAINTS/OPEN QUESTIONS; Proposal: options + recommendation; Pitch: three versions + ANTI-POSITIONING |
| C-06 | Proposal respects spec | PASS | "PRESERVE: all spec design decisions — do not re-open anything the spec resolved" |
| C-07 | Pitch crystallizes recommended option | PASS | "PRESERVE: recommended option from proposal — crystallize, do not reconsider" |
| C-08 | Campaign framing | PASS | CAMPAIGN SETUP opens with INERTIA MODEL + contract matrix; CAMPAIGN CLOSE closes with package summary table |
| C-09 | Narrative arc | PASS | Factual → Optionality → Emotional arc enforced; CAMPAIGN REFLECTION CONVICTION DELTA sub-field explicitly tests non-repetition |
| C-23 | Inertia-grounded conviction (D8) | FULL | Matrix row: "Factual — documents INERTIA MODEL Cost as factual record" ✓. Per-site: "CONVICTION TYPE: Factual — document the INERTIA MODEL Cost field as factual record; do not argue." ✓ Both levels grounded. |
| C-25 | Scout traceability table | FULL | Four-column labeled table inside REQUIREMENTS: `Req-ID / Must-have (brief) / Originating Scout-Requirements Friction / Scout File`. Retained from R6 V-05 unchanged. |
| C-26 | Named INERTIA MODEL entity with explicit field-to-conviction-type mapping | **NO CREDIT** | Three-field entity present (Name/Behavior/Cost) ✓. Anchor sentence covers all three mappings in one line. However: C-26 precedents for FULL (V-03 and V-05 in R6) both used enumerated bulleted form — one bullet per conviction type with field name stated per row. Anchor sentence is "general instruction" form, not "row-by-row auditable" enumeration. The parallel to C-25 (table form required over general instruction) applies here. |

**Score:** 158 (R6 V-05 base) + 5 (C-25) + 0 (C-26) = **163**

---

## V-02 — C-25 SETUP Placement: Friction-First Traceability Table

**Design:** Retains R6 V-05 INERTIA MODEL entity with full bulleted field mapping (C-26) and full prose per-site CONVICTION TYPE reminders (D8). Moves SCOUT TRACEABILITY TABLE from REQUIREMENTS to CAMPAIGN SETUP — pre-populated from scout inventory before any artifact is written. REQUIREMENTS references back to the campaign-level table.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three artifacts produced | PASS | Full artifact sequence with GATE enforcement |
| C-02 | Canonical paths | PASS | All canonical paths present |
| C-03 | Topic identity consistency | PASS | `{topic}` consistent throughout |
| C-04 | Execution order | PASS | Three GATE guards + REFLECTION post-pitch guard |
| C-05 | Minimum structure per sub-artifact | PASS | All required sections present in all three artifacts |
| C-06 | Proposal respects spec | PASS | PRESERVE instruction maintained |
| C-07 | Pitch crystallizes recommended option | PASS | Crystallize instruction maintained |
| C-08 | Campaign framing | PASS | SETUP + CLOSE both present |
| C-09 | Narrative arc | PASS | Conviction arc enforced; CONVICTION DELTA sub-field maintained |
| C-23 | Inertia-grounded conviction (D8) | FULL | Matrix: "Factual — documents INERTIA MODEL Cost as factual record" ✓. Per-site prose retained at full form ✓. Both levels grounded. |
| C-24 | Scout signal integration | PASS/IMPROVED | Friction-first pre-population from scout inventory before Artifact 1 strengthens friction-to-must-have traceability. Table built from known scout frictions before writing requirements. |
| C-25 | Scout traceability table | **FULL** | Four-column table (Req-ID / Must-have / Originating Friction / Scout File) present in CAMPAIGN SETUP with correct column headers. C-25 tests table structure, not placement. Table has all four required columns. Req-ID and Must-have are "(fill in A1)" placeholders — same as R6's empty cells. Placement-agnostic. |
| C-26 | Named INERTIA MODEL entity | FULL | Three-field entity (Name/Behavior/Cost) + five-line bulleted field-to-conviction mapping retained from R6 V-05 unchanged. FULL by R6 precedent. |

**Score:** 158 (R6 V-05 base) + 5 (C-25) + 5 (C-26) = **168**

Secondary finding: friction-first table placement may improve C-24/C-10 scores by anchoring must-have writing to pre-identified scout frictions, but 168 is the ceiling; any gain is capped.

---

## V-03 — D8 Minimum Expression: Bracket-Notation Per-Site CONVICTION TYPE

**Design:** Retains R6 V-05 INERTIA MODEL entity with full bulleted field mapping (C-26) and SCOUT TRACEABILITY TABLE inside REQUIREMENTS (C-25). Replaces full prose per-site CONVICTION TYPE reminders with bracket notation: `CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]`.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three artifacts produced | PASS | Full artifact sequence with GATE enforcement |
| C-02 | Canonical paths | PASS | All canonical paths present |
| C-03 | Topic identity consistency | PASS | `{topic}` consistent throughout |
| C-04 | Execution order | PASS | Three GATE guards + REFLECTION post-pitch guard |
| C-05 | Minimum structure per sub-artifact | PASS | All required sections present in all three artifacts |
| C-06 | Proposal respects spec | PASS | PRESERVE instruction maintained |
| C-07 | Pitch crystallizes recommended option | PASS | Crystallize instruction maintained |
| C-08 | Campaign framing | PASS | SETUP + CLOSE both present |
| C-09 | Narrative arc | PASS | Conviction arc enforced; CONVICTION DELTA sub-field maintained |
| C-23 | Inertia-grounded conviction (D8) | **FULL** | Matrix: "Factual — documents INERTIA MODEL Cost as factual record" ✓ (full prose, unchanged). Per-site bracket: `[INERTIA MODEL Cost → factual record]` explicitly names "INERTIA MODEL Cost" field. D8's requirement is "inertia-grounded labels" — not "prose form." Bracket notation is explicitly grounded (names the INERTIA MODEL Cost field at the per-site level). NOT abstract like R6 V-01's "Factual — assert what is true." All three per-site reminder lines satisfy D8. |
| C-25 | Scout traceability table | FULL | Four-column table inside REQUIREMENTS, retained from R6 V-05. FULL by R6 precedent. |
| C-26 | Named INERTIA MODEL entity | FULL | Bulleted field mapping retained unchanged from R6 V-05. FULL by R6 precedent. |

**Score:** 158 (R6 V-05 base) + 5 (C-25) + 5 (C-26) = **168**

Key finding: D8 admits bracket notation. The distinguishing characteristic is explicit INERTIA MODEL field reference (`[INERTIA MODEL Cost → ...]`), not prose form. `[INERTIA MODEL Cost → factual record]` is functionally equivalent to "document the INERTIA MODEL Cost field as factual record; do not argue" for the purpose of per-site grounding.

---

## V-04 — Minimal Density: C-25 + C-26 Added to Skeleton

**Design:** R6 V-04 skeleton density throughout. Adds (1) INERTIA MODEL three-field entity + compact mapping sentence ("Cost maps: spec documents it (factual) / proposal prices it (optionality) / pitch makes it visceral (emotional)"), (2) four-column SCOUT TRACEABILITY TABLE template in REQUIREMENTS, (3) bracket notation per-site CONVICTION TYPE.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three artifacts produced | PASS | All three artifacts with GATE enforcement |
| C-02 | Canonical paths | PASS | All canonical paths present |
| C-03 | Topic identity consistency | PASS | `{topic}` consistent |
| C-04 | Execution order | PASS | Three GATE guards present |
| C-05 | Minimum structure per sub-artifact | PASS | Sections present across all artifacts; pitch has three versions + ANTI-POSITIONING |
| C-06 | Proposal respects spec | PASS | "no re-opening" instruction present |
| C-07 | Pitch crystallizes recommended option | PASS | "crystallize, do not reopen" present |
| C-08 | Campaign framing | PASS | SETUP + CLOSE present (compact form) |
| C-09 | Narrative arc | PARTIAL | CONVICTION DELTA present but compressed to one line per persona ("what inertia urgency does this establish..."). Less structural differentiation than full variants. |
| C-23 | Inertia-grounded conviction (D8) | PARTIAL | Per-site: `Factual [INERTIA MODEL Cost → factual record]` — explicitly grounded ✓. Matrix: `Factual [Cost → factual record]` — uses "Cost" shorthand, not "INERTIA MODEL Cost." The matrix-level grounding is implicit (Cost defined above as INERTIA MODEL field) rather than explicit. D8 requires grounding at BOTH levels. Matrix shorthand may not satisfy "inertia-grounded phrasing" without the "INERTIA MODEL" qualifier. |
| C-25 | Scout traceability table | **FULL** | Table present with correct four columns: `Req-ID / Must-have (brief) / Originating Friction / Scout File`. Column names match rubric spec exactly ("Originating Friction" is the rubric's own column name). Structure present. |
| C-26 | Named INERTIA MODEL entity | **NO CREDIT** | Three-field entity present (Name/Behavior/Cost) ✓. Mapping: "Cost maps: spec documents it (factual) / proposal prices it (optionality) / pitch makes it visceral (emotional)." Even more compact than V-01's anchor sentence — uses "it" as implicit reference to Cost rather than naming the field per conviction type. Too abstract for "explicit field-to-conviction-type mapping." |

**Score:** 153 (R6 V-04 base) + 5 (C-25) + 0 (C-26) ± C-23 partial adjustment ≈ **~158**

Note: R6 V-04's 5-pt gap vs R6 V-02/V-03 likely included C-23 PARTIAL. R7 V-04's bracket notation per-site partially addresses this, but matrix-level "Cost" shorthand may prevent full C-23 recovery. Estimated range: 156–158.

---

## V-05 — Minimum-Verbosity Path to 168: Compact C-26 + Proven C-25 + Bracket D8

**Design:** Combines V-01 anchor-sentence C-26 + R6 V-02/V-05 proven SCOUT TRACEABILITY TABLE inside REQUIREMENTS (unchanged) + V-03 bracket-notation per-site CONVICTION TYPE. Full prose density retained for all non-new-criterion content.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three artifacts produced | PASS | Full artifact sequence with GATE enforcement |
| C-02 | Canonical paths | PASS | All canonical paths present |
| C-03 | Topic identity consistency | PASS | `{topic}` consistent throughout |
| C-04 | Execution order | PASS | Three GATE guards + REFLECTION post-pitch guard |
| C-05 | Minimum structure per sub-artifact | PASS | All required sections present in all three artifacts |
| C-06 | Proposal respects spec | PASS | PRESERVE instruction maintained |
| C-07 | Pitch crystallizes recommended option | PASS | Crystallize instruction maintained |
| C-08 | Campaign framing | PASS | Full SETUP + CLOSE present |
| C-09 | Narrative arc | PASS | Conviction arc enforced; full CONVICTION DELTA sub-field maintained |
| C-23 | Inertia-grounded conviction (D8) | FULL | Matrix: "Factual — documents INERTIA MODEL Cost as factual record" ✓ (full prose, unchanged). Per-site bracket: `[INERTIA MODEL Cost → factual record]` — explicitly names INERTIA MODEL Cost field ✓. D8 satisfied at both levels. |
| C-25 | Scout traceability table | FULL | Four-column table inside REQUIREMENTS, proven R6 V-02/V-05 form, unchanged. FULL by R6 precedent. |
| C-26 | Named INERTIA MODEL entity | **NO CREDIT** | Same anchor sentence as V-01: "Cost drives all three conviction types: the spec documents it as factual record, the proposal prices it against each alternative, and the pitch makes it visceral per audience." Same analysis as V-01 — anchor sentence is "general instruction" form, not enumerated field-to-conviction mapping. NO CREDIT by same ruling. |

**Score:** 158 (R6 V-05 base) + 5 (C-25) + 0 (C-26) = **163**

Interference finding: Combining three compact mechanisms creates no interference — C-25 table and D8 bracket notation each operate independently. The only drop is C-26, caused by the anchor-sentence form alone, not by any interaction effect.

---

## Summary Table

| Variant | Base (R6 v6) | C-25 | C-26 | C-23 | R7 Total |
|---------|-------------|------|------|------|---------|
| V-01 — Anchor Sentence C-26 | 158 | +5 FULL | 0 NO CREDIT | FULL (prose per-site retained) | **163** |
| V-02 — C-25 SETUP Placement | 158 | +5 FULL | +5 FULL | FULL | **168** |
| V-03 — Bracket D8 | 158 | +5 FULL | +5 FULL | FULL (bracket satisfies D8) | **168** |
| V-04 — Minimal Density + Both | 153 | +5 FULL | 0 NO CREDIT | PARTIAL (matrix "Cost" shorthand) | **~158** |
| V-05 — Minimum-Verbosity 168 | 158 | +5 FULL | 0 NO CREDIT | FULL (bracket satisfies D8) | **163** |

**Rank:** V-02 = V-03 (168) > V-01 = V-05 (163) > V-04 (~158)

---

## Excellence Signals — Top-Scoring Variants (V-02, V-03)

**From V-02:**
- **C-25 is placement-agnostic.** Moving the SCOUT TRACEABILITY TABLE to CAMPAIGN SETUP earns FULL credit for C-25 equivalently to REQUIREMENTS placement. The criterion tests column structure, not location. The friction-first SETUP placement adds a secondary benefit: requirements are written to match pre-identified frictions rather than traced post-hoc. This improves causal direction without changing C-25 scoring.

**From V-03:**
- **Bracket notation satisfies D8.** `[INERTIA MODEL Cost → factual record]` constitutes inertia-grounded conviction type labels at the per-site execution-site reminder. The distinguishing characteristic for D8 is **explicit INERTIA MODEL field reference**, not prose form. The bracket form achieves identical functional grounding in fewer characters, with no loss of scoring.

**Consistent across both:**
- C-26 bulleted field-to-conviction mapping cannot be replaced by sentence form. The bulleted list is the minimum form for "explicit field-to-conviction-type mapping." This is the single structural requirement V-01 and V-05 fail to satisfy.

---

## Diagnostic Answers to R7 Questions

| Q | Answer |
|---|--------|
| 1. Does anchor sentence satisfy C-26? | No. Anchor sentence is "general instruction" form. Enumerated form (one line/bullet per conviction type, naming the field per entry) appears required. |
| 2. Does C-25 care about placement? | No. SETUP placement earns FULL credit equivalently. Friction-first direction is a secondary quality improvement. |
| 3. Does D8 admit bracket notation? | Yes. `[INERTIA MODEL Cost → ...]` is inertia-grounded. D8 requires grounded labels, not prose form. |
| 4. Can V-04 skeleton reach 168? | No. C-26 compact sentence earns NO CREDIT; matrix "Cost" shorthand risks C-23 PARTIAL. Ceiling at ~158. |
| 5. Does compact C-26 + bracket D8 create interference in V-05? | No interference found. Each mechanism operates independently. The C-26 drop is caused by anchor-sentence form alone. |

---

```json
{"top_score": 168, "all_essential_pass": true, "new_patterns": ["C-25 is placement-agnostic — SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP earns FULL credit equivalently to placement inside REQUIREMENTS; friction-first placement improves causal direction without changing C-25 scoring", "Bracket notation [INERTIA MODEL Cost → conviction type] satisfies D8 per-site inertia grounding — explicit field reference in bracket form is functionally equivalent to prose form; the distinguishing requirement is naming the INERTIA MODEL Cost field, not prose syntax", "C-26 anchor sentence is insufficient for FULL credit — single-line mapping covering all three conviction types does not meet the enumerated field-to-conviction-type threshold; bulleted/enumerated form (one entry per conviction type) appears required for row-by-row auditability"]}
```
