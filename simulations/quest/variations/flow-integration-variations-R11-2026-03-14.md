Written to `simulations/quest/rubrics/flow-integration-rubric-v11-variations-R11-2026-03-15.md`.

---

# flow-integration — R11 Variations (v11 rubric, 212 pt ceiling)

**Open questions under test:**
- **Q1 (C-32)**: IS per-item assertive form vs. multi-subject ARE form
- **Q2 (C-31)**: Partial inline enumeration (3-of-4 tokens) vs. full enumeration

---

## Axes selected

| # | Axis | Type | Hypothesis |
|---|------|------|-----------|
| V-01 | C-32 per-item IS form | Single-axis (Q1 probe) | IS in assertive sentence satisfies C-32 |
| V-02 | C-31 partial inline enumeration 3-of-4 | Single-axis (Q2 probe) | Partial enumeration satisfies C-31 |
| V-03 | Lifecycle emphasis — expanded stage rationale | Single-axis (neutrality probe) | Lifecycle commentary additions are structurally neutral |
| V-04 | IS form + partial enumeration | Combined (Q1+Q2 joint) | Both open questions resolve positively |
| V-05 | Phrasing register shift — imperative/action | Combined confirming (clean sweep) | Register variation is structurally neutral |

---

## Score predictions

| Variation | Pass | Fail | Delta |
|-----------|------|------|-------|
| V-01 | 212/212 if IS satisfies C-32+C-29 | 202/212 (−5 C-29, −5 C-32) if only ARE satisfies |
| V-02 | 212/212 if partial satisfies C-31 | 202/212 (−5 C-27, −5 C-31) if full required (prohibition surface incomplete for omitted token — C-27 also fails) |
| V-03 | 212/212 — confirming | No criterion exposure expected |
| V-04 | 212/212 if both pass | 202/212 (−5 C-29/C-32) or (−5 C-27/C-31) per failing axis; 192/212 if both fail |
| V-05 | 212/212 — confirming | No criterion exposure expected |

---

## V-01 — C-32 Per-Item IS Form (Q1 Probe)

**Axis**: C-32 assertive form variants — `IS` in a per-item assertive sentence instead of `ARE` in a multi-subject assertive sentence.

**Hypothesis**: `Each flag column header in the Stage 1 inventory table IS one of the Obligation Term values from the obligation table above` satisfies C-32 because IS is an uppercase assertive identity verb equivalent to ARE in this position. If C-29 allows any uppercase assertive identity verb (not only ARE), scores 212/212. If only multi-subject ARE satisfies, scores 202/212 (−5 C-29, −5 C-32). C-26 is expected to survive in either outcome — the schema-only enforcement mechanism is present; only the specific verb form is under test.

Canonical obligation terms. C-27/C-30/C-31 N/A.

---

```
You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

Each flag column header in the Stage 1 inventory table IS one of the Obligation Term values from
the obligation table above — use those exact tokens as column headers. A column header that does
not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing
this table to the Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do
not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate
limits, retry/idempotency, and error propagation each have their own sections below)*
...
**[N.5] ERROR PROPAGATION** *(this section: error propagation only — ...)*
...

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:
| Authentication documented | [] |  | Request/response documented | [] |  ... | Error propagation documented | [] |

---

**STAGE 3 — GAP INVENTORY**
...

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.
```

*(Full prompt in file — schema instruction is the only axis change.)*

---

## V-02 — C-31 Partial Inline Enumeration (Q2 Probe)

**Axis**: C-31 enumeration completeness — single YOU MUST NOT block names 3 of 4 non-standard tokens inline; fourth token (relay-chain) not named.

**Hypothesis**: `YOU MUST NOT use footprint-call, implicit-pass, or ghost-system as column headers or obligation names in this trace` satisfies C-31 despite omitting relay-chain. If partial satisfies: 212/212. If all required: 202/212 (−5 C-27, −5 C-31) — prohibition surface is incomplete for relay-chain; C-27's self-contained coverage requirement also fails.

Non-standard terms: `footprint-call / implicit-pass / ghost-system / relay-chain`. Uppercase ARE (C-29/C-32 confirmed pass). YOU MUST NOT block: single, names first three, omits relay-chain.

---

*Key structural change from baseline — the YOU MUST NOT block:*

