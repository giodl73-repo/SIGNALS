**Round 2 variations written** to `simulations/quest/golden/trace-migration-variate-R2-2026-03-15.md`.

---

## Round 2 Variation Map

| Variation | Axis | C-11 | C-12 | C-09 |
|-----------|------|------|------|------|
| V-01 | Phrasing register | PASS — DIRECTIVE 0 defines approved verbs (20), disallowed phrases (5), enforcement example | PASS — DIRECTIVE 1 halt block form with no-gap declaration required | PASS — DIRECTIVE D-1/D-2 explicit two-trace floor + cross-layer requirement |
| V-02 | Output format | PASS — TABLE 0 vocabulary contract, COMPLIANCE STATUS column flags violations inline | PASS — TABLE 1-HALT mandatory form row fires when GAP-DETECTED is non-empty | PASS — TABLE 8 minimum two rows, Impact Layer column separates schema/cross-layer |
| V-03 | Lifecycle emphasis | PASS — VOCABULARY GATE fires at each phase entry; disallowed phrases block phase advancement | PASS — GAP HALT GATE fires at every phase boundary; halt block is a named re-entry mechanism | PASS — Phase 5 requires two traces, gap halt gate fires if mitigation is missing |
| V-04 | Role sequence + Phrasing register | PASS — DIRECTIVE 0 contract + DIRECTIVE 0 VIOLATION enforcement tag | PASS — DIRECTIVE 1 with explicit no-gap declaration even when no gaps fire | PASS — DIRECTIVE D-1 two-trace requirement stated, DIRECTIVE D-2 cross-layer requirement |
| V-05 | Role sequence + Output format + Lifecycle | PASS — Vocabulary Contract table + Compliance column | PASS — Halt Protocol table + no-gap declaration form | PASS — Phase 4 gate checks cascade count >= 2 and cross-layer presence |

---

**Key design decisions for Round 2:**

- **C-11 mechanism varies by axis.** V-01/V-04 use DIRECTIVE capitalized contracts. V-02/V-05 embed the vocabulary list in a TABLE 0 column header with a COMPLIANCE STATUS column. V-03 makes vocabulary a phase gate that blocks advancement. All three mechanisms produce the approved verb list (5+), disallowed phrases (3+), and enforcement example.

- **C-12 mechanism varies by axis.** V-01/V-04 use DIRECTIVE 1 HALT BLOCK form. V-02 uses a mandatory TABLE 1-HALT that fires when GAP-DETECTED is non-empty. V-03/V-05 use named phase gates (GAP HALT GATE / Phase gate = HALT). All include the no-gap declaration even when no gaps fire — the rubric requires the block exists structurally regardless.

- **C-09 tightening:** Every variation explicitly states the two-trace minimum at the structural level (not as a prose suggestion) and separates the cross-layer requirement from the count requirement.
