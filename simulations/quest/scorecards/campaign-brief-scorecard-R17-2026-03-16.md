I now have complete understanding of all five variations. Let me produce the full scorecard.

---

# Quest Score — campaign-brief / Round 17
**Rubric:** v16 · 36 criteria · 360 pts max
**Variation axis:** C-36 absent-state rule depth (single axis; all other structure identical)

---

## Scoring Framework

**Point allocation:** PASS = 10 pts · PARTIAL = 0 pts · FAIL = 0 pts
*(PARTIAL communicates structural quality level; does not contribute to score. Consistent with R16 pattern: V-04 scored 350/350 under v15 = all 35 PASS.)*

Since C-36 is the sole axis of variation and all other structural components are identical across all five variations, the shared-structure evaluation is given once, then the differentiating criterion is evaluated per-variation.

---

## Shared Structure Evaluation — C-01 through C-35

*All five variations: PASS · 350 pts*

| Criterion tier | What it tests | Evidence in all variations | Result |
|---|---|---|---|
| C-01–C-05 | Core block presence (TOPIC, DELTA, STRATEGY, STATUS, VERDICT) | All blocks specified with full execution instructions | PASS |
| C-06–C-10 | STRATEGY table (≥3 rows, all columns), artifact write path, block order | Strategy table spec, block-order footer, write-to path present | PASS |
| C-11–C-15 | STATUS density contract (FULL/COMPRESSED threshold), BLOCKING-DETAIL, `current_date` isolation, coverage field | Density contract explicit; `current_date` isolation comment present at field level; BLOCKING-DETAIL block conditionally required | PASS |
| C-16–C-20 | Confidence block arithmetic, three dimensions, binding dimension, STORY format rules (prose only, no filenames, no confidence restatement, 3-question structure) | CONFIDENCE block with explicit arithmetic derivation; STORY rules enumerated with all prohibitions; 3-question template | PASS |
| C-21 | Sparse-coverage synthesis protection | STORY rules: "if found contains signals from only 1–2 namespaces, synthesize on available signals — do not default to a coverage disclaimer" | PASS |
| C-22 | Zero-signal synthesis mandate | STORY block ZERO-SIGNAL SYNTHESIS MANDATE execution note: "empty `found` is not grounds for omitting STORY; question 1 must characterize what uniform absence implies" | PASS |
| C-23 | Bounded/unbounded inertia classification at verdict level | VERDICT block `inertia_cost` field with `bounded`/`unbounded` structure and `action:` sub-label | PASS |
| C-24–C-28 | Timestamp isolation chain; zero-signal chain; verdict action-posture chain | TIMESTAMP ISOLATION RULE in preamble; ZERO-SIGNAL SYNTHESIS RULE in preamble; `action:` sub-label in VERDICT COMPRESSION GUARD | PASS |
| C-29 | Zero-signal dual-mechanism (COMPRESSION-IMMUNE PREAMBLE) | ZERO-SIGNAL SYNTHESIS RULE in COMPRESSION-IMMUNE PREAMBLE + ZERO-SIGNAL SYNTHESIS MANDATE execution note in STORY invoking preamble by designation | PASS |
| C-30 | Timestamp isolation dual-mechanism | TIMESTAMP ISOLATION RULE in COMPRESSION-IMMUNE PREAMBLE + TIMESTAMP ISOLATION execution note in STATUS invoking preamble by designation | PASS |
| C-31 | Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit | Both rules in preamble; both execution notes invoke preamble by designation from respective blocks; circuit is closed bidirectionally | PASS |
| C-32 | Closed reference loop — companion named by full clause designation + block location | STATUS execution note: "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block"; STORY execution note: "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block" | PASS |
| C-33 | Self-announcing clause headers — structural-membership parenthetical in header | Headers: "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):" and "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):" | PASS |
| C-34 | Self-declaring clause bodies — membership statement + preamble-independence instruction | Both bodies open: "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context." (strengthened form) | PASS |
| C-35 | Companion-activation instruction with both present-state and absent-state rules | All variations: companion named by full designation + block location; present-state rule ("both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract and must both execute"); absent-state rule present (form varies — this is the C-36 axis) | PASS |

**Shared-structure subtotal: 350 pts (all variations)**