```
YOU MUST NOT use footprint-call, implicit-pass, or ghost-system as column headers or
obligation names in this trace.
```

*(Full prompt in file.)*

---

## V-03 — Lifecycle Emphasis Expansion (Structural Neutrality Probe)

**Axis**: Lifecycle emphasis — each stage opens with an explicit rationale paragraph naming the stage's purpose, failure mode it guards against, and why the gate constraint exists.

**Hypothesis**: Rationale paragraphs are prose-only additions; no schema instruction, no obligation term, no format directive is added or changed. Expected: 212/212. Confirms lifecycle emphasis is a free variation axis.

Canonical terms. Uppercase ARE. No YOU MUST NOT block.

---

*Key addition — stage preamble (Stage 1 example):*

> Stage 1 exists because a trace that begins with per-call analysis is a product summary, not an integration trace. The specification names the calls the author thought of; Stage 1 names the calls the system will actually make. The inventory gate enforces the separation: per-call analysis in Stage 2 cannot begin until the complete call surface is known.

*(Full prompt in file — rationale blocks precede each stage header.)*

---

## V-04 — Combined: IS Form + Partial Enumeration (Q1+Q2 Joint Probe)

**Axis**: Combined — IS per-item assertive form (V-01 axis) plus partial inline enumeration 3-of-4 (V-02 axis) with non-standard terms.

Non-standard terms: `footprint-call / implicit-pass / ghost-system / relay-chain`. Schema instruction: IS form. YOU MUST NOT block: single, names footprint-call + implicit-pass + ghost-system, omits relay-chain.

**Score matrix:**

| Q1 (IS) | Q2 (partial) | Score |
|---------|-------------|-------|
| PASS | PASS | 212/212 |
| FAIL | PASS | 202/212 (−5 C-29, −5 C-32) |
| PASS | FAIL | 202/212 (−5 C-27, −5 C-31) |
| FAIL | FAIL | 192/212 (−5 C-27, −5 C-29, −5 C-31, −5 C-32) |

*(Full prompt in file.)*

---

## V-05 — Phrasing Register Shift (Confirming, Clean Sweep)

**Axis**: Phrasing register — imperative/action-oriented register replaces descriptive-formal preamble language throughout. Structural architecture is identical to confirmed-pass baseline.

Selected register changes:

| Old (descriptive-formal) | New (imperative-directive) |
|--------------------------|---------------------------|
| "Discovery obligation table" | "Your four discovery commitments" |
| "Populate this table before opening Stage 2" | "Build this inventory now" |
| "STAGE 1 — CALL INVENTORY" | "STAGE 1 — BUILD THE CALL INVENTORY" |
| "STAGE 2 — PER-CALL ANALYSIS" | "STAGE 2 — TRACE EVERY CALL" |
| "STAGE 3 — GAP INVENTORY" | "STAGE 3 — NAME EVERY GAP" |

**Hypothesis**: Register is structurally neutral — no criterion is phrasing-sensitive at the schema or schema-instruction level. Expected: 212/212.

Canonical terms. Uppercase ARE. No YOU MUST NOT block. Full structure intact.

*(Full prompt in file.)*

---

## Structural decisions for R11

**Q1 isolation (V-01)**: Uses canonical terms so C-27/C-30/C-31 do not fire. The only criterion under test is whether IS satisfies C-32 (and by implication C-29). If IS fails, the failure is localized to the verb form; C-26 is expected to survive because schema-only enforcement is present.

**Q2 isolation (V-02)**: Uses non-standard terms with uppercase ARE so C-29/C-32 are at confirmed PASS. The fourth non-standard token (relay-chain) is absent from the YOU MUST NOT block. If C-27 requires the prohibition surface to cover every substituted token, relay-chain's absence fails both C-27 and C-31 simultaneously — the same joint failure observed when table-reference shorthand was used in R10 V-01.

**V-03 neutrality confirmation**: The lifecycle expansion adds the most text of any variation. If a structurally-neutral prose addition triggered a criterion, it would invalidate the "structure-only" interpretation of the rubric. Expected 212/212 closes this as a confound.

**V-05 register confirmation**: Establishes that imperative register is safe for future high-conversion-rate prompt engineering work on this skill.
