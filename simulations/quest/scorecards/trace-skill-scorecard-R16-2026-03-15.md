# trace-skill Round 16 — Scorecard

## Entry State

R15 V-05 passes C-01 through C-47 (all 47 criteria). R16 variations are purely additive — each axis adds a new structural element without removing or altering any passing element. No variation can regress below the entry state.

---

## Per-Variation Scoring

### Shared baseline: C-01 through C-47 (all variations)

All five variations inherit the R15 V-05 baseline. Evidence notes below apply uniformly unless a variation axis touches a criterion directly.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-01 | Four phases in sequence | PASS | PASS | PASS | PASS | PASS | No axis touches phase structure |
| C-02 | Gather enumerates inputs by name + source | PASS | PASS | PASS | PASS | PASS | Inherited; no axis alters Gather |
| C-03 | Bind maps every Gather input to resolved value | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-04 | Execute produces correct artifact | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-05 | Verdict declares explicit PASS/FAIL with rationale | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-06 | Phases carry exact schema labels | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-07 | Verdict cites criterion IDs | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-08 | Artifact complete — no elision markers | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-09 | Coverage Matrix with closed-world preamble | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-10 | Execute relays carry evidence fields | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-11 | Gather enumerates spec inputs before invocation | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-12 | BLOCKED declaration on any Gap=YES | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-13 | Artifact delimiter markers | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-14 | Pre-trace Phase Label Schema table | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-15 | Verdict is compliance ledger table | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-16 | Bind Status enum (RESOLVED/UNRESOLVED/BLOCKED) | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-17 | Bind conflict precedence rule declared | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-18 | Relay rows carry `InputName = "ResolvedValue"` pairs | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-19 | Bind table "Precedence applied" column | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-20 | Coverage Matrix CLOSED assertion names each Required=YES input | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-21 | Relay Schema anti-pattern prohibition | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-22 | "Precedence applied" closed three-value vocabulary | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-23 | CLOSED ASSERTION terminates with explicit closure line | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-24 | Anti-pattern prohibition as structurally independent row with `VIOLATION` | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-25 | `PrecedenceVocabulary` named type; column header cites type | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-26 | Closure terminus as labeled structural mandate in prompt | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-27 | Relay Schema Required column closed two-value vocabulary (YES/VIOLATION) | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-28 | Uniform `(TypeName)` annotation convention across all typed columns | PASS | PASS | PASS | PASS | PASS | V-02 adds row 29 to ASR; typed column notation carried — uniform convention maintained |
| C-29 | Named structural mandates carry formal defect classification | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-30 | `DefectCodeVocab` declared as closed type | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-31 | C-28 uniform annotation propagates to all composed criteria columns | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-32 | Verdict compliance ledger `Defect code` column fully populated | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-33 | `DefectCodeVocab` includes independence statement | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-34 | C-28 annotation-site count assertion resolves to PASS/FAIL binary | PASS | PASS | PASS | PASS | PASS | V-02 changes count from 28→29; gate updates accordingly — still binary PASS/FAIL |
| C-35 | Empty-cell check structurally ordered before ledger reading | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-36 | `**Independence Statement**:` label declared as named structural mandate | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-37 | C-28 COUNT GATE failure emits `DefectCodeVocab`-coded defect | PASS | PASS | PASS | PASS | PASS | Inherited; count update doesn't break defect-emission mechanism |
| C-38 | PRE-READ GATE carries formal defect classification for empty-cell | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-39 | STRUCTURAL MANDATE block header carries inline criterion citation `(C-XX)` | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-40 | STRUCTURAL MANDATE block closes with scorer confirmation heuristic | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-41 | Canonical STRUCTURAL MANDATE template declared explicitly | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-42 | Canonical template encodes scorer confirmation closing line | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-43 | C-42 CONFORMANCE-COLLAPSE CLAIM carries scorer confirmation heuristic | PASS | PASS | PASS | PASS | PASS | V-03: heuristic step (b) now explicitly names C-47 — still satisfies "SCORER HEURISTIC present with confirmation path" |
| C-44 | COUNT GATE scope enumerates TCR as annotation site | PASS | PASS | PASS | PASS | PASS | Inherited; V-02 extends scope to row 29 but TCR still present |
| C-45 | SCORER HEURISTIC label is self-citing (`SCORER HEURISTIC (C-43)`) | PASS | PASS | PASS | PASS | PASS | Inherited; V-03 changes the heuristic body, not the label format |
| C-46 | COUNT GATE scope declared as formal ANNOTATION SCOPE REGISTRY table | PASS | PASS | PASS | PASS | PASS | V-02: row 29 added; TCR remains a named row — C-46 still satisfied |
| C-47 | ANNOTATION SCOPE REGISTRY appears as TCR row (e.g., Component 5) | PASS | PASS | PASS | PASS | PASS | V-01: TCR row 5 now carries `(C-47)` criterion citation; presence verifiable by row lookup — C-47 still satisfied and strengthened |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|-----------|---------------|-----------------|-------------------|-------|
| V-01 | 60 (5/5) | 30 (3/3) | 10 (39/39) | **100** |
| V-02 | 60 (5/5) | 30 (3/3) | 10 (39/39) | **100** |
| V-03 | 60 (5/5) | 30 (3/3) | 10 (39/39) | **100** |
| V-04 | 60 (5/5) | 30 (3/3) | 10 (39/39) | **100** |
| V-05 | 60 (5/5) | 30 (3/3) | 10 (39/39) | **100** |