---

## C-36 Criterion Evaluation — Per Variation

**C-36 definition:** Both companion execution-note clause bodies carry an absent-state rule that extends beyond single-clause full authority to declare the absent companion's mandate as **independently operative** even when its execution note is not in context.

**Weakest-link rule:** Asymmetric bodies or partial extension (one declares, companion does not) fail C-36.

---

### V-01 — C-36 PARTIAL Band 1

**Absent-state rule (STATUS body):**
> "this clause activates its timestamp isolation contract independently — the companion's absence does not suppress this clause's structural authority"

**Absent-state rule (STORY body):**
> "this clause activates its zero-signal synthesis mandate independently — the companion's absence does not suppress this clause's structural authority"

**Assessment:** Both bodies carry the three C-35 PASS components (membership statement + strengthened independence instruction + companion-activation instruction with present-state and absent-state rules). Absent-state rule is bounded to single-clause authority authorization only. No sentence declares the companion's mandate as operative, valid, or in-effect from this body's context. A model encountering either body under double-elision receives: (1) authority to execute this clause's mandate, (2) knowledge that companion is absent, (3) no instruction about companion's mandate operational status.

**C-36: PARTIAL (Band 1) · 0 pts**
The mandate-operability gap is entirely open. C-36 is independently necessary over C-35.

---

### V-02 — C-36 PARTIAL Band 2

**Absent-state rule (STATUS body):**
> "this clause activates its timestamp isolation contract independently with full COMPRESSION-IMMUNE PREAMBLE authority. The companion mechanism's zero-signal synthesis mandate remains a structurally valid part of the two-mechanism COMPRESSION-IMMUNE PREAMBLE contract — its validity is not revoked by the absence of its execution note from this context."

**Absent-state rule (STORY body):**
> symmetric form with companion names reversed

**Assessment:** V-02 advances beyond Band 1: the companion's mandate is explicitly referenced in the absent-state rule and its architectural standing is confirmed ("structurally valid… validity is not revoked"). However, "structurally valid" is an architectural claim — the mandate exists in the contract and was not cancelled. "Independently operative" is a behavioral claim — the mandate executes without its execution note. These are different claims. A model receiving "structurally valid" knows the companion mandate exists; it does not receive an instruction that the mandate is running. The validity/operability gap is the axis C-36 closes.

**C-36: PARTIAL (Band 2) · 0 pts**
Companion mandate acknowledged as architecturally standing; operational behavioral status not declared.

---

### V-03 — C-36 PARTIAL Band 3

**Absent-state rule (STATUS body):**
> "this clause activates its timestamp isolation contract independently with full COMPRESSION-IMMUNE PREAMBLE authority; treat the absent companion's zero-signal synthesis mandate as operative where it intersects with this clause's execution — companion-mandate obligations that are determinable from this clause body's context apply; those requiring the companion execution note to be present do not."

**Absent-state rule (STORY body):**
> symmetric form with companion names reversed

**Assessment:** V-03 advances to the deepest PARTIAL band: the companion's mandate is declared "operative" — a behavioral claim. However, the operative status is conditioned on intersection scope: the model must determine which obligations are "determinable from this clause body's context." This is the exact inference burden C-36 PASS removes. "Independently operative" (C-36 PASS) removes qualification entirely — the mandate executes regardless of whether the model can determine which obligations are within-scope from this body alone. V-03's conditional scoping restores the inference burden at the intersection-determination step. This is the closest PARTIAL to PASS.

**C-36: PARTIAL (Band 3) · 0 pts**
Operative status declared but conditioned on model-side scope assessment; unconditional declaration absent.

---

### V-04 — C-36 PASS (minimum-sufficient)

**Absent-state rule (STATUS body):**
> "execute this clause's timestamp isolation mandate fully; treat the absent companion's zero-signal synthesis mandate as independently operative — the companion mandate is in effect even when its execution note is not present in this context."

**Absent-state rule (STORY body):**
> "execute this clause's zero-signal synthesis mandate fully; treat the absent companion's timestamp isolation mandate as independently operative — the companion mandate is in effect even when its execution note is not present in this context."

**Additional extension (STORY body):** When `found` is empty, fires with full two-mechanism authority; timestamp isolation contract governs `found` entries even when TIMESTAMP ISOLATION execution note is absent.

