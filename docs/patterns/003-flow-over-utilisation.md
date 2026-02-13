---
id: 3
name: "Flow Over Utilisation"
confidence: 2
scale: 1
context_patterns: [1]
completion_patterns: [7, 17, 28]
ai_dimension: true
tags: [flow, queuing-theory, throughput, slack]
references:
  - "Reinertsen, D. G. The Principles of Product Development Flow: Second Generation Lean Product Development. Celeritas, 2009."
  - "Goldratt, E. M. The Goal: A Process of Ongoing Improvement, 3rd rev. ed. North River Press, 2004."
  - "Ohno, T. Toyota Production System: Beyond Large-Scale Production. Productivity Press, 1988."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Flow Over Utilisation **

_Within a **Generative Culture (1)** that gives teams permission to optimise for outcomes rather than activity, the question arises: what, exactly, should the organisation optimise for?_

---

**Traditional management optimises for keeping people busy — high utilisation of every resource. Queueing theory proves this destroys the very throughput it intends to maximise: as utilisation approaches 100 per cent, wait times approach infinity.**

---

The intuition that idle resources are wasteful is deeply rooted in industrial-age management. If a developer is not writing code, a manager is not in a meeting, or a server is not processing requests, something must be wrong. This intuition is not merely imprecise — it is mathematically backwards for knowledge work.

Donald Reinertsen brought queueing theory into product development and demonstrated the core result: for any system with variability (and knowledge work is nothing if not variable), wait time is a non-linear function of utilisation. At 50 per cent utilisation, wait times are manageable. At 80 per cent, they are painful. At 95 per cent, they are catastrophic. The relationship is not linear — it follows a hyperbolic curve. This means that the last 10 per cent of utilisation improvement buys you more queue time than the first 50 per cent. Organisations that pride themselves on "everyone is busy" are organisations where everything takes forever.

Eliyahu Goldratt's Theory of Constraints complements this insight. The throughput of any system is determined by its bottleneck. Optimising anything other than the bottleneck is an illusion of progress — it merely piles up work-in-progress in front of the constraint. Taiichi Ohno built the Toyota Production System on the same foundation: flow is a pillar, and the system is designed to make flow problems visible rather than hiding them behind buffers of inventory.

The practical implication is that slack is not waste — it is the capacity that absorbs variability and enables improvement. A team that is 100 per cent utilised has zero capacity to respond to the unexpected, zero capacity to improve its own processes, and zero capacity to help other teams. Protecting slack requires organisational courage because it means defending "unproductive" time against the relentless pressure to fill every hour with output.

AI collapses some bottlenecks — code generation, test creation, documentation drafting — while creating new queues elsewhere. AI-generated code still requires human review, validation, and integration. AI-suggested architectural changes still require human judgement. The pattern holds; the bottleneck moves. Organisations that adopt AI without understanding flow will simply shift the queue from "waiting for code" to "waiting for review of AI-generated code," and the hyperbolic curve will punish them just as severely at the new bottleneck.

Therefore:

**Optimise for flow of value through the system, not for resource utilisation. Protect slack capacity deliberately — it is what absorbs variability and enables improvement. Make queues and wait times visible. When AI shifts bottlenecks, follow the constraint rather than celebrating the local speed-up.**

---

_Flow requires structural support. **Value Stream Alignment (7)** organises teams around the flow of value rather than around functional specialisation. **Thin Slice Delivery (17)** reduces batch size so that work moves through the system in small, fast increments. The **Deployment Pipeline (28)** is the concrete mechanism through which value flows from idea to production._

## References

- Reinertsen, D. G. *The Principles of Product Development Flow: Second Generation Lean Product Development.* Celeritas, 2009.
- Goldratt, E. M. *The Goal: A Process of Ongoing Improvement*, 3rd rev. ed. North River Press, 2004.
- Ohno, T. *Toyota Production System: Beyond Large-Scale Production.* Productivity Press, 1988.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
