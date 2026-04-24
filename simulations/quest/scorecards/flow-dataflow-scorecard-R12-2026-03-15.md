I have all five variations fully read. Scoring now against the v10 rubric.

---

## flow-dataflow — Round 12 Scorecard (Rubric v10)

**Scoring formula**: composite = (full\_passes + 0.5 × partials) / 24 × 100
**Criteria tiers**: Essential C-01–C-04 | Recommended C-05–C-07 | Aspirational C-08–C-24

---

## V-01 — Conversational/Question-Driven Register

**Domain**: Finance — AP invoice automation
**Axis**: Phrasing register (imperatives replaced with invitations)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Pipeline stage identification | PASS | 6 stages explicitly named in "Stages to trace" list |
| C-02 | Error handling per stage | PASS | NH-NN format defined; boundary Error Handling column present |
| C-03 | Data loss point identification | PASS | LP-NN format with concrete example; stage trace column |
| C-04 | Schema state at each stage | PASS | Schema Change? column; verification format example given |
| C-05 | Latency characterization | PASS | Stage Latency column; "real-time, micro-batch, hourly, daily" examples |
| C-06 | Stale data windows | PASS | Dedicated stale window section with worst-case failure mode |
| C-07 | Domain framing | PASS | Finance/AP domain; named entities VendorInvoice, OCRExtract, etc. |
| C-08 | Recovery prescriptions | PASS | Recovery table with mechanism column; "not just 'manual review'" |
| C-09 | Pattern trade-off | PASS | Pattern section; ≥2 dimensions, ≥1 quantified in AP/finance terms |
| C-10 | Pre-trace entity inventory | PASS | Entity inventory section before stages; mid-trace introduction flagged |
| C-11 | Systematic boundary labeling | PASS | B1->2 through B5->6 rows explicit in boundary table |
| C-12 | Verified-unchanged schema assertion | **PARTIAL** | "is clearer than a bare 'unchanged'" is an invitation, not an enforcement gate; model may omit clause |
| C-13 | Structural completeness enforcement | PASS | Boundary table with explicit blank-cell = visible gap; stage trace table structure |
| C-14 | Incumbent baseline anchoring | PASS | Recovery columns "Which MS step?" + "Incumbent step (exact text from T-01)" |
| C-15 | Structured incumbent baseline table | PASS | 4-column table (Step ID, Manual Step, Who, How long); specific AP example given |
| C-16 | Full recovery-to-baseline traceability | **PARTIAL** | "Each entry should also cite" — reminder framing, not "must"; C-16 requires ALL entries; enforcement signal weak |
| C-17 | Entity-at-risk per boundary | PASS | Explicit format `VendorInvoice.vendor_id — risk description`; "entity name alone isn't specific enough" |
| C-18 | Structured recovery audit table | PASS | 5-column recovery table; all required columns present |
| C-19 | Typed stage-exit manifests | PASS | EXIT MANIFEST format fully specified with typed notation; format shown |
| C-20 | Field-level entity-at-risk traceability | PASS | "both the entity AND the specific field from the upstream exit manifest" explicit |
| C-21 | Decomposed boundary latency | PASS | Separate Transport Latency (ms) + Processing Overhead (ms) columns; "rough estimates more useful than 'negligible'" |
| C-22 | Cumulative SLA% + domination point | PASS | Both SLA% columns; domination point question explicit |
| C-23 | Structurally separate closure gate | PASS | Separate closure check section; per-identifier table; "count summary isn't what I need" |
| C-24 | Pre-declared complete output scaffold | **PARTIAL** | Planning table present (4 columns); upstream references phrased as "it would be helpful to list T-NN tokens" — invitation, not contract; upstream refs column likely sparse |

**Tally**: Essential 4/4 | Recommended 3/3 | Aspirational 14 PASS + 3 PARTIAL + 0 FAIL (effective 15.5/17)

**Composite**: (21 + 1.5) / 24 × 100 = **93.75 → 94**

---

## V-02 — Boundary-First Lifecycle

