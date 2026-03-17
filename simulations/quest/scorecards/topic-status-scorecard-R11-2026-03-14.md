## Round 11 Scorecard — `topic:status`

**Rubric v11 (max 245)**

### Score Summary

| Rank | Variant | C-37 | C-38 | Score |
|------|---------|------|------|-------|
| T-1 | V-01 | PASS | PASS | **245/245** |
| T-1 | V-04 | PASS | PASS | **245/245** |
| T-1 | V-05 | PASS | PASS | **245/245** |
| T-4 | V-02 | FAIL | PASS | **240/245** |
| T-4 | V-03 | PASS | FAIL | **240/245** |

All 5 variants pass C-01 through C-36 (235-pt baseline). Tier 10 is the sole differentiator.

### C-37 Evaluation

- **V-02 FAIL**: Exit declarations carry names only (`Exit A -- file absent:`) — no inline trigger clause at the declaration site. Preamble trigger sentences (C-35) do not propagate to the GUARD site; C-35 ∧ C-32 ⊄ C-37 confirmed.
- **V-01/V-03/V-04/V-05 PASS**: All carry "fires when..." clauses co-located with exit names at their declaration sites (prose form for V-01/V-03, GUARD-contract-field form for V-04/V-05). **C-37 form-agnosticism confirmed.**

### C-38 Evaluation

- **V-03 FAIL**: Third C-36 site is a COMMIT DECISION block — post-execution, outside any execution phase body. C-36 via commit-framing ⊄ C-38 confirmed.
- **V-01/V-02/V-04/V-05 PASS**: PHASE 2 OUTPUT DECLARATION is embedded in the PHASE 2 execution body. **C-38 form-agnosticism confirmed** across inline-appended label (V-01, V-04) and elevated titled box (V-05).

### Excellence Signals

