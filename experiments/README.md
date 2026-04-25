# experiments/

Parameter study data for Signal skill calibration.

## S2-04-floor-variation/

Floor variation experiment. Tests how varying the `--confidence` floor parameter affects signal quality and coverage across scout and prove skills.

Source paper: S2-04 in `craftworks-research\signals\papers\`

Key findings: Confidence floor at 0.7 produces the best precision/coverage tradeoff for standard depth runs. Below 0.6, spurious findings increase. Above 0.85, coverage drops sharply.

## S2-06-confidence-floor/

Confidence floor experiment. Tests the interaction between `--confidence strict` flag and skill-specific floor values.

Source paper: S2-06 in `craftworks-research\signals\papers\`

Key findings: Strict mode and explicit floor interact multiplicatively. Strict + high floor is appropriate only for `--depth deep` runs where coverage is less critical than precision.

## Related research

All Signal research papers are in `craftworks-research\signals\`. See the [research module README](../../craftworks-research/signals/MODULE.md) for the full index of 27+ papers.
