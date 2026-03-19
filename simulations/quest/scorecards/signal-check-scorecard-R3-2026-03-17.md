Scorecard written to `signal-check-scorecard-R3-2026-03-17.md`.

---

## Signal-Check R3 Results

### Scores

| Variation | Aspirational | Composite | Grade |
|-----------|-------------|-----------|-------|
| V-01 (C-39 only) | 31/34 | 99.1 | A+ |
| V-02 (C-40 only) | 31/34 | 99.1 | A+ |
| V-03 (C-41 only) | 31/34 | 99.1 | A+ |
| V-04 (C-42 only) | 31/34 | 99.1 | A+ |
| **V-05 (all four)** | **34/34** | **100.0** | **A+** |

Essential: 5/5 all. Recommended: 3/3 all. The only differentiators are C-39/C-40/C-41/C-42 — each contributes exactly 0.29 points (1/34 of the aspirational weight).

### What the scoring reveals

**V-01 through V-04 tied at 99.1**: The four new criteria are independently contributive and non-overlapping. Each single-axis variation isolates one and only one structural gap. No criterion's presence or absence changes another's result.

**V-05 is the first 100.0** in the signal-check series. All four changes are local annotations or Consumed-by column extensions — zero structural overhead relative to R12 V-04.

### New patterns identified

