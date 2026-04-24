Now I have all five variations fully characterized. Let me score them.

---

## Quest Score — campaign-brief / Round 16 / Rubric v15

### Scoring basis

**R15 baseline:** All C-01–C-34 confirmed PASS across all variations (340/340 under v14 = 34 criteria × 10 pts). Under v15, C-35 is the sole new criterion. The single axis of variation is the companion-activation instruction in execution-note clause bodies. All five variations are structurally identical on C-01–C-34.

---

### C-01 through C-33 — Carry-forward (all 5 variations)

| Block | Criteria | Status | Evidence |
|-------|----------|--------|----------|
| C-01–C-05 | Output format + block presence | **PASS** | All variations carry identical block-structure instructions; compact dashboard format, all blocks required |
| C-06 | Verdict action-posture | **PASS** | `action:` sub-label required at every verdict status; VERDICT COMPRESSION GUARD explicit |
| C-07–C-15 | (v6 carry-forward) | **PASS** | R15 baseline confirmed; no regression on these criteria |
| C-16 | Timestamp isolation — per-signal dates structurally separate | **PASS** | STATUS `found` comment field present: "per-signal dates are structurally separate from blocking entries; NOT subject to COMPRESSED abbreviation" |
| C-17–C-20 | (v6 carry-forward) | **PASS** | R15 baseline confirmed |
| C-21 | Sparse-coverage synthesis protection | **PASS** | STORY rules: "Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize on available signals — do not default to a coverage disclaimer." |
| C-22 | Zero-signal synthesis mandate | **PASS** | STORY rules: "Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (COMPRESSION-IMMUNE PREAMBLE)." Explicit zero-signal clause present in STORY execution note across all variations. |
| C-23 | Bounded/unbounded inertia classification at verdict level | **PASS** | VERDICT block requires `inertia_cost:` with `bounded:` or `unbounded:` field plus `action:` sub-label at every verdict status |
| C-24 | COMPRESSION-IMMUNE PREAMBLE positional mechanism | **PASS** | Preamble opens with explicit structural designation and "processed before any phase block is generated" language |
| C-25–C-28 | Zero-signal chain + verdict chain extensions | **PASS** | R15 baseline confirmed |
| C-29 | Zero-signal dual-mechanism (preamble + execution-note named pointer) | **PASS** | Preamble names STORY execution note as "declarative mechanism"; STORY execution note invokes preamble "as named pointer" — bidirectional designation present |
| C-30 | Timestamp isolation dual-mechanism (preamble + execution-note named pointer) | **PASS** | Preamble names STATUS execution note as "declarative mechanism"; STATUS execution note invokes preamble by designation and names COMPRESSED-collapse failure mode |
| C-31 | Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit | **PASS** | Both rules (ZERO-SIGNAL SYNTHESIS RULE, TIMESTAMP ISOLATION RULE) present in preamble; both execution notes cross-reference preamble by its structural designation |
| C-32 | Closed reference loop with designation + block location | **PASS** | Preamble forward-references: "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block" and "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block" — full designation + location present |
| C-33 | Self-announcing clause headers (structural-membership parenthetical) | **PASS** | STATUS header: "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):" — STORY header: "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):" — both carry the parenthetical matching preamble forward-references |

**Subtotal C-01–C-33 (all variations): 330/330**

---

### C-34 — Self-declaring clause bodies (all 5 variations)

