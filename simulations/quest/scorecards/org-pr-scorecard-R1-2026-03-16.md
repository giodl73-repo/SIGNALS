## org-pr — Quest Score R1

**Rubric**: v1 (2026-03-16) | **Variations available**: V-01 (full text), V-02 (partial — truncated at Step 4 Conflicts row). V-03 through V-05 text was not included in the input; scores for those are estimated from their stated axis descriptions.

---

## Scoring

Weights: PASS = 10 pts, PARTIAL = 5 pts, FAIL = 0 pts. 10 criteria × 10 pts = 100 max.

---

### V-01 — Role Sequence: Risk-First Ordering

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 Coverage | **PASS** 10 | Only INCLUDED roles produce sections; role selection step forces ≥2 active reviewers |
| C-02 Severity | **PASS** 10 | Findings table has Severity column; "Every finding requires a severity" stated explicitly |
| C-03 File-based selection | **PASS** 10 | File Manifest → Role Selection table; each decision requires one-sentence file rationale |
| C-04 Go/no-go | **PASS** 10 | Dedicated GO/NO-GO block: Verdict + Basis + Formula, all labeled fields |
| C-05 Structure | **PASS** 10 | `### [ROLE NAME]` header per section, template enforces clear separation |
| C-06 Consensus | **PASS** 10 | Convergence + Conflicts subsections both present and templated |
| C-07 P1 formula | **PASS** 10 | "Any open P1 = No-Go. This formula is not editable at this step." — explicit and locked |
| C-08 Actionable | **PARTIAL** 5 | `[file:function or pattern]` format shown; no "80%" floor enforcement stated |
| C-09 Author-blind | **PARTIAL** 5 | Role perspective is implicit adversarial signal but no "challenge an embedded assumption" instruction |
| C-10 Non-obvious | **PARTIAL** 5 | Role variety could surface cross-cutting issues; not explicitly requested |

**V-01 Total: 85** — all essential PASS

---

### V-02 — Output Format: Severity Matrix

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 Coverage | **PASS** 10 | "Minimum 2 ACTIVE roles must contribute at least one non-null finding row" |
| C-02 Severity | **PASS** 10 | "Every finding must have a severity. No row may omit the Severity column." |
| C-03 File-based selection | **PASS** 10 | Role Selection Manifest with "Triggered By" column per role |
| C-04 Go/no-go | **PARTIAL** 5 | Text truncated before Step 5; P1 count in Step 4 implies formula exists but not confirmed |
| C-05 Structure | **FAIL** 0 | Unified matrix; role appears as a column, not a labeled section — no separate reviewer blocks |
| C-06 Consensus | **PASS** 10 | Step 4 Convergence table present |
| C-07 P1 formula | **PARTIAL** 5 | P1 count enumerated in Step 4; full formula not visible due to truncation |
| C-08 Actionable | **PASS** 10 | "'General concern' is not a location" — strongest locator enforcement of all visible variations |
| C-09 Author-blind | **FAIL** 0 | No instruction to challenge embedded assumptions |
| C-10 Non-obvious | **FAIL** 0 | No cross-cutting or out-of-diff concern instruction |

**V-02 Total: 60** — C-05 essential FAIL

---

### V-03 — Phrasing Register *(text not in input — estimated)*

Axis changes language register (formal → more prescriptive or conversational). Structure assumed identical to V-01.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01 through C-05 | PASS × 5 | 50 | Structure preserved from V-01 |
| C-06, C-07 | PASS × 2 | 20 | Inherited |
| C-08 | PARTIAL | 5 | Same as V-01 |
| C-09, C-10 | PARTIAL × 2 | 10 | Register change unlikely to add assumption-challenge prompts |

**V-03 Estimated: 85** — all essential PASS (tied with V-01; phrasing rarely changes structure scores)

---

### V-04 — Lifecycle Emphasis + Inertia Framing *(text not in input — estimated)*

Adds lifecycle stage context and "cost of not fixing" (inertia). Structural shell expected to preserve all essential criteria; the inertia frame explicitly asks "what breaks if this stays in" — that directly elicits C-10 non-obvious concerns and may prompt C-09 assumption-challenging.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01 through C-05 | PASS × 5 | 50 | Structural bones preserved |
| C-06, C-07 | PASS × 2 | 20 | Inherited |
| C-08 | PARTIAL | 5 | Locator guidance present but no floor |
| C-09 | PARTIAL | 7 | Inertia framing nudges toward "what the author didn't ask" |
| C-10 | PASS | 10 | Lifecycle view surfaces cross-cutting concerns naturally |

**V-04 Estimated: 87** — all essential PASS

---

### V-05 — Triple Combination: Role Sequence + Output Format + Phrasing *(text not in input — estimated)*

Combines risk-first ordering (V-01) + severity matrix format (V-02) + register change (V-03). The matrix format reappears — C-05 (labeled per-role sections) expected to fail again, same as V-02.

| Criterion | Score | Note |
|-----------|-------|------|
| C-01 through C-04 | PASS × 4 | 40 | Matrix enforces these |
| C-05 | FAIL | 0 | Matrix format → no separate labeled reviewer sections |
| C-06, C-07 | PASS × 2 | 20 | Consensus + formula likely preserved |
| C-08 | PASS | 10 | V-02's strict "no general concern" enforcement likely inherited |
| C-09, C-10 | PARTIAL × 2 | 10 | Register change may help; no structural guarantee |

**V-05 Estimated: 80** — C-05 essential FAIL

---

## Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-04 Lifecycle + Inertia | **87** (est.) | Yes |
| 2 | V-01 Risk-First Ordering | **85** | **Yes (confirmed)** |
| 3 | V-03 Phrasing Register | **85** (est.) | Yes |
| 4 | V-05 Triple Combo | **80** (est.) | No — C-05 |
| 5 | V-02 Severity Matrix | **60** | No — C-05 |

**Reliable winner (text confirmed)**: V-01 at 85, all essential pass.

---

## Excellence Signals from V-01

1. **Risk-first role ordering** — adversarial roles (security, testing) run before rationalizing roles (architect, UX); anchors the review on failure modes before anyone has a chance to explain away the diff.
2. **File Manifest → Role Selection linkage** — every inclusion and exclusion must cite specific files, making the selection auditable and preventing lazy "not applicable" exclusions.
3. **Formula locked with "not editable at this step"** — the P1 = No-Go rule is stated as non-negotiable in the prompt itself, not just in post-hoc instructions; removes edge-case negotiation at output time.

---

## Diagnosis: Why V-02 and V-05 Fail C-05

The matrix format trades role-level narrative for cross-role comparison. That's a valid engineering tradeoff — but C-05 requires labeled sections per reviewer, not a role column. The matrix satisfies the spirit of multi-role coverage (C-01) but collapses the structure that lets a human quickly skim "what did the architect say?" A hybrid — per-role sections that also produce a summary matrix — would pass both.

---

```json
{"top_score": 85, "all_essential_pass": true, "new_patterns": ["risk-first role ordering anchors review on adversarial perspectives before rationalizing roles run", "file manifest to role selection linkage makes every inclusion and exclusion auditable by specific changed file", "P1 formula stated as not editable at this step in the prompt itself removes edge-case negotiation at output time"]}
```
