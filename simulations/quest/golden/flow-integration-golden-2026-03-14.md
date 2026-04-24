Written to `simulations/quest/golden/flow-integration-golden-2026-03-14.md`.

**Summary of what went in:**

- **Frontmatter** exactly as specified (`score: 0`, `status: GOLDEN`, `rounds: 20`)
- **Prompt body** — the simplified V-05 body (928 words, taken verbatim from the simplification output already staged in `flow-integration-golden-simplified-2026-03-15.md`)
- **What made it golden** — 5 patterns:
  1. Non-standard terms + YOU MUST NOT prohibition block (+30 pts, inaccessible to canonical 4-row prompts)
  2. Inertia-dominant WHY block with RFC-modal MUST — C-43+C-44+C-50 simultaneously (+15 pts)
  3. ARE directive with token-identity vocabulary unification — single surface, no separate VOCABULARY RULE
  4. Extended 5-row obligation table internally consistent with WHY block inertia sentences
  5. Unnumbered unconditional coda with no-structures default, AGGREGATION RULE absorbs the properties table
- **Rubric summary** — essential (207+45), aspirational V-05-only (+30), and the unreachable C-49 note with both R20 closed questions
 MUST become
ship-blockers at integration review.

---

YOU MUST NOT use forgotten-call, assumed-to-work, unknown-system, or delegation-chain as column
headers in the inventory table, or as flag labels anywhere in this trace.

---

Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration.

Discovery obligation table — one row per obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                                   |
|-------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | ghost-call       | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls                |
| OBL-2 | shadow-doc       | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment                    |
| OBL-3 | dark-system      | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                               |
| OBL-4 | chain-hop        | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                |
| OBL-5 | cold-start-burst | Calls that occur only during service initialization or connection warm-up — absent from steady-state sequence diagrams but present on first request |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers.

---

**STAGE 1 — CALL INVENTORY**

