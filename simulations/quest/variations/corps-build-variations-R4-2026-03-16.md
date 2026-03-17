Written to `simulations/quest/golden/corps-build-variate-R4-2026-03-16.md`.

---

## R4 Variate -- corps-build

**5 variations targeting C-17 and C-18.**

### Gap analysis

| New Criterion | R3 Coverage | Gap |
|---|---|---|
| C-17 IA lens-phrase verification at build-complete | R3 V-05 CROSS-REF C4 -- embedded as one of four checks | Not a named phase; can be abbreviated or skipped under length pressure |
| C-18 Contract verbatim transcription | R3 V-05 Phase 6 "transcribe verbatim" instruction | No seal, no receipt; regeneration with correct counts is indistinguishable from transcription |

### Variation axes

| Var | Axis | Criteria | Mechanism |
|-----|------|----------|-----------|
| V-01 | Lifecycle emphasis | C-17 | Named BUILD-VERIFY phase, single purpose, post-write |
| V-02 | Output format | C-18 | CONTRACT-SEAL + TRANSCRIPTION-RECEIPT |
| V-03 | Phrasing register | C-17, C-18 | Output-forward description with VERBATIM/DRIFT and VERBATIM/REVISED contrasts |
| V-04 | Lifecycle + Output format | C-17, C-18 | CONTRACT-SEAL -> TRANSCRIBE (receipt) -> BUILD-VERIFY pipeline |
| V-05 | All axes | C-09 through C-18 | R3 V-05 + CONTRACT-SEAL (Phase 3d) + BUILD-VERIFY (Phase 7) as new named phases |

**Key structural insight**: C-17 and C-18 are a verification pair. C-18 prevents drift at write time (seal the contract, copy it); C-17 catches drift that slipped through (verify after writing). V-04 and V-05 compose them as a pipeline. V-01 and V-02 isolate each mechanism for single-axis scoring.
