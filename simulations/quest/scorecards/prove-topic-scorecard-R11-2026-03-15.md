## Round 11 — prove-topic Scoring (v10 rubric)

---

### Scoring Framework Recap

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01 – C-05 | 10 | 50 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-33 | 4 | 100 |
| **Total** | | | **180** |

---

## V-01 — Inertia Framing

### Essential (50/50)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 All stages present | PASS | All five stages + GATE S + ROLE A/B + CAMPAIGN OPEN present |
| C-02 Scout artifact loaded | PASS | ROLE B loads `{topic}-scout-record-{date}.md` before Stage 1 |
| C-03 Progressive artifact writes | PASS | One write per stage: hypothesis → websearch → intelligence → analysis → synthesize |
| C-04 Synthesis readiness signal | PASS | "Evidence brief ready for topic-story." in Stage 5 confirm |
| C-05 Artifact naming consistent | PASS | Every write instruction: `{topic}-[artifact]-{date}.md` |

### Recommended (30/30)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-06 Stage order enforced | PASS | Forward-only sequence; each stage requires prior CLOSE confirmation |
| C-07 Scout signal handoff explicit | PASS | Named anchor in hypothesis frontmatter: `scout_anchor: {topic}-scout-record-{date}.md` |
| C-08 Synthesis signals topic-story | PASS | `next: topic-story` in handoff; named in synthesis confirm |

### Aspirational (100/100)

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-09 Thin-evidence acknowledgment propagates | PASS | 4 | Per-stage null tally; Stage 5 explicitly addresses null CE result |
| C-10 Progress narrated per stage | PASS | 4 | Detailed confirm lines per stage with findings summary |
| C-11 Hypothesis hard-gated on scout | PASS | 4 | GATE S blocks Stage 1; `gate_s_cleared: true` required |
| C-12 Comparator anchored at session open | **PASS** | **4** | INCUMBENT THREAT BLOCK at CAMPAIGN OPEN; explicit INCUMBENT CHECK at Stages 2, 3, and 4; Stage 4 asks "does evidence make a credible case for displacing {incumbent}?" |
| C-13 Per-artifact path enforcement | PASS | 4 | Every write instruction names full path |
| C-14 Counter-evidence unconditionally required | PASS | 4 | "MANDATORY SECTION. Counter-evidence is unconditionally required." with null fallback |
| C-15 Gate clearance in hypothesis frontmatter | PASS | 4 | `gate_s_cleared: true [ROLE B — sole source]` in frontmatter |
| C-16 Null CE triggers adversarial escalation | PASS | 4 | If null: SESSION INVARIANT A fires as "pre-committed obligation" |
| C-17 Confidence mechanically capped | PASS | 4 | SESSION INVARIANT B: CE-score = -2 locks confidence at MEDIUM |
| C-18 Null CE synthesis doubly locked | PASS | 4 | ATOMIC DUAL-LOCK activates both simultaneously; `co_activation_confirmed` required |
| C-19 Full null-CE protocol pre-committed | PASS | 4 | SESSION INVARIANT A + B at CAMPAIGN OPEN with "cannot be modified or bypassed at synthesis" |
| C-20 Per-stage null tally with protocol ref | PASS | 4 | Running tally at each stage; "SESSION INVARIANTs A and B active as pre-committed obligations" |
| C-21 Co-activation echoed into handoff | PASS | 4 | `co_activation_confirmed: [must equal dual_lock_fired]` in handoff block |
| C-22 Invariant registry as distinct gate field | PASS | 4 | `invariant_registry_confirmed: true [ROLE A — sole source]` in hypothesis frontmatter; GATE S requires both |
| C-23 Campaign-outcome boolean independent | PASS | 4 | `incumbent_defense_closed` separate from `co_activation_confirmed` in handoff |
| C-24 Role-structural dual attestation | PASS | 4 | ROLE A produces `invariant_registry_confirmed` only; ROLE B produces `gate_s_cleared` only |
| C-25 Handoff fields carry inline derivation | PASS | 4 | SESSION INVARIANT C; all 9 fields carry `[derived from: X]` with format-error consequence |
| C-26 Handoff schema pre-committed at CAMPAIGN OPEN | PASS | 4 | 9-field schema table at CAMPAIGN OPEN; `schema_compliance_confirmed` field in schema |
| C-27 Independence path chain on campaign-outcome | PASS | 4 | `positive_derivation:` and `independence_chain: NOT dual_lock_fired; NOT co_activation_confirmed` on `incumbent_defense_closed` |
| C-28 Symmetric independence chains both lock fields | PASS | 4 | Both `incumbent_defense_closed` and `co_activation_confirmed` carry `positive_derivation:` + `independence_chain:` |
| C-29 Per-stage schema integrity counts | PASS | 4 | SCHEMA INTEGRITY NOTE at Stages 2, 3, 4: "9/9 — 0 additions, 0 omissions, 0 source mismatches" |
| C-30 Derivation annotation rule as session invariant | **PASS** | **4** | "SESSION INVARIANT C — Derivation Annotation: … Invariant language: pre-registered — cannot be modified or bypassed at synthesis." |
| C-31 Per-stage CE verdict as owned schema field | PASS | 4 | CE VERDICT OWNERSHIP TABLE at CAMPAIGN OPEN; `null_tally_final` derivation formula names `{s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}` explicitly |
| C-32 Counter-hypothesis declared S1, closed S5 | PASS | 4 | `counter_hypothesis:` field at Stage 1 as "incumbent's voice"; COUNTER-HYPOTHESIS RESOLUTION at Stage 5 with REFUTED/PARTIALLY REFUTED/OPEN RISK; OPEN RISK reduces confidence one tier |
| C-33 Null tally chain in ATOMIC DUAL-LOCK | PASS | 4 | NULL TALLY CHAIN RULE at CAMPAIGN OPEN; chain S2→N, S3→N, S4→N=null_tally_final with cross-check inside ATOMIC DUAL-LOCK |