**Domain**: Operations — Supplier ASN → DC receiving
**Axis**: T-03 (boundary inventory) declared as first-class scaffold entry before stage trace tables

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Pipeline stage identification | PASS | 6 stages in Sections 4–9 |
| C-02 | Error handling per stage | PASS | NH-NN format; T-03 Error Handling column with "Silence fails C-02" |
| C-03 | Data loss point identification | PASS | LP-NN with format in stage trace instructions |
| C-04 | Schema state at each stage | PASS | Schema Delta column present |
| C-05 | Latency characterization | PASS | Stage Latency column; "may not be omitted" |
| C-06 | Stale data windows | PASS | Section 10 stale window with normal + worst-case |
| C-07 | Domain framing | PASS | Operations/DC receiving domain; named entities SupplierASN, DCReceiptEvent, etc. |
| C-08 | Recovery prescriptions | PASS | T-10 Recovery Audit with mechanism column; specific action requirement |
| C-09 | Pattern trade-off | PASS | Section 13 pattern assessment with ≥2 dimensions, ≥1 quantified |
| C-10 | Pre-trace entity inventory | PASS | T-02 Entity Inventory before stage traces; required entities listed |
| C-11 | Systematic boundary labeling | PASS | T-03 pre-declared with B1->2 through B5->6; complete inventory before stages |
| C-12 | Verified-unchanged schema assertion | PASS | "A bare 'NONE' without the verification clause fails C-12" — explicit enforcement |
| C-13 | Structural completeness enforcement | PASS | T-03 stub with pre-committed rows; missing entry is structurally visible |
| C-14 | Incumbent baseline anchoring | PASS | T-10 MS Step ID column; "Generic 'manual intervention' without a named incumbent step fails C-16" |
| C-15 | Structured incumbent baseline table | PASS | T-01 with 4 columns; specific DC receiving example; INCUMBENT TOTAL declared |
| C-16 | Full recovery-to-baseline traceability | PASS | "Every entry must cite an MS-NN step from T-01" — imperative enforcement |
| C-17 | Entity-at-risk per boundary | **PARTIAL** | T-03 pre-declared at entity level; update-after-manifest instruction present but model may not return to fill field citations |
| C-18 | Structured recovery audit table | PASS | T-10 with 5 required columns; missing row = structural gap |
| C-19 | Typed stage-exit manifests | PASS | EXIT MANIFEST with typed field assertions; minimum two required |
| C-20 | Field-level entity-at-risk traceability | **PARTIAL** | "A boundary row whose entity-at-risk annotation remains at entity level only after stage trace sections fails C-20" — explicit failure condition, but stub-update execution is an inherent risk of boundary-first design |
| C-21 | Decomposed boundary latency | PASS | Separate Transport + Processing Overhead columns in T-03; "'negligible' does not qualify" |
| C-22 | Cumulative SLA% + domination point | PASS | SLA% + Cumulative SLA% in T-03; DOMINATION POINT appended post-stages |
| C-23 | Structurally separate closure gate | PASS | T-11 Closure Gate "structurally separate from T-10"; per-identifier status |
| C-24 | Pre-declared complete output scaffold | PASS | STEP 0 scaffold imperative; T-03 declared before T-04–T-09 in dependency order; upstream T-NN references fully specified |

**Tally**: Essential 4/4 | Recommended 3/3 | Aspirational 15 PASS + 2 PARTIAL + 0 FAIL (effective 16/17)

**Composite**: (22 + 1.0) / 24 × 100 = **95.83 → 96**

---

## V-03 — Incumbent-Centric Narrative Framing

