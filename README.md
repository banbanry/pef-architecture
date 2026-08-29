# PEF Architecture

> **A first-principles assembly of deterministic, verifiable system pipelines.**
> PEF does not invent new parts. It takes foundational primitives — subject, variable, result — and assembles them into a pipeline with strict definitions, axiomatic constraints, and verifiable mechanisms. The value is in the assembly: what each part is forced to be, how they are forced to interact, and what becomes possible that was not possible before.

---

## What is PEF

PEF is not a framework, not a library, not a language. PEF is an **axiomatic assembly system** for software and hardware pipelines.

Traditional engineering starts from *how to implement*. PEF starts from *what each part must be, and what constraints must hold between them*. When definitions are strict and constraints are axiomatic, the pipeline becomes **deterministic and verifiable** — not because it is simple, but because ambiguity has been eliminated by construction.

---

## A Note on Originality

The tripartition **subject – variable – result** is **not a PEF invention**. It is a foundational cognitive structure — as old as the Input-Process-Output model in computer science and the agent-action-result framework in philosophy. Every programming language has some version of it.

**What PEF contributes is not the discovery of these three categories. What PEF contributes is:**

1. **Strict, language-independent definitions** — grounded in physics (potential difference) and epistemology (observer effect), not borrowed from any particular language
2. **Axiomatic constraints** between the parts — unforgeability (A1), variable partition (A3), temporal causality (A4)
3. **Verifiable mechanisms** that enforce those constraints — the π-anchor coordinate system and the MOD3 three-state interrogation

**Analogy:** John Dalton did not invent atoms — the ancient Greeks had atomism. What Dalton did was give atoms *measurable quantitative properties and relationships*, turning a philosophical speculation into a testable scientific foundation. PEF does not invent subject-variable-result. What PEF does is give them *strict definitions, axiomatic constraints, and enforceable mechanisms*, turning a vague commonplace into a deterministic, auditable pipeline.

---

## The Three Foundational Primitives

PEF is built on three foundational primitives. The value is not in the primitives themselves — it is in **how PEF defines them and what constraints PEF imposes on them**.

### P · Primary Entity (Subject)

**The acting subject of a computation task.**

PEF requires P to be explicitly declared with four fields: `name`, `type` (LOGICAL / PHYSICAL / HUMAN), `boundary` (scope of responsibility), and `unit` (unit of measurement).

**Why this definition:**
In traditional code, "who executed this" is often ambiguous — anonymous callbacks, global functions, concurrent threads, inherited methods. Without an explicit subject, variable boundary violations and result illegitimacy cannot be judged. An actor without identity cannot be held accountable.

**Practical benefit:**
Every action has a clear owner. Audit becomes trivial — you do not search logs to infer who did what; the subject is declared before the action begins. This reduces forensic effort from hours of log reconstruction to a direct lookup.

### E · Execution Variable (Variable)

> **In PEF, a variable is not a static container. A variable is a measurable shift in potential difference.**

This is the strict PEF definition of "variable" — deliberately distinct from the loose, overloaded meaning in programming languages, where "variable" means a memory slot in C, a reference in Java, a binding in Python, a channel in Go. None of these are wrong, but none are universal.

**Why this definition:**
- A variable exists **only where there is a gradient** — a difference, a tension, a potential to be measured. No potential difference, no variable. This gives "variable" a physical meaning independent of any language.
- **Even observation is an influence on the variable.** There is no passive measurement. The act of observing introduces a perturbation; observer and observed are coupled. This is not a bug — it is an axiomatic property. Ignoring it is why "read-only" audits fail in practice.
- Variables must be explicitly partitioned into **E_in** (controllable input: the subject may construct and modify) and **E_out** (uncontrollable output: the subject may only observe, never modify).

**Why E_in / E_out partition matters:**
Mixing them causes **hallucinatory optimization**: the subject treats an uncontrollable variable as if it were controllable, producing illusory "improvements" that collapse in the real environment. This is especially dangerous in AI-assisted programming, where the model may "optimize" system clock behavior or network latency — variables it cannot actually control. Traditional code does not enforce this partition, so these false improvements pass review and fail in production.

