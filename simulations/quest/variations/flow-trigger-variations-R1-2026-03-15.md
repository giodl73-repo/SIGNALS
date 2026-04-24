Written to `flow-trigger-variate-R1-2026-03-15.md`. Here is the summary:

---

## Round 1 — 5 Variations for flow-trigger (Rubric v1, C-01..C-10)

| Variation | Axis | Key Differentiator | Primary Criteria Targeted |
|-----------|------|--------------------|--------------------------|
| **V-01** | Role sequence | Cascade Mapper runs before Enumerator — precommits cascade rows as numbered entries, not annotations. Auditor closes all 3 anomaly questions against the complete chain. | C-04, C-01, C-10, C-08 |
| **V-02** | Output format | Two-tier table (sync/async) with mandatory **Cascade Depth** column. PA vocab enforced per cell — violations are empty or non-conforming cells, not hidden omissions. | C-01, C-02, C-03, C-07, C-10 |
| **V-03** | Phrasing register | Conversational named-slot blocks per trigger (Type / Tier / Fires when / Doesn't fire when / Reads / Produces / Side effects / Cascade). Absent slots are blank lines, not hidden omissions. | C-03, C-05, C-06, C-07, C-09 |
| **V-04** | Lifecycle + role sequence | Four-pass protocol: (1) candidate scan, **(2) cascade map as a dedicated pass**, (3) fire evaluation ordered by Pass 2 chain, (4) pathology scan. C-10 is load-bearing — Pass 3 ordering depends on Pass 2 output. | C-01, C-04, C-10, C-02 |
| **V-05** | Inertia framing + output format | Opens with four named failure modes of informal trigger analysis, then maps each protocol step to the failure mode it fixes. Inline `VOCAB FAIL` cells + Cascade Depth column create structural + motivational enforcement. | C-01, C-04, C-07, C-08, C-10 |

**Key design choices vs prior R1 (9-criterion rubric)**:
- C-10 (cascade completeness) is now a first-class structural requirement in every variation — not just a "cascade rule" footnote
- V-04 makes cascade tracing its own dedicated pass (Pass 2), forcing Pass 3 to consume it as an ordering constraint
- V-01 uses a **Cascade Mapper role** that builds the full write-to-fire graph before enumeration begins
- V-02 and V-05 enforce cascade depth as a required table column — a missing cascade entry becomes a structural gap, not an omission