**Domain**: Commerce — ERP-to-storefront catalog sync
**Axis**: INCUMBENT EQUIVALENT block per stage; T-01 as primary narrative anchor throughout

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Pipeline stage identification | PASS | 6 stages named in Section 3–8 |
| C-02 | Error handling per stage | PASS | NH-NN format; boundary Error Handling column |
| C-03 | Data loss point identification | PASS | LP-NN with Commerce-specific example |
| C-04 | Schema state at each stage | PASS | Schema Delta column |
| C-05 | Latency characterization | PASS | Stage Latency column; characterization required |
| C-06 | Stale data windows | PASS | Section 10 compares automated latency against SLA AND INCUMBENT TOTAL — dual stale-window analysis |
| C-07 | Domain framing | PASS | Commerce domain; named entities ERPProductMaster, PriceRecord, etc. |
| C-08 | Recovery prescriptions | PASS | T-10 with mechanism column; "revert to MS-NN" framing drives specific prescriptions |
| C-09 | Pattern trade-off | PASS | Section 13 with INCUMBENT TOTAL comparison baseline; ≥2 dimensions required |
| C-10 | Pre-trace entity inventory | PASS | T-02 Entity Inventory before stage traces; Catalog SLA restatement anchored to T-01 |
| C-11 | Systematic boundary labeling | PASS | T-09 with B1->2 through B5->6 |
| C-12 | Verified-unchanged schema assertion | PASS | "Bare 'NONE' without verification fails C-12" — imperative enforcement |
| C-13 | Structural completeness enforcement | PASS | T-09 structured table; T-10 with row-level gap visibility |
| C-14 | Incumbent baseline anchoring | PASS | Per-stage INCUMBENT EQUIVALENT block citing specific MS-NN step verbatim; "A stage trace with no INCUMBENT EQUIVALENT block fails C-14 for that stage" |
| C-15 | Structured incumbent baseline table | PASS | T-01 with 4 columns; Commerce-specific example; INCUMBENT TOTAL + Catalog SLA declared |
| C-16 | Full recovery-to-baseline traceability | PASS | "every recovery entry must be written as 'On [condition], revert to [MS-NN]'" — strongest C-16 enforcement design; incumbent co-location at stage level makes every recovery row carry a natural MS-NN citation |
| C-17 | Entity-at-risk per boundary | PASS | T-09 entity-at-risk: "`entity.field_name — risk description`. Field must be from upstream exit manifest. Entity-only annotations fail C-20" |
| C-18 | Structured recovery audit table | PASS | T-10 with 5 required columns; "upstream T-NN tokens as declared in scaffold" |
| C-19 | Typed stage-exit manifests | PASS | EXIT MANIFEST format specified; minimum two typed assertions |
| C-20 | Field-level entity-at-risk traceability | PASS | "Entity-only annotations fail C-20" — explicit failure condition; no stub-update dependency (boundary table produced after stages, so field citations available at declaration time) |
| C-21 | Decomposed boundary latency | PASS | T-09 separate Transport + Processing Overhead; "'Negligible' does not qualify" |
| C-22 | Cumulative SLA% + domination point | PASS | Both SLA% columns; DOMINATION POINT includes incumbent elapsed time comparison — richer than minimum requirement |
| C-23 | Structurally separate closure gate | PASS | T-11 "structurally separate from T-10"; per-identifier status required |
| C-24 | Pre-declared complete output scaffold | PASS | STEP 0 imperative; T-01 as "primary narrative anchor" with each stage table (T-03–T-08) citing T-01 in upstream refs; complete dependency graph declared; no table may appear mid-trace |

**Tally**: Essential 4/4 | Recommended 3/3 | Aspirational 17/17 PASS

**Composite**: 24/24 × 100 = **100**

---

## V-04 — Combined: Conversational Register + Boundary-First Lifecycle