**Practical benefit:**
- **Cross-language audit foundation:** one definition of "variable" works across C, Python, Go, hardware description languages — no translation loss.
- **Hallucination prevention:** AI cannot silently optimize uncontrollable variables; the partition is enforced before optimization begins.
- **Observer-aware design:** measurement perturbation is accounted for, not ignored — audits are more accurate because they model the real physics of observation.

### F · Final Result (Result)

**The output of a computation task.**

PEF requires F to be traceable to `(P, E, t)` — a result produced by a specific subject, using specific variables, at a specific moment on an unforgeable coordinate.

Formal statement: `F = f(P, E_in, E_out, t)`

**Why this definition:**
Traditional results often lack provenance — you know *what* was output, but not *who* produced it, *with what variables*, or *when*. Without provenance, a result cannot be verified or repeated.

**Practical benefit:**
Every result carries a complete causal chain. Reproducibility is guaranteed by construction — not by hoping the environment is the same, but by recording exactly which subject, variables, and temporal coordinate produced it. This eliminates "it works on my machine" because the machine state is not the reference — the (P, E, t) tuple is.

---

## Axiomatic Constraints

Definitions alone are not enough. PEF imposes three axioms that **cannot be violated** — violation triggers熔断 (circuit breaker) or裁决失败 (adjudication failure).

### A1 · Unforgeability Axiom

**Statement:** Any position requiring an unforgeable coordinate must obtain it from an external precomputed source. Self-computation of the coordinate triggers熔断.

**Why:** Traditional timestamps, auto-increment IDs, and counters can all be predicted, rewound, or forged by a programmable device — especially by an AI. If the coordinate is forgeable, the entire audit chain collapses: identities can be faked, timestamps can be rewritten, causal order can be reversed.

**Mechanism:** PEF uses the digit sequence of the mathematical constant π as its anchor coordinate. π's digits are determined by mathematics — no entity can predict the next digit, no entity can rewind consumed digits. This is the **π-anchor system** (see pi-anchor.md).

**Practical benefit:**
- **Identity and time become objective:** no more "the log says X but the log was tampered with." The coordinate cannot be tampered with.
- **AI-resistant audit:** an AI cannot forge its own identity or backdate its actions — the coordinate is external and unforgeable.
- **Third-party verifiability:** anyone can independently compute π's digits and verify the coordinate was not forged.

### A3 · Variable Partition Axiom

**Statement:** Execution variables must be explicitly partitioned into E_in (controllable) and E_out (uncontrollable). Mixed variables trigger "hallucinatory optimization"熔断.

**Why:** See E above. The partition prevents subjects from optimizing variables they cannot control.

**Practical benefit:**
- **Fewer production failures from false optimizations** — hallucinatory improvements are caught at definition time, not at 3 AM in production.
- **Clearer responsibility boundaries** — everyone knows what the subject is actually allowed to change.

### A4 · Temporal Causality Axiom

**Statement:** Time in PEF is not continuous. It proceeds in **discrete, irreversible steps**. A result cannot precede its cause. No downstream result may be referenced as upstream input.

**Why:** Traditional software treats time as continuous and rewoundable — version control rolls back, databases undo, logs are edited. This makes causal order fragile: a "result" can appear before its "cause" if the timeline is manipulated. For audit and safety, causal order must be objective and irreversible.

**Mechanism:** Each temporal step consumes π-anchor coordinate bits that **cannot be returned**. The coordinate is strictly increasing. There is no rollback, no rewind, no "undo" on the temporal axis.

**Practical benefit:**
- **Tamper-proof causal order:** you cannot rewrite history to make a result appear before its cause. The coordinate is irreversible.
- **Simpler incident analysis:** when something goes wrong, the causal chain is fixed and objective — no disputed timelines.
- **Safety-critical readiness:** in domains where causal order matters (industrial control, blasting, aerospace), an irreversible timeline is not a luxury — it is a prerequisite.

---

## Mechanisms That Make It Work

The axioms are only as strong as the mechanisms that enforce them. PEF has two distinctive mechanisms:

### π-Anchor Coordinate System

