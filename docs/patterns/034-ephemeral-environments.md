---
id: 34
name: "Ephemeral Environments"
confidence: 1
scale: 5
context_patterns: [28, 22]
completion_patterns: [35, 36]
ai_dimension: false
tags: [environments, testing, immutability, isolation]
references:
  - "Reinertsen, D. The Principles of Product Development Flow. Celeritas, 2009."
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
  - "Morris, K. Infrastructure as Code, 2nd ed. O'Reilly, 2020."
---

# Ephemeral Environments *

_Your **Deployment Pipeline (28)** needs environments in which to test changes, and **Continuous Integration (22)** demands that every commit be validated. But where do those tests run? If the answer is a shared, long-lived staging environment, you have created a bottleneck that undermines the very practices you are trying to enable._

---

**Shared, long-lived test environments create contention (teams queue for access), configuration drift (the environment accumulates manual changes that diverge from production), and "works on my machine" failures (what passes in staging may fail in production because staging has silently drifted). Yet every additional persistent environment adds to the scope that must be comprehended, maintained, and paid for.**

---

The root cause is that long-lived environments are stateful in all the wrong ways. They accumulate changes — a debug flag left on, a test database with stale data, a dependency pinned to an old version by a previous team's experiment. Each of these accumulated changes makes the environment less representative of production and more difficult to reason about. The environment becomes its own complex system, requiring its own maintenance and tribal knowledge.

Ephemeral environments solve this by inversion: instead of maintaining environments and deploying changes to them, you create environments for changes and destroy them afterwards. Each pull request, each feature branch, each test run gets its own isolated environment, provisioned from scratch by **Infrastructure as Code (35)** and destroyed when the work is complete. Nothing persists to drift. The environment is comprehensible because it is scoped to a single change and exists only for the duration of that change.

Donald Reinertsen's work on batch size is relevant here. Large, shared environments are the equivalent of large batch sizes: they create queuing delays, increase cycle time, and make feedback slower and less specific. Ephemeral environments scoped to individual changes are small batches — fast feedback, no contention, clear attribution of failures. When a test fails in an ephemeral environment, you know exactly which change caused the failure because the environment contains only that change.

The practical prerequisites are non-trivial. Ephemeral environments require that your infrastructure can be provisioned and destroyed programmatically, quickly, and cheaply. Container orchestration platforms have made this dramatically more feasible than it was a decade ago, but the underlying discipline remains: if you cannot describe your environment as code and spin it up in minutes, you cannot make it ephemeral. There is also the question of external dependencies — databases, third-party services, shared resources — that may need to be stubbed, mocked, or provisioned in miniature. Getting this right is engineering work, but the payoff in testing speed and reliability is substantial.

There is an important boundary to respect: not everything should be ephemeral. Production environments are, by definition, persistent. Some integration testing may require shared environments with real external dependencies. The pattern is not "make everything ephemeral" but "make environments ephemeral by default, and justify the ones that are not."

Therefore:

**Provision on-demand, short-lived environments for testing and review, created by Infrastructure as Code and destroyed after use. Scope each environment to a single change or a single team's work. Treat persistent test environments as exceptions that require justification, not as the default.**

---

_Ephemeral environments are only practical when your infrastructure can be declared and provisioned programmatically, which is the domain of **Infrastructure as Code (35)**. The principle of replacing rather than modifying extends naturally to **Immutable Infrastructure (36)** — the same reasoning that makes environments ephemeral makes infrastructure components disposable._

## References

- Reinertsen, D. *The Principles of Product Development Flow: Second Generation Lean Product Development.* Celeritas, 2009.
- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
- Morris, K. *Infrastructure as Code*, 2nd ed. O'Reilly, 2020.
