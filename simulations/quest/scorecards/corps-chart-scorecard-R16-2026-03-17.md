Scorecard written to `simulations/quest/scorecards/corps-chart-scorecard-R16-2026-03-17.md`.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": []}
```

---

**Round summary:**

| Variation | Score | Gap |
|-----------|-------|-----|
| V-01 | 107.5 | No FORMAT CONTRACT stack, no C-40 |
| V-02 | 107.5 | No per-granularity enforcement hierarchy, no C-39 |
| V-03 | 110.0 | No FORMAT CONTRACT stack only |
| V-04 | 120.0 | All pass; 3 implementation gaps vs V-05 |
| V-05 | 120.0 | Reference implementation |

The symmetric failure at V-01/V-02 is the key structural finding: C-39 alone and C-40 alone each fail 5 criteria but completely different 5. The enforcement hierarchy (C-28/C-34/C-36/C-37) is worth more cumulative score than the FORMAT CONTRACT stack (C-20/C-23/C-26/C-35), which is why V-03's STOP/audit base outscores both single-axis variations despite lacking FORMAT CONTRACT.

V-05 beats V-04 in implementation depth on C-39 specifically — the DRI/Owner annotation moved inside HALT item 3 means the exclusivity declaration and the requirement it governs are now co-located rather than displaced. That's the pattern that closes the last structural gap in the corps-chart skill.
- C-39 single axis, R15 V-01 base

Fails: C-20, C-23, C-26, C-35, C-40

C-39 PASS: Both HALT blocks carry sole-instruction-site annotations.
  ROLE-NAME LOCK HALT: "[sole instruction site for lock-enumeration accuracy requirements
  (a)(b)(c). No other location introduces competing language.]"
  Rebuttal HALT: "[sole instruction site for Rebuttal four-field form-order requirement.
  No other location names the Rebuttal field sequence.]"
C-38 PASS: Rebuttal HALT header embeds field sequence in HALT header line.
C-36 PASS: DRI/Owner and Key Roles per-cell notes embedded in ROLE-NAME LOCK block with
  "verify before populating next row -- do not complete and verify after."
C-37 PASS: Membership/Decides per-name note embedded in ROLE-NAME LOCK block.
C-33 PASS: Sole-instruction annotations declare HALT blocks as exclusive authority;
  no competing advisory language introduced elsewhere.
C-40 FAIL: Single-axis variation; no REGISTER-CONSISTENCY AUDIT at any phase gate.
C-20/C-23/C-26/C-35 FAIL: Architectural choice -- no FORMAT CONTRACT.

---

## V-02 (107.5) -- C-40 single axis, R15 V-02 base

Fails: C-28, C-34, C-36, C-37, C-39

C-40 PASS: 4-item Gate 1; 4-item Gate 2; 2-item Gate 3; 7-item Gate 4; 2-item Gate 5.
C-38 PASS: HALT before ROLE-NAME LOCK embeds structure summary; Rebuttal HALT embeds field
  sequence in header.
C-33 PASS: "The HALT checklist item 3 above is the sole instruction site for this requirement."
C-28 FAIL: HALT item 3 says "every cell value must be a role" (post-hoc assertion); CHECK SITE 5
  says "every role name must appear" -- neither has "verify before next row -- do not complete
  and verify after" temporal sequencing.
C-34 FAIL: DRI/Owner and Key Roles use emphatic framing ("must be a role") not temporal procedure
  at per-granularity sites; per-granularity hierarchy incomplete.
C-36 FAIL: ROLE-NAME LOCK block has only role list and five-site enumeration; no per-cell notes
  embedded.
C-37 FAIL: No per-name note embedded in ROLE-NAME LOCK block.
C-39 FAIL: No sole-instruction-site annotations in any HALT block.

---

## V-03 (110.0) -- C-39 on C-40 base, R15 V-03

Fails: C-20, C-23, C-26, C-35

C-39 PASS: STOP blocks carry sole-instruction annotations with anti-drift extension:
  "[sole instruction site for lock-enumeration accuracy requirements (a)(b)(c). No other
  location introduces competing language. A subsequent revision that adds qualifying language
  at any other location violates the sole-instruction-site constraint declared in this STOP
  block.]" Rebuttal STOP has parallel annotation.
C-40 PASS (from R15 V-03): Gate 1 item 6 explicitly checks both annotation presence AND
  "no competing instruction added elsewhere."
C-37 PASS: Per-name note in ROLE-NAME LOCK includes anti-drift prohibition -- the only
  variation where the per-name note itself carries this language.
C-33 PASS: Best mechanism -- STOP blocks declare exclusivity at declaration time; anti-drift
  prohibition extends protection to revision time.
C-28/C-34 PASS: Per-cell temporal sequencing at both DRI/Owner and Key Roles sites.
C-20/C-23/C-26/C-35 FAIL: Architectural choice -- no FORMAT CONTRACT.

---

## V-04 (120.0) -- C-39 + C-40 combined, R15 V-04 base

All 40 criteria PASS.

C-39 PASS: Every governed HALT block annotated:
  ROLE-NAME LOCK HALT -- lock-enumeration accuracy requirements (a)(b)(c)
  Rebuttal HALT -- four-field form-order requirement
  Schema 1 HALT -- column-structure and DISQUALIFY-IF requirements
  Schema 2 HALT item 3 -- DRI/Owner role-lock (inline annotation on the requirement)
  Schema 3 HALT -- Charter schema requirements
  Schema 5 HALT -- citation-prefix requirement
C-40 PASS: Gate 1 (6-item); Gate 2 (5-item); Gate 3 (2-item); Gate 4 (9-item -- sole-annotation
  presence for schemas 1/2/3/5, DISQUALIFY-IF, Quorum fraction, per-name directives);
  Gate 5 (2-item).

Three implementation gaps vs V-05 (not captured by binary criteria scoring):
1. DRI/Owner annotation positioned as separate bracket below HALT item 3, not inline within it.
2. Gate 1 audit item 6 checks annotation presence only; omits "no competing language at any
   other site."
3. ROLE-NAME LOCK lacks "These directives travel with the lock and govern those sites from
   declaration time."

---

## V-05 (120.0) -- All 40 criteria, R15 V-05 base

All 40 criteria PASS.

C-39 gap fixed: DRI/Owner annotation moved inside HALT item 3 as inline bracket:
  "3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
   [sole instruction site for DRI/Owner role-lock requirement -- this checklist item 3 is the
   exclusive authority for the DRI/Owner role membership constraint; no other instruction site
   in this prompt introduces competing language for this requirement]"
  Annotation and requirement now occupy the same syntactic position.

C-40 extended: Gate audit items explicitly include "no competing language at any other site."
  Gate 4 items 8+9 check "anti-drift prohibition" in per-name directives.
  Gate 4 item 4 checks "no competing language at any other site" for DRI/Owner.

ROLE-NAME LOCK extended: "These directives travel with the lock and govern those sites from
  declaration time." Lock block is self-governing from emission; activation-gap closed.

---

## Excellence Signals (V-05)

Signal 1 -- Annotation co-location eliminates declaration-instruction gap.
Sole-instruction annotation embedded inline within HALT item 3. Exclusivity declaration and
requirement occupy the same syntactic position. A revision satisfying item 3 cannot add
competing language without creating a visible contradiction at that item. Co-location converts
C-39 from a structural property to a per-item constraint.

Signal 2 -- Gate audit actively verifies sole-instruction invariant.
"No competing language at any other site" as explicit gate audit items. C-39 declares exclusivity
at declaration time; C-40 audits that exclusivity at each gate boundary. C-33 + C-39 + C-40
cover declaration time, revision time, and gate-transition time respectively.

Signal 3 -- Temporal scope of lock directives declared at the lock itself.
"These directives travel with the lock and govern those sites from declaration time." Closes
the activation-gap failure mode where per-cell and per-name notes in ROLE-NAME LOCK are treated
as non-binding until echoed at the call site.

---

## New Patterns for R17

None. The three V-05 refinements are implementation-depth improvements of C-39 and C-40,
not new architectural moves. No new criterion candidates identified from this round.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": []}
```
