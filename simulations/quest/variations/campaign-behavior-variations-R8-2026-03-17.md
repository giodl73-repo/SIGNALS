---

# Quest Variations — campaign-behavior (R8)

**Rubric:** v6 (C-01–C-23, aspirational denominator 15) | **Base:** R7 V-01 (90/90)

---

## Axes explored in R8

Three single-axis variations, then two combinations:

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | **DEPTH asymmetry labeling** | Anchor phases (Ph1, Ph2) carry `[ANCHOR: ...]` tags in headers; execution phases (Ph3–5) carry none. Tests R7 Signal 1 in isolation. |
| V-02 | **Q6 sequence integrity gate** | Sixth calibration question verifies anchor guarantee was delivered (zero post-hoc blast radius revisions). Tests R7 Signal 2 in isolation. |
| V-03 | **Propagation chain enumeration** | Field 3 of every finding block is extended to an ordered chain: `[origin] → [component-B] → [terminal]`. New axis — not tested in any prior round. |
| V-04 | **DEPTH asymmetry + Q6** | Both R7 excellence signals combined; no other change from R7 V-01. |
| V-05 | **Full combination** | DEPTH asymmetry + Q6 + propagation chain + max structural reinforcement of all 15 aspirational criteria. |

---

## Key structural decisions in each variation

**V-01** — only change from R7 V-01 is the phase header format:
- `## PHASE 1 — trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]`
- `## PHASE 2 — trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]`
- Ph3–Ph5 headers are plain. The asymmetry is the entire signal.

**V-02** — only change is Q6 in the calibration block:
> *"Were any blast radius values revised post-hoc because a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified? Zero revisions = anchor guarantee delivered. Any revision = log as anchor violation."*

**V-03** — only change is field 3 format in every atomic finding block:
```
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal]
```
Q1 is also updated: *"trace the full propagation chain to terminus — does it reach a shared state surface?"* instead of checking components in isolation. This makes blast radius upgrades mechanically auditable.

**V-04** — V-01 + V-02 combined. Tests for interference between the two R7 signals.

**V-05** — all three axes. Additionally reinforces: VERDICT paragraph names the propagation chain from origin to terminal blast surface. Definitions section adds the `Propagation chain` term formally.

---

## Expected scoring against v6

| Var | C-01–C-05 | C-06–C-08 | C-09–C-23 (15) | Total |
|-----|-----------|-----------|-----------------|-------|
| V-01 | 50/50 | 30/30 | 15/15 → 10/10 | **90/90** |
| V-02 | 50/50 | 30/30 | 15/15 → 10/10 | **90/90** |
| V-03 | 50/50 | 30/30 | 15/15 → 10/10 | **90/90** |
| V-04 | 50/50 | 30/30 | 15/15 → 10/10 | **90/90** |
| V-05 | 50/50 | 30/30 | 15/15 → 10/10 | **90/90** |

All five should hold 90/90 — the new axes do not disturb existing criteria. The scoring interest is in whether any new excellence patterns emerge from the variations that would become C-24 and C-25.

---

## New pattern candidates for potential C-24/C-25

**C-24 candidate — DEPTH asymmetry labeling (from V-01, V-04, V-05):**
Anchor phases carry explicit inline structural markers in their headers; execution phases carry none. The asymmetry makes the two-tier dependency chain (anchor → execution) scannable from the document outline without reading prose.

**C-25 candidate — Propagation chain enumeration (from V-03, V-05):**
Each finding's blast radius field contains an ordered chain `[A] → [B] → [C]` naming every census component in the failure's propagation path. Makes blast radius claims auditable by chain inspection rather than description. Q6 (R7 signal 2) remains a candidate for C-25 if propagation chain is deferred.

---

Saved to: `simulations/quest/golden/campaign-behavior-variate-R8-2026-03-17.md`
