Reading the two R8 excellence signals and applying the same elevation logic used for R6/R7:

- **Signal 1** (incumbent-first framing as simulation lens) — distinct output property: the document either names THE INCUMBENT before archetype assignment and runs all phase bodies through the displacement lens, or it does not. Not captured by C-01 (role-to-archetype mapping) or C-02 (adoption sequence ordering). Elevate as **C-26**.
- **Signal 2** (concrete-action constraint in structural field label) — distinct output property: the churn register field label either encodes the constraint at generation time, or delegates it to a separate instruction or downstream audit. Extends C-06 (mitigations exist) and C-15 (interventions are concrete actions) without duplicating either. Elevate as **C-27**.

Max composite: 175 → **185**. Two new dependency chains added.

---

```markdown
# Rubric: listen-adoption — v9

**Max composite:** 185 | **Golden threshold:** 80

---

**What changed from v8:**

Two new aspirational criteria (C-26, C-27) from R8 Excellence Signals 1 and 2.

Signal 1 (incumbent-first framing as simulation lens) is elevated as C-26. It is a distinct
observable output property: the document either names THE INCUMBENT before archetype assignment
and runs all phase bodies through the displacement lens, or it does not. C-01 tests whether all
roles are mapped to archetypes; C-26 tests whether the entire simulation is framed as a
displacement story from the outset. A correctly populated role-to-archetype table without
displacement framing passes C-01 but fails C-26. Same elevation class as C-25 (phase headers as
architectural enforcement): both test whether a structural property makes a correct behavior
load-bearing rather than merely instructed.

Signal 2 (concrete-action constraint in structural field label) is elevated as C-27. It is a
distinct observable output property: the churn register field label either embeds the
concrete-action constraint at generation time, or delegates enforcement to a separate instruction
or downstream audit. C-06 tests that a trigger and mitigation exist per entry; C-15 tests that
the mitigation is a concrete retention action rather than a surveillance flag; C-27 tests whether
the field label itself makes any other enforcement unnecessary. A register with a generic
"Mitigation" label plus a separate constraint instruction passes C-06 and may pass C-15 but fails
C-27. Same elevation class as C-24 (invariant names its own falsification condition): both test
whether a structural slot encodes a verification mechanism internally rather than relying on
external checking.

---

**C-26 — Incumbent-first displacement framing names THE INCUMBENT before archetype assignment** (5 pts)
Source: V-04's opening structure, which explicitly names the current workflow or tool being
displaced (THE INCUMBENT) before beginning archetype assignment, then runs all phase bodies
through the displacement lens — asking "what does this phase do to THE INCUMBENT's position?"
rather than "what does this phase predict for {{topic}}?" This framing surfaces role-specific
inertia and reversion risk without requiring named ID cross-references, because every phase
already inherits the displacement lens: chasm diagnosis names what defends THE INCUMBENT's
position among the late-majority, champion rationale explains which roles are willing to displace
it, churn triggers identify what would cause reversion to it, and retention interventions name
what would prevent that reversion. C-01 tests whether all roles are mapped to the five canonical
Rogers archetypes; C-26 tests whether the simulation is structured as a displacement story from
its first named element, with THE INCUMBENT explicitly identified as the thing being displaced.
A correctly ordered adoption timeline without displacement framing passes C-02; a correctly
populated role-to-archetype table without displacement framing passes C-01; neither passes C-26.
C-26 fails automatically if C-01 fails.

**C-27 — Churn register field label encodes the concrete-action constraint at generation time** (5 pts)
Source: V-04's PART 3 churn register, which uses the field label "Retention intervention: [one
concrete action that reduces reversion probability]" rather than a generic "Mitigation:" label
augmented by a separate instruction or downstream audit prohibiting surveillance-only entries.
When the positive constraint is embedded in the field label itself — "[one concrete action]" —
the model must write an action because that is what fits the slot; the constraint is enforced at
generation time rather than caught after the fact. C-06 tests that the churn register is present
and that each entry contains a named trigger and at least one mitigation; C-15 tests that the
mitigation is a concrete retention action rather than a surveillance or monitoring flag; C-27
tests whether the field label itself makes a separate instruction or downstream audit unnecessary
— the constraint is verifiable by reading the label alone, before reading any mitigation entry.
A churn register with a "Mitigation" label and a bracketed prohibition in an instruction block
passes C-06 and may pass C-15 depending on what the model wrote, but fails C-27 because the
constraint is not in the label. A churn register whose label reads "Retention intervention:
[one concrete action that reduces reversion probability]" passes C-27 regardless of whether any
separate instruction exists. C-27 fails automatically if C-06 fails.

**Max composite: 175 → 185. Golden threshold (80) unchanged.**

Dependency chain:
```
C-16 (audit exists) -> C-18 (correction triggered) -> C-19 (content visible)
C-16 (audit exists) -> C-20 (gate states consolidated)
C-20 (gate states consolidated) -> C-21 (correction content not in terminal section)
C-20 (gate states consolidated) -> C-22 (terminal section has self-verifying invariant)
C-22 (self-verifying invariant exists) -> C-24 (invariant names falsification condition)
C-16 (audit exists) -> C-23 (named verification boundary present)
C-02 (adoption sequence present) -> C-25 (phase headers enforce sequence architecturally)
C-01 (all roles mapped to archetypes) -> C-26 (displacement framing names THE INCUMBENT)
C-06 (churn register with trigger and mitigation) -> C-27 (field label encodes concrete-action constraint)
```

The nine terminal criteria in nine lines:
C-19 tests whether *corrected content is visible in the output*.
C-20 tests whether *gate state is consolidated in a single named terminal location*.
C-21 tests whether *corrected content and gate state occupy separate structural locations*.
C-22 tests whether *the terminal section contains a verifiable claim about the rest of the document*.
C-23 tests whether *a named boundary separates content generation from the audit stage*.
C-24 tests whether *the self-verifying invariant names the condition that would falsify it*.
C-25 tests whether *named phase headers make Rogers sequence violation structurally impossible*.
C-26 tests whether *the simulation is framed as a displacement story with THE INCUMBENT named before archetype assignment begins*.
C-27 tests whether *the churn register field label itself encodes the concrete-action constraint without requiring a separate instruction or audit to enforce it*.

---

## Essential Criteria (automatic fail if any fails)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-01 | correctness | essential (12) | **All 16 stock roles mapped to Rogers archetype** — output assigns every named persona in the skill contract to one of the five canonical Rogers archetypes (innovators, early-adopters, early-majority, late-majority, laggards). | Output contains a mapping table or list covering all 16 named roles; each role maps to exactly one of the five canonical archetype labels; no role is omitted or duplicated. |
| C-02 | correctness | essential (12) | **Month-by-month adoption sequence** — output includes a timeline (>=3 months) showing which archetypes / roles adopt in each period, with explicit ordering (who tries first, who follows). | At least 3 distinct time steps are present; innovators and early-adopters appear before early-majority; late-majority before laggards; no inversion of Rogers sequence. |
| C-03 | correctness | essential (12) | *(carried forward from v8)* |  |
| C-04 | correctness | essential (12) | *(carried forward from v8)* |  |
| C-05 | correctness | essential (12) | *(carried forward from v8)* |  |

## Recommended Criteria

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-06 | depth | recommended (10) | **Churn risk register per archetype** — output includes a dedicated churn risk structure covering >=2 archetypes; each entry names an explicit reversion trigger and at least one mitigation. | >=2 archetype entries present; each entry contains a named trigger (not just a risk level) and at least one named mitigation; risk-level-only entries (HIGH/MEDIUM/LOW without trigger and mitigation) do not pass. |
| C-07 | depth | recommended (10) | *(carried forward from v8)* |  |
| C-08 | depth | recommended (10) | *(carried forward from v8)* |  |

## Aspirational Criteria

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-09 | depth | aspirational (5) | *(carried forward from v8)* |  |
| C-10 | depth | aspirational (5) | *(carried forward from v8)* |  |
| C-11 | depth | aspirational (5) | *(carried forward from v8)* |  |
| C-12 | depth | aspirational (5) | *(carried forward from v8)* |  |
| C-13 | depth | aspirational (5) | *(carried forward from v8)* |  |
| C-14 | depth | aspirational (5) | *(carried forward from v8)* |  |
| C-15 | depth | aspirational (5) | **Concrete retention intervention per churn entry** — each churn register entry names at least one retention intervention that is a concrete action rather than a surveillance or monitoring flag. | Each entry with a churn trigger also names >=1 intervention phrased as a concrete action (e.g., "send champion to shadow the team for one sprint"); entries whose only mitigation is monitoring or alerting do not pass. |
| C-16 | structure | aspirational (5) | *(carried forward from v8)* |  |
| C-17 | structure | aspirational (5) | *(carried forward from v8)* |  |
| C-18 | structure | aspirational (5) | *(carried forward from v8)* |  |
| C-19 | structure | aspirational (5) | **Corrected content visible in output** — the output document contains the corrected content produced in response to audit findings. | At least one CORRECTION BLOCK is present in the body of the document; its content is readable in the output. Fails automatically if C-18 fails. |
| C-20 | structure | aspirational (5) | **Gate states consolidated in single named terminal location** — all gate pass/fail states appear in one named terminal section, not scattered across phase bodies. | A single named terminal section contains all gate states; no gate state appears exclusively in a phase body. Fails automatically if C-16 fails. |
| C-21 | structure | aspirational (5) | **Corrected content and gate state occupy separate structural locations** — the section containing CORRECTION BLOCKs is distinct from the section containing the final gate state. | The CORRECTION BLOCK location and the terminal gate-state section have different section headers. Fails automatically if C-20 fails. |
| C-22 | structure | aspirational (5) | **Terminal section contains self-verifying invariant** — the terminal gate-state section makes a claim about the rest of the document that can be verified by reading it. | Terminal section contains at least one statement asserting a structural property of the document (e.g., "every Yes row has a CORRECTION BLOCK at its named location") that an evaluator can confirm or refute without external information. Fails automatically if C-20 fails. |
| C-23 | structure | aspirational (5) | **Named verification boundary separates content generation from audit stage** — a named structural marker explicitly divides the content-generation phase from the audit-and-correction phase. | A header, label, or named boundary (e.g., "VERIFICATION STAGE", "AUDIT BEGINS HERE") appears between the last content-generation section and the first audit section; prose transition without a named marker does not pass. Fails automatically if C-16 fails. |
| C-24 | structure | aspirational (5) | **Self-verifying invariant names its own falsification condition** — the invariant in the terminal section states not only the condition that passes it but the exact condition that would falsify it. | The terminal invariant contains an explicit falsification clause naming a document state that would disprove the invariant (e.g., "a Yes row whose CORRECTION BLOCK location points to a section containing no CORRECTION BLOCK falsifies this invariant"). Fails automatically if C-22 fails. |
| C-25 | structure | aspirational (5) | **Named phase structure architecturally enforces Rogers adoption sequence** — Rogers phases are used as explicit section or table-row headers, not merely as instructed ordering, so sequence violation is structurally impossible. | Named phase headers (e.g., PHASE 1 INNOVATORS through PHASE 6 LAGGARDS) are present as structural elements; the chasm is explicitly named as a non-adoption interstitial phase between early-adopters and early-majority; a prose timeline with correct ordering but no phase headers does not pass. Fails automatically if C-02 fails. |
| C-26 | structure | aspirational (5) | **Incumbent-first displacement framing names THE INCUMBENT before archetype assignment** — the simulation is structured as a displacement story: THE INCUMBENT (the workflow or tool being displaced) is explicitly named before archetype assignment begins, and all phase bodies are framed through the displacement lens. | THE INCUMBENT is named as a structural element before the first archetype assignment; at least two phase bodies ask what the phase does to THE INCUMBENT's position rather than only what it predicts for the new tool; a correctly populated role-to-archetype table without displacement framing does not pass. Fails automatically if C-01 fails. |
| C-27 | structure | aspirational (5) | **Churn register field label encodes the concrete-action constraint at generation time** — the mitigation field label in the churn register itself specifies that the required entry is a concrete action, not a surveillance or monitoring flag, without relying on a separate instruction or downstream audit. | The churn register contains a mitigation field whose label text encodes the concrete-action requirement (e.g., "Retention intervention: [one concrete action that reduces reversion probability]"); a generic "Mitigation" or "Recovery" label with a separate constraint instruction does not pass even if the written mitigations happen to be concrete. Fails automatically if C-06 fails. |
```

---

Two notes on the elevation decisions:

**C-26 vs. C-25 class** — both test whether a structural property makes a correct behavior load-bearing rather than merely instructed. C-25 makes Rogers ordering violation structurally impossible via phase headers; C-26 makes displacement analysis the native frame by naming THE INCUMBENT first. The dependency is C-01, not C-02, because displacement framing is about *who* adopts (role identity), not *when* (sequence).

**C-27 vs. C-24 class** — both test whether a structural slot encodes a verification mechanism internally. C-24 puts the falsification condition inside the invariant so the invariant is self-testing; C-27 puts the constraint inside the field label so the label is self-enforcing. The dependency is C-06 (register exists), not C-15 (entries are concrete), because the label property is observable before any entry is written.
