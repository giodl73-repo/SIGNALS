Rubric written to `simulations/quest/rubrics/quest-rubric-mock-review-v1-2026-03-15.md`.

**5 essential criteria** — the hard correctness and behavior invariants of the skill:
- **C-01** Decision completeness — no namespace left undecided
- **C-02** Automatic rule correctness — EVIDENCE-HEAVY / TIER-CRITICAL / COMPLIANCE rules all fire correctly
- **C-03** MOCK-ACCEPTED reason code present — exact codes only, no paraphrase
- **C-04** Status fields written back — the in-place edit actually happens (the defining behavior of this skill)
- **C-05** Next-steps list in priority order — critical namespaces before evidence-heavy

**3 recommended** — depth and traceability:
- **C-06** Rule trigger named per REAL-REQUIRED — "why" not just "what"
- **C-07** PM/Architect/Strategy evaluation shown — three-role trace for non-auto namespaces
- **C-08** Tier flag respected — tier applied consistently and stated explicitly

**2 aspirational** — raise the bar once the basics are solid:
- **C-09** Coverage gap synthesis — next-steps grouped by urgency with cross-namespace risk statement
- **C-10** Namespace-specific MOCK-ACCEPTED rationale — reason codes with actual supporting explanation, not boilerplate
