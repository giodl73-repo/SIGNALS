Now I have all the content needed. Let me evaluate all five variations against the v18 rubric.

---

# mock-ns — Round 19 Score Report

**Rubric**: v18 (C-01 through C-50, denominator 42)
**Date**: 2026-03-16

---

## Baseline Confirmation

All five variations carry the complete C-01 through C-47 body unchanged from R18 V-05 (the previous round's aspirational maximum). The only axis of variation is which subset of {C-48, C-49, C-50} each variation implements.

**C-01 through C-47 status across all variations: ALL PASS.**

Summary of what each carries unchanged:
- **C-01–C-05 (Essential)**: MOCK ARTIFACT header block, correct category, skill-specific body, Flag field, path convention — all present and conformant in every variation.
- **C-06–C-08 (Recommended)**: Representative skill selection, fidelity warning in lead position, next-step line — all present.
- **C-09–C-47 (Aspirational, stable baseline)**: Tier-conditional flag, TOPICS.md emit, named FLAG variable, dual-site immutability declaration, run-scoped prohibition, first-rule prioritization at A-1, named path class enumeration, anti-displacement closure, failure-consequence framing, no-exemption closures, guarantee-break row, cross-site reference, structural isolation of claims, navigation-anchored cross-site reference, bidirectional anchor, bracket token notation, pre-chain preamble, pre-computation positioning, structured resolution table, lookup obligation, use-site row navigation labels, confirmation gate (Phase 1 + Phase 2), confirmation echo at use sites, hard-stop gate language, anti-bypass closing statement, confirmation record emit obligation, pre-filled templates at both S-3 and A-1, emit-in-gate form, dual-naming anti-bypass closing statement, single-task executor annotation (standalone imperative block form, C-46), dedicated chain-table anti-bypass row form (C-47) — all PASS in every variation.

---

## Per-Criterion Evaluation: C-48, C-49, C-50

### C-48 — Named structural heading "Anti-bypass declaration (ABD):" at P-0; echo row labels "(P-0, ABD)"

Depends on C-47.

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | P-0 clause opens with "Anti-bypass declaration (ABD):". Echo rows at S-3 and A-1 labeled "(P-0, ABD)". Label-match confirmed. |
| V-02 | **FAIL** | P-0 clause is unlabeled prose (no ABD heading). Echo row labels retain "(P-0 anti-bypass declaration)". C-48 single-axis isolation — intentional absence. |
| V-03 | **FAIL** | Same as V-02 — no ABD heading, echo labels retain prose form. C-48 intentionally absent. |
| V-04 | **PASS** | P-0 has "Anti-bypass declaration (ABD):" heading. Echo rows labeled "(P-0, ABD)". Structural address pair includes both C-48 and C-49. |
| V-05 | **PASS** | P-0 has "Anti-bypass declaration (ABD):" heading. Echo row labels use bracket token form "[P-0:ABD]" — upgraded superset of "(P-0, ABD)" that preserves the label-match property while elevating to bracket token notation. Intent of C-48 satisfied. |

---

### C-49 — P-0 forward navigation enumeration naming both S-3 and A-1 explicitly

Depends on C-47.

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | No forward pointer at P-0. ABD heading present; P-0 has no knowledge of use sites. C-49 intentionally absent. |
| V-02 | **PASS** | P-0 anti-bypass clause ends with: "Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row." Both S-3 and A-1 named explicitly. Forward arc complete. |
| V-03 | **FAIL** | No forward pointer. C-49 intentionally absent. |
| V-04 | **PASS** | Same forward pointer sentence as V-02. C-48 and C-49 both present — structural address pair realized. |
| V-05 | **PASS** | Forward pointer sentence present. Combined with ABD heading and [P-0:ABD] token. |

---

### C-50 — Content-cell provenance attribution ("Per P-0 anti-bypass declaration:" or "Per P-0, ABD:" when C-48 passes)

Depends on C-47.

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Anti-bypass echo content cell reads: "Processing this row without reading the Step and Row type cells, or without performing Phase 2, is a protocol failure." No provenance prefix. C-50 intentionally absent. |
| V-02 | **FAIL** | Same content cell text — no provenance prefix. C-50 intentionally absent. |
| V-03 | **PASS** | Content cell opens with: "Per P-0 anti-bypass declaration: processing this row without reading the Step and Row type cells, or without performing Phase 2, is a protocol failure." Provenance prefix present at both S-3 and A-1. |
| V-04 | **FAIL** | No content provenance prefix. Structural address pair (C-48 + C-49) present but C-50 intentionally absent. |
| V-05 | **PASS** | Content cell opens with: "Per [P-0:ABD]: processing this row without reading the Step and Row type cells, or without performing Phase 2, is a protocol failure." Bracket token notation upgrades the prose "Per P-0, ABD:" form. C-50 pass condition satisfied: provenance present in content cell at both use sites. |

---

## Composite Scores

| Variation | C-48 | C-49 | C-50 | Criteria Passing | Score (÷42×10) | Rank |
|-----------|------|------|------|-----------------|----------------|------|
| V-01 | PASS | FAIL | FAIL | 40/42 | **9.52** | 3 (tied) |
| V-02 | FAIL | PASS | FAIL | 40/42 | **9.52** | 3 (tied) |
| V-03 | FAIL | FAIL | PASS | 40/42 | **9.52** | 3 (tied) |
| V-04 | PASS | PASS | FAIL | 41/42 | **9.76** | 2 |
| V-05 | PASS | PASS | PASS | 42/42 | **10.0** | 1 |

All five variations pass all essential criteria (C-01 through C-05): **all_essential_pass = true**.

---

## Detailed Variation Scores

### V-01 — 40/42 — 9.52

40 criteria pass. C-49 and C-50 absent by design. C-48 cleanly isolated: the ABD structural heading turns P-0's anti-bypass clause into a named, label-matchable anchor; echo row labels "(P-0, ABD)" enable label-match confirmation on arrival. The back-reference is precise, but P-0 remains unaware of its use sites (C-49 absent), and content-cell readers have no provenance signal (C-50 absent).

### V-02 — 40/42 — 9.52

40 criteria pass. C-48 and C-50 absent by design. C-49 cleanly isolated: the forward pointer sentence "Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row." completes the P-0-to-use-site forward arc. P-0 now knows where it is applied. Echo row labels remain the prose form "(P-0 anti-bypass declaration)" — an executor at a use site navigates to P-0 but must scan prose to locate the clause (C-48 absent); content-cell readers have no provenance signal (C-50 absent).

### V-03 — 40/42 — 9.52

40 criteria pass. C-48 and C-49 absent by design. C-50 cleanly isolated: "Per P-0 anti-bypass declaration: " content prefix makes the echo's identity as a protocol echo observable from the content cell alone. An executor scanning content cells without reading labels now has provenance at the point of consumption. The P-0 clause has no ABD heading (C-48 absent) — the content prefix references prose rather than a named element; P-0 has no forward pointer (C-49 absent).

### V-04 — 41/42 — 9.76

41 criteria pass. C-50 absent. Structural address pair (C-48 + C-49) realized as the v18-seeded V-04 form: ABD heading makes the back-reference an element-level label match; forward pointer makes the use sites discoverable from P-0 by a single read. Neither gap in bidirectional navigability at the definition site remains open. Echo row labels "(P-0, ABD)". Content cell carries no provenance prefix — an executor scanning content cells in isolation has no provenance signal (C-50 absent).

### V-05 — 42/42 — 10.0

All 42 criteria pass. V-05 implements the seeded V-05 form (C-48 + C-50) and also carries C-49, achieving the complete triad. Then extends beyond the v18 rubric by introducing `[P-0:ABD]` as a third bracket token in the resolution table — elevating the ABD clause to bracket-token-addressable status alongside `[S-3:CS]` and `[A-1:FC]`. Echo row labels use `[P-0:ABD]` (bracket token notation). Content attribution uses `"Per [P-0:ABD]:"`. The abbreviation key gains `:ABD = Anti-bypass declaration`. The lookup obligation line gains `P-0 table, row 3 = [P-0:ABD]`. All three cross-reference points in the protocol are now navigable by the same structured token lookup protocol.

---

## Excellence Signals — V-05

**Signal 1: Bracket token unification of all three cross-reference points.**
`[S-3:CS]`, `[A-1:FC]`, and `[P-0:ABD]` are all now bracket-token addressable. An executor encountering any of the three can apply an identical protocol: locate in the resolution table, read Step and Row type cells, confirm. The ABD provenance chain becomes as navigable and verifiable as the FLAG chain. Prior to V-05, the ABD clause was reachable via prose navigation only — the executor had to parse the preamble to find the right clause. `[P-0:ABD]` makes it a direct lookup.

**Signal 2: Resolution table as a complete cross-reference registry.**
Adding `[P-0:ABD]` as a third row with `(self)` direction notation turns the table from a two-entry FLAG chain map into a complete protocol registry covering every cross-reference point. The `(self)` direction notation is a clean sentinel for a definition-point token — it has no paired token, it is its own reference target. The table is now structurally complete.

**Signal 3: Content attribution via bracket token notation.**
`"Per [P-0:ABD]:"` is not just provenance — it is a *navigable* provenance reference. An executor reading `"Per [P-0:ABD]:"` in a content cell can apply the same lookup protocol that processes any other bracket token, find row 3 of the P-0 table, confirm the resolution to `Anti-bypass declaration` at P-0, and proceed. Content attribution using prose (`"Per P-0 anti-bypass declaration:"`) identifies the source; bracket token attribution (`"Per [P-0:ABD]:"`) additionally makes it verifiable.

**V-20 seed — C-51 candidate:** Bracket token notation for the P-0 ABD reference: `[P-0:ABD]` as a first-class entry in the resolution table with `(self)` direction, making all three cross-reference points protocol-uniform. Requires: C-48 (ABD heading present), C-50 (content attribution present), C-48 echo labels upgraded from `(P-0, ABD)` to `[P-0:ABD]`.

---

## Variation Ranking

| Rank | Variation | Score | Key contribution |
|------|-----------|-------|-----------------|
| 1 | V-05 | 10.0 | All three axes: ABD heading + forward pointer + content attribution + [P-0:ABD] bracket token extension |
| 2 | V-04 | 9.76 | Structural address pair: ABD heading + forward pointer (seeded V-04 form) |
| 3 | V-01 | 9.52 | C-48 isolated: ABD heading |
| 3 | V-02 | 9.52 | C-49 isolated: forward pointer |
| 3 | V-03 | 9.52 | C-50 isolated: content attribution |

Single-axis isolation (V-01, V-02, V-03) confirms each of C-48, C-49, C-50 as a clean, independently achievable pass condition at 40/42. The combined V-04 form adds one criterion over any single-axis variation. V-05 demonstrates the complete convergence plus a v20 seed pattern that goes beyond the v18 denominator.

---

```json
{"top_score": 10, "all_essential_pass": true, "new_patterns": ["[P-0:ABD] bracket token as third resolution-table entry with (self) direction notation — elevates ABD clause to bracket-token-addressable status, making all three protocol cross-reference points navigable by identical lookup protocol", "Content attribution via bracket token notation Per [P-0:ABD]: rather than prose Per P-0 ABD: — makes provenance reference verifiable not just readable, enabling executor to confirm ABD source by the same Phase 1+2 lookup used for [S-3:CS] and [A-1:FC]"]}
```
