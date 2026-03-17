Good. Now the full report:

---

## Simplified Prompt Body

Written to `simulations/quest/golden/program-plan-variate-R20-QU5-simplified-2026-03-16.md`.

---

## What Was Removed and Why

| # | Removed | Why (doing no work) |
|---|---------|---------------------|
| 1 | "Failure mode to prevent: catalog-first construction..." paragraph (25 words) | Aspirational teaching context; the CONSTRUCTION ORDER's "catalog closed until Step 3" instruction enforces the same constraint |
| 2 | Three-class information table: Zone membership / Artifact provenance / Investigative intent (70 words) | Supports aspirational criteria ladders only (Arc-structure ladder, Gate-behavior ladder, Question-framing ladder); no essential criterion depends on it |
| 3 | "Each of these formats is individually disqualified -- content completeness does not compensate for format non-compliance." (25 words) | The MUST language and explicit Forbidden formats list already establish disqualification; this sentence restates it |
| 4 | "Read all steps before beginning Step 1." (10 words) | CONSTRUCTION ORDER is a numbered list; the instruction to read it first is implicit in its presentation |
| 5 | "Do not proceed to Step 3 until Step 2 SELF-VERIFY passes." (15 words) | Redundant: the SELF-VERIFY mechanism at the end of Step 2 already blocks progression |
| 6 | Step 1 second sentence: "All artifact names, phase groupings, and gate artifact types must be coherent with this specific topic." (18 words) | Aspirational elaboration; the SELF-VERIFY IS clause ("a specific topic name stated that will anchor all subsequent artifact naming") covers the intent concisely |
| 7 | Opening sentence compression: "its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair" → "all Produces/Consumes derivation runs backward from echo" (saves ~13 words) | Long causal chain description; the compressed form states the same fact with half the words |
| 8 | ARTIFACT 1: "Produce ARTIFACT 1 -- Band Taxonomy Table: Band ID | Namespaces | Zone | Gap class | Owner role" (20 words) | Aspirational intermediate artifact; no essential criterion requires this output |
| 9 | Step 2 SELF-VERIFY: 3 NOT items compressed into 1 NOT ("namespace label, cluster, or generic identifier" with examples) (saves ~20 words) | Three separate NOT lines all prohibited the same category of bad phase names; one line enumerates all three sub-types |
| 10 | Step 4 second NOT: "NOT: skills placed in phases solely by namespace proximity rather than investigation match" (16 words) | The first NOT ("new phases created") and IS ("every skill maps to a declared phase from Step 2") together define the boundary; proximity mis-assignment is covered by the IS rule |
| 11 | CORRECTION TABLE: 17 rows → 12 rows (removes 2 duplicate C-04, 2 duplicate C-03, 1 duplicate C-02 examples) (saves ~75 words) | Each criterion only needs 1-2 contrasting examples; 3 near-identical gate or skill examples teach nothing the first example didn't |
| 12 | Step 10 C-55 through C-59 multi-line parenthetical explanations (saves ~55 words) | The YES annotation on each item is sufficient; the parenthetical restatements duplicate the protocol section declarations already in the prompt |
| 13 | BAD PLAN body mandate echo lines ("# Mandate (C-06): IS investigation-intent -- NOT: namespace label (violated above)") (saves ~30 words) | C-59 is fully satisfied by the Step 8 YAML template field saturation; the BAD PLAN echoes are belt-and-suspenders for an aspirational criterion already covered |
| 14 | Component 2 and 3 descriptions compressed (saves ~20 words) | "Wrong YAML with criterion tags at every violating field line" is the complete rule; the prior verbose form adds no testable precision |
| 15 | Navigation contract final sentence: "Each Component 1 table row carries 'BOUNDED BLOCK PROTOCOL decl. above' in column 4." (18 words) | This fact is visible directly in the BAD PLAN's C1 table Column 4 cells; stating it in the navigation contract is redundant |
| 16 | FIELD CO-LOCATION PRINCIPLE prose: "The BAD PLAN C1 table below implements this family per the Component 1 format requirement stated in the protocol section" (22 words) | The section header and the table itself make this relationship evident without prose explanation |
| 17 | "Each row maps to a specific C1 table row below (see 'BAD PLAN entry' column)." (16 words) | The "BAD PLAN entry" column in the table already says "Row (1) in... C1 table below"; the sentence merely restates what the column shows |
| 18 | CONSTRUCTION ORDER "(Step N)" parentheticals (saves ~20 words) | The steps are immediately below in section order; back-references to their own location add nothing |
| 19 | C-59 YAML template field echoes compressed from multi-line to single-line per field (saves ~35 words) | The mandate and NOT list can be combined on one line without losing any testable content; C-59 only requires presence, not multi-line formatting |
| 20 | Step 4 body sentence compression (saves ~5 words) | "No new phases may be created. Discard skills with no matching phase." → "No new phases. Discard unmatched skills." — same rule, tighter phrasing |
| 21 | Step 5b body sentence compression (saves ~5 words) | "Fix all forward references before Step 6" → "Fix before Step 6" — same constraint |