1. **Two-sided enforcement contract**: C-39 (producer obligation) + C-26 (consumer prohibition) close the last asymmetry — every handoff now has a locally visible constraint on both sides.
2. **Self-documenting terminal verdict**: The one-phrase reason makes the verdict a complete artifact for external consumers — decision + driver without internal record access.
3. **System-identity as boundary marker**: A single external-identity entry in the ARCHITECTURE table makes the register boundary structurally visible by table-scan.
4. **Complete fan-out audit**: Listing all consumers closes the ARCHITECTURE block's last incomplete audit point — the table is now a true single-read C-26/C-28 verification contract.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["two-sided enforcement contract: C-39 at producer mirrors C-26 at consumer -- symmetric local visibility for both omission and re-derivation violations", "terminal verdict with one-phrase reason is self-documenting across register boundaries -- external consumers need no analytical record access", "system identity in ARCHITECTURE terminal row makes register boundary structurally distinguishable from internal handoffs at table-scan level", "complete fan-out audit: listing all consumers for multi-consumer outputs closes the last gap in ARCHITECTURE C-26/C-28 verification contract"]}
```
| C-23 | Named binaries consumed by label in STEP 3 and PART 2 | PASS | PASS | PASS | PASS | PASS |
| C-24 | STEP 3 root-pattern label consumed by PART 2 | PASS | PASS | PASS | PASS | PASS |
| C-25 | Upfront ARCHITECTURE block declares all outputs | PASS | PASS | PASS | PASS | PASS |
| C-26 | Consuming steps carry "do not re-derive" prohibition | PASS | PASS | PASS | PASS | PASS |
| C-27 | ARCHITECTURE in three-column table form | PASS | PASS | PASS | PASS | PASS |
| C-28 | C-26 prohibition per-input, not grouped | PASS | PASS | PASS | PASS | PASS |
| C-29 | STEP C drift binary emitted; STEP D consumes by label | PASS | PASS | PASS | PASS | PASS |
| C-30 | Production steps annotate with forward-declaration arrow | PASS | PASS | PASS | PASS | PASS |
| C-31 | ARCHITECTURE opens with per-input meta-rule | PASS | PASS | PASS | PASS | PASS |
| C-32 | STEP D named confirmed-readiness consumed by STEP E | PASS | PASS | PASS | PASS | PASS |
| C-33 | STEP A named inertia-case verdict consumed by STEP E | PASS | PASS | PASS | PASS | PASS |
| C-34 | STEP E opens with two per-input prohibitions | PASS | PASS | PASS | PASS | PASS |
| C-35 | ARCHITECTURE extends to PART 2 internal outputs | PASS | PASS | PASS | PASS | PASS |
| C-36 | Per-input prohibitions independently self-standing at STEP E | PASS | PASS | PASS | PASS | PASS |
| C-37 | ARCHITECTURE Consumed-by entries at step-level granularity | PASS | PASS | PASS | PASS | PASS |
| C-38 | STEP E emits named terminal verdict | PASS | PASS | PASS | PASS | PASS |
| **C-39** | STEP E production site carries `Required output -- emit exactly:` | **PASS** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| **C-40** | Terminal verdict includes one-phrase reason | **FAIL** | **PASS** | **FAIL** | **FAIL** | **PASS** |
| **C-41** | ARCHITECTURE terminal row names external consumer by system identity | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| **C-42** | Multi-consumer ARCHITECTURE rows list all consuming steps | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** |

---

## Scoring Summary

| Variation | Essential | Recommended | Aspirational | Composite | Grade |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-01 (C-39 only) | 5/5 | 3/3 | 31/34 | 99.1 | A+ |
| V-02 (C-40 only) | 5/5 | 3/3 | 31/34 | 99.1 | A+ |
| V-03 (C-41 only) | 5/5 | 3/3 | 31/34 | 99.1 | A+ |
| V-04 (C-42 only) | 5/5 | 3/3 | 31/34 | 99.1 | A+ |
| V-05 (all four)  | 5/5 | 3/3 | 34/34 | **100.0** | **A+** |

**Formula**: `(essential/5 x 60) + (recommended/3 x 30) + (aspirational/34 x 10)`

V-01 through V-04: `(5/5 x 60) + (3/3 x 30) + (31/34 x 10)` = 60.0 + 30.0 + 9.12 = **99.1**
V-05: `(5/5 x 60) + (3/3 x 30) + (34/34 x 10)` = 60.0 + 30.0 + 10.0 = **100.0**

---

## Criterion-Level Evidence Notes

### C-39 — STEP E production-site annotation

**V-01 PASS evidence**: Locked structural feature 12 annotates STEP E closure with:
```
Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
```
The annotation is present before the verdict line; omission creates a locally visible missing line without ARCHITECTURE cross-reference.

**V-02/V-03/V-04 FAIL evidence**: STEP E closes with bare `Terminal readiness: [...]` line. No `Required output -- emit exactly:` annotation. Omission of the verdict is detectable only by checking the ARCHITECTURE table, not locally.

### C-40 — One-phrase reason in terminal verdict

**V-02 PASS evidence**: Locked structural feature 12 emits `Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]`. Reason is embedded in the verdict; external consumer (topic namespace) receives decision + driver in one line without re-reading the analytical record.

**V-01/V-03/V-04 FAIL evidence**: Terminal verdict = `Terminal readiness: [PROCEED / LOOP / INVESTIGATE]` only. Reason omitted by design. External consumer must trace back through PART 1 or PART 2 to determine the driving dimension.

### C-41 — System identity in ARCHITECTURE terminal row

**V-03 PASS evidence**: ARCHITECTURE terminal row Consumed-by = `topic namespace (by label)`. Register boundary is structurally visible as a table-scan property: the single external-identity entry distinguishes the final row from the eleven internal-handoff rows.

**V-01/V-02/V-04 FAIL evidence**: Consumed-by = `external consumer (by label)`. Generic placeholder makes the terminal row structurally identical to internal rows; the register boundary crossing is not distinguishable from the ARCHITECTURE table alone.

### C-42 — All consumers listed for fan-out outputs

**V-04 PASS evidence**: All five multi-consumer ARCHITECTURE rows list complete Consumed-by sets:
- `[MECHANISM VERDICT]`: `SEQUENCE (verbatim); PART 2 STEP A (verbatim)`
- `Pre-specification gap`: `STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)`
- `Mechanism-relevant contradiction`: `STEP 3 (by label); PART 2 STEP C COHERENCE (by label)`
- `Mechanism-stale`: `STEP 3 (by label); PART 2 STEP C STALENESS (by label)`
- `Root pattern`: `PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name)`

C-26/C-28 compliance is verifiable from one table scan without traversing consuming steps.

Additionally, STEP 3 carries three forward-declaration arrows for Root pattern (to STEP B, STEP C per-dim, STEP D), making production-site declarations complete for all three consumers.

**V-01/V-02/V-03 FAIL evidence**: Each of those five rows lists primary consumer only. Audit requires traversing PART 2 to confirm secondary consumers carry the required C-26 prohibitions. Root pattern's three-consumer fan-out creates the largest gap (two undeclared consumers). STEP 3 carries only one forward arrow (to STEP B), leaving STEP C and STEP D undeclared at the production site.

---

## Variation Ranking

1. **V-05** — 100.0 — canonical R3 form; all four new criteria at zero structural overhead relative to R12
2. **V-01** — 99.1 — C-39: two-sided enforcement contract closed at production site
2. **V-02** — 99.1 — C-40: terminal verdict self-documenting for external consumers
2. **V-03** — 99.1 — C-41: register boundary structurally explicit in ARCHITECTURE table
2. **V-04** — 99.1 — C-42: full fan-out audit in ARCHITECTURE table

V-01 through V-04 are tied at 99.1. Each contributes exactly 1/34 of aspirational weight (0.29 points) above the common 30/34 baseline inherited from R12 V-04. The single-axis isolations confirm the four criteria are independently contributive and non-overlapping at the structural level.

---

## Excellence Signals from V-05

**EX-01: Two-sided enforcement contract at register boundary**
C-39 (producer obligation) + C-26 (consumer re-derivation prohibition) create symmetric enforcement at every named-binary handoff. This is the first variation in the signal-check series where both sides of every handoff carry a locally visible constraint — enforcement is complete without global-scan dependency.

**EX-02: Self-documenting terminal verdict for external systems**
C-40's one-phrase reason converts the terminal verdict from a routing signal (`LOOP`) into a diagnostic artifact (`LOOP -- mechanism evidence absent for inertia-beating claim`). The pattern generalizes: any named output crossing a register boundary should carry enough context for the receiver to act without access to the internal record.

**EX-03: System-identity as structural boundary marker**
C-41's `topic namespace` entry makes the ARCHITECTURE table self-describing with respect to register scope: eleven rows end at internal steps; one row ends at a system identity. The boundary is readable as a structural property without a separate annotation or legend.

**EX-04: Complete fan-out audit closes last ARCHITECTURE gap**
C-42 closes the gap that existed since C-25 introduced the ARCHITECTURE block: the table was a complete contract for single-consumer outputs but an incomplete one for fan-out outputs. With all consumers listed, the table is a true single-read C-26/C-28 verification point for the full pipeline. Root pattern (3 consumers) demonstrates the maximum gap size closed.

---

## Research Question Answers

**RQ-1** (C-39 vs baseline): CONFIRMED. The `Required output -- emit exactly:` annotation makes terminal-verdict omission locally visible at the production site without ARCHITECTURE cross-reference. The enforcement asymmetry between producer (no constraint) and consumer (C-26 prohibition) that existed through R12 is closed.

**RQ-2** (C-40 vs degraded baseline): CONFIRMED. The one-phrase reason makes the terminal verdict independently interpretable across the register boundary. A consumer receiving only the label must re-read the analytical record; a consumer receiving label + reason has both decision and primary driver as a complete artifact.

**RQ-3** (C-41 vs degraded baseline): CONFIRMED. `topic namespace` in Consumed-by makes the register boundary a structural property of the ARCHITECTURE table, distinguishable by table-scan from the eleven internal-handoff rows. The generic `external consumer` label leaves the boundary invisible at the table level.

**RQ-4** (C-42 vs degraded baseline): CONFIRMED. Listing all consumers for fan-out outputs converts the ARCHITECTURE table from a partial audit point to a complete one. The Root pattern row (3 consumers) demonstrates the largest gap closed -- a single-consumer ARCHITECTURE entry implied no fan-out; the three-consumer entry reveals the actual consumption surface and enables verifying C-26 at each site without traversing PART 2.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["two-sided enforcement contract: C-39 at producer mirrors C-26 at consumer -- symmetric local visibility for both omission and re-derivation violations", "terminal verdict with one-phrase reason is self-documenting across register boundaries -- external consumers need no analytical record access", "system identity in ARCHITECTURE terminal row makes register boundary structurally distinguishable from internal handoffs at table-scan level", "complete fan-out audit: listing all consumers for multi-consumer outputs closes the last gap in ARCHITECTURE C-26/C-28 verification contract"]}
```
