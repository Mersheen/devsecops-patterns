---
id: 30
name: "Progressive Delivery"
confidence: 1
scale: 5
context_patterns: [28, 17]
completion_patterns: [49, 48]
ai_dimension: false
tags: [delivery, canary, feature-flags, rollout, resilience]
references:
  - "Perrow, C. Normal Accidents: Living with High-Risk Technologies. Princeton University Press, 1999."
  - "Hollnagel, E. Safety-I and Safety-II: The Past and Future of Safety Management. Ashgate, 2014."
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
  - "Fowler, M. 'Feature Toggles (aka Feature Flags).' martinfowler.com, 2023."
---

# Progressive Delivery *

_Your **Deployment Pipeline (28)** can push changes to production reliably, and you practise **Thin Slice Delivery (17)** to keep increments small and valuable. But deploying a change to production and releasing it to every user are not the same act — and conflating them turns every release into an all-or-nothing bet._

---

**Binary deployment — where all users receive the new version simultaneously — means that any defect, performance regression, or unexpected interaction affects the entire user base at once. The blast radius of every release is, by definition, total. This creates fear of deployment, which leads to batching, which leads to larger and riskier releases, which justifies the fear.**

---

The solution is to decouple deployment from release. Deployment is the mechanical act of placing new code into production infrastructure. Release is the business decision about which users experience that code. These are fundamentally different concerns, and separating them gives you a powerful lever for managing risk.

Canary releases expose a new version to a small percentage of traffic — perhaps 1%, then 5%, then 25% — while monitoring for anomalies. Blue-green deployments maintain two identical production environments, switching traffic between them. Feature flags allow new functionality to be deployed but hidden, then revealed to specific user segments. Percentage rollouts combine these ideas: the code is in production for everyone, but the feature is progressively enabled. In each case, the common principle is the same: start small, observe, and expand only when confidence warrants it.

Charles Perrow's work on normal accidents is illuminating here. In tightly coupled systems, a failure in one component propagates rapidly to others before operators can intervene. Binary deployment is tight coupling between the deployment act and user impact — there is no buffer, no slack, no room for intervention. Progressive delivery introduces loose coupling: the deployment happens, but user impact is controlled independently. This slack is what gives you time to detect problems and respond before they become incidents.

This is adaptive delivery within a deterministic mechanism. The pipeline itself remains deterministic — the same artefact, the same stages, the same quality gates. But the exposure strategy is adaptive, responding to real-world signals (error rates, latency percentiles, user feedback) rather than following a fixed script. Erik Hollnagel would recognise this as a Safety-II approach: succeeding under varying conditions, rather than merely preventing failure under anticipated conditions.

Therefore:

**Decouple deployment from release. Use canary releases, blue-green deployments, feature flags, or percentage rollouts to expose changes to progressively larger audiences. Monitor at each stage. If problems emerge, the blast radius is limited and rollback is fast. Let the pipeline be deterministic; let the exposure strategy be adaptive.**

---

_Progressive delivery demands that you can observe what is happening as you roll out. **SLOs as Contracts (49)** provide the objective criteria against which rollout health is measured, and **Observability Over Monitoring (48)** gives you the ability to ask novel questions about novel failure modes during a rollout._

## References

- Perrow, C. *Normal Accidents: Living with High-Risk Technologies.* Princeton University Press, 1999.
- Hollnagel, E. *Safety-I and Safety-II: The Past and Future of Safety Management.* Ashgate, 2014.
- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
- Fowler, M. "Feature Toggles (aka Feature Flags)." martinfowler.com, 2023.
