| Variate | Essential | Recommended | Aspirational passing | Aspirational pts | Composite | % max | Golden? |
|---------|-----------|-------------|----------------------|------------------|-----------|-------|---------|
| V-01 | 60 | 30 | 43/47 | 215.0 | **305.0** | 93.8% | YES |
| V-02 | 60 | 30 | 43/47 | 215.0 | **305.0** | 93.8% | YES |
| V-03 | 60 | 30 | 42/47 | 210.0 | **300.0** | 92.3% | YES |
| V-04 | 60 | 30 | 42/47 | 210.0 | **300.0** | 92.3% | YES |
| V-05 | 60 | 30 | 47/47 | 235.0 | **325.0** | 100% | YES |

_43/47 × 235 = 10105/47 = 215.0. 42/47 × 235 = 9870/47 = 210.0._

---

## Rankings

| Rank | Variate | Score | Delta from top |
|------|---------|-------|----------------|
| 1 | **V-05** (BOUNDED BLOCK PROTOCOL — full chain) | 325/325 | — |
| 2 | **V-01** (SCAN PROTOCOL) | 305/325 | −20 |
| 2 | **V-02** (BOUNDED BLOCK PROTOCOL first) | 305/325 | −20 |
| 4 | **V-03** (INERTIA CONTRAST PROTOCOL) | 300/325 | −25 |
| 4 | **V-04** (EXCLUSION-BOUNDARY PROTOCOL) | 300/325 | −25 |

V-01 and V-02 tie: each achieves one half of the chain (C-50 or C-51) but not both. V-03 and V-04 are new single-axis variants that don't target either C-50 or C-51; the 5-criterion chain deficit gives −25 pts vs V-05.

---

## Excellence Signals from V-05

V-05 uniquely achieves the full C-50→C-54 chain. The five-criterion superiority over V-01/V-02 collapses to a design principle: **mutual reinforcement across architectural positions**.

### Signal 1 — Principle-before-instance architecture (C-51)
The protocol declaration appears as the document's opening structural element. Every subsequent section (catalog, construction steps, correction table, BAD PLAN) is read with the protocol frame already established. V-01 achieves C-50 (table format) but reads as instance-before-principle — the table appears in the BAD PLAN block before the model understands the protocol that governs it. V-02 achieves C-51 but uses prose enumeration, losing the scan-column benefit.

### Signal 2 — Pre-declaration closes the format-verification gap (C-52)
The protocol-first position (C-51) creates a structural slot in which to pre-specify the format that Component 1 will instantiate. Without C-51, the C-50 table format is an implicit observation the model makes upon encountering the BAD PLAN block; with C-51+C-52, the model reads the column schema before any construction step, making format verification a prediction-then-confirmation loop rather than a discovery at encounter.

### Signal 3 — Prescriptive mandate converts observation into requirement (C-53)
"Component 1 MUST be a 4-column pipe-delimited table" closes the gap between C-52 (descriptive: "here is what it looks like") and a format requirement (directive: "deviation is a violation"). This is the same mechanism the rubric applies to echo: pre-positioning is structural suggestion; `# REQUIRED:` annotation converts it to a constraint. C-53 applies that same conversion at the protocol-declaration level.

### Signal 4 — Negative boundary enumeration completes the mandate (C-54)
Naming each forbidden format individually ("prose enumeration, indented list, bulleted entries — each individually disqualified") closes the mandate in both directions. The positive mandate ("must be X") alone leaves structurally ambiguous forms — a dense bulleted approximation of columns might satisfy the positive form while violating the intent. Named exclusions make each category directly checkable, removing ambiguity from the design space boundary.

### Signal 5 — Self-review diagnostic step (V-05 R18 enhancement, exceeds C-54)
After the column mandate, V-05 adds four explicit NOT/IS checks the model runs before completing Component 1:
- NOT a prose enumeration
- NOT an indented list
- NOT a bulleted entry set
- IS a pipe-delimited table with the four columns

This converts the static exclusion list from a declarative rule into an active verification protocol. The model is not merely informed of forbidden forms — it is instructed to run per-item confirmation steps. The exclusion categories become checklist items, not background context.

### Signal 6 — Mandate echo at instantiation point (V-05 R18 enhancement)
The BAD PLAN Component 1 header includes:
```
# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)
```
The exclusion list appears a second time at the exact location where Component 1 is instantiated — applying the co-location principle to the format mandate itself. The protocol declaration is the rule site; the BAD PLAN header is the application site. Repeating the NOT list there means the model encounters the exclusion boundary at both sites independently, without requiring cross-document recall.

---

## New Patterns (potential C-55 / C-56 seeds)

**Pattern from Signal 5 — Active exclusion verification protocol**: The C-53/C-54 prescriptive mandate includes an explicit self-review step enumerating the forbidden formats as individually checkable NOT-IS items, converting each named exclusion from a static rule into a per-item confirmation action the model executes before finalizing Component 1.

**Pattern from Signal 6 — Co-located mandate echo**: The protocol mandate and its C-54 exclusion list are echoed inline at the Component 1 header position, applying the field-level co-location principle (C-26/C-37/C-39 family) to the format mandate itself — the requirement is present at both its declaration site (protocol section) and its application site (BAD PLAN header).

---

```json
{"top_score": 325, "all_essential_pass": true, "new_patterns": ["Active exclusion verification protocol -- the C-53/C-54 prescriptive mandate includes an explicit self-review step enumerating forbidden formats as individually checkable NOT-IS items the model runs before completing Component 1, converting each named exclusion from a static rule into a per-item confirmation action rather than background context", "Co-located mandate echo -- the protocol mandate and C-54 exclusion list are repeated inline at the BAD PLAN Component 1 header, applying the co-location principle to the format mandate itself so the exclusion boundary appears at both the protocol declaration site and the instantiation site independently"]}
```