---

## Essential Criteria Verification

| Criterion | Status | How preserved in simplified version |
|-----------|--------|--------------------------------------|
| C-01: YAML valid, `program:` top-level key, `stages:` list | PASS | Step 10 checklist line, correction table row ("program: key missing"), BAD PLAN `# WRONG C-01` at `stages:` |
| C-02: `echo` last, `auto: true`, `skills: []` | PASS | Step 8 YAML template echo stage with `# REQUIRED` comments, correction table rows, BAD PLAN `# WRONG C-02` |
| C-03: All skills from catalog, no invented names | PASS | Catalog section, Step 3 SELF-VERIFY NOT/IS, correction table 3 C-03 rows, BAD PLAN `# WRONG C-03` |
| C-04: Every non-echo stage has evidence-state gate | PASS | Compound gate format section, Step 5a template with `# WRONG C-04`, SELF-VERIFY, correction table 2 C-04 rows |
| C-05: Namespace ordering respected | PASS | Lifecycle zones establish zone sequence; Step 5a `# requires: ... (C-05)` dual-position reminders; correction table 2 C-05 rows |
| C-06: Stage names as investigative purpose | PASS | Step 2 SELF-VERIFY, correction table 2 C-06 rows, BAD PLAN `# WRONG C-06` |
| C-07: Plan framed as signal-gathering artifact | PASS | Opening sentence "plan, not an executor"; `strategy:` field mandate in YAML template; correction table C-07 row; BAD PLAN `# WRONG C-07` |

**All essential criteria: YES**

---

## Simplification Report

**What was removed:** 21 items across four categories:
- **Pure redundancy** (items 3, 4, 5, 15, 16, 17, 18): Text that restated something already visible in the same prompt
- **Aspirational-only teaching content** (items 1, 2, 8): Framework tables and paragraphs that support aspirational criteria ladders but have no essential criterion dependency
- **Over-specified elaboration** (items 6, 7, 9, 10, 11, 12, 19, 20, 21): Content that explained or extended an already-complete rule — cutting the explanation while preserving the rule
- **Belt-and-suspenders** (items 13, 14): Content that reinforced aspirational criteria already fully satisfied elsewhere in the prompt

**What was preserved in full:**
- All SELF-VERIFY blocks (C-58 requires them at every constrained step)
- All C-59 field saturation echoes in the Step 8 YAML template
- The BAD PLAN with complete C1 table, C3 exit verification, and all seven WRONG annotations
- BOUNDED BLOCK PROTOCOL with C-55, C-56, C-57 all intact
- Compound gate format section, lifecycle zones, catalog
- All correction table entries covering C-01 through C-07

```json
{"simplified_word_count": 2754, "original_word_count": 3452, "all_essential_still_pass": true}
```
