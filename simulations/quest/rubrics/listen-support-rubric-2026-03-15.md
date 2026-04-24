Written to `simulations/quest/rubrics/listen-support-rubric-v1-2026-03-15.md`.

**Rubric summary:**

**Essential (5)** — all must pass:
- **C-01** Ticket inventory present — title + category + volume + severity on every entry
- **C-02** Persona attribution — named stock role per ticket, 2+ distinct personas
- **C-03** Ticket body in persona voice — first-person, role-appropriate language, 2+ sentences
- **C-04** Gap analysis — all three categories (doc/design/operational), each tied to a ticket
- **C-05** Non-trivial distribution — 2+ volume levels, 2+ severity levels, P0 ≤ 25%, high-vol ≤ 50%

**Recommended (3):**
- **C-06** Ticket count in [6, 12]
- **C-07** 3+ distinct personas, no persona > 50% share
- **C-08** Gap entries name a concrete artifact/action (≥75% of entries)

**Aspirational (2):**
- **C-09** Clusters tickets into 2-3 named themes with product-risk framing
- **C-10** Resolution path (triage owner + root cause + resolution type) for all high-vol/P0-P1 tickets

The hardest gate to fake is **C-04** (gap analysis must reference specific tickets and close with a named artifact) — the worked example shows an output can score 73 composite and still fail golden because one essential was missed.
