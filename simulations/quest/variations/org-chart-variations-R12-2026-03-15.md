Written to `simulations/quest/golden/org-chart-variate-R12-2026-03-16.md`.

---

## org-chart Variate — Round 12

**Target:** 24/24 (first 100.0). All 5 variations carry both C-31 and C-32 simultaneously.

### What changed from R11

| R11 result | Why it didn't reach 24/24 |
|---|---|
| V-01/R11 (22/24) | Neither C-31 nor C-32 — had section-order directives but no gate markers; had code-fenced templates |
| V-02/R11 (23/24) | Earned C-31 (gate markers) but failed C-32 (still had code-fenced template blocks showing gate text) |
| V-03/R11 (23/24) | Earned C-32 (no templates, inline backtick format specs) but failed C-31 (no gate markers at all) |

R12 combines both: phase gates expressed as inline backtick emit directives (satisfying C-31 **and** C-32 simultaneously).

### Variation summary

| Variation | Axis | Hypothesis | New elements |
|---|---|---|---|
| **V-01** | Canonical C-31+C-32 synthesis | Minimal combination holds 24/24 | Phase gates (inline backtick) + no code blocks |
| **V-02** | Inertia framing — FLAT-CASE-PRESSURE (1-5 scale) | Pressure rating inside Inertia phase doesn't cross gate boundaries | `FLAT-CASE-PRESSURE: [rating] — [justification]` block after Rebuttal, referenced in VERDICT |
| **V-03** | Role sequence — ROLE-LOAD-ORDER constraint | Engineering/Operations-first classification is C-28 safe if kept away from gate directives | `ROLE-LOAD-ORDER` directive between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION |
| **V-04** | Combined V-02 + V-03 | Two independent-phase additions have no shared directive surface | FLAT-CASE-PRESSURE (Inertia phase) + ROLE-LOAD-ORDER (Roles phase) |
| **V-05** | Combined V-02 + Charter Quorum field | C-17 (four charter fields) is extensible; a fifth field is additive | FLAT-CASE-PRESSURE + `Quorum: [N roles required]` as fifth charter field |

### Key C-31/C-32 mechanics in every variation

**C-31** — Each gate is expressed as:
> `When [phase] is complete, DO emit: === [PHASE GATE: X COMPLETE — Y BEGINS] ===; DO NOT proceed to Y until this gate line is present in the output.`

No explanatory sentence adjacent. Four gate positions: after ROLE-TYPE-CLASSIFICATION, after VERDICT, after ASCII Org Diagram, after Committee Charters.

**C-32** — All format specs are inline backtick strings within directive sentences. Examples:
- `- [role name] — [domain type]` (not a code block)
- `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---` (inline)
- Table columns: `Area | Headcount | Key Roles | Decides | Escalates` (inline, not scaffolded)

**V-05 risk flag:** C-17 requires "all four fields" in charters. V-05 adds a fifth (`Quorum`). If the rubric scorer reads C-17 as exactly-four rather than at-minimum-four, V-05 may fail C-17 — surfacing a rubric precision finding rather than a prompt failing.
