# Contributing to PEF Architecture

> **Source**: https://github.com/banbanry/pef-architecture
> **Author**: banbanry (沈鹭)
> **License**: MIT

First off, thank you for considering contributing to the PEF Architecture. This is a one-person architecture experiment, and contributions — especially rigorous challenges — are what will make it robust.

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Architecture Challenges (Most Valuable)](#architecture-challenges-most-valuable)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Code Contributions](#code-contributions)
- [Documentation Contributions](#documentation-contributions)
- [Development Setup](#development-setup)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Code of Conduct](#code-of-conduct)

## Ways to Contribute

There are many ways to contribute to PEF Architecture, not just code:

1. **Architecture challenges** — Challenge a core assumption, axiom, or claim. This is the most valuable contribution.
2. **Bug reports** — Report issues in the demo code, documentation, or CI.
3. **Feature requests** — Suggest new applications, operators, or mechanisms.
4. **Code contributions** — Fix bugs, improve the demo, add new test cases.
5. **Documentation** — Fix typos, clarify concepts, add examples, translate.
6. **Testing** — Run the demo and A/B tests on different platforms, report edge cases.
7. **Outreach** — Write about PEF, share it, discuss it in your community.

## Architecture Challenges (Most Valuable)

The PEF architecture is a one-person experiment. It needs rigorous challenge to become robust. If you believe a core assumption is wrong, incomplete, or circular, please open an issue using the **Architecture Challenge** template.

A good architecture challenge includes:

1. The specific claim you're challenging (quote from docs)
2. Why you believe it's wrong, incomplete, or circular
3. A counterexample, edge case, or logical flaw
4. What would change your mind

All challenges will be addressed honestly. Valid challenges will be incorporated into the architecture with attribution. Invalid challenges will be documented as "considered and rejected" with reasoning.

## Reporting Bugs

Before creating a bug report, please check the [existing issues](https://github.com/banbanry/pef-architecture/issues) to avoid duplicates.

When reporting a bug, use the **Bug Report** template and include:

- Clear description of the bug
- Steps to reproduce
- Expected behavior vs actual behavior
- Environment (OS, Python version, commit hash)
- Error messages or stack traces

## Suggesting Enhancements

Use the **Feature Request** template for enhancement suggestions. Include:

- The problem statement
- Proposed solution
- How it fits into the PEF architecture
- Alternatives considered

## Code Contributions

### Prerequisites

- Python 3.8+
- Git
- No external dependencies for the core demo (stdlib only)

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/banbanry/pef-architecture.git
cd pef-architecture

# Run the demo to verify your setup
python demo_minimal.py
# Expected: SELF-CHECK: 8/8 PASS

# For the code reference repository
git clone https://github.com/banbanry/pef-core-reference.git
cd pef-core-reference
pip install -r requirements.txt
python demo_minimal.py
```

### Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Write docstrings for public functions and classes
- Keep functions focused and testable
- Add comments for non-obvious logic, especially PEF-specific mechanisms

### Testing

Before submitting a PR, make sure:

1. The demo still passes: `python demo_minimal.py` → `SELF-CHECK: 8/8 PASS`
2. For pef-core-reference: the A/B test still produces expected results
3. CI passes (GitHub Actions will run automatically on PR)

## Documentation Contributions

Documentation is just as important as code. You can contribute by:

- Fixing typos and grammatical errors
- Clarifying ambiguous concepts
- Adding examples and use cases
- Improving the README navigation
- Translating documentation to other languages
- Adding diagrams and visualizations

When editing documentation, maintain the source watermark at the top and bottom of each file.

## Development Setup

### Repository Structure

```
pef-architecture/
├── README.md                    # Main entry point
├── demo_minimal.py              # 30-second verifiable demo
├── axioms.md / primitives.md / pi-anchor.md / mod3.md / topology.md
├── 01-core-spec/                # Complete design specification
├── 02-applications/             # π-anchor application extensions
├── 03-operator-library/         # PEF triad operator library
├── 04-engineering-cases/        # Real-world engineering deployments
├── 05-references/               # External reference & analysis
├── docs/                        # Additional documentation
└── .github/                     # CI workflows, issue templates
```

### Running Tests

```bash
# Demo self-check
python demo_minimal.py

# A/B evaluation (in pef-core-reference)
cd evaluation
python run_ab_test.py
```

## Commit Message Guidelines

Use clear, descriptive commit messages. Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature or mechanism
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring without behavior change
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

Examples:
- `feat(pi-anchor): add anchor reuse detection`
- `fix(demo): correct domain mismatch check in scenario 4`
- `docs(readme): add layered reading path section`
- `test(evaluation): add 3 new anomaly test cases`

## Pull Request Process

1. Fork the repository and create your branch from `main`
2. Make your changes, following the code and documentation guidelines
3. Test your changes locally (demo must pass 8/8)
4. Update documentation if you've changed functionality
5. Create a PR with a clear title and description
6. Link any related issues
7. Wait for CI to pass
8. Address any review comments

### PR Description Template

```
## What does this PR do?

## Why is this change needed?

## How was it tested?

- [ ] Demo self-check: 8/8 PASS
- [ ] A/B evaluation (if applicable): expected results
- [ ] CI passes

## Related issues

Closes #

## Additional notes
```

## Code of Conduct

This project follows a simple code of conduct:

1. **Be respectful** — Disagree with ideas, not people. Personal attacks, harassment, or discrimination will not be tolerated.
2. **Be honest** — Present evidence for your claims. Acknowledge when you're wrong.
3. **Be constructive** — Criticism should include suggestions for improvement.
4. **Be inclusive** — Welcome contributors of all backgrounds and skill levels.

Architecture challenges are encouraged and valued, but they must be presented respectfully and with evidence.

## Questions?

If you have questions about contributing, feel free to open an issue or start a discussion.

---

*PEF Architecture © 2026 banbanry. Anchored Determinism Meta-Architecture.
唯锚才有势差产生。Source: https://github.com/banbanry/pef-architecture*
