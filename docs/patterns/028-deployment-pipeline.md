---
id: 28
name: "Deployment Pipeline"
confidence: 2
scale: 5
context_patterns: [7, 21, 22]
completion_patterns: [29, 30, 31, 32, 33, 34]
ai_dimension: true
tags: [pipeline, delivery, ci-cd, continuous-delivery]
references:
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
  - "Marques, A. and Correia, F. 'Foundational DevOps Patterns.' PLoP, 2022."
---

# Deployment Pipeline **

_You have committed to **Value Stream Alignment (7)** and your teams practise **Continuous Integration (22)** against a codebase where **Version Control Everything (21)** is the norm. Code is being integrated frequently. But integration alone does not get software into the hands of users._

---

**The path from a developer's commit to running software in production is long, error-prone, and — in most organisations — poorly understood. When this path is manual, inconsistent, or opaque, it becomes the primary bottleneck to delivering value and the primary source of deployment failures.**

---

Jez Humble and David Farley formalised the deployment pipeline in 2010, but the pattern was already emerging in organisations that had learned, painfully, what happens without one. The core insight is that every change to the system — code, configuration, infrastructure, database schema — should travel through the same automated sequence of build, test, and deployment stages on its way to production. This sequence is the pipeline.

The pipeline serves multiple purposes simultaneously. It is a manufacturing line: it produces tested, deployable artefacts reliably and repeatably. It is a feedback mechanism: it tells the developer within minutes whether their change is viable. It is an audit trail: it records what was built, what was tested, how it was tested, and when it was deployed. And it is a forcing function: it makes the team's definition of "done" explicit and automated rather than implicit and manual.

The most common failure mode is a pipeline that exists on paper but not in practice — a CI server runs some tests, but the actual path to production involves manual steps, tribal knowledge, and a deployment day that everyone dreads. The second most common failure mode is a pipeline so slow that developers stop integrating frequently and start batching changes, which defeats the purpose entirely.

A well-functioning pipeline has several properties. It is the only way to get to production — no side doors. It is fast enough that developers get feedback within minutes for the commit stage and within an hour for the full pipeline. Every stage is automated. Failures stop the line. And the whole thing is defined as code, versioned alongside the application.

The DORA research consistently finds that deployment pipeline capabilities — specifically deployment frequency, lead time for changes, change failure rate, and failed deployment recovery time — are predictive of both organisational performance and well-being. This is not a technical nicety; it is an organisational capability with measurable business impact.

AI modifies this pattern in several ways. AI can optimise pipeline execution — predicting which tests are likely to fail for a given change and running those first, identifying flaky tests, estimating deployment risk based on the nature of the change. AI-generated code increases pipeline throughput (more commits, faster) which places greater stress on pipeline speed and reliability. And the pipeline itself must now handle AI-specific artefacts — models, training data references, prompt configurations — which do not follow the same versioning and testing patterns as traditional code. A pipeline that was designed for application code may need to be rethought when the "code" includes a 7-billion-parameter model.

Therefore:

**Create a single automated deployment pipeline through which every change must pass on its way to production. Define it as code. Make it fast. Make it the only path. Instrument it so that every stage provides feedback and leaves a record. When AI changes what flows through the pipeline — generated code, model artefacts, AI-assisted decisions — extend the pipeline to handle those artefacts with the same rigour.**

---

_The pipeline's effectiveness depends on the practices that feed it and the patterns that extend it. **Build Once, Deploy Many (29)** ensures artefact consistency across environments. **Progressive Delivery (30)** decouples deployment from release, reducing the blast radius of any single change. **Pipeline as Code (31)** ensures the pipeline itself is versioned and testable. **GitOps (32)** provides a pull-based reconciliation model for the deployment stages. **Quality Gates with Escape Hatches (33)** replaces manual gates with automated enforcement and accountable overrides. And **Ephemeral Environments (34)** provide isolated testing without environment contention._

## References

- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
- Marques, A. and Correia, F. "Foundational DevOps Patterns." PLoP, 2022. arXiv:2302.01053.
- Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. *The DevOps Handbook*, 2nd ed. IT Revolution, 2021.
