## prove-topic — Round 9 Scoring (Rubric v8)

---

### Scoring Matrix

All five variations are built on the full v8 stack and claim C-01 through C-27 compliance. I evaluate each criterion from the actual variation text.

---

#### Essential Tier (C-01–C-05, 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** All five stages executed | PASS | PASS | PASS | PASS | PASS |
| **C-02** Scout context loaded | PASS | PASS | PASS | PASS | PASS |
| **C-03** Artifacts written progressively | PASS | PASS | PASS | PASS | PASS |
| **C-04** Terminal output usable | PASS | PASS | PASS | PASS | PASS |
| **C-05** Artifacts discoverable | PASS | PASS | PASS | PASS | PASS |
| **Essential subtotal** | **50** | **50** | **50** | **50** | **50** |

All five: 5/5 essential pass, full 50 pts.

---

#### Recommended Tier (C-06–C-08, 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** Stage order enforced | PASS — "Stages run forward only — no skipping" | PASS — "Forward only — no skipping, no re-running" | PASS — schema + null tally tracked per-stage forward | PASS — "forward only" | PASS |
| **C-07** Scout handoff explicit | PASS — `scout_anchor: {topic}-scout-record-{date}.md` in frontmatter | PASS | PASS | PASS | PASS |
| **C-08** Synthesis → topic-story | PASS — `next: topic-story` | PASS | PASS | PASS | PASS |
| **Recommended subtotal** | **30** | **30** | **30** | **30** | **30** |

All five: 3/3 recommended pass, full 30 pts.

---

#### Aspirational Tier (C-09–C-27, 4 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-09** Thin-evidence propagates | PASS — mandatory CE section, null fallback | PASS | PASS | PASS | PASS |
| **C-10** Progress narrated per stage | PASS — Confirm statement at each stage | PASS | PASS | PASS | PASS |
| **C-11** Hypothesis hard-gated on scout | PASS — GATE S blocking gate before Stage 1 | PASS | PASS | PASS | PASS |
| **C-12** Comparator anchored at session open | **PARTIAL (2)** — comparator at CAMPAIGN OPEN + Stage 2 only; not at Stage 3 or Stage 4 | **PARTIAL (2)** — comparator at CAMPAIGN OPEN; no explicit per-stage references | **PARTIAL (2)** — comparator at CAMPAIGN OPEN; no per-stage references | **PARTIAL (2)** — comparator at CAMPAIGN OPEN; no per-stage references | **PASS (4)** — "every evidence stage compares {topic} against this comparator"; table column `Incumbent Comparator Coverage` at S2/S3; "vs incumbent" at S4 |
| **C-13** Per-artifact path enforcement | PASS — every write names `{topic}-X-{date}.md` | PASS | PASS | PASS | PASS |
| **C-14** Counter-evidence unconditionally required | PASS — "MANDATORY SECTION. Unconditionally required." with null fallback | PASS | PASS | PASS | PASS |
| **C-15** Gate clearance in hypothesis artifact | PASS — `gate_s_cleared: true` + `invariant_registry_confirmed: true` in frontmatter | PASS | PASS | PASS | PASS |
| **C-16** Null CE triggers adversarial escalation | PASS — "Adversarial review required before any promotion decision" | PASS | PASS | PASS | PASS |
| **C-17** Confidence mechanically capped | PASS — "CE-score = -2. Cannot be bypassed." | PASS | PASS | PASS | PASS |
| **C-18** Null CE synthesis doubly locked | PASS — ATOMIC DUAL-LOCK with both locks | PASS | PASS | PASS | PASS |
| **C-19** Protocol pre-committed at CAMPAIGN OPEN | PASS — SESSION INVARIANT A + B with "cannot be modified or bypassed" | PASS | PASS | PASS — also adds INVARIANT C | PASS |
| **C-20** Per-stage null tally with protocol ref | PASS — "Running tally: [count] null. [X] stages remain. SESSION INVARIANTs A and B remain active." | PASS | PASS — both NULL TALLY NOTE and SCHEMA INTEGRITY NOTE | PASS | PASS |
| **C-21** Co-activation echoed into handoff | PASS — `co_activation_confirmed: [must equal dual_lock_fired]` in handoff | PASS | PASS | PASS | PASS |
| **C-22** Invariant registry as distinct gate field | PASS — `invariant_registry_confirmed` separate from `gate_s_cleared` in GATE S | PASS | PASS | PASS | PASS |
| **C-23** Campaign-outcome boolean independent | PASS — `incumbent_defense_closed` separate from `co_activation_confirmed` | PASS | PASS | PASS | PASS |
| **C-24** Role-structural dual attestation | PASS — ROLE A sole owner of `invariant_registry_confirmed`; ROLE B sole owner of `gate_s_cleared`; each declared "Sole producer" | PASS | PASS | PASS | PASS |
| **C-25** Handoff fields carry inline derivation annotations | PASS — DERIVATION ANNOTATION RULE at synthesis with "Unlabeled field = format error"; all 9 fields carry `[derived from: X]` | PASS — DERIVATION ANNOTATION RULE; 9 fields labeled; full symmetric chains | PASS — DERIVATION ANNOTATION RULE; 8 declared fields + compliance field labeled | PASS — EXECUTE SESSION INVARIANT C at synthesis; all 8 declared fields labeled | PASS |
| **C-26** Handoff schema pre-committed at CAMPAIGN OPEN | PASS — 9-field PRE-COMMITTED HANDOFF SCHEMA (including field 9 self-registration); `schema_compliance_confirmed` at synthesis | PASS — 9-field schema with mutual independence declared; compliance check at synthesis | PASS — 8-field schema; compliance check at synthesis; `schema_compliance_confirmed` produced (convention consistent with R8 V-02 exemplar) | PASS — 8-field PRE-COMMITTED HANDOFF SCHEMA; compliance check at synthesis | PASS |
| **C-27** Independence path chain on campaign-outcome | PASS — `positive_derivation` + `independence_chain` on `incumbent_defense_closed`; `co_activation_confirmed` has brief NOT annotation only | PASS — full `positive_derivation` + `independence_chain` on both fields (R9 axis 2); C-27's required chain on `incumbent_defense_closed` PASS | PASS — `positive_derivation` + `independence_chain` on `incumbent_defense_closed`; `co_activation_confirmed` has NOT annotation only | PASS — full chain on `incumbent_defense_closed`; `co_activation_confirmed` has NOT annotation only | PASS |
| **Aspirational subtotal** | **74** | **74** | **74** | **74** | **76** |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** | Status |
|-----------|-----------|-------------|--------------|---------------|--------|
| V-01 | 50 | 30 | 74 | **154** | Golden |
| V-02 | 50 | 30 | 74 | **154** | Golden |
| V-03 | 50 | 30 | 74 | **154** | Golden |
| V-04 | 50 | 30 | 74 | **154** | Golden |
| V-05 | 50 | 30 | 76 | **156** | Golden |