**V-01 Total: 180/180**

---

## V-02 — Table-Dominant Format

### Essential / Recommended: 80/80 (all PASS — same as V-01)

### Aspirational Differences from V-01

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-12 Comparator anchored at session open | **PARTIAL** | **2** | `status_quo_comparator` named at CAMPAIGN OPEN but no dedicated per-stage incumbent column or INCUMBENT CHECK at Stages 2, 3, 4; CE-RELEVANT column implicitly tracks displacement but incumbent not named at each stage |
| C-30 Derivation annotation rule as session invariant | PASS | 4 | SESSION INVARIANT C in the INVARIANTS table with "Cannot be modified or bypassed at synthesis." |
| All other aspirational (C-09–C-11, C-13–C-29, C-31–C-33) | PASS | 4 each | Table format cleanly encodes all structural obligations; NULL TALLY CHAIN table in Stage 5; independence chains compressed but complete in handoff row |

**V-02 Aspirational: 98/100**
**V-02 Total: 178/180**

---

## V-03 — Lifecycle Emphasis (ENTER/WORK/CLOSE)

### Essential / Recommended: 80/80 (all PASS)

### Aspirational Differences from V-01

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-12 Comparator anchored at session open | **PARTIAL** | **2** | Incumbent explicitly loaded at Stage 2 ENTER ("Load: incumbent from CAMPAIGN OPEN") and referenced in Stage 2 WORK ("Incumbent comparator: [from CAMPAIGN OPEN]"); absent from Stage 3 ENTER/WORK and Stage 4 WORK sections |
| C-30 Derivation annotation rule as session invariant | PASS | 4 | "SESSION INVARIANT C — Derivation Annotation: … Invariant language: pre-registered — cannot be modified or bypassed at synthesis." |
| All other aspirational | PASS | 4 each | ENTER/WORK/CLOSE structure enforces verdict recording in CLOSE before confirmation; all per-stage null tally and schema integrity notes appear in CLOSE sections; Stage 5 CLOSE has synthesis summary |

**V-03 Aspirational: 98/100**
**V-03 Total: 178/180**

---

## V-04 — Phrasing Register + Numbered Gate

### Essential / Recommended: 80/80 (all PASS)

