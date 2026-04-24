**v13 written** — one new criterion, one gap closed.

---

**What changed:**

**C-37** — *Non-terminal container COMPLETE lines carry a forward-reference clause naming the downstream container's input dependencies* (V-03 R13 gap signal):

- **Gap it closes**: C-22 is backward-looking (encodes own phase results). V-03 demonstrated `→ [NEXT] receives:` clauses on DESIGN/CALIBRATE/BUILD COMPLETE lines that name the specific values the downstream container will consume. No v12 criterion scored this forward-looking handoff surface.
- **Prerequisite**: C-22 (can't commit downstream inputs without encoding own results first)
- **Exempt**: CLOSE COMPLETE — no downstream container; C-36 already governs that terminal line
- **Weight**: 7 pts

**Updated point totals**: Aspirational 160 → 167. Total 260 → **267**.

**Completion-line contract now spans four criteria:**

| Criterion | Direction | Applies to |
|-----------|-----------|------------|
| C-22 | Backward — own phase results | All completion lines |
| C-37 | Forward — next container's inputs | DESIGN, CALIBRATE, BUILD |
| C-36 | Arc-spanning — full result chain | CLOSE only |
| C-20 | Exit marker | All gate-protected sections |

**R13 seed (V-04)** scores 260/267 under v13. R14 seed: V-04 + V-03's `→ [NEXT] receives:` fields combined, expected 267.