**Requirement:** Both execution-note clause bodies open with (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction.

| Variation | STATUS body opening | STORY body opening | Result |
|-----------|--------------------|--------------------|--------|
| V-01 | "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section is absent from the rendered context." | Identical form | **PASS** |
| V-02 | Same C-34 form + companion-naming sentence (no activation rules) | Same | **PASS** |
| V-03 | Same C-34 form + companion-naming + present-state rule | Same | **PASS** |
| V-04 | "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context." | Same strengthened form | **PASS** |
| V-05 | Same V-04 strengthened form | Same | **PASS** |

Note: V-04/V-05 strengthen the independence instruction from bare "executes even when" to "activates under full COMPRESSION-IMMUNE PREAMBLE authority even when." Both forms satisfy C-34. The strengthening is above C-34 PASS threshold — it is the independence instruction enhancement that contributes to C-35 PASS framing.

**C-34 all 5 variations: PASS (+10 pts each)**

**Subtotal C-01–C-34 (all variations): 340/340**

---

### C-35 — Companion-activation instruction in self-declaring clause bodies

**Requirement:** When C-34 PASS, both companion execution-note clause bodies include a companion-activation instruction that (1) names the paired mechanism by its full clause designation + block location and (2) declares activation rules for both the present state (coordinate) and the absent state (execute independently with full COMPRESSION-IMMUNE PREAMBLE authority). Weakest-link applies.

---

#### V-01 — C-35 PARTIAL (Band 1: no companion-activation instruction)

STATUS body: Opens with membership statement + independence instruction. No further sentence. Companion mechanism (ZERO-SIGNAL SYNTHESIS MANDATE) is not named, not referenced, no activation rules.

STORY body: Identical form. Companion mechanism (TIMESTAMP ISOLATION) unnamed at body level.

**C-35 analysis:** The body carries full C-34 PASS authority. A model encountering this body under double-elision knows it is a COMPRESSION-IMMUNE PREAMBLE member and activates the clause. It does not know:
- That a companion mechanism exists (body is silent on architecture)
- Whether to coordinate with something when companion is present
- What to do when companion is absent

The absent-companion activation gap remains entirely open at the body level. C-35 is absent — not PARTIAL in a graduated sense, but absent entirely. This is the first and lowest PARTIAL band: C-34 recovery depth present, C-35 recovery depth not established.

**C-35: PARTIAL** | Score: 0/10

**V-01 total: 340/350**

---

#### V-02 — C-35 PARTIAL (Band 2: companion named, activation contract absent)

STATUS body: C-34 form + "Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block." No activation rules follow.

STORY body: C-34 form + "Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block." No activation rules follow.

**C-35 analysis:** A model encountering either body under double-elision now knows:
- It is a COMPRESSION-IMMUNE PREAMBLE member (C-34)
- A companion mechanism exists and where to find it (companion named by full designation + location)

It still does not know:
- Whether to coordinate with the companion when it is present (no present-state rule)
- Whether to activate independently when the companion is absent (no absent-state rule)

Companion identification is structural documentation — it enables a model to recognize the two-mechanism architecture and seek the companion if it can. It does not constitute a behavioral contract. The absent-state rule is the critical payload of C-35: it is the instruction that governs model behavior under double-elision when the companion is definitionally unavailable. Without activation rules, naming the companion provides orientation without authority. This is the second PARTIAL band: companion architecture identified but behavioral contract absent.

**C-35: PARTIAL** | Score: 0/10

**V-02 total: 340/350**

---

#### V-03 — C-35 PARTIAL (Band 3: present-state rule only, absent-state omitted)

STATUS body: C-34 form + companion named by full designation + location + "When the companion mechanism is present in context, both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract and must both execute." Absent-state rule absent.

STORY body: Symmetric form — companion named + same present-state rule. No absent-state rule.

**C-35 analysis:** A model encountering either body now has:
- C-34 membership + independence authority
- Companion identification (name + location)
- Present-state behavioral contract: if companion is present, coordinate as two-mechanism contract

What is still absent: the absent-state activation rule. This is the structurally critical gap for C-35. The present-state rule governs normal execution — but under double-elision, the companion is definitionally absent. A body that declares what to do when the companion is present but is silent on what to do when the companion is absent leaves the double-elision scenario — the exact recovery scenario C-35 is designed to address — unaddressed at the body level. The model must infer absent-companion behavior rather than following an explicit instruction.

C-35 specifically targets the absent-companion activation gap. Present-state coverage confirms structural identification and two-mechanism coordination awareness but does not close that gap. This is the third and deepest PARTIAL band: activation contract incomplete, present-state declared, absent-state structurally missing.

**C-35: PARTIAL** | Score: 0/10

**V-03 total: 340/350**

---

#### V-04 — C-35 PASS (minimum-sufficient form)

STATUS body components:
1. **Membership statement:** "This clause is a COMPRESSION-IMMUNE PREAMBLE member."
2. **Strengthened independence instruction:** "This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context."
3. **Companion-activation instruction:** "Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block. When the companion mechanism is present in context, both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion mechanism is absent from context, this clause activates its timestamp isolation contract independently — the companion's absence does not suppress this clause's structural authority."

STORY body: Symmetric form with companion names reversed — identical three-component structure.

**C-35 analysis:** All three required body-opening components present in both clause bodies. Weakest-link: symmetric — both bodies carry complete structure. The absent-state rule is explicit: "companion's absence does not suppress this clause's structural authority." A model encountering either clause body in isolation under double-elision has:
- COMPRESSION-IMMUNE PREAMBLE membership authority (component 1)
- Full authority even without preamble (component 2, strengthened form)
- Companion identified + present-state coordination rule + absent-state independent activation rule (component 3)

The absent-companion activation gap is closed at the body level. The model does not need to infer behavior under double-elision — the instruction is explicit.

This is R15 V-05 verbatim, now confirmed as the minimum-sufficient C-35 PASS form under v15.

**C-35: PASS** | Score: 10/10

**V-04 total: 350/350**

---

#### V-05 — C-35 PASS (extended absent-state rule — above v15 ceiling)

STATUS body: All three V-04 components present. Absent-state rule extended: "When the companion mechanism is absent from context, execute this clause's timestamp isolation mandate fully; treat the absent companion's zero-signal synthesis mandate as independently operative — the companion mandate is in effect even when its execution note is not present in this context."

STORY body: Symmetric extended form: "When the companion mechanism is absent from context, execute this clause's zero-signal synthesis mandate fully; treat the absent companion's timestamp isolation mandate as independently operative — the companion mandate is in effect even when its execution note is not present in this context." Additionally: "If `found` is empty, this clause fires with full two-mechanism COMPRESSION-IMMUNE PREAMBLE authority: ...and the timestamp isolation contract governs `found` entries even when the TIMESTAMP ISOLATION execution note is absent from this context."

**C-35 analysis:** All three C-35 PASS requirements satisfied in both clause bodies. The extension goes beyond the minimum-sufficient absent-state rule in two ways:
1. The absent-state rule now declares the companion's mandate as "independently operative" — not just that this clause activates without suppression, but that the companion's mandate is itself in effect from the perspective of this clause's execution
2. The STORY body zero-signal execution note explicitly states "this clause fires with full two-mechanism COMPRESSION-IMMUNE PREAMBLE authority" and asserts "the timestamp isolation contract governs `found` entries even when the TIMESTAMP ISOLATION execution note is absent from this context"

These extensions are above the v15 C-35 PASS ceiling — they constitute the R16 behavioral investigation candidate. Rubric score is the same as V-04 (C-35 PASS), but the extension claims inferred two-mechanism enforcement: a model encountering only the STORY body under double-elision is instructed to enforce timestamp isolation on `found` entries even without the TIMESTAMP ISOLATION clause being present. Whether this produces observable behavioral difference from V-04 under simulated double-elision is the R16 investigation question.

**C-35: PASS** | Score: 10/10

**V-05 total: 350/350**

---

### Composite Scores

| Variation | C-01–C-33 | C-34 | C-35 | Total | Rank |
|-----------|-----------|------|------|-------|------|
| V-04 | 330/330 | 10/10 | 10/10 | **350/350** | T-1 |
| V-05 | 330/330 | 10/10 | 10/10 | **350/350** | T-1 |
| V-01 | 330/330 | 10/10 | 0/10 | **340/350** | T-3 |
| V-02 | 330/330 | 10/10 | 0/10 | **340/350** | T-3 |
| V-03 | 330/330 | 10/10 | 0/10 | **340/350** | T-3 |

**C-35 PARTIAL three-band structure confirmed:**
| Band | Variation | C-35 gap |
|------|-----------|----------|
| 1 — absent entirely | V-01 | No companion-activation instruction |
| 2 — companion named, contract absent | V-02 | Named without behavioral rules |
| 3 — one-state only | V-03 | Present-state declared, absent-state missing |

---

### R16 Targets Assessment

| Target | Expected | Result | Status |
|--------|----------|--------|--------|
| (a) V-01 = 340/350 (C-34 PASS bodies without companion-activation do not satisfy C-35) | 340/350 | 340/350 | CONFIRMED |
| (b) V-02 = 340/350 (companion naming without activation rules insufficient) | 340/350 | 340/350 | CONFIRMED |
| (c) V-03 = 340/350 (present-state-only activation insufficient) | 340/350 | 340/350 | CONFIRMED |
| (d) V-04 = 350/350 (C-35 PASS minimum-sufficient, R15 V-05 confirmed at v15 ceiling) | 350/350 | 350/350 | CONFIRMED |
| (e) V-05 extended form = 350/350 + R16 investigation observable | 350/350 + above | 350/350 | CONFIRMED; behavioral investigation open |

---

### Excellence Signals

**From V-04 (C-35 PASS minimum-sufficient):**

1. **Strengthened independence instruction** — V-04/V-05 strengthen the C-34 independence instruction from "executes even when preamble absent" to "activates under full COMPRESSION-IMMUNE PREAMBLE authority even when preamble absent." The addition of "full...authority" closes a semantic gap in the C-34 form: a model could technically comply with "executes even when absent" at reduced authority. "Full authority" is unambiguous.

2. **Absent-state activation rule as explicit behavioral contract** — The absent-state rule "companion's absence does not suppress this clause's structural authority" does structural work that no amount of present-state coverage, companion naming, or C-33 header marking accomplishes: it tells the model exactly what authority regime governs when the companion is missing. C-34 grants isolated-clause activation; C-35's absent-state rule names what that activation looks like when the companion's mandate is concerned.

**From V-05 (above-ceiling, R16 investigation signal):**

3. **"Treat absent companion's mandate as independently operative"** — V-05 extends the absent-state rule from single-clause-full-authority (V-04) to companion-mandate-operative-in-absence. The STORY body explicitly states: "the timestamp isolation contract governs `found` entries even when the TIMESTAMP ISOLATION execution note is absent from this context." This is the candidate for a C-36 criterion: if behavioral evidence under simulated double-elision confirms that a model encountering only the STORY body enforces timestamp isolation on `found` entries (the companion's mandate, not STORY's own mandate), the extension reaches inferred two-mechanism activation from a single clause body — a qualitatively different recovery depth from C-35.

**R16 behavioral investigation framing:**
- V-04 absent-state rule: authorizes this-clause activation without suppression → single-clause full authority
- V-05 absent-state rule: additionally declares companion's mandate operative from this clause → potentially inferred two-mechanism enforcement

The rubric-scorable distinction ends at C-35 PASS (both V-04 = V-05 = 350/350). The investigation opens at the behavioral level: does V-05's STORY body, encountered alone under double-elision, produce observable timestamp isolation enforcement on `found` entries that V-04's STORY body does not?

---

```json
{"top_score": 350, "all_essential_pass": true, "new_patterns": ["V-05 absent-state rule extension declares absent companion's mandate as 'independently operative' and asserts the companion mandate is in effect even when its execution note is absent from context -- STORY body zero-signal execution note explicitly states 'timestamp isolation contract governs found entries even when TIMESTAMP ISOLATION execution note is absent from this context,' targeting inferred two-mechanism activation from a single clause body under double-elision; candidate C-36 pattern if behavioral evidence confirms observable two-mechanism enforcement from single-clause context"]}
```