R11 hypothesis fully confirmed: C-37 and C-38 compose freely — no design tension between GUARD-site trigger co-location and execution-body OUTPUT DECLARATION. Both Tier 10 isolation tests return clean 5-point gaps matching the predicted score map exactly. No new structural gap is observable at 245 (the maximum).

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": []}
```
field form | **PASS** |
| V-05 | GUARD contract field identical to V-04 — trigger clauses in GUARD-contract-field form | **PASS** |

V-02 isolates C-37: preamble per-axis trigger sentences (C-35 PASS) and
execution-body OUTPUT DECLARATION (C-38 PASS) are both present; only the
GUARD-site co-location is withheld. Confirms that trigger characterization at
the preamble site alone does not satisfy C-37.

C-37 form-agnosticism result: execution-prose inline form (V-01, V-03) and
GUARD-contract-field form (V-04, V-05) both satisfy when the trigger clause
appears at the exit declaration site. Form is not evaluated.

#### C-38 — Phase-output invariant declaration

C-38 requires the third C-36 site to be an explicitly declared OUTPUT
DECLARATION block embedded within the execution phase body. COMMIT DECISION
block echoes (post-execution) and lifecycle PHASE 2 OUTPUT fields (phase
definition header) satisfy C-36 but not C-38.

| Variant | Third C-36 site form | C-38 |
|---------|----------------------|------|
| V-01 | `PHASE 2 OUTPUT DECLARATION:` inline label within PHASE 2 execution body (below execution logic, before PHASE 3) — execution-body resident | **PASS** |
| V-02 | `PHASE 2 OUTPUT DECLARATION:` inline label within PHASE 2 execution body — execution-body resident | **PASS** |
| V-03 | COMMIT DECISION block line: `Dual-axis gate invariant: file-absent and topic-absent exits are structurally distinct stop conditions with distinct messages` — post-execution commit-framing section, outside any execution phase body; C-38 deliberately withheld | **FAIL** |
| V-04 | `PHASE 2 OUTPUT DECLARATION:` inline label appended to PHASE 2 execution section (below lifecycle contract header box) — execution-body resident, distinct from the OUTPUT field within the contract header | **PASS** |
| V-05 | `+-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant -+` elevated titled box embedded in PHASE 2 execution section — execution-body resident, maximally explicit | **PASS** |

V-03 isolates C-38: GUARD-site trigger clauses (C-37 PASS) and COMMIT DECISION
echo (C-36 PASS, confirmed R10 V-01 at 235) are both present; only the
execution-body residency is withheld. Confirms that post-execution commit-framing
is insufficient for C-38 despite satisfying C-36's minimum-sufficient third-site
requirement.

C-38 form-agnosticism result: inline-appended label (V-01, V-04) and elevated
titled box (V-05) both satisfy when the OUTPUT DECLARATION is embedded in the
execution phase body. Block presentation form is not evaluated.

---

### Per-Variant Scorecards

#### V-01 — Minimum delta: C-37 + C-38 in execution-prose form

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35–C-36 | 10/10 | 2/2 PASS |
| Tier 10 | C-37 | 5/5 | **PASS** |
| Tier 10 | C-38 | 5/5 | **PASS** |
| **Total** | | **245/245** | **38/38** |

Hypothesis confirmed: two targeted changes from R10 V-01's 235-scoring structure
are sufficient. (1) Each exit declaration in PHASE 2 gains an inline "fires
when..." trigger clause, satisfying C-37 at the declaration site. (2) The
COMMIT DECISION echo is replaced with a `PHASE 2 OUTPUT DECLARATION:` inline
label inside the PHASE 2 execution body, satisfying C-38. Both changes are
minimal and non-disruptive to surrounding structure.

---

#### V-02 — C-37 withheld: exits named, no inline trigger clauses (isolation test)

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35–C-36 | 10/10 | 2/2 PASS |
| Tier 10 | **C-37** | **0/5** | **FAIL** |
| Tier 10 | C-38 | 5/5 | **PASS** |
| **Total** | | **240/245** | **37/38** |

C-37 isolation confirmed: preamble per-axis trigger sentences (C-35 PASS) and
execution-body OUTPUT DECLARATION (C-38 PASS) are both present. Exit
declarations carry named labels only (`Exit A -- file absent:`, `Exit B --
topic not registered:`) without inline trigger clauses. The 5-point gap from
V-01 (245) confirms that GUARD-site co-location of trigger characterization is
independently necessary beyond what C-35 establishes at the preamble site.
C-35 ∧ named exits ⊄ C-37.

---

#### V-03 — C-38 withheld: COMMIT DECISION echo as third C-36 site (isolation test)

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35–C-36 | 10/10 | 2/2 PASS |
| Tier 10 | C-37 | 5/5 | **PASS** |
| Tier 10 | **C-38** | **0/5** | **FAIL** |
| **Total** | | **240/245** | **37/38** |

C-38 isolation confirmed: GUARD-site trigger clauses (C-37 PASS) and COMMIT
DECISION echo (C-36 PASS, confirmed baseline from R10 V-01 at 235) are both
present. The third C-36 site is the COMMIT DECISION block: a post-execution
commit-framing section, structurally outside any execution phase body. The
5-point gap from V-01 (245) confirms that execution-body residency is
independently necessary beyond C-36's minimum-sufficient third-site requirement.
C-36 via COMMIT DECISION ⊄ C-38.

---

#### V-04 — Lifecycle GUARD form: C-37 + C-38 via contract entries and execution-body label

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35–C-36 | 10/10 | 2/2 PASS |
| Tier 10 | C-37 | 5/5 | **PASS** |
| Tier 10 | C-38 | 5/5 | **PASS** |
| **Total** | | **245/245** | **38/38** |

C-37 via GUARD-contract-field form: lifecycle GUARD entries carry inline trigger
clauses (`Exit A -- file absent: fires when strategy.md does not exist on
disk ->`) within the contract box, satisfying C-37 via the GUARD-field path.
C-38 via inline-appended execution-body label: `PHASE 2 OUTPUT DECLARATION:`
appears in the execution section below the contract header box -- execution-body
resident, distinct from R10 V-04's failure case where the OUTPUT field was
inside the contract header box (phase definition field). V-04 confirms C-37
form-agnosticism across execution-prose (V-01) and lifecycle GUARD contract
(V-04) entry formats.

---

#### V-05 — Lifecycle GUARD + elevated titled PHASE 2 OUTPUT DECLARATION block

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35–C-36 | 10/10 | 2/2 PASS |
| Tier 10 | C-37 | 5/5 | **PASS** |
| Tier 10 | C-38 | 5/5 | **PASS** |
| **Total** | | **245/245** | **38/38** |

GUARD entries identical to V-04 (C-37 via GUARD-contract-field form). C-38 via
elevated titled box: `+-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant
-+` is a formally named, visually demarcated block embedded in the PHASE 2
execution section. The block's title makes execution-phase-resident status
independently verifiable without reference to the preamble or GUARD entries --
a scorer reading only the box can determine that the dual-axis invariant is
declared within phase execution. V-05 confirms C-38 form-agnosticism: the
titled-block form and the inline-appended label form (V-01, V-04) both satisfy.

---

### Ranking

| Rank | ID | Score | Differentiator |
|------|----|-------|----------------|
| T-1 | V-01 | **245/245** | Minimum delta -- execution-prose inline trigger clauses (C-37) + PHASE 2 OUTPUT DECLARATION label (C-38) |
| T-1 | V-04 | **245/245** | C-37 via lifecycle GUARD-contract entries + C-38 via inline-appended execution-body label |
| T-1 | V-05 | **245/245** | C-37 via lifecycle GUARD-contract entries + C-38 via elevated titled execution-body block |
| T-4 | V-02 | **240/245** | C-37 FAIL -- exits named at GUARD site without inline trigger characterization |
| T-4 | V-03 | **240/245** | C-38 FAIL -- COMMIT DECISION echo is post-execution, outside execution phase body |

---

### C-37 Isolation Confirmed

V-01 (245) vs V-02 (240): clean 5-point gap. Both variants carry per-axis
trigger sentences in the preamble (C-35 PASS) and an execution-body OUTPUT
DECLARATION (C-38 PASS). The sole difference is the presence of inline trigger
clauses at the GUARD exit declaration sites. Named exits alone at the GUARD site
do not propagate C-35's preamble-level trigger characterization to the exit
declaration level. C-35 ∧ C-32 ⊄ C-37 confirmed.

### C-38 Isolation Confirmed

V-01 (245) vs V-03 (240): clean 5-point gap. Both variants carry GUARD-site
inline trigger clauses (C-37 PASS) and a valid C-36 third site (C-36 PASS).
The sole difference is the structural location of the third site: post-execution
commit-framing section (V-03) vs execution-body declaration (V-01). COMMIT
DECISION is a valid C-36 third site -- C-38 is independently necessary beyond
C-36's minimum-sufficient third-site requirement. C-36 via commit-framing ⊄ C-38
confirmed.

### C-37 Form-Agnosticism Confirmed

V-01 (execution-prose inline: `Exit A -- file absent: fires when...`) and
V-04/V-05 (lifecycle GUARD contract: `Exit A -- file absent: fires when... ->`
within the contract box): all three score 245. C-37 requires trigger clause
co-location at the exit declaration site but is agnostic to whether the
declaration site is an execution-prose line or a GUARD-contract-field entry.

### C-38 Block-Form Agnosticism Confirmed

V-01/V-04 (inline-appended `PHASE 2 OUTPUT DECLARATION:` label) and V-05
(elevated `+-- PHASE 2 OUTPUT DECLARATION --+` titled box): all three score 245.
C-38 requires execution-body residency but is agnostic to the visual presentation
of the OUTPUT DECLARATION within the body.

---

### Excellence Signals

**Signal 1 — R11 hypothesis confirmed: C-37 and C-38 jointly satisfiable**

The R10 gap closed at R11. V-04 (R10) satisfied C-37 but not C-38; V-05 (R10)
satisfied C-38 but not C-37. R11 V-01, V-04, and V-05 each satisfy both
simultaneously. There is no design tension between GUARD-site trigger
co-location (C-37) and execution-body OUTPUT DECLARATION (C-38). The two
mechanisms compose freely across both execution-prose and lifecycle-contract
structural forms.

**Signal 2 — Minimum delta: two targeted changes from R10 V-01 achieve 245**

V-01 changes exactly two things from R10 V-01's 235-scoring structure: (1) each
exit declaration gains a "fires when..." inline trigger clause, and (2) the
COMMIT DECISION echo is replaced with a `PHASE 2 OUTPUT DECLARATION:` label
inside the PHASE 2 execution body. The per-phase contract boxes (V-04, V-05) and
the elevated titled block (V-05) are additive presentations, not prerequisites.
245 is achievable via the minimum-friction execution-prose form.

**Signal 3 — C-38 distinguishes execution-phase-resident from post-phase-resident invariant sites**

The C-38 isolation (V-03 vs V-01) cleanly characterizes the distinction:
COMMIT DECISION block echoes describe the invariant in the context of a commit
decision made after all phases complete; PHASE 2 OUTPUT DECLARATION blocks
describe the invariant as an active constraint during phase execution. C-38
formalizes that execution-phase residency -- co-location with the logic being
constrained -- is a stronger structural site than commit-framing. This is the
same logic that drove C-37: co-location at the GUARD site is stronger than
preamble-only characterization.

---

### R11 Findings

**F-01: Both Tier 10 isolation tests return clean 5-point gaps**

V-02 isolates C-37 (5-point gap at 240 vs 245): C-35 preamble trigger sentences
do not imply C-37 GUARD-site co-location. V-03 isolates C-38 (5-point gap at
240 vs 245): C-36 minimum-sufficient third site does not imply C-38 execution-
body residency. Both isolation results match the predicted score map exactly.
The R11 rubric is analytically clean: no criterion degeneracy at Tier 10.

**F-02: C-37 and C-38 are form-agnostic within their respective constraints**

Four cross-form tests in R11:
- C-37 via execution-prose (V-01, V-03): PASS
- C-37 via lifecycle GUARD-contract field (V-04, V-05): PASS
- C-38 via inline-appended label (V-01, V-04): PASS
- C-38 via elevated titled block (V-05): PASS
All predicted 245-scoring variants reach 245. All predicted 240-scoring variants
reach 240. Zero prediction errors. Form-agnosticism is confirmed for both
criteria.

**F-03: No new structural gap observable at 245**

Three variants achieve 245/245. No variant achieves more than 245 (the maximum).
The patterns distinguishing the 245 cluster from the 240 cluster are the two
mechanisms directly encoded in C-37 and C-38. No pattern observable in V-01,
V-04, or V-05 that the others lack would constitute a new criterion beyond what
C-37 and C-38 already capture. The form-agnosticism findings are pass-condition
clarifications, not new structural gaps. R11 is a closed round.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": []}
```