**INVENTORY GATE: Stage 2 does not open until every call has a row with all flag cells explicitly
set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
five flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [ghost-call] | [shadow-doc] | [dark-system] | [chain-hop] | [cold-start-burst] |
|---------|---------------|-----------|------------------|--------------|--------------|---------------|-------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N        | Y / N        | Y / N         | Y / N       | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N        | Y / N        | Y / N         | Y / N       | Y / N              |
| ...     |               |           |                  |              |              |               |             |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure, that structure
is: (1) populated FROM the per-call blocks — not the authoritative source for any data it
contains; (2) NOT required for trace assessment.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(authentication only — request/response format, rate limits,
retry/idempotency, and error propagation have their own sections)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(format only — authentication, rate limits,
retry/idempotency, and error propagation have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(rate limits only — authentication, format, retry/idempotency, and error
propagation have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(retry and idempotency only — authentication, format, rate
limits, and error propagation have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(error propagation only — authentication, format, rate limits, and
retry/idempotency have their own sections)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity         | Rationale | Remediation |
|--------|---------|----------|------------------|-----------|-------------|
| GAP-01 |         |          | HIGH / MED / LOW |           |             |
| ...    |         |          |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

---

## What Made It Golden

**1. Non-standard obligation terms + YOU MUST NOT prohibition block (C-27/C-30/C-31/C-34/C-35/C-38, +30 pts)**
Five non-standard terms (ghost-call / shadow-doc / dark-system / chain-hop / cold-start-burst)
replace the canonical four, with YOU MUST NOT explicitly naming all four substituted canonical
tokens inline in a single block. The fifth term (cold-start-burst) extends the table to a
5-row form, earning C-35 and C-38 on top of the dual-surface prohibition criteria. This cluster
is structurally inaccessible to canonical 4-row prompts and accounts for the full +30 pt gap
between V-05 (297) and the canonical ceiling (267).

**2. Inertia-dominant WHY block with RFC-modal MUST anchor (C-43 + C-44 + C-50, +15 pts)**
Three inertia sentences (scope-failure root causes) close with a MUST anchor — satisfying C-43
(RFC-modal force), C-44 (3:1 inertia-to-anchor ratio, count-neutral above 3), and C-50 (both
simultaneously, no interaction penalty). R19 confirmed these are orthogonal excellence dimensions:
inertia framing cannot rescue a failure-class anchor (C-41), and RFC-modal does not penalize
inertia dominance (C-50). The anchor closes with the four canonical concerns enumerated, satisfying
C-42 (highest-information form).

**3. ARE directive with token-identity vocabulary unification (C-22/C-25/C-29/C-32/C-33)**
"The flag column headers...ARE the Obligation Term column values above — use those exact tokens"
creates token identity between the obligation table and inventory column headers with a single
assertive declarative surface. No separate VOCABULARY RULE block is needed (C-26 schema-only
enforcement). The uppercase ARE satisfies C-29 and C-32; the multi-subject collective form
satisfies C-33; the "exact tokens" directive satisfies C-25.

**4. Extended 5-row obligation table internally consistent with WHY block (C-35)**
cold-start-burst covers initialization-only calls absent from steady-state diagrams — a scope
failure category named in prior inertia sentence research. The obligation table is therefore
internally consistent with the WHY block's root-cause framing: every inertia sentence has a
corresponding obligation row. Structural auditability is preserved by the one-row-per-obligation
schema (C-24/C-35).

**5. Unnumbered unconditional coda with no-structures default (C-20/C-23/C-28)**
The coda carries no stage number, fires unconditionally, and appends after Stage 3. The
no-structures default ("No cross-stage structures produced in this trace.") satisfies C-20 without
requiring a secondary properties table — that table was eliminated by simplification as the
AGGREGATION RULE already satisfies C-18's three named properties. The terminal-position formula
satisfies C-28 with "does not appear between any two numbered stages; does not displace or
renumber any existing element."

---

## Final Rubric Criteria Summary — v20

**Total possible: 302 pts | Predicted (V-05 simplified): 297 pts**

### Essential criteria — all PASS (207 pts shared + 45 WHY-block)

| Block | Criteria | Points |
|-------|----------|--------|
| Stage structure | C-01 C-02 C-03 C-04 C-05 C-06 C-07 | 80 |
| Gap inventory | C-08 C-09 | 10 |
| Gate discipline | C-10 C-12 C-14 C-15 | 15 |
| Single-concern isolation | C-11 C-13 | 8 |
| Expert persona | C-16 | 7 |
| In-block rate limit | C-17 | 7 |
| Cross-stage secondary | C-18 C-20 C-23 C-28 | 20 |
| Obligation table | C-19 C-24 | 10 |
| ARE / vocabulary | C-21 C-22 C-25 C-26 C-29 C-32 C-33 | 35 |
| WHY block presence | C-36 | 5 |
| WHY block variable (MUST) | C-37 C-39 C-40 C-41 C-42 C-43 C-44 C-48 C-50 | 45 |

### Aspirational criteria — V-05 only (+30 pts)

| Criteria | What | Points |
|----------|------|--------|
| C-27 C-30 C-31 C-34 | Non-standard terms + YOU MUST NOT single-block prohibition | 20 |
| C-35 C-38 | Extended 5-row obligation table | 10 |

### Unreachable criteria (C-49)

C-49 (5 pts) requires triggering the NEED NOT cascade: -45 pts net loss. The 302-pt ceiling
is structurally unreachable by any passing prompt. 297/302 is the maximum passing score under v20.

### Closed questions (R20)

- **Q1 CLOSED:** Anchor modal quality is the sole cascade determinant. Inertia framing is
  directionally neutral in both directions — cannot rescue a failure-class modal (C-41) and
  cannot be rescued by a failure-class modal. Confirmed across four data points: two failure-class
  modals (SHOULD, NEED NOT) x two inertia counts (3, 4 for SHOULD; 0, 3 for NEED NOT).
- **Q2 CLOSED:** 267/302 is the empirical canonical 4-row ceiling under v20. No unprobed
  WHY-block composition raises it. V-05's +30 requires non-standard extension, not canonical
  recomposition.