### Aspirational Differences

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-12 Comparator anchored at session open | **PARTIAL** | **2** | Stage 2 has "CE = evidence that the incumbent already does what {topic} claims"; Stages 3 and 4 work sections do not explicitly reference the incumbent by name |
| C-30 Derivation annotation rule as session invariant | **PARTIAL** | **2** | "Annotation rule: Every field in the final handoff must say [derived from: X]. Missing label = format error. You will execute this rule at synthesis." — no "SESSION INVARIANT C" naming; "You will execute" is weaker than "cannot be modified or bypassed"; contrast with confidence rule which explicitly says "You cannot override this at synthesis" |
| All other aspirational (C-09–C-11, C-13–C-29, C-31–C-33) | PASS | 4 each | Second-person imperative register fully compatible with all structural obligations; Step 1/Step 2/Step 3 checklist satisfies role-structural dual attestation (C-24); "Dual-Lock Section" satisfies C-18/C-33 despite renamed header; sole-producer language intact ("Only you produce this field") |

**V-04 Aspirational: 96/100**
**V-04 Total: 176/180**

---

## V-05 — All Four Combined

### Essential / Recommended: 80/80 (all PASS)

### Aspirational Differences

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-12 Comparator anchored at session open | **PASS** | **4** | INCUMBENT THREAT BLOCK at CAMPAIGN OPEN with `incumbent_strength` + `incumbent_vulnerability`; Stage 2 WORK table adds "ADDRESSES INCUMBENT?" column; Stage 3 WORK has INCUMBENT CHECK; Stage 4 WORK asks "does the evidence make a credible case against {incumbent}?" and "Does CE strengthen {incumbent}?" — explicit at all three evidence stages |
| C-30 Derivation annotation rule as session invariant | **PARTIAL** | **2** | Lock-Rules table has "Annotation rule | Every handoff field carries [derived from: X]. Missing = format error." with overall "Everything above is locked. Do not modify." — no "SESSION INVARIANT C" label; "locked. Do not modify." applies generally; no specific "cannot be bypassed" on the annotation rule row (contrast: confidence cap row has "Cannot be overridden") |
| All other aspirational (C-09–C-11, C-13–C-29, C-31–C-33) | PASS | 4 each | Table format + ENTER/WORK/CLOSE + incumbent framing + conversational register cohere; sole-producer language intact in Step 1/Step 2; NULL TALLY CHAIN table in Dual-Lock section; both independence chains present in compressed handoff table rows |

**V-05 Aspirational: 98/100**
**V-05 Total: 178/180**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | **Total** | Key Partials |
|-----------|-----------|-------------|--------------|-----------|--------------|
| V-01 | 50 | 30 | 100 | **180** | — |
| V-02 | 50 | 30 | 98 | **178** | C-12 |
| V-03 | 50 | 30 | 98 | **178** | C-12 |
| V-04 | 50 | 30 | 96 | **176** | C-12, C-30 |
| V-05 | 50 | 30 | 98 | **178** | C-30 |

**Rank:** V-01 > V-02 = V-03 = V-05 > V-04

---

## Excellence Signals from V-01

V-01 achieves the perfect score by satisfying C-12 (per-stage comparator reference) at all three evidence stages through its INCUMBENT THREAT BLOCK architecture. Two patterns emerge that exceed existing v10 criteria:

**Pattern 1 — Incumbent decomposed into named dimensions at CAMPAIGN OPEN.**
V-01 does not merely name the comparator; it captures `incumbent_strength` (why the incumbent is currently winning) and `incumbent_vulnerability` (where it is weakest) as distinct CAMPAIGN OPEN fields. Per-stage INCUMBENT CHECKs then route evidence findings against these two sub-fields, enabling Stage 4's displacement assessment (STRONG/MODERATE/WEAK) to be grounded in specific incumbent-model dimensions rather than a single undifferentiated judgment. Not captured by C-12, which only requires the comparator to be named.

**Pattern 2 — Synthesis findings tagged by displacement dimension.**
"The Case Against {incumbent}" at Stage 5 requires each finding to be tagged as addressing `incumbent_strength`, `incumbent_vulnerability`, or being "neutral to displacement." This maps evidence to the incumbent model declared at CAMPAIGN OPEN, making the campaign outcome structurally auditable: a synthesis claiming STRONG displacement with all findings tagged "neutral to displacement" would be an immediate structural inconsistency. Not captured by any existing criterion.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Incumbent decomposed into named strength/vulnerability fields at CAMPAIGN OPEN, enabling per-stage evidence classification against specific incumbent dimensions rather than generic displacement", "Synthesis findings tagged by displacement dimension (addresses incumbent_strength / incumbent_vulnerability / neutral) making the case-against-incumbent structurally auditable from the evidence-to-incumbent-model mapping"]}
```
