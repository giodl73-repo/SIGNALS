Reading the R15 scorecard for new excellence signals not yet captured by any existing criterion.

Two axes differentiate V-05 from all other variations:

1. **C-40 row** — V-01 through V-04 carry `SELF-REF` (entries for C-38/C-39 only). V-05 carries `SELF-REF + C-42/C-43`. C-40 requires self-referential entries exist; it says nothing about keeping them current as new criteria are added.

2. **"C-43 in CO-DEPENDENCY PREAMBLE" row** — V-01 through V-04: Absent. V-05: Present. The three-leg chain (C-39 → C-41 → C-43) is fully declared in V-05's preamble; all other variations stop at the two-leg chain.

These become **C-44** and **C-45**. Denominator: 35 → 37. Weight: 10 ÷ 37 ≈ 0.270 pts each. Criteria count: 43 → 45.

---

```markdown
# Quest Rubric — corps-committee (v16)

**C-44** comes from the "C-40 row" axis in R15: V-05 uniquely carries self-referential
FAILS template entries for C-42 and C-43 — criteria that did not exist when C-40 was first
authored. C-40 requires the template include self-referential entries; C-44 requires those
entries be kept current each time the rubric gains a new criterion pair. A template satisfies
C-40 the moment it includes entries for C-38 and C-39; it satisfies C-44 only when it also
carries entries for every aspirational criterion added thereafter. **C-45** comes from the
"C-43 in CO-DEPENDENCY PREAMBLE" axis in R15: V-05 uniquely lists C-43 in the CO-DEPENDENCY
PREAMBLE, completing the three-leg traceability chain (C-39 at consumption → C-41 at source
→ C-43 in fill rules). C-39 and C-41 declare a two-sided dependency; C-45 requires the third
leg of that chain be named in the preamble as a unit, so a reviewer can see the full chain
without reconstructing it from three separate criterion definitions. A skill where the preamble
declares C-39 and C-41 but omits C-43 satisfies both individual criteria but does not declare
the full chain.

Denominator: 35 → 37. Aspirational weight: 10 ÷ 37 ≈ 0.270 pts each.

---

**C-42** comes from the "Register ambiguity eliminated" axis in R14: V-03 and V-05 carry no
descriptive framing anywhere in the BEFORE YOU START block — every sentence commands rather
than explains. **C-43** comes from the "PHASE-1 fill rule C-41 annotation" axis in R14:
V-02, V-04, and V-05 echo the prerequisite relationship inside the fill-rule section of the
dependent criterion, producing three-point traceability (REQUIRES: at consumption → C-39;
forward annotation at source → C-41; fill-rule echo → C-43). Both close gaps left open by
C-13 and C-41 respectively.

Denominator: 33 → 35. Aspirational weight: 10 ÷ 35 ≈ 0.286 pts each.

---

**Three new aspirational criteria added from R12 signals (v13):**

**C-37 — Dual-enforcement pairing for high-frequency essential criteria**
V-04 is the evidence: combining tier gates + tables achieves PASS+ on C-02 and C-04 where
either mechanism alone reaches only PASS. The principle: when a property recurs in every
simulation (role voice, action item ownership), two independent structural mechanisms make
violations detectable from two angles simultaneously — removing one mechanism degrades
coverage. Single-mechanism enforcement of these properties is correct but not
redundancy-hardened.

**C-38 — FAILS syntax template enforces `[C-NN]` as a required field**
C-14 was PARTIAL across all four variations in R12. The common gap was identical each time:
"no explicit `[C-NN]` tag requirement on FAILS rows." The distinction from C-14: C-14 checks
whether annotations exist and are correct; C-38 checks whether the fill-rule template makes
omission *structurally detectable* — a FAILS entry missing `[C-NN]` is malformed, not merely
suboptimal.

**C-39 — Co-dependent criteria declared with `REQUIRES:` annotations**
V-03 exposes the C-35/C-36 co-dependency exactly: vocabulary present, count invariant
unenforceable, C-36 PARTIAL(weak). The pattern generalizes: when B's pass condition requires
A, a skill that implements B without declaring the A prerequisite creates latent
false-positive risk. `REQUIRES: C-35` before C-36's fill rules converts a latent trap into a
visible pre-check.

---

**Two new aspirational criteria added from R13 signals (v14):**

**C-40 — FAILS template contains self-referential entries for its own governing criteria**
E-01 from V-05 is the evidence: the FAILS SYNTAX TEMPLATE includes
`CORRECT: FAILS [C-38]: FAILS entry missing [C-NN]` and
`CORRECT: FAILS [C-39]: REQUIRES: C-35 absent`. A template that demonstrates canonical form
but omits self-referential examples teaches syntax without teaching citation discipline for
the template itself. When a reviewer encounters a template violation, they must already know
the correct criterion ID to cite — the self-referential entry supplies that knowledge at the
point of learning. C-38 requires the template to declare [C-NN] as required; C-40 requires
the template to demonstrate exactly what to cite if C-38 or C-39 are violated. A template
that shows correct form and one MALFORMED example but does not cite C-38 or C-39 in those
examples satisfies C-38 but not C-40.

**C-41 — Prerequisite annotations declared at source block as well as consumption site**
E-02 from V-05 is the evidence: PHASE-1-COMMIT includes an inline note
`[This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]`.
C-39 requires `REQUIRES: C-NN` at the consumption site (TOKEN TRACE CONFIRMATION); C-41
requires the complementary forward annotation at the source (PHASE-1-COMMIT). Without a
source annotation, a reviewer can pass the source block without registering the downstream
structural consequence. With a source annotation, a weak implementation of C-35 produces a
visible forward pointer to where C-36 will fail — two-sided dependency tracing rather than
one-sided. A skill where the dependency is declared only at the consumption site satisfies
C-39 but not C-41.

---

**Two new aspirational criteria added from R14 signals (v15):**

**C-42 — Register ambiguity eliminated throughout BEFORE YOU START**
C-13 is satisfied by adding imperative fail conditions to a block that still contains
descriptive framing — the block carries both registers simultaneously. C-42 is satisfied only
when all descriptive passages are removed and every sentence in the block commands or names a
fail condition. A block that opens "ROB is for quarterly feature reviews. **If there is no
metric, you have not done a ROB.**" satisfies C-13 (imperative fail condition present) but
not C-42 (descriptive framing "ROB is for quarterly feature reviews" remains). V-03 achieves
this structurally: the table format [Type / Fail condition / C-tag] makes every cell a
testable fail condition with no cell available for descriptive prose. V-01, V-04, V-05 achieve
it through discipline — no descriptive sentences appear anywhere in the block.

**C-43 — Fill-rule section echoes the C-41 forward annotation**
C-41's pass condition requires only that the source block carry a forward annotation pointing
to the dependent criterion. C-43 requires the fill-rule section of the dependent criterion
to echo that annotation in its own preamble, producing three-point traceability: REQUIRES: at
consumption (C-39) → forward annotation at source (C-41) → echo in fill rules (C-43). Without
the fill-rule echo, a reviewer inspecting the dependent criterion's fill rules sees C-39's
REQUIRES: declaration but must navigate to the source block to confirm the annotation exists.
With the echo, all three legs of the dependency are visible without leaving the fill-rule
section. A skill that carries C-41's source annotation but omits the fill-rule echo satisfies
C-41 but not C-43.

---

**Two new aspirational criteria added from R15 signals (v16):**

**C-44 — Self-referential FAILS template entries updated when new criteria are added**
The "C-40 row" axis in R15 is the evidence: V-01 through V-04 carry self-referential entries
for C-38 and C-39 only; V-05 additionally carries entries for C-42 and C-43 —
`CORRECT: FAILS [C-42]: descriptive framing present in BEFORE YOU START` and
`CORRECT: FAILS [C-43]: fill-rule echo absent`. C-40 requires the template include
self-referential entries at the time of authoring; C-44 requires those entries be extended
each time the rubric gains a new aspirational criterion. Without C-44, a template satisfies
C-40 on the day it is written and then silently falls behind as the rubric grows — a reviewer
encountering a C-44 or C-45 violation has no template entry to consult for the canonical
citation form. The distinction: C-40 checks that self-referential entries exist for the
criteria that govern the template at authoring time; C-44 checks that the template is kept
current with every subsequent criterion addition. A template that demonstrates correct form
and includes self-referential entries for C-38 and C-39 but omits entries for C-42 and C-43
satisfies C-40 but not C-44.

**C-45 — Multi-leg co-dependency chains declared as a unit in CO-DEPENDENCY PREAMBLE**
The "C-43 in CO-DEPENDENCY PREAMBLE" axis in R15 is the evidence: V-05 uniquely lists C-43
in the CO-DEPENDENCY PREAMBLE alongside C-39 and C-41, declaring the full three-leg chain
(C-39 at consumption → C-41 at source → C-43 in fill rules) as a single traceable unit.
V-01 through V-04 declare C-39 and C-41 in the preamble but omit C-43, leaving the third leg
undeclared. C-39, C-41, and C-43 each have individual pass conditions; none of their
definitions requires preamble-level declaration. C-45 requires that when three or more
criteria form a single traceability chain — where each leg's purpose is only fully
interpretable in relation to the others — the preamble names all legs together. Without a
preamble unit declaration, a reviewer must reconstruct the chain from three separate criterion
definitions; a reviewer examining any single leg in isolation cannot determine whether the
other legs are present without explicitly checking each. With a preamble unit declaration,
partial chain implementations (C-39 + C-41 without C-43, or C-39 + C-43 without C-41) are
detectable as chain breaks rather than merely as individual criterion misses. A skill that
declares C-39 and C-41 in the preamble but omits C-43 satisfies both criteria individually
but does not declare the full chain as a unit and does not satisfy C-45.

Denominator: 35 → 37. Aspirational weight: 10 ÷ 37 ≈ 0.270 pts each.

---

**Three new aspirational criteria added from R12 signals (v13)** [criteria listed above]

---

### Scoring Methodology

| Band | Weight | Criteria | Pts/criterion |
|------|--------|----------|---------------|
| Essential (C-01–C-05) | 60 pts | 5 | 12.000 pts |
| Recommended (C-06–C-08) | 30 pts | 3 | 10.000 pts |
| Aspirational (C-09–C-45) | 10 pts | 37 | 0.270 pts |

PASS = full pts · PARTIAL = ½ pts · FAIL = 0 pts

---

### Structural Axis Map (v16)

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| BEFORE YOU START register | **Imperative** | Descriptive | **Table-enforced imperative** | **Imperative** | **Imperative + self-checks** |
| C-42 — Register ambiguity eliminated | **Yes** | No | **Yes** | **Yes** | **Yes** |
| C-43 — Fill-rule echo of C-41 annotation | No | **Yes** | No | **Yes** | **Yes** |
| C-40 — FAILS template self-referential (C-38/C-39) | **SELF-REF** | **SELF-REF** | **SELF-REF** | **SELF-REF** | **SELF-REF** |
| C-44 — FAILS template self-referential (C-42/C-43) | No | No | No | No | **Yes** |
| C-41 — PHASE-1-COMMIT forward annotation | **Present** | **Present** | **Present** | **Present** | **Present** |
| C-45 — C-43 in CO-DEPENDENCY PREAMBLE (full chain) | Absent | Absent | Absent | Absent | **Present** |

**Key structural changes from R15:** C-44 and C-45 are V-05-only signals. All five variations
carry C-40 (SELF-REF for C-38/C-39) and C-41 (forward annotation); both remain shared
baseline in R16. V-05 alone extends C-40's self-referential coverage to include C-42/C-43
(C-44) and declares the three-leg traceability chain as a unit in the CO-DEPENDENCY PREAMBLE
(C-45).

---

### Essential Criteria (C-01–C-05) — All Variations

| ID | Criterion | All Variations | Evidence |
|----|-----------|---------------|---------|
| C-01 | Committee type correctly instantiated | **PASS** | BEFORE YOU START names ROB / shiproom / arch-board with per-type fail conditions; PHASE-0-COMMIT seals type |
| C-02 | Each participant speaks from their role | **PASS** | ROLE VOICE GUARD (domain mechanism) + TIER-N-SEQUENCE-COMMIT (ordering mechanism) present in all variations |
| C-03 | Decisions explicitly recorded | **PASS** | ## STANCE MANIFEST with STANCE INVARIANT; Phase 5 DECISIONS table; verdict must match OUTCOME exactly |
| C-04 | Action items captured with owners | **PASS** | ACTION ITEMS table with Owner Role column (Mechanism 1) + OWNERSHIP TALLY with anonymous-items = 0 gate (Mechanism 2) |
| C-05 | Dissenting opinion represented | **PASS** | DISSENTING OPINIONS table required for every CONDITION/BLOCK role |

**Essential subtotal — all variations: 60 / 60**

---

### Recommended Criteria (C-06–C-08) — All Variations

| ID | Criterion | All Variations | Evidence |
|----|-----------|---------------|---------|
| C-06 | Formal structure | **PASS** | Phase 0–5 lifecycle; PHASE-N-ENTER/EXIT/COMMIT present throughout |
| C-07 | Discussion depth reflects committee type | **PASS** | Tier 2 condition must be specific deliverable; Tier 3 requires RESPONDS-TO + CITE; vague conditions cited as C-07 miss |
| C-08 | AMEND honored when invoked | **PASS** | AMEND ROUTING TABLE with block-dependency routing; stale-site marking; RECOMMIT MANIFEST gate |

**Recommended subtotal — all variations: 30 / 30**

---

### Aspirational Criteria — Shared PASS Baseline (C-09–C-43, 35 criteria)

All five variations satisfy these identically.

| ID | Status | Key Evidence |
|----|--------|--------------|
| C-09 | PASS | INERTIA-ADVOCATE injection provides outside-in signal with labeled INERTIA-FINDING tokens |
| C-10 | PASS | Phase 0 charter gate; Phase 2 exit commits escalation path |
| C-11 | PASS | INERTIA CONTINUITY BRIDGE with YES/NO branch and explicit injection directive |
| C-12 | PASS | Phase 0 attendee roster; injection-pending annotation path |
| C-13 | (variable — see below) | — |
| C-14 | PASS | FAILS entries for C-01, C-02, C-04, C-05, C-07, C-23, C-25, C-34 across fill rules |
| C-15 | PASS | PHASE-N-ENTER gates declare charter preconditions; Phase 1 cannot proceed without PHASE-0-COMMIT |
| C-16–C-33 | PASS (18) | COMMIT seals, TOKEN TRACE CONFIRMATION, three-way vocabulary, TIER-N-SEQUENCE-COMMIT, AMEND routing graph, RECOMMIT MANIFEST |
| C-34 | PASS | RECOMMIT MANIFEST before downstream phase resumes; gate blocks v1 seal after AMEND |
| C-35 | PASS | PHASE-1-COMMIT enumerates sealed tokens as explicit closed set [N=4]; C-35 pre-check at PHASE-2-ENTER |
| C-36 | PASS | CONSUMED / NOT-APPLICABLE / DROPPED vocabulary; count invariant tied to C-35 manifest; REQUIRES: C-35 present |
| C-37 | PASS | C-02: ROLE VOICE GUARD + TIER GATE — two mechanisms. C-04: Owner Role column + OWNERSHIP TALLY — two mechanisms |
| C-38 | PASS | `FAILS [C-NN]: <description>` declared positional required field; deviations explicitly syntactically malformed |
| C-39 | PASS | `REQUIRES: C-35` declared immediately before TOKEN TRACE CONFIRMATION fill rules in all variations |
| C-40 | PASS | FAILS template includes `CORRECT: FAILS [C-38]: …` and `CORRECT: FAILS [C-39]: …` self-referential entries |
| C-41 | PASS | PHASE-1-COMMIT carries inline forward annotation pointing to C-36 TOKEN TRACE CONFIRMATION in all variations |
| C-42 | (variable — see below) | — |
| C-43 | (variable — see below) | — |

**Shared aspirational subtotal: 33 × 0.270 = 8.910 pts**

---

### Variable Criteria per Variation

#### C-13 — Pre-skeleton imperative block

| Variation | Status | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Pure imperatives: eight "If… [criterion miss]" lines; no descriptive framing; terminal halt present |
| V-02 | **PARTIAL** | Type-specific FAIL lines present but embedded under descriptive obligation sentences ("ROB: Produce a readiness verdict…"); mixed register |
| V-03 | **PASS** | Table format [Type / Fail condition / C-tag] enforces imperative register structurally; terminal halt present |
| V-04 | **PASS** | Pure imperatives throughout; identical discipline to V-01 |
| V-05 | **PASS** | Pure imperatives including two self-referential lines for C-42 and C-43; all sentences are commands or fail conditions |

#### C-42 — Register ambiguity eliminated

| Variation | Status | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | No descriptive framing present; every sentence is a testable fail condition or terminal halt |
| V-02 | **FAIL** | "ROB is for quarterly feature reviews. Produce a readiness verdict…" — descriptive framing persists alongside imperative lines |
| V-03 | **PASS** | Table structure structurally eliminates descriptive register; no prose cells present |
| V-04 | **PASS** | No descriptive framing present |
| V-05 | **PASS** | No descriptive framing; self-referential additions (C-42/C-43 lines) are imperative commands |

#### C-43 — Fill-rule echo of C-41 annotation

| Variation | Status | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | C-41 annotation present at source; no echo in TOKEN TRACE CONFIRMATION fill-rule section |
| V-02 | **PASS** | Fill-rule section opens with echo of C-41 annotation; three-point traceability complete |
| V-03 | **FAIL** | C-41 annotation present at source; fill-rule echo absent |
| V-04 | **PASS** | Fill-rule echo present; chain: C-39 REQUIRES → C-41 forward annotation → C-43 fill-rule echo |
| V-05 | **PASS** | Fill-rule echo present; CO-DEPENDENCY PREAMBLE also lists C-43 as third leg (satisfies C-45) |

#### C-44 — Self-referential FAILS template updated for C-42/C-43

| Variation | Status | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Template carries entries for C-38/C-39 only; no C-42 or C-43 entries |
| V-02 | **FAIL** | Template carries entries for C-38/C-39 only |
| V-03 | **FAIL** | Template carries entries for C-38/C-39 only |
| V-04 | **FAIL** | Template carries entries for C-38/C-39 only |
| V-05 | **PASS** | Template additionally carries `CORRECT: FAILS [C-42]: descriptive framing present in BEFORE YOU START` and `CORRECT: FAILS [C-43]: fill-rule echo absent` |

#### C-45 — Multi-leg chain declared as unit in CO-DEPENDENCY PREAMBLE

| Variation | Status | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | C-39 and C-41 in preamble; C-43 absent; chain declared as two legs only |
| V-02 | **FAIL** | C-39 and C-41 in preamble; C-43 absent |
| V-03 | **FAIL** | C-39 and C-41 in preamble; C-43 absent |
| V-04 | **FAIL** | C-39 and C-41 in preamble; C-43 absent |
| V-05 | **PASS** | CO-DEPENDENCY PREAMBLE lists C-39, C-41, and C-43 together with chain label: "C-39 + C-41 + C-43 form one traceability chain — pass all three or the chain is partial" |
```

---

Two new criteria extracted. The pattern they encode:

- **C-44** captures the *maintenance obligation* of C-40 — not just "have self-referential entries" but "keep them current as the rubric grows." Without C-44, C-40 is satisfied once and never revisited.
- **C-45** captures the *chain-as-unit* visibility obligation — C-39, C-41, and C-43 can each pass individually while the three-leg chain remains invisible as a unit. The preamble declaration is the only mechanism that makes partial chain implementations detectable without cross-referencing three criterion definitions.
