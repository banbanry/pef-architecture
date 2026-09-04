# PEF Architecture · Knowledge Base Guide & Sync Mapping (GitHub Edition)

> **Source**: https://github.com/banbanry/pef-architecture/docs/knowledge-base-guide.en.md
> **Author**: banbanry (沈鹭)
> **License**: MIT
> **中文版**: [knowledge-base-guide.zh.md](knowledge-base-guide.zh.md)
> **PEF Architecture**: Anchored Determinism Meta-Architecture — Only the anchor produces the potential difference

This page is a **theory guide** to the public PEF architecture repository, mirrored with the internal Feishu knowledge base. It helps readers quickly locate: what this repo is, how files are organized, and what the core theory is.

---

## 1. Repository Positioning (30-Second TL;DR)

**PEF (Positional Evidence Framework / Primary Entity–Execution Variable–Final Result)** is an **anchored deterministic meta-architecture**: it uses the mathematical constant π as an unforgeable coordinate axis, constrains AI behavior with the P (Primary Entity) / E (Execution Variable) / F (Final Result) triad, and achieves **auditable, reproducible, traceable** AI output through audit chains, circuit breakers, and multi-model alignment.

**One sentence**: It stamps an "anti-forgery ID" on AI output — hallucination, tampering, and drift have nowhere to hide.

**Core claim**: *Only the anchor produces the potential difference.* The anchor is an unforgeable, irreversible, globally-unique foundation — π (a transcendental number) in software, thermodynamic law in physics.

---

## 2. Repository Directory Guide (34 files)

| Layer | Content | Core documents |
|---|---|---|
| **Root (entry)** | 5 theory summaries + Demo | [README](../README.md) · [primitives](../primitives.md) · [pi-anchor](../pi-anchor.md) · [mod3](../mod3.md) · [topology](../topology.md) · [axioms](../axioms.md) · [demo_minimal.py](../demo_minimal.py) |
| **01-core-spec (core spec)** | Complete design spec + executable engine | [7.6 Pro design spec](pef-7.6-pro-design-spec.md) · [Three-tier closed-loop engine spec](pef-three-tier-closed-loop-engine.md) · [Engine impl pef_cl_engine.py](pef_cl_engine.py) · [E2E pef_cl_e2e.py](pef_cl_e2e.py) · [Time theory appendix](time-theory-appendix.md) |
| **02-applications** | π-anchor application extensions | [CIC cross-model governance](../02-applications/cic-cross-model-governance.md) · [PIMEM genetic memory](../02-applications/pimem-genetic-memory.md) |
| **03-operator-library** | P/E/F/M four-layer operators | [800-operator library](../03-operator-library/operator-library-v3-800.md) · [CLE probe operators](../03-operator-library/operator-library-3.8-probe.md) |
| **04-engineering-cases** | CLE probe deployment | [Five-stage workflow](../04-engineering-cases/cle-probe/cle-five-stage-workflow.md) · [L1-L3 technical](../04-engineering-cases/cle-probe/cle-l1-l3-technical.md) |
| **05-references** | External validation | [AI programming trio](../05-references/ai-programming-trio.md) · [Multimodal hallucination report](../05-references/multimodal-hallucination-report.md) |
| **Hardware whitepaper** | Physical instantiation | [PEF-Gate Hardware Veto White Paper](../PEF-Gate-Hardware-Veto-White-Paper-Public.pdf) |
| **Promotion article** | Chinese narrative | [I use π as an anchor](../docs/promotion-article-zh.md) |

---

## 3. Core Theory Guide: The Three-Tier Closed-Loop Engine

Latest core deliverable (2026-09-05): **PEF Three-Tier Closed-Loop Engine** (Internal Loop → External Calibration → Multi-Model Compile Alignment)

| Tier | Stage | Function | Code |
|---|---|---|---|
| ① | **Internal Loop (token mining)** | Pure rule engine chunk scoring, S/A/B/C grading, zero external cost | See spec in 01-core-spec |
| ② | **External Calibration (multi-model divergence)** | 12 probes pre-filter + GLM/Claude/GPT independent verdicts | [pef_cl_engine.py](pef_cl_engine.py) |
| ③ | **Multi-Model Compile Alignment** | P/E/F unified Schema → divergence rate ρ → PASS/FAIL veto | Same |

**Measured results** (142-doc ash corpus): low-confidence blocks all FAIL (ρ=0.57~0.87, multi-model divergence veto); high-confidence blocks all PASS (ρ=0.02, consensus); 16-entry audit ledger, hash chain integrity verified.

Run it:

```bash
# Offline demo (3 scenarios + tamper detection)
python 01-core-spec/pef_cl_engine.py

# End-to-end pipeline (reads tier1 intermediate results → low-confidence upgrade → calibration)
python 01-core-spec/pef_cl_e2e.py
```

---

## 4. Theory Sync Mapping (GitHub ↔ Feishu Knowledge Base)

| GitHub document | Feishu KB counterpart |
|---|---|
| Root 5 summaries (primitives/pi-anchor/mod3/topology/axioms) | 02-Theory & Design |
| 01-core-spec (7.6 Pro spec) | 02-Theory & Design · Axioms A1–A8 |
| 01-core-spec (three-tier closed-loop engine) | Ash token-level mining verdict |
| 02-applications (CIC/PIMEM) | 02-Theory & Design · 06-PEF Memory |
| 03-operator-library (800 operators) | 01-Operator Definitions · 800-operator library 4 layers |
| 04-engineering-cases (CLE probes) | 03-Testing & Verification · 08-902 batch |
| 05-references (trio/hallucination report) | 05-Knowledge Cards |
| Hardware whitepaper (PEF-Gate) | 04-Versions & Changes |

---

## 5. Public Statement

This repository contains **public theory**, licensed under MIT. Reviews, challenges, and reproductions are welcome.
- Repository: https://github.com/banbanry/pef-architecture
- Code reference implementation: [pef-core-reference](https://github.com/banbanry/pef-core-reference)
- Author: banbanry (沈鹭)
- Core claim: **Only the anchor produces the potential difference** (Anchored Determinism Meta-Architecture)

*PEF Architecture © 2026 banbanry. Anchored Determinism Meta-Architecture.
Source: https://github.com/banbanry/pef-architecture*
