## flow-throttle — Round 4 Scoring (v4 Rubric, 130-point max)

---

### Base Assumption

All five variations are built on R3 foundations confirmed to pass **C-01 through C-16** (118 pts under v3). The scoring below focuses on incremental pass/fail for **C-17, C-18, C-19, C-20** (3 pts each).

---

### C-01 — Bottleneck Localization

**All variations: PASS (12 pts)**

Every variation inherits the bottleneck statement template: `"[Component] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time]..."`. Names a specific component, exact PA construct, and numeric saturation volume. Vague language excluded by the template constraint.

---

### C-02 — Rate Limit Hit Ordering

**All variations: PASS (12 pts)**

TABLE 2 (or equivalent) enforces ranked hit order with a "Why this order holds at scenario volume" column. Two tiers in explicit sequence with causal explanation. The column rule blocks ascending-limit copies.

---

### C-03 — Backpressure Propagation Trace

**All variations: PASS (12 pts)**

TABLE 3 (BACKPRESSURE HOP CHAIN) has columns: signal emitted, signal type (error code / retry-after header / queue depth / other), receiving component, response behavior. At least two hops required by structure. Causal chain explicit.

---

### C-04 — User Experience per Throttle Tier

**All variations: PASS (12 pts)**

USER EXPERIENCE MAP section requires distinct UX categories across tiers — rule embedded in the section: "Categories must differ across tiers." Two-tier minimum satisfied by TABLE 1 structure.

---

### C-05 — Domain Grounding in Connectors / Power Automate

**All variations: PASS (12 pts)**

PA VALIDATION ROUND 1 requires per-construct lines citing exact PA construct names. Domain rule: "Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits." Generic HTTP 429 blocked by domain rule.

---

### C-06 through C-13 — Recommended and Advisory Criteria

**All variations: PASS** (inheriting R3 base scores — TABLE 4 burst path, RETRY-AFTER GAPS, TABLE 6 risk register, PA-SPECIFIC REMEDIATIONS, two-barrier validation structure all present in every variation).

---

### C-14 — Gate Mechanism

**All variations: PASS (inherited)**

V-01 confirms prose gate format: `"GATE 1: All TABLE 1 rows have PA constructs, numeric limits, and Round 1 validation lines. Block: TABLE 2 is blocked until all three conditions are met."` Carries (a) name "GATE 1," (b) conditional prerequisite (three conditions listed), (c) named block target "TABLE 2." V-02 carries identical structure for ROLE 1.2. C-20 confirms format is decorative — prose suffices.

---

### C-15 — Non-Deference Sentence

**All variations: PASS (inherited)**

Non-deference sentence present in second-barrier preamble for all variations. "Round 1's confidence is not evidence of Round 1's precision" (V-01) and equivalent formulations in V-02–V-05.

---

### C-16 — Scope Extension Declaration

**All variations: PASS (inherited)**

Named construct populations excluded from Round 1 declared in Round 2 preamble: TABLE 3 propagation signals, TABLE 5 cascade mechanism labels. Three population categories named across all variations.

---

### C-17 — Pre-Barrier Independence Instruction Placement

**Pass condition:** Non-deference sentence in preamble/header, **before** any construct-by-construct evaluative output, naming prior layer and asserting confidence-is-not-evidence.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Named section `SECOND BARRIER — PRE-EVALUATION HEADER (before any construct evaluation begins)` — sentence appears inside this section, which precedes all Round 2 construct lines. Explicit positional announcement. | **PASS** |
| V-02 | Two-role design: ROLE 2 preamble precedes validation table by structural necessity. Base R3 V-03 confirmed C-15 pass from preamble placement — same placement satisfies C-17. | **PASS** |
| V-03 | ROLE 2 preamble with labeled pair. Placement before validation table inherited. | **PASS** |
| V-04 | Named `SECOND BARRIER — PRE-EVALUATION PREAMBLE` with labeled pair, explicitly before evaluative output. | **PASS** |
| V-05 | `PRE-ANALYSIS ASSERTION` header in PHASE 4.A with labeled pair, before evaluative output. | **PASS** |

**C-17 scores: all +3**

---

### C-18 — Structural Closure Reason for Scope Extension

**Pass condition:** Scope declaration names the **structural reason** why the first barrier's window excluded those categories. Naming categories without a closure reason does not pass.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Scope section states: "introduced after Round 1's execution window had closed" / "introduced after Round 1's scope window closed." This IS the closure reason. Matches the pass condition example verbatim. | **PASS** |
| V-02 | Adds explicit closure sentence: "ROLE 1's definition window closed at section 1.2 completion, before 1.3–1.5 executed." Window boundary stated as structural fact. | **PASS** |
| V-03 | Base carries closure reason (scope extension label in labeled pair includes window boundary). | **PASS** |
| V-04 | Labeled pair includes closure reason in `Scope extension:` directive. | **PASS** |
| V-05 | Full synthesis includes closure reason in PRE-ANALYSIS ASSERTION header. | **PASS** |