**Domain**: Finance — payroll processing
**Axes**: H1 (question-driven phrasing) + H2 (boundary pre-committed as T-03)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Pipeline stage identification | PASS | 6 stages in Stages list |
| C-02 | Error handling per stage | PASS | NH-NN format with assignment instruction |
| C-03 | Data loss point identification | PASS | LP-NN with payroll-specific example |
| C-04 | Schema state at each stage | PASS | Schema Change? column; verification format shown in example |
| C-05 | Latency characterization | PASS | Stage Latency column |
| C-06 | Stale data windows | PASS | Dedicated stale window section; worst-case failure |
| C-07 | Domain framing | PASS | Finance/payroll domain; named entities TimesheetRecord, PayCalculationResult, etc. |
| C-08 | Recovery prescriptions | PASS | Recovery table with 5 columns; "specific action at a specific boundary or stage" |
| C-09 | Pattern trade-off | PASS | Pattern section with ≥2 dimensions, ≥1 quantified in payroll/Finance terms |
| C-10 | Pre-trace entity inventory | PASS | Entity inventory before stages; mid-trace introduction framed as gap |
| C-11 | Systematic boundary labeling | PASS | T-03 pre-committed with B1->2 through B5->6 rows |
| C-12 | Verified-unchanged schema assertion | **PARTIAL** | "'NONE — verified: no field added, removed, renamed, or retyped' is clearer than just 'unchanged'" — invitation, not enforcement; combines with V-01's same weakness |
| C-13 | Structural completeness enforcement | PASS | T-03 boundary pre-commitment; blank cells = visible structural gaps |
| C-14 | Incumbent baseline anchoring | PASS | Recovery columns "Which MS step?" + "Incumbent step (verbatim)"; "link back to a specific MS-NN step" stated |
| C-15 | Structured incumbent baseline table | PASS | 4-column table; specific payroll example with 5 concrete steps |
| C-16 | Full recovery-to-baseline traceability | **PARTIAL** | "Each entry should link back to a specific MS-NN step" — "should" phrasing, not "must"; C-16 requires ALL entries; combined phrasing weakness from V-01 axis |
| C-17 | Entity-at-risk per boundary | **PARTIAL** | T-03 pre-committed at entity level; "please update to entity.field_name after each stage's exit manifest" — invitation; stub-fill risk from V-02 axis |
| C-18 | Structured recovery audit table | PASS | 5-column table; all columns present |
| C-19 | Typed stage-exit manifests | PASS | EXIT MANIFEST format fully specified with typed notation |
| C-20 | Field-level entity-at-risk traceability | **PARTIAL** | "return to the boundary pre-commitment table and update the Entity at Risk cell" — invitation phrasing; stub-update execution risk from V-02 axis |
| C-21 | Decomposed boundary latency | PASS | Separate Transport + Processing Overhead columns; "rough numeric estimates are fine" but separate |
| C-22 | Cumulative SLA% + domination point | PASS | SLA% + Cumulative SLA% in T-03; domination point after full table |
| C-23 | Structurally separate closure gate | PASS | Separate closure check; "per-identifier status" explicit; "count summary doesn't surface gaps" |
| C-24 | Pre-declared complete output scaffold | **PARTIAL** | Planning table present; T-03 listed as early commitment; but "Could you fill in the 'Which prior tables feed into this?' column?" is an invitation — upstream T-NN tokens likely sparsely populated; V-01 phrasing weakness compounds with V-02 complexity |

**Tally**: Essential 4/4 | Recommended 3/3 | Aspirational 12 PASS + 5 PARTIAL + 0 FAIL (effective 14.5/17)

**Composite**: (19 + 2.5) / 24 × 100 = **89.58 → 90**

**Axis interaction finding**: The two axes do not cancel — they compound. V-01's phrasing weakness degrades the upstream-references column (C-24 PARTIAL) while V-02's stub-update dependency adds C-17/C-20 exposure. The net gap is wider than either axis alone. V-04 produces 5 PARTIAL vs V-01's 3 and V-02's 2, confirming H4 prediction that combined weakening exceeds individual axis penalties.

---

## V-05 — Combined: Scaffold-First + Inertia-First + Three-Role Sequence

