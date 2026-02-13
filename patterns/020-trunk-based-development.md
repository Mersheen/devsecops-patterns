---
id: 20
name: "Trunk-Based Development"
confidence: 2
scale: 4
context_patterns: [17, 15]
completion_patterns: [22, 28]
ai_dimension: false
tags: [branching, integration, small-batches, version-control]
references:
  - "Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution Press, 2018."
  - "Hammant, P. *Trunk Based Development.* trunkbaseddevelopment.com, 2017."
  - "Ohno, T. *Toyota Production System: Beyond Large-Scale Production.* Productivity Press, 1988."
---

# Trunk-Based Development **

_You have adopted **Thin Slice Delivery (17)** so that work is decomposed into small, releasable increments, and your **Service Domain Boundaries (15)** are clear enough that teams can work without stepping on each other. The question now is how developers integrate their work — and how often._

---

**Long-lived branches defer integration, creating large, risky merges. Each branch is a local divergence — an exercise of autonomy — that becomes progressively harder to reconcile with the mainline the longer it lives. The merge cost grows non-linearly, and the risk of subtle integration defects grows with it.**

---

The intuition behind feature branches is sound: give developers space to work without disrupting others. But the cure is worse than the disease. A branch that lives for days or weeks accumulates changes that interact in ways no one can predict until the merge happens. By that point, the developer has moved on mentally, the context is stale, and the merge becomes an exercise in archaeology rather than engineering.

Deming and Ohno demonstrated decades ago that small batches outperform large batches across virtually every dimension: shorter lead times, fewer defects, faster feedback, lower risk. This principle applies to code integration with particular force. Each small merge is trivial to understand, trivial to review, and trivial to revert if something goes wrong. The cumulative effect of many small merges is a codebase that evolves continuously and predictably, rather than lurching forward in large, destabilising jumps.

The empirical evidence from the DORA research programme confirms this: trunk-based development is a statistically significant predictor of software delivery performance. Teams that work on a single shared trunk — with short-lived branches lasting less than a day, or no branches at all — integrate more frequently, detect problems earlier, and deliver faster. The practice requires discipline (small commits, feature flags for incomplete work, good test coverage) but the discipline pays for itself almost immediately.

The common objection is that trunk-based development is unsafe — that it risks breaking the build for everyone. This is precisely backwards. Trunk-based development is safer because it forces you to invest in the practices that make integration safe: automated testing, continuous integration, and small increments. The long-lived branch only feels safe because it hides the risk until later.

Therefore:

**Work on a single shared trunk with short-lived branches lasting less than one day, or commit directly to the mainline. Merge frequently and in small increments. Use feature flags to decouple deployment from release when work-in-progress must be committed before it is ready for users. The discipline of frequent integration is both faster and safer than periodic large merges.**

---

_Trunk-based development is made safe by **Continuous Integration (22)**, which verifies each commit automatically, and feeds directly into the **Deployment Pipeline (28)**, which carries each verified change toward production._

## References

- Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution Press, 2018.
- Hammant, P. *Trunk Based Development.* trunkbaseddevelopment.com, 2017.
- Ohno, T. *Toyota Production System: Beyond Large-Scale Production.* Productivity Press, 1988.