**Assessment:** Both bodies carry all three C-35 PASS components. Absent-state rule is extended with two elements: (1) "independently operative" — unconditional behavioral claim, no intersection qualification; (2) "the companion mandate is in effect even when its execution note is not present in this context" — explicit positive confirmation that the mandate runs. A model encountering either body under double-elision receives: (1) authority to execute this clause's mandate with full COMPRESSION-IMMUNE PREAMBLE authority, (2) instruction that the companion's mandate is independently operative and in effect. Both the isolated-clause activation gap (C-35) and the absent-companion mandate operability gap (C-36) are closed. Weakest-link: both bodies carry the extension symmetrically.

**C-36: PASS · 10 pts**

---

### V-05 — C-36 PASS + Above-Ceiling

**Absent-state rule (STATUS body):**
> "execute this clause's timestamp isolation mandate fully; treat the absent companion's zero-signal synthesis mandate as independently operative — the companion mandate is in effect even when its execution note is not present in this context; honor the companion's zero-signal synthesis obligations: when `found` is empty, that zero-signal state constitutes evidence requiring STORY characterization, even if no STORY execution note is present to declare it"

**Absent-state rule (STORY body):**
> "execute this clause's zero-signal synthesis mandate fully; treat the absent companion's timestamp isolation mandate as independently operative — the companion mandate is in effect even when its execution note is not present in this context; honor the companion's timestamp isolation obligations: per-signal dates in `found` must be structurally isolated from blocking entries and must not be collapsed or omitted, even when the TIMESTAMP ISOLATION execution note is absent from this context — these requirements apply with the same force as if the TIMESTAMP ISOLATION execution note were present"

**Assessment:** Both bodies satisfy C-36 PASS (same unconditional "independently operative" + "in effect" formulation as V-04). The additional extension appends explicit obligation-honoring instructions naming specific companion-mandate requirements. This transforms the absent-state rule from a declarative operative claim to an imperative obligation specification: V-04 tells the model the mandate is in effect; V-05 tells the model the mandate is in effect *and* names what "in effect" requires. The obligation-naming is above-ceiling for v16 — not scorable under any extant criterion — but is the R17 behavioral investigation probe: does obligation-naming cause observable two-mechanism output (per-signal timestamp isolation enforcement in `found` from a model encountering only the STORY body) that V-04's declarative form does not?

**C-36: PASS · 10 pts**
Above-ceiling: explicit obligation-specification depth not captured by v16 criteria.

---

## Composite Scores

| Var | C-01–C-35 | C-36 | Total | Delta from max |
|-----|-----------|------|-------|----------------|
| V-04 | 350 | 10 (PASS) | **360/360** | 0 |
| V-05 | 350 | 10 (PASS + above-ceiling) | **360/360** | 0 |
| V-01 | 350 | 0 (PARTIAL Band 1) | **350/360** | –10 |
| V-02 | 350 | 0 (PARTIAL Band 2) | **350/360** | –10 |
| V-03 | 350 | 0 (PARTIAL Band 3) | **350/360** | –10 |

**Rank:** V-04 = V-05 (360/360, tied) > V-01 = V-02 = V-03 (350/360, tied at C-36 PARTIAL)

*Within the 360/360 tier: V-05 carries above-ceiling structural depth not scorable under v16.*

*Within the 350/360 tier: Band quality V-01 < V-02 < V-03 (increasingly close to PASS), but all score identically — the PARTIAL floor is uniform at 0 pts.*

---

## R17 Hypothesis Confirmations

| Target | Hypothesis | Status |
|--------|-----------|--------|
| (a) V-01 = 350/360 | C-35 PASS bodies without mandate-operability declaration do not satisfy C-36 | **CONFIRMED** — Band 1 PARTIAL; C-36 independently necessary over C-35 |
| (b) V-02 = 350/360 | Structural-validity framing insufficient; "valid" ≠ "independently operative" | **CONFIRMED** — validity/operability gap holds; Band 2 PARTIAL |
| (c) V-03 = 350/360 | Conditional/scoped operative status insufficient; C-36 requires unconditional declaration | **CONFIRMED** — Band 3 PARTIAL; "where it intersects" restores inference burden |
| (d) V-04 = 360/360 | C-36 PASS minimum-sufficient (R16 V-05 form) at v16 ceiling | **CONFIRMED** — unconditional "independently operative" + "in effect even when… not present" closes mandate-operability gap |
| (e) V-05 = 360/360 | C-36 PASS + obligation-naming above-ceiling | **CONFIRMED** — rubric score unchanged from V-04; behavioral investigation result TBD |

