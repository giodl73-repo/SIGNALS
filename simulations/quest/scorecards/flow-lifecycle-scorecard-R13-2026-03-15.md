PASS ("certified Handler R-ID" in Gate D).

**V-04 divergences:**

| ID | Result | Note |
|----|--------|------|
| C-25 | **PARTIAL** | Gate: "it produces a lifecycle trace containing at least one defect named in the Defect Type column" — pointer only, no inline enumeration |
| C-27 | **PARTIAL** | Taxonomy referenced by pointer; gate doesn't enumerate |
| C-35 | **PARTIAL** | Non-overlapping mandate by pointer |
| C-37 | **PARTIAL** | D-04/D-05 by pointer |
| C-38 | **PARTIAL** | Detected By column by pointer |
| C-41 | **PARTIAL** | "Group A / B / C" named but not written as labeled section headers |

**V-04 Score: 42/45 = 93.3%**

---

### V-05 — Full v13 Floor

New v13: C-42 PASS, C-43 PASS, C-44 PASS (eligibility conditions in imperative instruction paragraphs at point of use — same pattern as V-02, which passed), C-45 PASS.

Coverage Scan explicitly written (AC-01–AC-21 all present). Defect Type Taxonomy D-01–D-08 present with Detected By column. Production Gate enumerates inline: "(an unterminated path, an uncertified exception handler, a missing Initial Phase field, unlabeled pre-schema blocks, a generic escape code in a downstream trace column, or a decision condition without both mechanisms)."

| ID | Result | Note |
|----|--------|------|
| C-25 | **PASS** | Inline enumeration of defects including v13-specific types |
| C-27 | **PASS** | Gate references "Defect Type column above" by name; taxonomy explicitly present |
| C-35 | **PASS** | "no cell may share the same coverage claim across rows" in Group B header |
| C-37 | **PASS** | D-04 / D-05 both present as distinct rows |
| C-38 | **PASS** | Detected By column present |
| C-41 | **PASS** | Group A / B / C as explicit section headers |

**V-05 Score: 45/45 = 100%**

---

### Composite Score Summary

| Variation | Score | PARTIALs | Notes |
|-----------|-------|----------|-------|
| V-01 | **100%** | 0 | Inline column-header enforcement; full scan explicit |
| V-02 | **98.9%** | 1 (C-25) | Scan explicit; gate causal mechanism by pointer |
| V-03 | **93.3%** | 6 (C-27,C-35,C-37,C-38,C-41,C-44) | Scan and taxonomy by pointer; DERIVED eligibility absent |
| V-04 | **93.3%** | 6 (C-25,C-27,C-35,C-37,C-38,C-41) | Scan by pointer; gate enumeration absent |
| V-05 | **100%** | 0 | Full floor + inertia framing; all scan infrastructure explicit |

**Rank: V-01 = V-05 > V-02 > V-03 = V-04**

All essential criteria (C-01–C-05) PASS for all five variations.

---

### Excellence Signals (from V-01 / V-05)

1. **Full eligibility conditions embedded in column headers** — not just the code name ("SECONDARY:[rationale]") but the complete trigger condition ("if role exists outside all LT scopes, write SECONDARY:[rationale naming why this role exists without any LT anchor]"). This makes the authorship decision visible at the exact cell where it must be made, converting a semantic omission into a scannable blank.

2. **Production Gate enumerates specific structural defect types inline** — naming "an unterminated path, an uncertified exception handler, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape code" in the gate sentence itself. Pointer references to the defect taxonomy satisfy C-27 (the taxonomy exists and is named) but not C-25 (the causal explanation must be inline).

3. **Coverage Scan written out explicitly** — V-03 and V-04 reference the scan by pointer ("same Group A / B / C structure as V-01"), which satisfies intent but makes C-35 (non-overlapping mandate), C-37 (dual-mechanism defect entries), C-38 (Detected By column), and C-41 (semantic group headers) unverifiable inline.

4. **V-05 dual-column pressure pattern** — pairing DERIVED:rationale with a Status-Quo Gap column forces an author to explain both the LT combination logic *and* the incumbent failure simultaneously. A generic fill on one column exposes the incompleteness of the other. Structurally harder to satisfy vacuously than a single-column constraint.

---

### New Patterns (V-05, not yet captured as rubric criteria)

1. **Pre-schema incumbent-process anchoring** — the STATUS-QUO PROCESS DECLARATION block establishes a named comparison reference (incumbent name, failure modes FM-1/FM-2/FM-3, inertia driver) before STEP 0A. All downstream comparison columns (Status-Quo Gap, Incumbent Delta, As-Is Detection?, Incumbent Workaround) trace back to this declaration. The comparison chain is a traceable reference structure, not decorative commentary.

2. **Inertia-framing as structural pressure on escape codes** — when the Phase Index Entry Trigger carries both DERIVED:rationale *and* a Status-Quo Gap column, an author who writes a vague DERIVED:rationale must simultaneously explain the status-quo gap. The two columns audit each other: a phase whose DERIVED:rationale is generic ("combination of triggers") will also have a vague Status-Quo Gap unless the author understands the domain. This is a coverage mechanism that increases escape-code specificity without adding a new gate.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-schema incumbent-process anchoring: STATUS-QUO PROCESS DECLARATION before STEP 0A names incumbent failure modes and inertia driver, creating a traceable reference chain that all downstream comparison columns (Status-Quo Gap, Incumbent Delta, As-Is Detection) must be consistent with", "Dual-column structural pressure on escape codes: pairing DERIVED:rationale with a Status-Quo Gap column in the Phase Index forces the author to explain both LT combination logic and the incumbent failure simultaneously, making generic fills structurally implausible because both columns would need to be vague at once"]}
```