**Domain**: Operations/Finance/Commerce — multi-tier inventory sync
**Axes**: Scaffold Architect role (C-24) + Operations-only T-01 (C-15 quality) + cross-role citation enforcement (C-16)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Pipeline stage identification | PASS | 6 stages named in Commerce pass, Stages 1–6 |
| C-02 | Error handling per stage | PASS | NH-NN format; boundary Error Handling column |
| C-03 | Data loss point identification | PASS | LP-NN with inventory-specific example; "Errors may occur" disqualified |
| C-04 | Schema state at each stage | PASS | Schema Delta with "NONE — verified: no field added, removed, renamed, or retyped" — bare NONE fails |
| C-05 | Latency characterization | PASS | Stage Latency column; characterization required |
| C-06 | Stale data windows | PASS | Stale Window Analysis compares against SLA (T-02) AND INCUMBENT TOTAL (T-01) — dual-anchor |
| C-07 | Domain framing | PASS | Inventory domain; named entities PhysicalCountEvent, DCReconciliationRecord, etc. |
| C-08 | Recovery prescriptions | PASS | T-10 with mechanism column; "specific action at specific boundary or stage" |
| C-09 | Pattern trade-off | PASS | Pattern Assessment in Commerce pass; ≥2 dimensions; INCUMBENT TOTAL as comparison baseline |
| C-10 | Pre-trace entity inventory | PASS | T-02 produced by Finance before Commerce stages; Finance-exclusive scope enforced |
| C-11 | Systematic boundary labeling | PASS | T-09 with B1->2 through B5->6; complete inventory |
| C-12 | Verified-unchanged schema assertion | PASS | "Bare 'NONE' without verification fails C-12" — explicit enforcement in Commerce pass |
| C-13 | Structural completeness enforcement | PASS | T-10 with row-level gap visibility; T-09 with blank-cell enforcement |
| C-14 | Incumbent baseline anchoring | PASS | T-10 MS Step ID + "Incumbent Step (verbatim from T-01)" columns; cross-role citation makes the enforcement architecture explicit |
| C-15 | Structured incumbent baseline table | PASS | T-01 produced exclusively by Operations; 4 columns; minimum five specific steps; Operations-dedicated pass maximizes incumbent step quality — specific actors, times, systems expected |
| C-16 | Full recovery-to-baseline traceability | PASS | "every row must cite a specific MS-NN step from T-01 (produced by Operations)... A recovery entry that names the incumbent process category without an MS-NN step identifier fails C-16. Commerce is responsible for cross-role citation accuracy" — strongest C-16 enforcement design alongside V-03 |
| C-17 | Entity-at-risk per boundary | PASS | T-09 boundary: "`entity.field_name — risk description`, entity from T-02, field from upstream exit manifest. Entity-only fails C-20" — boundary declared post-stages so field citations available at declaration time (same structural advantage as V-03) |
| C-18 | Structured recovery audit table | PASS | T-10 five columns; missing rows = structural gaps |
| C-19 | Typed stage-exit manifests | PASS | EXIT MANIFEST with typed assertions; minimum two required |
| C-20 | Field-level entity-at-risk traceability | PASS | "Entity-only fails C-20" — explicit; T-09 produced after stage manifests, so no stub-update dependency |
| C-21 | Decomposed boundary latency | PASS | T-09 separate Transport + Processing Overhead; "'Negligible' does not qualify" |
| C-22 | Cumulative SLA% + domination point | PASS | Both SLA% columns in T-09; DOMINATION POINT statement required |
| C-23 | Structurally separate closure gate | PASS | T-11 "structurally separate from T-10"; per-identifier; count summaries disqualified |
| C-24 | Pre-declared complete output scaffold | PASS | Scaffold Architect is a scope-isolated role whose ONLY output is the scaffold table — the strongest C-24 enforcement design in any round. "Every table appearing anywhere in this response must have a row here. No domain pass may introduce a table not registered in this scaffold." Upstream Tables column enforcement rules explicitly stated: T-10 must list T-01 + T-09 + all stage T-NN; T-11 must list T-10 |

**Tally**: Essential 4/4 | Recommended 3/3 | Aspirational 17/17 PASS

**Composite**: 24/24 × 100 = **100**

---

## Rankings

| Rank | Variation | Composite | Asp. Pass | Gap Summary |
|------|-----------|-----------|-----------|-------------|
| 1 (tied) | **V-03** — Incumbent-centric narrative | **100** | 17/17 | None — single-axis control, elegant C-14/C-16 co-location mechanism |
| 1 (tied) | **V-05** — Scaffold-first + inertia-first + roles | **100** | 17/17 | None — strongest C-24 architecture (Scaffold Architect), strongest C-15 quality (Operations-only T-01) |
| 3 | **V-02** — Boundary-first lifecycle | **96** | 15.5/17 | C-17/C-20 PARTIAL: T-03 stub-update mechanism relies on model returning to fill field citations after manifests |
| 4 | **V-01** — Conversational register | **94** | 14.5/17 | C-12/C-16/C-24 PARTIAL: invitation phrasing degrades enforcement signal on verification clause, recovery all-entries requirement, and upstream T-NN references |
| 5 | **V-04** — Conversational + boundary-first | **90** | 14.5/17 | 5 PARTIAL: axes compound rather than cancel — phrasing weakness degrades C-24 while stub-update adds C-17/C-20 risk |

