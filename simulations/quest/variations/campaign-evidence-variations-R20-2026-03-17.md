Written to `simulations/quest/golden/campaign-evidence-variate-R20-2026-03-17.md`.

---

## Variates: campaign-evidence (Round 20)

**Three new criteria targeted (C-48, C-49, C-50). Three single-axis variations, then two combined.**

---

### V-01 -- Axis A: Typed-ID-only binary cells (C-48 only)
**Stage order:** Web-first (default) -- isolates C-48 from C-43 confounding.

**Key signal:** Binary cell annotations shift to typed-ID-only format: `[ Yes / No ] — [IB-ATTR]`.
No English antipattern name appears in the cell body. The annotation is mechanically parseable --
any token that is not `[IB-XXX]` format is a structural violation, not a name-match dispute. A cell
format contract is declared in the Form Templates preamble section. N/A cells retain English names
only (no IB-IDs in the N/A tier -- C-50 FAIL). Audit table retains English antipattern names (C-49
FAIL).

**Hypothesis:** C-48 requires the typed identifier to be the sole annotation, making the cell-to-
fixture link mechanically verifiable. The distinction from R19 baseline (English+IB-ID suffix like
`no attribution collapse [IB-ATTR]`) is that C-48 removes the English name entirely -- the IB-ID
is not a supplement to the name but the only reference. Any annotation string not parseable as
`[IB-XXX]` is a violation regardless of English-name correctness. C-48 is independently satisfiable
without N/A IB-IDs (C-50) or FK-typed audit table (C-49).

---

### V-02 -- Axis B: FK-typed audit table (C-49 only)
**Stage order:** Web-first. Binary cells use English+IB-ID suffix (C-44/C-45 baseline; C-48 absent
because cells are not ID-only). N/A cells carry English names only (C-50 absent).

**Key signal:** The consolidated invocation audit table's antipattern column is renamed to
`Antipattern (IB-ID FK)` and populated exclusively with IB-ID values (`IB-ATTR`, `IB-CAL`, etc.).
No English antipattern names appear in this column. The audit table becomes a reference table
joinable against the IB fixture by identifier -- any cell value not matching an IB-ID row is a
structural violation detectable by lookup, not name-string comparison.

**Hypothesis:** C-49 is a property of the final output section (the audit table), independent of
how binary cells are formatted. FK-typing the audit table's antipattern column creates a second
machine-verifiable link between the invocation apparatus and the IB fixture, complementary to but
separate from the binary-cell ID-only commitment of C-48. C-49 is satisfiable without binary cells
being ID-only (C-48 absent) and without N/A IB-IDs (C-50 absent).

---

### V-03 -- Axis C: Three-tier homogeneity declaration (C-50 only)
**Stage order:** Web-first. Binary cells use English+IB-ID suffix (C-48 absent: names present
alongside IDs, not ID-only). Audit table uses English antipattern names (C-49 absent).

**Key signal:** A HOMOGENEITY INVARIANT is declared in the governance preamble:
> "PRE binary cells, POST binary cells, and N/A cells all cite IB-IDs uniformly."

N/A cells gain IB-IDs alongside English names: `CALIBRATION -- N/A [IB-CAL] (evidence stage; ...)`.
All three tiers now carry IB-IDs. Stage timing directives include a reminder: "C-50 check: N/A cells
carry IB-IDs." The HOMOGENEITY INVARIANT names the property as an architectural commitment, making
any tier that lacks IB-IDs a violation of a stated rule rather than a structural convention.

**Hypothesis:** C-50 requires an explicit declaration of the three-tier uniformity as a named
invariant -- not just structural coincidence. The declaration makes the property referenceable and
enforceable: a tier that lacks IB-IDs violates the HOMOGENEITY INVARIANT by name. C-50 is
satisfiable without making binary cells ID-only (C-48 absent: cells still carry English names) and
without FK-typing the audit table (C-49 absent).

---

### V-04 -- Combined A+B: C-48 + C-49
**Stage order:** Intel-first (carries C-43 -- SEQUENCING-ORDER invocations name the live ordering
decision: "Intel-first ordered as governed decision").

**Key signal:** Binary cells use typed-ID-only format (C-48). Audit table `Antipattern (IB-ID FK)`
column uses IB-IDs only (C-49). The two artifacts -- form cells and audit table -- are jointly
machine-verifiable against the same IB fixture. N/A cells carry English names only (C-50 absent:
third tier lacks IB-IDs; no HOMOGENEITY INVARIANT declared).

**Cross-reinforcement:** C-48 makes individual invocation cells machine-checkable by ID syntax. C-49
makes the audit table a FK reference against the same fixture. Together they create a two-artifact
verification path: the executor fills cells with `[IB-ATTR]` and the audit table records `IB-ATTR`
-- both derivable from the same fixture row. C-50 fails because the N/A tier breaks homogeneity.

---

### V-05 -- Combined A+B+C: Full integration (C-48 + C-49 + C-50)
**Stage order:** Intel-first (C-43 in effect).

**Key signal:** Complete structural homogeneity across all cell types and all output artifacts.
Binary cells: `[IB-XXX]` typed-ID-only (C-48). Audit table: FK-typed IB-IDs only (C-49). N/A cells:
carry `[IB-XXX]` identifiers (C-50 structural). HOMOGENEITY INVARIANT declared in preamble with
explicit cell format contracts for both binary and N/A tiers (C-50 declared). Intel-first ordering
with `[IB-SEQ-O]` governing the decision (C-43).

**Closing property:** The invocation apparatus becomes a self-auditing reference system. Any cell
annotation lacking an `[IB-XXX]` token is a C-48 or C-50 violation detectable by identifier-syntax
scan without English-name interpretation. The audit table's FK column makes the final output section
independently machine-verifiable against the IB fixture. The HOMOGENEITY INVARIANT names the
uniformity property so that any reader can cite it by name and any tier violation is a named-rule
failure.

---

**Isolation matrix:**

| | C-43 Intel-first | C-48 binary ID-only | C-49 audit FK-typed | C-50 three-tier + declaration |
|---|---|---|---|---|
| V-01 | -- | **NEW** | -- | -- |
| V-02 | -- | -- | **NEW** | -- |
| V-03 | -- | -- | -- | **NEW** |
| V-04 | yes | **NEW** | **NEW** | -- |
| V-05 | yes | **NEW** | **NEW** | **NEW** |
