● List directory signals
  └ 7 files found

● Search (glob)
  │ "signals/**/ai-code-review-*"
  └ 18 files found

Now let me check the discover directory structure for any additional signals I might have missed:

● List directory signals\discover
  └ 6 files found

---

# 🗺️ DISCOVER ORCHESTRATE — ai-code-review

## PHASE 1: WHAT HAS ALREADY RUN

| Signal | Artifact Found | Date | Status |
|--------|---------------|------|--------|
| discover-competitors | `signals\discover\competitors\ai-code-review-competitors-2026-03-19.md` | 2026-03-19 | ✅ DONE |
| discover-inertia | `signals\discover\inertia\ai-code-review-inertia-2026-03-19.md` | 2026-03-19 | ✅ DONE |
| discover-feasibility | `signals\discover\feasibility\ai-code-review-feasibility-2026-03-19.md` | 2026-03-19 | ✅ DONE |
| discover-risk | MISSING | -- | ❌ MISSING |
| discover-hypothesis | MISSING | -- | ❌ MISSING |
| discover-websearch | `signals\discover\websearch\ai-code-review-websearch-2026-03-19.md` | 2026-03-19 | ✅ DONE |
| discover-causal | MISSING | -- | ❌ MISSING |
| discover-coherence | MISSING | -- | ❌ MISSING |
| discover-synthesize | MISSING | -- | ❌ MISSING |

**Skills complete: 4 of 9**
**Skills pending: 5 of 9**

> **Bonus coverage detected:** `discover-competitors-alt` and `discover-feasibility-alt` also present — these provide supplementary analysis from alternate framing but do not replace the core 9.

---

## PHASE 2: RECOMMENDED SEQUENCE

The 4 completed signals (competitors, inertia, feasibility, websearch) provide a strong foundation. The remaining 5 skills should run in this order:

---

**1. discover-risk** ← NEXT UP
> **Question answered:** What could go wrong across technical, compliance, adoption, and dependency dimensions?
>
> **Why it matters for ai-code-review:** AI-powered code review sits at the intersection of several high-risk dimensions: **false positive fatigue** (adoption risk), **hallucinated vulnerability reports** (trust/safety risk), **LLM cost scaling** with repo size (financial risk), **IP/code exfiltration** through model APIs (compliance risk), and **CI pipeline latency** injection (technical risk). Feasibility has already surfaced build complexity — risk will confirm or expand those concerns and flag what feasibility missed.
>
> **Prerequisite:** ✅ Met. Competitors + feasibility are done, providing the technical landscape and build complexity that risk should cross-reference.

---

**2. discover-hypothesis**
> **Question answered:** What is the team assuming, and what would prove them wrong?
>
> **Why it matters for ai-code-review:** The core bet is likely: *"AI-generated code review comments will be accurate enough and actionable enough that developers accept them rather than ignoring or disabling the tool."* This is a falsifiable claim — acceptance rate, false-positive rate, and time-to-resolve are all measurable. Without stating this explicitly, the team risks building features that optimize the wrong metric (e.g., coverage over accuracy).
>
> **Prerequisite:** ✅ Met. Competitors + risk context sharpens what assumptions are worth testing.

---

**3. discover-causal**
> **Question answered:** Does the proposed feature actually address the root cause of the problem it claims to solve?
>
> **Why it matters for ai-code-review:** The assumed causal chain is: *"Code review is slow/inconsistent → AI automates first-pass review → Developers get faster, higher-quality feedback → Fewer bugs ship."* But the root cause of slow reviews may not be lack of automation — it may be unclear ownership, poor PR hygiene, or architectural complexity that AI cannot address. Causal analysis validates whether the intervention hits the actual bottleneck.
>
> **Prerequisite:** ✅ Met. Websearch provides external grounding; hypothesis (once run) defines the specific claims to trace.

---

**4. discover-coherence**
> **Question answered:** Do the existing signals agree with each other, or are there contradictions?
>
> **Why it matters for ai-code-review:** With 6+ signals completed by this point, coherence checks for: Does the competitor analysis agree with the feasibility assessment on build effort? Does the inertia analysis align with the risk register on switching costs? Does the websearch evidence support or contradict the hypothesis? Any blocking contradictions must be resolved before synthesis.
>
> **Prerequisite:** ✅ Will be met. Requires 3+ prior signals — we'll have 7 by this point.

---

**5. discover-synthesize** ← FINAL
> **Question answered:** What do all the signals say together? Should the team PROCEED, PAUSE, or PIVOT?
>
> **Why it matters for ai-code-review:** This is the decision gate. AI code review is a crowded, high-stakes space. Synthesis will weigh: competitive differentiation (from competitors), switching friction (from inertia), build viability (from feasibility), threat landscape (from risk), core bet validity (from hypothesis), evidence grounding (from websearch), causal soundness (from causal), and internal consistency (from coherence) — then render a verdict.
>
> **Prerequisite:** Run last. All 8 prior signals feed the synthesis.

---

## DISPLAY SUMMARY

**Next skill to run:** `discover-risk`
**Command:** `/discover-risk ai-code-review`

**Full remaining sequence:**
1. `/discover-risk ai-code-review`
2. `/discover-hypothesis ai-code-review`
3. `/discover-causal ai-code-review`
4. `/discover-coherence ai-code-review`
5. `/discover-synthesize ai-code-review`

**Campaign complete when:** `discover-synthesize` has run and returned a **PROCEED / PAUSE / PIVOT** verdict.

**Estimated effort:** 5 skill runs to complete the discover namespace. At ~2 min each, the full campaign finishes in ~10 minutes.

---

No artifact written. This skill produces display output only.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Glob and view worked cleanly. No issues with Copilot tooling vs Claude Code — all operations are basic file discovery and display. The skill is read-only by design so there are no write-path concerns.


Total usage est:        6 Premium requests
API time spent:         54s
Total session time:     1m 1s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       94.7k in, 2.6k out, 77.8k cached (Est. 6 Premium requests)
