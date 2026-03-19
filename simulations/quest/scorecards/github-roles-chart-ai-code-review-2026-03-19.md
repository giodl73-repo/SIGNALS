● Search (glob)
  │ ".craft/roles/**/*.md"
  └ 1 file found

● Read false-positive-analyst.md
  │ .craft\roles\product\false-positive-analyst.md
  └ 96 lines read

Here is the roles-chart output:

---

```
ROLE REGISTRY: sim-test
========================

Domain: product
  - false-positive-analyst: Product and engineering leads who must guarantee
    that the system's false-positive rate stays below the 15% perceived-noise
    threshold identified in the competitive analysis, so that adoption survives
    past the first sprint and the tool is not silenced permanently.

========================
Total: 1 role across 1 domain

Coverage gaps:
  Standard domains: signal, craft, platform, security, data, ops
  Missing: signal, craft, platform, security, data, ops
  (all 6 standard domains uncovered — only "product" is installed,
   which is outside the standard set)
```

| Domain | Role slug | orientation.serves |
|---|---|---|
| product | false-positive-analyst | Product/eng leads ensuring false-positive rate stays below 15% noise threshold so adoption survives past first sprint |

**Total found:** 1 role across 1 domain

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Single role file parsed cleanly. Glob and view worked without issue. No Copilot-specific problems — YAML frontmatter inside a fenced code block is a minor parse nuance but handled fine.


Total usage est:        6 Premium requests
API time spent:         20s
Total session time:     23s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       92.0k in, 540 out, 76.5k cached (Est. 6 Premium requests)
