# corps-committee · Quest Scorecard · Round 11

## Scoring Approach

No trace artifact. Scoring from skill description and spec.

**Weights:** Essential (C-01–C-05) = 60% | Recommended (C-06–C-08) = 30% | Aspirational (C-09–C-36, 28 criteria) = 10%

**R10 baseline assumption:** All variations inherit R10 full (C-01 through C-33 PASS). Differentiation on C-34, C-35, C-36 per the design notes discriminator matrix.

---

## R10 Baseline Notes (C-01–C-33, all variations)

All five variations: **PASS** on C-01 through C-33.

Critical baseline callouts:

- **C-08 (AMEND honored):** All variations reflect amendments in output regardless of mechanism completeness. PASS all.
- **C-30 (AMEND routing through block dependency graph):** All declare block-level re-execution scope for each amendment type. PASS all.
- **C-31 (per-block COMMIT seal):** All emit COMMIT annotations closing each block before downstream citation. C-35 (new) requires the seal to enumerate tokens; C-31 requires only the seal to exist. PASS all.
- **C-32 (TOKEN TRACE CONFIRMATION in Phase 2):** All include a named, structured CONFIRMATION element. C-36 (new) requires three-way status; C-32 requires only that the element exist. PASS all.
- **C-33 (AMEND-AFFECTED SITES):** All emit staleness notation before re-execution. PASS all.

---

## Key Discriminator Matrix (C-34 / C-35 / C-36)

| Criterion | What it requires | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------------|------|------|------|------|------|
| **C-34** Re-COMMIT after AMEND | Re-executed blocks emit versioned RECOMMIT MANIFEST before any phase resumes | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| **C-35** COMMIT seal token manifest | Each COMMIT seal enumerates sealed tokens explicitly; downstream can reconcile against closed set | FAIL | **PASS** | FAIL | **PASS** | **PASS** |
| **C-36** Three-way CONFIRMATION status | CONSUMED / NOT-APPLICABLE / DROPPED vocabulary with manifest count reconciliation | FAIL | FAIL | **PASS** *(weak)* | FAIL | **PASS** |

**C-36 V-03 note:** Three-way vocabulary present — C-36 PASS. However, without C-35's manifest, the "count must equal N" reconciliation invariant cannot be enforced. DROPPED is detectable only when a token is visibly absent from a row, not when it was never assigned one. Structurally valid; audit coverage incomplete.

---

## Per-Variation Scoring

### V-01 — Re-COMMIT cycle after AMEND

| Category | Criteria | Passed | Weighted Score |
|----------|----------|--------|----------------|
| Essential (60%) | C-01–C-05 | 5 / 5 | 60.00 |
| Recommended (30%) | C-06–C-08 | 3 / 3 | 30.00 |
| Aspirational (10%) | C-09–C-33: 25 PASS · C-34: PASS · C-35: FAIL · C-36: FAIL | 26 / 28 | 9.29 |
| **Composite** | | | **99.29** |

**Gap:** C-34 PASS adds the re-COMMIT cycle — after AMEND, each invalidated block must emit a seal before phases resume. But the seal enumerates nothing (C-35 FAIL): a reviewer cannot verify whether the re-COMMIT captured all tokens or silently dropped one. C-36 FAIL: CONFIRMATION remains binary CONFIRMED/DROPOUT. Dropout is detectable only by observation, not by count invariant.

---

### V-02 — COMMIT seal token manifest

| Category | Criteria | Passed | Weighted Score |
|----------|----------|--------|----------------|
| Essential (60%) | C-01–C-05 | 5 / 5 | 60.00 |
| Recommended (30%) | C-06–C-08 | 3 / 3 | 30.00 |
| Aspirational (10%) | C-09–C-33: 25 PASS · C-34: FAIL · C-35: PASS · C-36: FAIL | 26 / 28 | 9.29 |
| **Composite** | | | **99.29** |

**Gap:** C-35 PASS means each initial COMMIT seal enumerates its token set — reconciliation is possible at first execution. But C-34 FAIL: amendments do not update manifests. Post-AMEND CONFIRMATION reconciles against a manifest frozen at v1. A token invalidated by amendment and not re-added is invisible to the reconciliation. The manifest is authoritative only until the first amendment.

---

### V-03 — CONSUMED / NOT-APPLICABLE / DROPPED

| Category | Criteria | Passed | Weighted Score |
|----------|----------|--------|----------------|
| Essential (60%) | C-01–C-05 | 5 / 5 | 60.00 |
| Recommended (30%) | C-06–C-08 | 3 / 3 | 30.00 |
| Aspirational (10%) | C-09–C-33: 25 PASS · C-34: FAIL · C-35: FAIL · C-36: PASS | 26 / 28 | 9.29 |
| **Composite** | | | **99.29** |

**Gap:** Three-way vocabulary is present, satisfying C-36's pass condition. But the closed-set reconciliation ("table row count must equal B3 manifest token count") is absent — without C-35 there is no manifest to reconcile against. A token that was never given a row cannot be detected as DROPPED by count check; only tokens with rows can be classified. The vocabulary is correct; the invariant is unenforceable.