**C-18 scores: all +3**

---

### C-19 — Label-Enforced Co-location Independence

**Pass condition:** When two independent directives occupy the same block, each must carry a **distinct named label**. Unlabeled co-location scores as one mechanism for both. Pass: `Independence:` / `Scope extension:` labels (or equivalent) present.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Pre-evaluation header contains two paragraphs — non-deference and scope extension — but they carry no distinct sub-labels. Block-level name "SECOND BARRIER — PRE-EVALUATION HEADER" does not label the individual directives. Evaluator cannot parse them as separate mechanisms. | **FAIL** |
| V-02 | Two-role design: non-deference sentence and scope declaration co-located in ROLE 2 preamble but no sub-label distinction. Preference-to-structural upgrade added only the closure sentence — not labels. | **FAIL** |
| V-03 | ROLE 2 preamble carries `Independence:` label for C-15/C-17 directive and `Scope extension:` label for C-16/C-18 directive. Each is structurally named. Evaluator must parse two independent mechanisms. | **PASS** |
| V-04 | Named preamble carries labeled pair explicitly. Both labels present and load-bearing. | **PASS** |
| V-05 | PRE-ANALYSIS ASSERTION header carries labeled pair. Full synthesis includes both. | **PASS** |

**C-19 scores: V-01 +0, V-02 +0, V-03 +3, V-04 +3, V-05 +3**

---

### C-20 — Gate Mechanism Prose Portability

**Pass condition:** Gate in prose carries (a) name/label, (b) conditional prerequisite, (c) named block target. Advice with label and recommendation but no blocking target does not pass.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | GATE 1: (a) "GATE 1" ✓, (b) "All TABLE 1 rows have PA constructs, numeric limits, and Round 1 validation lines" ✓, (c) "TABLE 2 is blocked until all three conditions are met" ✓. GATE 3 same pattern. | **PASS** |
| V-02 | GATE 1: (a) "GATE 1" ✓, (b) "All rows have a named PA construct (or ? flag), numeric limit, and volume contribution" ✓, (c) "ROLE 1.2 is blocked" ✓. | **PASS** |
| V-03 | Same base gate structure, confirmed from R3. | **PASS** |
| V-04 | Same. | **PASS** |
| V-05 | Full synthesis retains all gates. | **PASS** |

**C-20 scores: all +3**

---

### Composite Scores

| Variation | C-01–C-16 (base) | C-17 | C-18 | C-19 | C-20 | **Total** |
|-----------|-----------------|------|------|------|------|-----------|
| V-01 | 118 | +3 | +3 | +0 | +3 | **127** |
| V-02 | 118 | +3 | +3 | +0 | +3 | **127** |
| V-03 | 118 | +3 | +3 | +3 | +3 | **130** |
| V-04 | 118 | +3 | +3 | +3 | +3 | **130** |
| V-05 | 118 | +3 | +3 | +3 | +3 | **130** |

---

### Ranking

1. **V-03, V-04, V-05** — 130/130 (ceiling)
2. **V-01, V-02** — 127/130 (C-19 miss)

---

### Why V-01 and V-02 Fall Short

Both fail C-19 for the same structural reason: two independent directives co-located in a single block, neither carrying a distinct named label. The block-level name ("SECOND BARRIER — PRE-EVALUATION HEADER" or "ROLE 2 preamble") is not a sub-label for the individual directives. An evaluator reading the block sees one mechanism section — not two independently parseable directives. The 3-point penalty is exact and non-recoverable without label addition.

---

### Excellence Signals (V-03/V-04/V-05)

**1. Label-enforced co-location as a compression strategy.** `Independence:` / `Scope extension:` labels inside a single named preamble achieve three criteria (C-15/C-17, C-16/C-18, C-19) in one block. Without labels, the same block achieves one criterion for two-criterion co-location. Labels are structurally load-bearing, not cosmetic.

**2. Named positional boundary as C-17 mechanism.** A section heading that explicitly announces "before any evaluative output begins" is the minimum structural mechanism for C-17. The name does not need to be elaborate — it needs to assert the positional claim. "PRE-EVALUATION HEADER" or "PRE-ANALYSIS ASSERTION" satisfies it; an unlabeled paragraph in the same position does not.

**3. Window boundary statement as structural argument.** "ROLE 1's window closed at section 1.2 completion, before 1.3–1.5 executed" transforms a scope declaration from preference ("these categories not covered") to structural argument (window boundary is a fact, exclusion is a consequence). One sentence is sufficient; the sentence must name the boundary event, not just the populations.

**4. Prose gate portability confirmed.** All three structural elements (name, conditional, named block target) present in plain-prose gate format. The rubric's C-20 confirmation means variations can simplify table-format gates to prose without scoring loss — format carries zero weight.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["label-enforced co-location: distinct sub-labels within one preamble block score two independent criteria instead of one", "named positional boundary: section heading asserting pre-evaluation placement is minimum C-17 mechanism", "window boundary statement: naming the closure event transforms scope preference into structural argument for C-18"]}
```
