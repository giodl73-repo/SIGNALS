Here are the 5 complete R17 variations written to `flow-dataflow-rubric-v17-R17-2026-03-15.md`.

---

## R17 variation summary

**C-50 (dual-slot anchoring)** — the four [A-01]-load-bearing SCs are upgraded across all variations:
- **SC-8**: governed-token slot now reads "requiring [A-01] as a mandatory citation token inside [A-14]"; enforcement clause also names [A-01] explicitly
- **SC-9**: governed-token slot reads "requiring [A-01] as a mandatory token in every cell"; enforcement clause names [A-01] in the detectability sentence
- **SC-11**: already natural (governs [A-01] itself); enforcement clause now explicitly says "[A-01] must appear before any stage trace"
- **SC-13**: governed-token slot reads "requiring [A-01] as a citation token in both [A-12] and [A-14]"; enforcement clause names [A-01] in the header-callback description

**C-51 (detectability-location)** — every SC entry now names where in the structure a violation surfaces:

| SC | Location |
|----|----------|
| SC-1 | "from the role-opener line without reading the role body" |
| SC-2 | "at the stage-boundary position" |
| SC-3 | "at the column-header and cell-value level" |
| SC-4 | "at the cell-value level without reading surrounding prose" |
| SC-5 | "within [A-02]'s body without searching other sections" |
| SC-6 | "at the role-boundary line before reading role content" |
| SC-7 | "at the table-header row without reading row contents" |
| SC-8 | "from [A-14]'s citation token list without prose interpretation" |
| SC-9 | "at the cell level without reading surrounding prose" |
| SC-10 | "at the [A-14] header position" |
| SC-11 | "at the output head without reading artifact content" |
| SC-12 | "by token-match at the role-opener line without reading the role body" |
| SC-13 | "from the header line alone" |

**Variation axes used:**

| Variation | Axis | Scenario | Skip-level cite |
|-----------|------|----------|----------------|
| V-01 | Natural sequence | Hotel F&B → revenue ledger | Commerce cites Finance [A-04] |
| V-02 | Non-natural (Ops→Fin→Com) | B2B distribution fulfillment-to-invoicing | Commerce cites Operations [A-04] |
| V-03 | Prose register + SC-14 | SaaS subscription renewal/churn | Commerce cites Finance [A-04] |
| V-04 | Max inertia (≥5 steps) | Retail loyalty points → liability ledger | Commerce cites Finance [A-04] |
| V-05 | Non-natural (Ops→Com→Fin) + Phase Gate 0 | Telecom CDR → billing → GL | Finance cites Operations [A-04] |
