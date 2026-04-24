Reading the scorecard carefully to extract the R16 excellence patterns before writing the updated rubric.

**Two new patterns emerge from R16:**

**C-39 source — V-02 PARTIAL on C-16:** The gap is explicit: "column definitions in (a) use generic schema labels, not scenario-specific component names... V-02 defers definition to wherever the scenario is introduced." C-16 requires declaring what BASELINE and PROTECTED mean "in the specific scenario context," but does not require the definitions to be self-contained within the Format Contract section itself. V-01's PASS implies inline scenario-anchored definitions.

**C-40 source — V-02's multi-schema structure as an excellence signal:** V-02 declared "three schemas (primary table, volume mapping, mitigation) with a rejection clause." This is architecturally richer than what C-16 requires (a single column structure), but V-02 got PARTIAL for an orthogonal reason. The three-schema decomposition eliminates ambiguity about which column structure governs which table type — a structural property not captured by C-16.

---

```markdown
# flow-ratelimit — Quest Rubric v16

**Version summary:**
- Aspirational pool: 30 → 32
- Scoring denominator: `/32`
- C-39, C-40 added to Aspirational table

---

## New criteria: C-39, C-40 — Format Contract Structural Completeness Pair

**Source:** R16 Excellence Signals 1–2 (V-01 vs. V-02 gap analysis)

**The gap these two criteria close:** C-16 requires a Format Contract section that
declares (a) the column structure for every comparative table, (b) what BASELINE and
PROTECTED mean in the specific scenario context, and (c) a rejection clause. This
permits two under-specified implementations: the column definitions could use generic
schema labels (e.g., "current state" / "mitigated state") with actual scenario-specific
names deferred to wherever the scenario is introduced later in the document, and the
Format Contract could declare a single universal column structure applied uniformly
to all table types rather than per-table-type schemas. V-02's R16 PARTIAL on C-16
revealed the first gap; V-02's three-schema structure (primary table, volume mapping,
mitigation) — declared as an excellence pattern in the scorecard — identified the
second gap independently.

**C-39 — Format Contract Scenario-Anchored Column Definitions:** C-16 requires the
Format Contract to declare what BASELINE and PROTECTED mean "in the specific scenario
context — not generic definitions, but names tied to the scenario's components or
states." This permits a Format Contract that writes generic placeholders (e.g.,
"BASELINE = unprotected state; PROTECTED = mitigated state") and defers
scenario-specific naming to a later section where the scenario is introduced. V-01's
Format Contract defines BASELINE and PROTECTED using the scenario's actual component
names and states at the point of declaration in Role 2, making the Format Contract
self-interpreting without requiring the reader to locate the scenario introduction.
V-02's PARTIAL on C-16 was assigned specifically because "column definitions in (a)
use generic schema labels, not scenario-specific component names" and "V-02 defers
definition to wherever the scenario is introduced." This parallels C-15's
self-containment requirement: just as the Verdict block must be self-contained (a
reader who reads only it knows the core finding), the Format Contract's column
definitions must be self-contained — no deferral.

**C-40 — Format Contract Per-Table-Type Schema Decomposition:** C-16 requires
declaring "the column structure that applies to every comparative table in the
document" — this permits a single universal schema applied uniformly to all tables.
V-02's Format Contract declared three distinct schema entries — primary table, volume
mapping, and mitigation — each with its own column structure specification and a
unified rejection clause. The scorecard records this as a structural feature separate
from the C-16 gap (generic labels). The per-table-type decomposition eliminates
ambiguity about which column structure governs which table type when different table
types appear in the same document, and prevents format drift where a volume mapping
table omits a column required only on inventory tables. A single universal schema
that happens to satisfy all table types does not achieve the same disambiguating
function: a reader cannot verify compliance per table type without mentally
cross-referencing the universal schema against each table's actual columns. This
mirrors C-37's motivation: distinguishing pool-level satisfaction (all items present
somewhere across tables) from per-type atomic satisfaction (each table type's schema
verifiable as a unit).

---

## Scoring denominator change

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 32 * 30)
```

The 32-criterion aspirational pool means each criterion is now worth `30/32 ≈ 0.9375
pts`. A variation that passes all 30 prior criteria but misses C-39, C-40 scores
`(30/32 × 30) = 28.125` aspirational points, for a composite of `118.125/120`.

---