---

### V-04 — C-34 + C-35 linked pair

| Category | Criteria | Passed | Weighted Score |
|----------|----------|--------|----------------|
| Essential (60%) | C-01–C-05 | 5 / 5 | 60.00 |
| Recommended (30%) | C-06–C-08 | 3 / 3 | 30.00 |
| Aspirational (10%) | C-09–C-33: 25 PASS · C-34: PASS · C-35: PASS · C-36: FAIL | 27 / 28 | 9.64 |
| **Composite** | | | **99.64** |

**Advance over V-01/V-02/V-03:** The re-COMMIT + manifest pairing closes the amendment availability loop. After AMEND, each invalidated block re-executes and emits a versioned RECOMMIT MANIFEST (B2-RECOMMIT MANIFEST v2, B3-RECOMMIT MANIFEST v2, etc.) with delta annotations. Phase re-entry checks verify current-version manifests, not original v1 seals. The amendment routing table maps each amendment type to a fixed block invalidation set — routing is deterministic, not inferred.

**Remaining gap:** CONFIRMATION still uses binary CONFIRMED/DROPOUT (design notes explicit). The count reconciliation ("must equal manifest token count") is unenforceable because CONFIRMATION cannot distinguish DROPPED (token never assigned a row) from absent (token consumed but mislabeled). Three-way vocabulary not present = C-36 FAIL.

---

### V-05 — Full integration (C-34 + C-35 + C-36 + R10 full)

| Category | Criteria | Passed | Weighted Score |
|----------|----------|--------|----------------|
| Essential (60%) | C-01–C-05 | 5 / 5 | 60.00 |
| Recommended (30%) | C-06–C-08 | 3 / 3 | 30.00 |
| Aspirational (10%) | C-09–C-36: all 28 PASS | 28 / 28 | 10.00 |
| **Composite** | | | **100.00** |

**What completes the loop:** CONFIRMATION reconciles against the B3-COMMIT MANIFEST current version (updated by any B3-RECOMMIT MANIFEST from AMEND). The "must equal N" invariant is enforceable because N is the sealed manifest token count. DROPPED REPAIR RULE forces re-entry into Phase 2 if any token is unaccounted for. NOT-APPLICABLE AUDIT RULE requires each NOT-APPLICABLE entry to cite a specific Phase 0 charter entry — vague justifications are invalidated to DROPPED. PHASE-2-COMMIT terminal seal closes the output at the confirmation line: no content may follow.

---

## Ranking

| Rank | Variation | Composite | New mechanisms |
|------|-----------|-----------|----------------|
| 1 | **V-05** | **100.00** | C-34 + C-35 + C-36 — closed audit loop |
| 2 | **V-04** | **99.64** | C-34 + C-35 — versioned manifests; C-36 open |
| 3 (tie) | **V-01** | **99.29** | C-34 only — re-COMMIT, no manifest |
| 3 (tie) | **V-02** | **99.29** | C-35 only — manifest, no re-COMMIT |
| 3 (tie) | **V-03** | **99.29** | C-36 only — three-way vocab, no closed-set invariant |

V-01/V-02/V-03 are symmetric single-axis isolators. Each passes exactly one of the three new criteria. V-04 advances by pairing the two upstream mechanisms (re-COMMIT + manifest), pulling ahead by one aspirational criterion. V-05 is the only variation where the full audit chain — from amendment through re-COMMIT through manifest count reconciliation through three-way status — closes without a gap.

---

## Excellence Signals (V-05)

**1. Versioned manifest handoff as the amendment record**
Each RECOMMIT MANIFEST includes a delta annotation (tokens added, removed, modified relative to the prior version). The manifest version number *is* the amendment history. A reviewer can reconstruct the full amendment trajectory from manifest versions alone, without reading prose. This pattern — delta-annotated versioned manifests rather than re-sealed but undifferentiated outputs — is the key structural innovation over R10's AMEND routing.

**2. Amendment type as a deterministic block invalidation contract**
The AMEND ROUTING TABLE maps amendment types to exactly which block manifests are invalidated before any phase re-executes. Given amendment type X, the re-execution set is fixed: not inferred from phase impact, not left to the model's discretion. Any amendment type not in the table is an unhandled case — not an implied pass. The routing table is the skill's formal contract for amendment correctness.

**3. Manifest count reconciliation as closed-set dropout detection**
The "table row count must equal B3 COMMIT MANIFEST token count" invariant makes DROPPED structurally detectable rather than observation-dependent. Without a manifest, a token can vanish without producing a missing row — it just never gets a row. With the count check, any unaccounted token produces a count mismatch before delivery. The DROPPED REPAIR RULE makes the confirmation a gate, not an audit: delivery is blocked until the count clears.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["versioned manifest handoff as delta-annotated amendment record", "amendment type routing table as deterministic block invalidation contract", "manifest count reconciliation as closed-set dropout detection invariant"]}
```