All five variations: **100/100. All essential PASS. Golden threshold met.**

---

## Ranking

All variations tie at 100. Discrimination is qualitative — excellence signal analysis below.

**Rank (rubric-equivalent, then structural depth):**

1. **V-05** — all three axes; SCORER HEURISTIC step (b) names C-47 explicitly as a confirmation step rather than an implied consequence of "rows 1–5"; self-complete ASR (row 29); self-citing TCR row 5
2. **V-04** — V-01 + V-02; self-complete ASR closes the registry's own open-world gap; TCR row 5 is self-citing; SCORER HEURISTIC still implies C-47 rather than citing it
3. **V-01** — TCR row 5 self-citing; no self-completeness in ASR; SCORER HEURISTIC does not split confirmation by row
4. **V-02** — ASR self-lists as row 29 (strongest single-axis upgrade for closed-world discipline); count gate = 29; TCR row 5 not self-citing
5. **V-03** — SCORER HEURISTIC names C-47 explicitly in step (b); neither TCR self-citation nor ASR self-completeness

---

## Excellence Signal Analysis

### Why V-05 is strongest

**Pattern 1 — SCORER HEURISTIC step decomposition by criterion (candidate C-48)**

V-03 / V-05 split the CONFORMANCE-COLLAPSE CLAIM's SCORER HEURISTIC step (b) from:
> "TCR rows 1–5 are present and typed"

into:
> "TCR rows 1–4 (canonical) + TCR row 5 (C-47) names the ANNOTATION SCOPE REGISTRY"

This makes C-47 a **named, cited confirmation step** in the SCORER HEURISTIC rather than an implied consequence of a count. The parallel chain is exact:
- C-39: STRUCTURAL MANDATE headers carry `(C-XX)` — mandate-to-criterion traceable by header inspection
- C-45: SCORER HEURISTIC label carries `(C-43)` — heuristic-to-criterion traceable by label inspection
- V-05 (C-48 candidate): each SCORER HEURISTIC **step** names the criterion it confirms — step-to-criterion traceable by step body alone, no header/label scan

A scorer using V-04 or earlier must count to 5 and infer that row 5 = ASR = C-47. A scorer using V-05 reads "TCR row 5 (C-47)" and the confirmation path is complete.

**Pattern 2 — Registry self-completeness as closed-world discipline (candidate C-48 or companion criterion)**

V-02 / V-04 / V-05 add ASR row 29 = the registry's own typed column. A registry that enumerates all annotation sites but omits itself has an internal open-world gap: the typed column within the ANNOTATION SCOPE REGISTRY table is a `(TypeName)` annotation site that C-28's count gate should cover but the registry itself does not declare. V-02's correction propagates C-20's closed-world discipline (CLOSED ASSERTION names every Required=YES input) to the C-46 registry: **a registry that enumerates annotation scope must enumerate its own typed column as scope**. Count gate = 29 is the verifiable signal that self-completeness is present.

**Why V-02 outranks V-01 and V-03 individually**

V-01 adds self-citation to a TCR row — valuable but the TCR row was already verifiable by table lookup (C-47 already passes). The upgrade is traceable but the path already existed.

V-02 closes a structural gap: before V-02, the ASR is a table whose typed column is not in its own enumeration — the very mechanism designed to guarantee closed-world coverage has an uncovered site. V-02's correction is more significant because it fixes a gap rather than strengthening an already-closed path.

---

## New Patterns Summary

Two patterns not covered by C-01 through C-47:

1. **SCORER HEURISTIC step-level criterion citation** — Each step in a multi-step SCORER HEURISTIC names the criterion it confirms by ID (`(C-XX)`) in the step body, not just in the label. Step-body citation makes individual confirmation steps bidirectionally traceable without reading surrounding steps or the label.

2. **Registry self-completeness** — A formal registry (ANNOTATION SCOPE REGISTRY, Defect Classification Registry, etc.) that declares its own typed column must list that column as a row in the registry itself. A registry that omits its own annotation site has an internal open-world gap inconsistent with the closed-world discipline applied to every other registry in the prompt.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SCORER HEURISTIC step-level criterion citation: each step in a multi-step SCORER HEURISTIC names the criterion it confirms by ID in the step body, making individual confirmation steps bidirectionally traceable without label or header inspection", "Registry self-completeness: a formal registry whose table carries a typed column must list that column as a row in itself; omitting the registry's own annotation site creates an internal open-world gap inconsistent with the closed-world discipline applied to all other registries in the prompt"]}
```
