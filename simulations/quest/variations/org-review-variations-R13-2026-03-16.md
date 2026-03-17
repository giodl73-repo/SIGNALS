Written to `simulations/quest/golden/org-review-variate-R13-2026-03-17.md`.

---

## org-review -- Variate R13 Summary

**Design target**: R12 achieved 225/225 (first perfect score). R13 applies the three excellence patterns extracted from R12 to protocol elements that are currently instruction-enforced but not count/key-bound.

**Gap analysis from R12 V-04/V-05:**

| R12 pattern | R13 target | New mechanism |
|-------------|-----------|--------------|
| Named-variable binding after sentinel → propagation chain | C-31 lens exhaustion: §5.7 row count is instructed but not counted | `lens_entry_count_[role] = N` bound at ROLE MANIFEST; §5.7 completeness check verifies by name |
| Typed assertion + verbatim-match → structural data validity | C-33 surface_anchor: requires text-search against §1 | `[S-NN]` key labels on §1 surfaces; surface_anchor cites key; lookup is index-based |
| Count assertion → enumeration forcing | C-27 CH-ID saturation: saturation verified by table scan, no bound count | `ch_id_count = M` bound after BRACKET OPENING; §3.8 and BRACKET CLOSING verify by name |

**Axes:**

| Variant | Axis | New mechanism | Predicted |
|---------|------|--------------|-----------|
| V-01 | Role sequence (single) | §15a LENS ENTRY COUNT BINDING | 225/225 |
| V-02 | Output format (single) | §1 [S-NN] SURFACE KEY LABELS + §17a KEY-CITATION | 225/225 |
| V-03 | Lifecycle emphasis (single) | §8a CH-ID COUNT BINDING | 225/225 |
| V-04 | Two-axis (V-01 + V-02) | lens count + surface key | 225/225 |
| V-05 | Three-axis (V-01 + V-02 + V-03) | all four binding points unified | 225/225 |

**V-05 distinguishing property**: Named-variable binding discipline applied to all four populated-list verification points simultaneously — `dimension_count`, `lens_entry_count_[role]`, `ch_id_count`, and `[S-NN]` keys. Independent fault isolation: a failure at any one binding point does not propagate to others.

**Potential v12 criteria:**
- **C-36**: Lens Entry Count Binding Pre-committed (`lens_entry_count_[role]` bound at ROLE MANIFEST; §5.7 completeness verifiable from count alone)
- **C-37**: §1 Surface Key Labels with §17a Key-Citation (bidirectional index: §1 assigns [S-NN], §17a cites by key)
- **C-38**: CH-ID Count Binding Pre-committed (`ch_id_count` bound after BRACKET OPENING; §3.8 and BRACKET CLOSING both verify against bound value)
