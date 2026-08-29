# PEF Architecture

> **A first-principles architecture for deterministic, verifiable systems.**
> PEF redefines what a system *is* before asking how it is built. Every concept below has a strict definition — these are not borrowed from any programming language.

---

## What is PEF

PEF is not a framework, not a library, not a language. PEF is an **axiomatic architecture system** — it defines the minimal complete primitives needed to describe any computational system, and the constraints that bind them.

Traditional software engineering starts from *how to implement*. PEF starts from *what a system is*. Axioms first, derivation second, implementation last.

---

## The Three Primitives (P · E · F)

PEF stands for **Primary Entity – Execution Variable – Final Result**. These three primitives form the minimal complete description of the act of computation: *who acts (P), with what variable (E), yielding what result (F)*. None is dispensable.

### P · Primary Entity

**The acting subject of a computation task.**

P must be explicitly declared with four fields:

| Field | Meaning |
|-------|---------|
| `name` | Identity of the entity |
| `type` | Category (LOGICAL / PHYSICAL / HUMAN) |
| `boundary` | Scope of responsibility |
| `unit` | Unit of measurement |

P is the starting point of all audit. Without an explicit subject, variable boundary violations and result illegitimacy cannot be judged. An anonymous actor is not admitted in PEF.

### E · Execution Variable

> **In PEF, a variable is not a static container. A variable is a measurable shift in potential difference.**

This is the strict PEF definition of "variable" — deliberately distinct from the loose, overloaded meaning of "variable" in programming languages. In PEF:

- A variable exists **only where there is a gradient** — a difference, a tension, a potential to be measured. No potential difference, no variable.
- **Even observation is an influence on the variable.** There is no passive measurement. The act of observing introduces a perturbation; the observer and the observed are coupled. This observer effect is not a bug to be eliminated — it is an axiomatic property built into the system.
- Variables must be explicitly partitioned into:
  - **E_in** (controllable input): variables the subject may construct and modify
  - **E_out** (uncontrollable output): environmental quantities the subject may only observe, never modify
- Mixing E_in and E_out causes **hallucinatory optimization**: the subject treats an uncontrollable variable as if it were controllable, producing illusory "improvements" that collapse in the real environment.

**Why PEF defines "variable" this way:** because every programming language defines "variable" differently — as a memory slot, a reference, a binding, a channel. PEF needs its own definition grounded in physics (potential difference) and epistemology (observer effect), so that the architecture does not inherit the ambiguity of any particular language.

### F · Final Result

**The output of a computation task.**

F must be traceable to `(P, E, t)` — a result produced by a specific subject, using specific variables, at a specific moment.

Formal statement:

```
F = f(P, E_in, E_out, t)
```

where `f` is an operator and `t` is a moment on an unforgeable coordinate.

---

## Temporal Causality Axiom (A4)

> **Time in PEF is not continuous. It proceeds in discrete, irreversible steps. A result cannot precede its cause.**

Key properties:

- **Discrete temporal steps**: time advances in jumps, not a smooth flow. Each step consumes anchor coordinate bits that **cannot be returned**.
- **No retro-causality**: no downstream result may be referenced as upstream input. A result cannot be used before it is generated.
- **Monotonicity**: the coordinate is strictly increasing. There is no rollback, no rewind, no "undo" on the temporal axis.
- **Observer coupling across time**: because observation itself influences variables (see E above), the temporal record is not a passive log — it is a causal chain where every measurement perturbs the next state.

This axiom is why PEF needs an **unforgeable coordinate** (the π-anchor system): if the coordinate could be predicted or rewound by a programmable device, retro-causality becomes possible, and the entire audit chain collapses.

---

## Why This Matters

PEF answers a question that traditional engineering avoids: **what is a system, at the most fundamental level?**

- Not "what language is it written in"
- Not "what framework does it use"
- But: *who acts, across what potential-difference shift, yielding what result, on an irreversible causal timeline*

When these primitives are strictly defined and axiomatically constrained, the system becomes **deterministic and verifiable** — not because it is simple, but because every ambiguity has been eliminated by definition.

---

## Repository Structure

```
pef-architecture/
├── README.md          # This file: first principles, primitives, temporal causality
├── axioms.md          # Full axiom system (A1 unforgeability, A3 variable partition, A4 temporal causality)
├── primitives.md      # Detailed P·E·F definitions (Chinese)
├── pi-anchor.md       # The unforgeable coordinate system (π-anchor)
├── mod3.md            # Three-state interrogation architecture
└── topology.md        # Five-layer pipeline topology (P→E→F→M→C)
```

> Detailed mechanism documents are in Chinese. English translations are in progress. The conceptual core — primitives, axioms, causality — is defined in this README.

## Public Boundary

This repository is PEF's **public theory layer**. It contains:
- Architecture definitions and axioms
- Abstract descriptions of primitives
- Conceptual explanations of core mechanisms
- The first-principles foundation

It does **not** contain: implementation code, circuit schematics, parameter thresholds, protocol field details, operator internals, or complete verification derivations. These are restricted technical materials, released only to contracted collaborators.

## Reading Path

1. **This README** — first principles, P·E·F definitions, temporal causality
2. **axioms.md** — the complete axiom system
3. **pi-anchor.md** — the unforgeable coordinate that makes causality enforceable
4. **mod3.md** — how different interrogation intensities reveal hidden fragility
5. **topology.md** — how the primitives assemble into a five-layer pipeline

---

*PEF Architecture · Public Theory Layer · Axioms first. Implementation last. No retro-causality.*
