Written to `simulations/quest/golden/flow-conversation-variate-R20-2026-03-15.md`.

---

## Round 20 Variation Map

| Variation | Axis | C-77 | C-78 | Notes |
|-----------|------|------|------|-------|
| V-01 | Lifecycle emphasis | PASS | PARTIAL | LIFECYCLE_PROTOCOL foregrounded as design-intent document; SOLE_AUTHORITY block required; gate standalone framing implicit only |
| V-02 | Output format | PARTIAL | PASS | Gate FIELD\|VALUE table with STANDALONE_DECLARATION as mandatory row; SOLE_AUTHORITY header present but closure statement not schema-enforced |
| V-03 | Phrasing register (formal imperative) | PASS | PASS | DIRECTIVE: labels for all C-77 + C-78 required strings; no prose hedging space |
| V-04 | Role sequence + Lifecycle emphasis | PASS | PARTIAL | Phase -1 issues LIFECYCLE_PROTOCOL_DESIGN_CONTRACT as pre-declared artifact; TA authors against it; gate framing organic not prescribed |
| V-05 | Combined: Lifecycle emphasis + Output format + Phrasing register | PASS | PASS | LIFECYCLE_PROTOCOL as FIELD\|VALUE block with mandatory CLOSURE_STATEMENT row; gate as FIELD\|VALUE table with mandatory STANDALONE_DECLARATION row; DIRECTIVE labels throughout — ceiling variation |

---

### Signal source rationale for C-77 and C-78

**C-77 extraction approach across variations:**

The R19 V-01 signal showed that naming both layers *and* stating "neither layer alone closes the system" is what converts C-76 (both layers operating) into C-77 (both layers *declared as a design intent*). The three single-axis variations attack this differently:
- V-01 uses prose design-intent framing (SOLE_AUTHORITY as a conceptual block)
- V-03 prescribes exact required strings as DIRECTIVE fields
- V-05 makes CLOSURE_STATEMENT a named FIELD|VALUE row — the most structurally enforceable form

**C-78 extraction approach:**

The R19 V-02 signal showed the standalone framing statement must be *explicit* inside the gate block. The variations attack this:
- V-02 makes STANDALONE_DECLARATION a required table field the Auditor can flag as MISSING
- V-03 prescribes exact phrasing as a DIRECTIVE with field name
- V-05 repeats the FIELD|VALUE table schema from Phase 0-CA-1 (where the gate schema is declared) through Phase 6-A (where the gate is emitted), so schema-enforcement is bidirectional