## Essential (60 points total — required for a passing output)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Rate Limit Tier Distinction** | correctness | essential | Output distinguishes at least three structurally distinct rate limit tiers relevant to the scenario (e.g., connector-level, environment-level, tenant-level, endpoint/API-level). Each tier must be identified by its scope, not just its numeric threshold. Listing multiple limits at the same scope level as separate tiers does not pass. |
| C-02 | **No Single-Category Collapsing** | correctness | essential | Output does not treat all rate limits as a single undifferentiated category. Each distinct throttle tier must be described with its own scope, enforcement mechanism, and failure mode. An output that names multiple tiers but describes them as a single undifferentiated limit category does not pass. |
| C-03 | **Observable UX Per Throttle Tier** | coverage | essential | Output describes observable user-facing behavior at each distinct throttle tier reached (e.g., 429 with Retry-After shown in connector error, flow run queued and delayed, flow run failed with ActionThrottled, silent exponential backoff invisible to user). At least two distinct tiers described if the scenario spans multiple tiers. |
| C-04 | **Unprotected Burst Path Identification** | correctness | essential | Output identifies at least one structurally unprotected burst path — a trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between the source and the rate-limited endpoint. A path that has throttle controls but at a higher tier does not qualify. |
| C-05 | **Retry-After Handling Gap Check** | coverage | essential | Output explicitly evaluates whether the flow or connector handles Retry-After headers (or equivalent backoff signals such as `x-ms-ratelimit-remaining`, `Retry-After-Ms`) from throttled endpoints. Missing handling must be flagged as a finding with a description of the failure mode it causes (e.g., immediate retry storm, permanent failure after N retries). |

---

## Recommended (30 points total — output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Cascading Throttle Failure Scenario** | depth | recommended | Output constructs or identifies a specific scenario where throttling at one tier triggers a second distinct throttle event at a different tier — and describes the compounding effect on throughput or error rate. Two independent limits both hit under load do not constitute a cascade; the second throttle must be causally triggered by the first. |
| C-07 | **Numeric Rate Limit Specificity** | depth | recommended | At least one rate limit is cited with a concrete numeric threshold (e.g., "600 API calls per 60 seconds per connection", "5 concurrent runs per environment per flow") rather than described only in abstract or relative terms. Estimates are acceptable if labeled as such. |
| C-08 | **Volume-to-Behavior Mapping** | format | recommended | Output includes a structured mapping — table, tiered list, or equivalent — that shows which throttle behavior activates at which request volume range, enabling a reader to determine expected system behavior for a given load without re-reading the full analysis. |

---