---

## Hypothesis Outcomes

| Hypothesis | Prediction | Finding |
|------------|------------|---------|
| H1 — Phrasing register scaffold decay (V-01) | Scaffold produced but upstream-references column sparse | **CONFIRMED** — C-24 PARTIAL; C-16 PARTIAL; C-12 PARTIAL. Invitation phrasing weakens three enforcement criteria simultaneously |
| H2 — Boundary pre-commitment fill rate (V-02) | Stronger C-11 compliance; C-17/C-20 depends on stub-update execution | **CONFIRMED** — C-11 PASS (all boundaries pre-declared); C-17/C-20 PARTIAL (stub-update risk) |
| H3 — Incumbent-centric C-16 density (V-03) | Per-stage INCUMBENT EQUIVALENT drives full C-16 compliance | **CONFIRMED** — V-03 achieves 17/17 including C-16 PASS; per-stage co-location of incumbent context produces the most reliable all-entries MS-NN citation design |
| H4 — Combined axes compound (V-04) | Net C-24 gap wider than either axis alone | **CONFIRMED** — 5 PARTIAL vs V-01's 3 and V-02's 2; axes do not cancel |
| H5 — Role-separated T-01 quality (V-05) | Operations-only T-01 drives richer C-15 content; Commerce cross-role citation passes C-16 | **CONFIRMED** — V-05 achieves 17/17; Scaffold Architect isolation achieves strongest C-24 design; cross-role T-01 citation requirement confirmed as structurally sound |

---

## Excellence Signals (V-03 — top single-axis design)

1. **Incumbent co-location as C-16 guarantee**: By requiring an INCUMBENT EQUIVALENT block at each stage, V-03 places the MS-NN step identifier immediately above the content it protects. When the recovery audit table (T-10) is written, the model has just seen each MS-NN step six times — once per stage. This structural repetition is the mechanism behind full C-16 compliance. Recovery entries don't require a lookup to T-01; they discharge a debt already accumulated at the stage level.

2. **T-01 as upstream reference for stage trace tables**: V-03's scaffold declares T-03–T-08 upstream references as "T-01, T-02" — every stage table structurally depends on the incumbent baseline. This means C-24 cross-table reference resolution is bidirectional: the scaffold tells the reader that every stage trace cites both the incumbent and the entity vocabulary. No other variation achieves this scaffold dependency pattern.

3. **Recovery-as-reversion framing eliminates ambiguity**: The "On [condition], revert to [MS-NN]" sentence template converts C-16's abstract "all recovery prescriptions cite step-level" requirement into a syntactic constraint. A recovery entry that fails the template is structurally malformed, not just semantically incomplete. This framing closes the gap between C-14 ("at least one") and C-16 ("every entry") without additional enforcement language.

**V-05 unique contributions** (tied for top score, distinct mechanism):
- Scaffold Architect role isolation prevents domain content from contaminating the scaffold — the cleanest C-24 production pattern across all rounds
- Operations-only T-01 authorship maximizes expected C-15 quality (domain expert dedicating an entire pass to incumbent steps produces richer actor/timing specifics)
- Cross-role citation (Commerce cites Operations' T-01 without having authored it) is the first design to test C-16 compliance under information transfer rather than within-author recall

---

## Rubric Validation Conclusion

**v10 is validated by Round 12.** No scoring behavior emerges that requires a C-25:

- Phrasing-register decay (H1) is fully captured by C-24 PARTIAL (upstream references sparse), C-16 PARTIAL (enforcement weakened), and C-12 PARTIAL (verification clause degraded)
- Boundary pre-commitment stub-update failure (H2) is captured by C-17 and C-20 PARTIAL
- Incumbent-centric C-16 density (H3) is captured by C-16 PASS/PARTIAL gradient
- Role-separated T-01 quality (H5) is captured by C-15 quality expectations already in the pass condition

The per-stage INCUMBENT EQUIVALENT block is a prompt mechanism for achieving C-14/C-16, not a separately scorable behavior — the rubric correctly scores the result (all entries with MS-NN citations) rather than the implementation path. **v10 = v9 = validated across three rounds.**

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
