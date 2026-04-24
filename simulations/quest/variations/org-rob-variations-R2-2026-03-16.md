Written to:
- `simulations/quest/golden/org-rob-variate-R2-2026-03-16.md` — complete prompt bodies
- `simulations/quest/variations/org-rob-variations-R2-2026-03-16.md` — summary + coverage map

---

## org-rob R2 -- Five Variations

R2's design principle: every variation targets at least one of the three new v2 criteria (C-11 phase gate contracts, C-12 dual-direction traceability, C-13 named blocker format). R1 showed all five variations cleared essential criteria universally — the differentiators are now the aspirational tier.

| Variation | Axis | Primary Target | Key Mechanic |
|-----------|------|----------------|--------------|
| **V-01** | Lifecycle emphasis | C-11 (core) | Phase gate is the skeleton — Entry/Review/Exit blocks, not a review with a gate appended |
| **V-02** | Output format | C-12 (core) | Global Finding Registry with `Acknowledged As` column makes dual-direction traceability a format invariant |
| **V-03** | Phrasing register | C-13 (core) | Retroactive voice — every role checks backward before reviewing forward; triad format in first-person check |
| **V-04** | Format + Lifecycle (combo) | C-11/C-12/C-13 | Table-first + phase gate contracts — three-block template (Phase Gate table / Findings table / Stage Exit table); all v2 criteria structurally enforced |
| **V-05** | Inertia + Blocker (combo) | C-02/C-13 | Inertia-advocate opens each stage; Named Blocker Protocol closes it; TPM register includes mandatory inertia-risk entry |

**Predicted leaderboard:** V-04 >= V-01 > V-02 > V-05 > V-03

The key open question R2 will answer: does C-11 require table format to be reliably enforced, or does the gate-as-skeleton architecture in V-01 achieve it equally well in prose?
ls this in or the registry shows a gap
- Final registry after all stages; residual open items (empty Acknowledged As) listed explicitly
- Retroactive Check section at every stage closing before verdict; triad format required

**Primary target criteria:** C-12 (core), C-13; C-11 weaker (no explicit entry/exit gate blocks)

---

### V-03 -- Phrasing Register: Retroactive Voice
**Axis:** Phrasing register
**Hypothesis:** When every role opens with a mandatory retroactive check -- "does anything I
see here break a prior verdict?" -- before writing forward findings, C-13 (named blocker
format) becomes grammatically enforced at discovery time. First-person voice throughout also
strengthens C-02 (role-loaded perspective) because role identity is the grammar, not a label.

**Key mechanics:**
- First-person role voice; orientation.frame opens each stage
- Mandatory Retroactive Check section before every forward-review section
- Retroactive Check uses triad format if blocker found; states "none" if not
- Arch-board retroactive check called out as most consequential (tpm authority)
- Retroactive Blocker Log in synthesis compiles all blocker events across stages

**Primary target criteria:** C-13 (core), C-02; C-11 and C-12 weaker

---

### V-04 -- Table-First + Phase Gate Contracts (Combination)
**Axes:** Output format + Lifecycle emphasis
**Hypothesis:** V-02 Round 1 scored 95 under v1 math (89 under v2 recomputation) using
table-first format. Adding explicit phase gate blocks to the table-first structure closes
the three v2 gaps: Phase Gate table enforces C-11, `Responds To` column + Escalation Chain
table with Acknowledged As column enforce C-12, Retroactive Check row in Stage Exit table
enforces C-13. The combination should match V-04 Round 1's 100 under v2 math.

**Key mechanics:**
- Three-block stage structure: Phase Gate table + Findings table + Stage Exit table
- No prose for structural elements; all requirements are table rows or columns
- `Responds To` column in Findings table: dual-direction traceability as column invariant
- `Retroactive Check` row in Stage Exit table: triad format required when blocker found
- Escalation Chain table in synthesis carries `Acknowledged As` column (both directions)

**Primary target criteria:** C-11, C-12, C-13 (all core); C-03, C-04, C-07 structurally enforced

---

### V-05 -- Inertia Framing + Named Blocker Protocol (Combination)
**Axes:** Inertia framing + Named blocker protocol
**Hypothesis:** V-03 Round 1 scored 87.5 -- highest C-02 signal in the round -- because
the inertia-advocate forced role-specific findings. It lost to V-04 on C-07/C-09/C-13.
Adding the Named Blocker Protocol at every stage exit closes those structural gaps while
preserving V-03 R1's C-02 differentiation. Two challengers per stage: inertia-advocate
opens (forward challenge), blocker scan closes (backward challenge).

**Key mechanics:**
- Inertia Challenge block at stage TOP (V-03 R1 mechanic; inertia-advocate.md required)
- Named Blocker Protocol at stage CLOSE: mandatory scan with triad format
- TPM risk register has a required inertia-risk entry (risk of NOT shipping)
- Inertia Resolution table in synthesis tracks inertia case across all stages
- Retroactive Blocker Log in synthesis compiles named blocker events

**Primary target criteria:** C-02 (inertia axis), C-13 (blocker protocol); C-11/C-12 weaker

---

**Rubric coverage map (v2 -- 13 criteria):**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Stage identity | + | + | + | + | + |
| C-02 Role-loaded lens | + | + | ++ | ++ | ++ |
| C-03 ROB format | + | ++ | + | ++ | + |
| C-04 Actionable findings | + | ++ | + | ++ | + |
| C-05 Explicit go/no-go | ++ | ++ | ++ | ++ | ++ |
| C-06 Cross-stage coherence | ++ | ++ | + | ++ | + |
| C-07 Risk register >=3 | ++ | ++ | ++ | ++ | ++ |
| C-08 Spire cascade | ++ | ++ | ++ | ++ | ++ |
| C-09 Inter-stage blockers | ++ | ++ | + | ++ | ++ |
| C-10 Cross-cutting themes | + | + | ++ | ++ | ++ |
| C-11 Phase gate contracts | ++ | o | o | ++ | o |
| C-12 Dual-direction trace | ++ | ++ | + | ++ | + |
| C-13 Named blocker format | ++ | ++ | ++ | ++ | ++ |

`++` = structural enforcement &nbsp;`+` = natural outcome &nbsp;`o` = possible but not enforced

**Predicted leaderboard:** V-04 >= V-01 > V-02 > V-05 > V-03

V-04 and V-01 are the contenders. V-04's table enforcement removes format variance (C-03/C-04
certainty). V-01's gate-as-skeleton makes C-11 structurally primary. Likely both near 100.
V-02 misses C-11 structural enforcement; predicted ~94-96. V-05 misses C-11/C-12; predicted
~90-94. V-03 misses C-11/C-12 and relies on first-person voice to enforce C-13 (format
variance risk); predicted ~88-92.

**R2 open questions:**
1. Does C-11 (phase gates) require table format to be structurally reliable, or does the
   gate-as-skeleton architecture in V-01 achieve it equally well in prose?
2. Does V-02's registry approach achieve C-12 as reliably as V-04's `Responds To` column +
   Escalation Chain table with Acknowledged As?
3. Is first-person retroactive voice (V-03) as reliable for C-13 as an explicit exit-block
   row (V-04)?