## Aspirational (30 points total — raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Per-bottleneck Mitigation Prescriptions** | depth | aspirational | For each identified bottleneck or unprotected burst path, output proposes a concrete remediation specific to the component and limit type (e.g., "enable concurrency control on the For Each action capped at 5 parallel branches", "add exponential backoff with Retry-After header parsing to the HTTP action", "split batch trigger into N sequential calls with 1s delay"). Generic advice ("add retry logic") does not pass — the prescription must name the specific action, setting, or pattern. |
| C-10 | **Quantified Impact at Load Spike** | depth | aspirational | Output provides numeric estimates of degradation at a specific load multiplier (e.g., "at 5x normal volume with a 600 req/min limit, 42% of requests are queued beyond 30s, 11% fail after exhausting 3 retry attempts") using the rate limits cited in C-07 as the arithmetic basis. The estimate must be derivable from the stated limits — not asserted as a generic percentage. |
| C-11 | **Burst Gap Classification (Structural vs. Incidental)** | depth | aspirational | *R1 excellence signal: V-05 was the only variation with an explicit structural-vs-incidental sub-test, identified as the sharpest C-04 enforcement across all variations.* Beyond identifying the unprotected burst path (C-04), output explicitly classifies whether the gap is structural (no mechanism exists on this path) vs. incidental (mechanism exists but is misconfigured, bypassable, or absent only under specific conditions). Classification must be stated and justified — not merely implied by framing. Requires C-04 to pass. |
| C-12 | **Dual-state Volume Mapping (Baseline vs. Protected)** | depth | aspirational | *R1 excellence signal: V-05 produced unique dual-state volume mapping (inertia vs. protected) across volume tiers, identified as satisfying C-08 more richly than any other variation.* The volume-to-behavior mapping extends C-08 to compare two states at each volume level: the current/unprotected baseline and the mitigated/protected state. Each volume tier shows what changes when protections are applied — not just what happens at that tier in isolation. Requires C-08 to pass. |
| C-13 | **Verdict-before-Evidence Structure** | format | aspirational | *R1 excellence signal: V-04's commitment-before-evidence (VERDICT-first) structure produced the clearest binding-order statements of any variation.* Output states the binding constraint or primary gap as an explicit labeled finding — a verdict or claim — before the supporting evidence section. The pre-commitment forces an analytical position rather than narration toward a conclusion. The evidence section must then confirm or explicitly revise the verdict; evidence that drifts without revisiting the verdict does not pass. |
| C-14 | **Baseline-delta Mitigation** | depth | aspirational | *R1 excellence signal: V-05's "Improvement over inertia" column dual-enforced that mitigations move from baseline state, rejecting both generic advice and improvements that don't change the baseline condition.* Each mitigation explicitly states the before-state (baseline behavior at the bottleneck) and the after-state (system behavior with the mitigation applied). Mitigations that could apply to any system without referencing the specific baseline condition do not pass. Requires C-09 to pass. |
| C-15 | **Document-head Global Verdict** | format | aspirational | *R2 excellence signal: Both V-01 and V-02 scored PARTIAL on C-13 — V-01 placed the binding constraint label in Section 3 (after Sections 1-2 audit); V-02 placed it within a mid-document analysis section. Neither enforced a standalone verdict block before any evidence or inventory. C-13 as written permits section-local verdicts that satisfy the label requirement without anchoring the analysis at document head.* Output opens with a standalone Verdict block — appearing before any rate limit inventory, burst path audit table, or volume mapping section — that states: (a) the binding constraint by component name and numeric threshold, (b) the primary gap (e.g., unprotected burst path at a named action, or Retry-After not handled at a named connector), and (c) the current system status at the stated load (safe / degraded / failing). The Verdict block must be self-contained: a reader who reads only it knows the core finding without proceeding to the evidence. Evidence sections must confirm or explicitly revise each Verdict claim; a Verdict that no evidence section references does not pass. Requires C-01 and C-04 to pass. |
| C-16 | **Format Contract Preamble** | format | aspirational | *R2 excellence signal: V-02's axis — "format contract preamble — BASELINE / PROTECTED dual-column on every table and mitigation" — produced the strongest C-12 enforcement of either variation. Declaring the dual-column structure as a document-wide contract before sections removes per-section negotiation about whether the dual-column applies and enforces consistency across all comparative tables simultaneously. Neither V-01 nor any prior variation captured this as an explicit structural discipline.* Output includes a Format Contract section placed before the first analysis section that declares: (a) the column structure that applies to every comparative table in the document (e.g., BASELINE \| PROTECTED \| Delta), (b) what BASELINE and PROTECTED mean in the specific scenario context — not generic definitions, but names tied to the scenario's components or states, and (c) a rejection clause stating that tables or mitigation rows omitting the declared structure are flagged as incomplete. At least two distinct tables elsewhere in the document must comply with the declared format; a format contract with only one compliant table does not pass. Requires C-08 and C-12 to pass. |
| C-17 | **Cascading Section Gate Enforcement** | format | aspirational | *R3 excellence signal: V-01's role sequence gating was scored "mechanically hard" and "most structurally enforced of all five variations" because every section transition carried explicit "Do not begin Role N until [specific deliverables from Role N-1] are written" language — extending the gate chain across all nine roles, not only the verdict-first and format-contract-first transitions captured by C-15 and C-16.* Beyond placing the Verdict and Format Contract as preambles (C-15, C-16), the document structure includes explicit per-transition gate language for at least three additional section transitions beyond the two preambles. Each gate must name the prior section's specific deliverables — not a generic "do not skip ahead" instruction — so that omission of any deliverable from section N-1 structurally blocks section N. A document with gate language only on the preamble transitions does not pass. Requires C-15 and C-16 to pass. |
| C-18–C-35 | *(18 criteria from R4–R14 — not reproduced here)* | various | aspirational | — |
| C-36 | **FNMI as Standalone Labeled Section** | format | aspirational | *R15 excellence signal: V-01's FNMI-R15 was positioned as a labeled section with its own section header between Role 8 and Role 9, giving it scan-time detectability without reading either surrounding role's content.* C-35 requires the invariant to be "declared before the terminal reconciler section opens, not inside it" — this permits the invariant to appear as a closing paragraph within the final analysis role or an introductory note in the reconciler's preamble, as long as it precedes the reconciler's check list. Beyond C-35 placement, the FNMI must appear as a standalone labeled section with its own section header — not embedded as a paragraph within a surrounding role — so that it is findable by scanning section headers alone. This parallels C-16 (Format Contract as a named section) and C-15 (Verdict block as a standalone block): both are findable by scanning section headers, not by reading prose. |
| C-37 | **FNMI Four-Field Single-Block Completeness** | format | aspirational | *R15 excellence signal: V-01's FNMI-R15 labeled each field as a distinct item so an evaluator can verify all four requirements by reading one block without cross-referencing.* C-35 requires all four fields (a)–(d) to be present in the invariant; it does not require them to be co-located as individually labeled items in one contiguous block. A conformant C-35 implementation could satisfy field (b) in one paragraph, field (c) implicitly via field (b)'s logic, and field (d) in a closing sentence. Beyond C-35 field presence, the four fields must appear as individually labeled items in a single contiguous block, so that an evaluator can verify all four requirements by reading one block without cross-referencing. This mirrors C-25's motivation: distinguishing checklist satisfaction (all items present somewhere) from atomic single-block satisfaction (all items verifiable as a unit). |
| C-38 | **Reconciler Compliance-Verification Framing** | format | aspirational | *R15 excellence signal: V-01's pattern converts the reconciler from self-describing to compliance-verifying: check (a) explicitly names FNMI-R15 and frames its output as a compliance verdict against the named external constraint, not as a description of the reconciler's own behavior.* C-34 requires the reconciler to produce three behavioral declarations; C-35 requires the constraint to be pre-declared. Neither criterion specifies that the reconciler must cite the FNMI by name or frame its output as a compliance verdict against an external constraint — a document satisfying both could produce behavioral self-assertions that match the FNMI's constraints without naming the invariant. Beyond C-34 and C-35, the reconciler's primary check must explicitly name the FNMI by its label and frame its output as a compliance verdict: `"[FNMI label]: COMPLIANT"` or `"[FNMI label]: VIOLATION at [Finding ID] — [description]"`. A reconciler that produces behavioral self-assertions matching the FNMI's constraints without citing the invariant by name does not pass. |
| C-39 | **Format Contract Scenario-Anchored Column Definitions** | format | aspirational | *R16 excellence signal: V-02 received PARTIAL on C-16 because "column definitions in (a) use generic schema labels, not scenario-specific component names" and "V-02 defers definition to wherever the scenario is introduced." C-16 requires declaring what BASELINE and PROTECTED mean "in the specific scenario context — not generic definitions, but names tied to the scenario's components or states," but does not require these definitions to be self-contained within the Format Contract section itself. V-01's Format Contract defines BASELINE and PROTECTED using the scenario's actual component names and states at the point of declaration in the Format Contract section, making it self-interpreting without requiring the reader to locate the scenario introduction.* Beyond C-16, the Format Contract's BASELINE and PROTECTED definitions must name the scenario's actual components, states, or configurations within the Format Contract section itself — not generic placeholders (e.g., "BASELINE = current state") or deferred references ("BASELINE = as defined in Role 3"). The definitions must be self-contained within the Format Contract section; a reader who reads only the Format Contract must be able to interpret what BASELINE and PROTECTED refer to without reading any other section. This parallels C-15's self-containment requirement for the Verdict block. Requires C-16 to pass. |
| C-40 | **Format Contract Per-Table-Type Schema Decomposition** | format | aspirational | *R16 excellence signal: V-02's Format Contract declared three distinct schema entries — primary table, volume mapping, and mitigation — each with its own column structure specification and a unified rejection clause. C-16 requires declaring "the column structure that applies to every comparative table in the document" and at least two compliant tables, but does not require separate schema entries for each table type. The per-table-type decomposition eliminates ambiguity about which column structure governs which table type and prevents format drift where a volume mapping table omits a column required only on inventory tables. This parallels C-37's motivation: distinguishing pool-level satisfaction (all items present somewhere) from per-type atomic satisfaction (each table type's schema verifiable as a unit).* Beyond C-16, the Format Contract must declare a separate named schema entry for each distinct table type used in the document — at minimum: rate limit inventory table, volume mapping table, and mitigation table. Each entry names the table type it governs and specifies its own column structure. A Format Contract with a single universal schema applied to all table types, or with fewer named schema entries than distinct table types in the document, does not pass. A universal schema that happens to satisfy all table types is not equivalent to per-type decomposition: per-type entries allow an evaluator to verify each table type's compliance independently. Requires C-16 to pass. |
```