All variations: all essential criteria pass. All composites ≥ 80.

---

### Ranking

1. **V-05 — 156** (full compound: all R9 axes + full inertia framing → C-12 PASS)
2. **V-01 through V-04 — 154** (tie; each adds one R9 axis but shares the C-12 PARTIAL)

**Separator within 154 tier** — not a rubric difference but an excellence-signal difference:
- V-01 earns the comparator reference at Stage 2 (stronger than V-02/V-03/V-04 which have none beyond CAMPAIGN OPEN)
- V-04 pre-commits the annotation rule as SESSION INVARIANT C, which strengthens C-25's enforcement chain
- V-03 adds formal per-stage schema integrity counts (R9 axis 3)
- V-02 closes the symmetric independence chain on `co_activation_confirmed` (R9 axis 2)

---

### Excellence Signals from V-05

**Why V-05 scores higher under v8:**

**C-12 gap closure** (full inertia framing): V-05 explicitly names the comparator in an orientation note at CAMPAIGN OPEN ("every evidence stage compares {topic} against this comparator"), adds `Incumbent Comparator Coverage` as a table column at Stages 2 and 3, and requires "Supporting evidence assessment vs incumbent" at Stage 4. This is the only v8-scoring difference — all other criteria score identically across V-01 through V-05.

**R9 axis patterns (exceed v8 ceiling — candidate v9 criteria):**

1. **Schema self-registration** (V-01 axis): `schema_compliance_confirmed` declared as field 9 in CAMPAIGN OPEN schema with locked derivation source. Omitting it from synthesis is a schema violation detectable from CAMPAIGN OPEN alone — the compliance check field is itself subject to the contract it certifies.

2. **Symmetric independence chain** (V-02 axis): `co_activation_confirmed` carries `positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"` + `independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"`. C-27 requires this only for `incumbent_defense_closed`; V-02 closes the reverse path with identical structural rigor.

3. **Per-stage schema integrity count** (V-03 axis): Formal `SCHEMA INTEGRITY NOTE` block at Stages 2, 3, and 4 recording `Schema fields locked: N/N — no additions, no omissions since CAMPAIGN OPEN`. Creates a per-stage audit chain for the schema contract across the collection phase, symmetric to C-20's null tally chain.

4. **Annotation rule pre-committed** (V-04 axis): DERIVATION ANNOTATION RULE declared as `SESSION INVARIANT C` at CAMPAIGN OPEN with invariant language ("session obligation, not synthesis instruction"). ROLE A's registry lock covers all three invariants. Synthesis EXECUTES the rule — does not declare it. `annotation_rule_active: true` in hypothesis frontmatter makes the obligation traceable from Stage 1 artifact alone.

---

```json
{"top_score": 156, "all_essential_pass": true, "new_patterns": ["schema_compliance_confirmed pre-declared as a member of the pre-committed handoff schema at CAMPAIGN OPEN (schema self-registration — compliance check field subject to the contract it certifies)", "symmetric two-part positive_derivation + independence_chain on co_activation_confirmed mirroring C-27 chain on incumbent_defense_closed — mutual independence of both campaign-sensitive fields proven by enumerated chains", "per-stage SCHEMA INTEGRITY NOTE with N/N field count at each evidence stage — schema contract auditable across collection phase symmetric to C-20 null tally chain", "DERIVATION ANNOTATION RULE pre-committed as SESSION INVARIANT C at CAMPAIGN OPEN with invariant language — annotation obligation registered before Stage 0, not declared at synthesis"]}
```