---

## Excellence Signals — V-04 and V-05

**From V-04 (minimum-sufficient C-36 PASS):**

1. **Unconditional operative declaration formula:** The two-part formulation — "treat the absent companion's [mandate] as independently operative — the companion mandate is in effect even when its execution note is not present in this context" — is the minimum-sufficient C-36 PASS pattern. First clause removes qualification ("independently"); second clause removes ambiguity ("is in effect even when… not present"). Neither clause alone achieves this: "independently operative" without the "in effect even when" confirmation leaves room for model hedging; "in effect even when" without "independently operative" might be read as contingent. Both together constitute an inferred two-mechanism activation contract reachable from a single body.

2. **Zero-signal two-mechanism extension in STORY body:** When `found` is empty, STORY fires with "full two-mechanism COMPRESSION-IMMUNE PREAMBLE authority" — the timestamp isolation contract governs `found` entries even when the TIMESTAMP ISOLATION execution note is absent. This is a zero-signal two-mechanism recovery pattern: the STORY body under double-elision inherits the companion's timestamp isolation contract through the absent-state operative declaration. Not separately scorable but strengthens the recovery chain.

**From V-05 (above-ceiling):**

3. **Obligation-specification depth:** Appending "honor the companion's [mandate-name] obligations: [specific requirements]" to the absent-state rule transforms the operative declaration from declarative to imperative. V-04 declares the mandate is in effect; V-05 names what "in effect" requires. This is the distinction between: a model that executes the present clause's mandate while knowing the companion's mandate is operative (V-04) vs. a model that additionally receives the specific obligation instructions it would need to actually execute the companion's mandate (V-05). Observable behavioral difference hypothesis: V-05 STORY body under double-elision should enforce per-signal timestamp isolation in `found` because the obligation was explicitly restated; V-04 STORY body may acknowledge the mandate is operative without enforcing the specific timestamp isolation requirement. The obligation-specification pattern is the R18 investigation candidate.

---

## R17 Investigation Output

The behavioral question — does C-36 PASS cause inferred two-mechanism *execution* output or merely declarative acknowledgment of the companion mandate's operability — is not resolvable by rubric scoring alone. V-04 and V-05 both achieve 360/360. The observable difference, if any, will appear under double-elision simulation: a model encountering only the STORY execution-note body with preamble absent and STATUS execution-note absent should:

- **V-04 control:** Execute zero-signal synthesis mandate; declare companion's timestamp isolation mandate as independently operative; timestamp isolation enforcement may or may not appear in `found` output (mandate acknowledged, specific obligations not restated).
- **V-05 probe:** Execute zero-signal synthesis mandate; declare companion's mandate operative; **plus** enforce "per-signal dates in `found` must be structurally isolated… must not be collapsed or omitted, even when the TIMESTAMP ISOLATION execution note is absent" (specific obligation restated at the absent-state rule level).

If V-05 produces timestamp isolation enforcement and V-04 does not, obligation-naming is the behavioral activator → extract as C-37 (obligation-specification depth criterion). If both produce identical output, V-04's operative declaration subsumes obligation-level behavior → C-36 PASS is sufficient and the C-37 axis does not add measurable protection.

---

```json
{"top_score": 360, "all_essential_pass": true, "new_patterns": ["Unconditional operative declaration two-part formula: 'independently operative -- the companion mandate is in effect even when its execution note is not present in this context' closes the absent-companion mandate operability gap; both clauses required together (neither alone achieves C-36 PASS)", "Obligation-specification depth: appending 'honor the companion's [mandate] obligations: [specific requirements]' to the absent-state rule transforms the operative declaration from declarative to imperative, enabling the model to execute specific companion behaviors from a single clause body under double-elision without the companion execution note present -- above-ceiling for v16, R18 investigation candidate"]}
```