An unforgeable coordinate derived from the digit sequence of π. Provides:
- **Unforgeability:** digits cannot be predicted or self-computed (A1)
- **Irreversibility:** consumed bits cannot be returned (A4)
- **Global uniqueness:** all entities share one coordinate — no fragmented anchors
- **Third-party verifiability:** anyone can independently verify

See [pi-anchor.md](pi-anchor.md) for details.

### MOD3 Three-State Interrogation

A verification mechanism that subjects the same system to **three different interrogation intensities** (loose / medium / strict), driven by the π-anchor coordinate.

**Why:** Traditional verification has one intensity — "pass" or "fail." But a system that passes under normal conditions may fail under extreme conditions. MOD3 reveals hidden fragility by showing how the same system behaves under different strictness.

**It is resource scheduling, not randomness:** loose state is normal operation (power-efficient, low-latency); strict state is a reserved escape hatch (high safety margin, early warning). Like a car having economy mode and sport mode — not random, but context-aware resource allocation.

**Practical benefit:**
- **Early warning:** fragility is exposed before an accident, not after.
- **Efficiency-safety balance:** the pipeline runs efficiently most of the time, but automatically increases scrutiny at high-risk moments.
- **Honest verification:** you see not just "does it pass" but "how much can it take before it fails."

See [mod3.md](mod3.md) for details.

---

## Why This Assembly Works — Practical Advantages

| Problem in traditional engineering | PEF solution | Resulting advantage |
|-------------------------------------|-------------|---------------------|
| "Who did this?" requires hours of log reconstruction | P is explicitly declared before action | **Audit lightweighting** — direct lookup, not forensic reconstruction |
| "Variable" means different things in different languages | E is defined as potential-difference shift, language-independent | **Cross-language unified audit** — one definition works everywhere |
| AI optimizes uncontrollable variables (hallucination) | E_in / E_out partition enforced by A3 | **False improvements caught at definition time** — fewer 3 AM production failures |
| Results lack provenance ("it works on my machine") | F = f(P, E, t) with unforgeable t | **Reproducibility by construction** — the (P,E,t) tuple is the reference, not the machine |
| Timestamps and IDs can be forged or rewound | π-anchor unforgeable coordinate (A1) | **Tamper-proof identity and time** — AI cannot backdate or fake |
| Logs can be edited, causal order disputed | Discrete irreversible temporal steps (A4) | **Fixed objective causal chain** — no disputed timelines |
| "Passes tests" but fails in extreme conditions | MOD3 three-state interrogation | **Early fragility warning** — see how much it can take before failure |
| Software and hardware need separate safety models | Hardware four-domain (P·E·F·M) and software three-primitive (P·E·F) are mathematically isomorphic | **One axiom system, two domains** — unified safety reasoning across software and hardware |

---

## Repository Structure

```
pef-architecture/
├── README.md          # This file: first principles, definitions, axioms, practical advantages
├── axioms.md          # Full axiom system (A1, A3, A4)
├── primitives.md      # Detailed P·E·F definitions (Chinese)
├── pi-anchor.md       # The unforgeable coordinate system
├── mod3.md            # Three-state interrogation architecture
└── topology.md        # Five-layer pipeline topology (P→E→F→M→C)
```

> Detailed mechanism documents are in Chinese. English translations are in progress. The conceptual core — definitions, axioms, and practical advantages — is in this README.

## Public Boundary

This repository is PEF's **public theory layer**. It contains architecture definitions, axioms, conceptual mechanism explanations, and the first-principles foundation.

It does **not** contain: implementation code, circuit schematics, parameter thresholds, protocol field details, operator internals, or complete verification derivations. These are restricted technical materials, released only to contracted collaborators.

## Reading Path

1. **This README** — what PEF is, why each definition, what practical advantages
2. **axioms.md** — the complete axiom system
3. **pi-anchor.md** — the unforgeable coordinate that enforces A1 and A4
4. **mod3.md** — how different interrogation intensities reveal hidden fragility
5. **topology.md** — how the primitives assemble into a five-layer pipeline

---

*PEF Architecture · Public Theory Layer · Not inventing parts — assembling them into a deterministic, verifiable pipeline. Axioms first. Implementation last. No retro-causality.*
