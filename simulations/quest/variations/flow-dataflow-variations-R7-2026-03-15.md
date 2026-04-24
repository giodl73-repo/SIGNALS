`flow-dataflow-variate-R7-2026-03-15.md` written — 5 complete variations.

---

## Round 7 design summary

**Three single-axis variations:**

| Variation | Axis | Scenario | Core mechanism |
|-----------|------|----------|----------------|
| **V-01** | Structure | Intercompany settlement (Finance) | **Typed entity handoff manifests** — stage exit declarations include field count and key field assertions (e.g., `net_amount: DECIMAL(18,4)`). Entity at Risk column must cite `entity.field_name` from the manifest, not just the entity. Drives C-04 and C-17 depth simultaneously. |
| **V-02** | Output format | Retail vendor replenishment (Operations) | **SLA budget framing** — boundary inventory gains Transport Latency + Processing Overhead columns plus SLA Budget Consumed (%). Forces numeric quantification at every boundary; surfaces SLA breach when the % sum exceeds 100% mid-table. Drives C-05/C-06 quantification. |
| **V-03** | Structure | Subscription billing (Commerce) | **Declaration-to-reference closure enforcement** — Section 6b requires an explicit reconciliation: declared NH/LP set vs recovery table rows present vs missing. Gap is visible without the scorer hunting across sections. Tests whether LLMs generate false-complete closure statements or genuine ones. |

**Two combined variations:**

- **V-04** (H1 + H2) — Typed manifests + SLA budget framing on a vendor payment terms sync pipeline. Tests whether field-type assertions in exit manifests cause the SLA stale analysis to cite specific field types at the domination point — a conclusion neither mechanism alone enforces.
- **V-05** (H1 + H2 + H3) — All three R7 axes on an order-to-cash pipeline. Tests whether H3 (closure check) is independently load-bearing when the other two are active, and whether the combined prompt length degrades C-01 coverage under cognitive load.

**New signal candidates for R7 scoring:**
- Does `entity.field_name` citation format appear in Entity at Risk annotations when the manifest is present?
- Do synchronous API boundaries receive a numeric SLA % (vs "< 1%" without support)?
- Does the closure check identify genuine gaps, or does it match the table and miss undeclared identifiers?
