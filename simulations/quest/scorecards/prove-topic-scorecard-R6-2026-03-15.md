## Round 6 Results

**All five variations: 136/136.** The rubric ceiling has been hit.

### What happened

Round 6 targeted C-20, C-21, and C-22 — the three criteria where Round 5's best variations each failed at least one. Every variation in Round 6 was engineered to carry all three, and every one succeeded. The full 8-criterion null-CE severity stack (C-14 through C-22) is now achievable in a single prompt.

### Ranking by structural robustness (scores equal)

**V-05 wins on robustness**: C-20 comes from the table (V-02 axis), C-22 comes from the role separation (V-01 axis), C-21 comes from the table echo into the Handoff (combined). Each criterion has a distinct structural source — no axis can be dropped without losing exactly one criterion.

### Excellence signals → candidate C-23

**V-05** introduces `incumbent_defense_closed: [true if all null, false if any found]` in the Handoff — a campaign-outcome boolean independent of `co_activation_confirmed`. A downstream `topic-story` skill reads the campaign state directly without inferring from dual-lock fields. This is the clearest candidate for Round 7.

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["Campaign-outcome named as distinct handoff boolean — incumbent_defense_closed: [true if all null] independent of co_activation_confirmed, enabling point-in-chain audit without dual-lock inference", "Role-structural origin of dual attestation — two blocking roles each producing one attestation field makes C-22 drift-resistant by construction rather than by instruction"]}
```
