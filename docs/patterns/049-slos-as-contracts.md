---
id: 49
name: "SLOs as Contracts"
confidence: 2
scale: 8
context_patterns: [4, 30]
completion_patterns: [52, 53]
ai_dimension: false
tags: [slo, reliability, error-budget, tradeoffs]
references:
  - "Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. Site Reliability Engineering. O'Reilly, 2016."
  - "Robbins, L. An Essay on the Nature and Significance of Economic Science. Macmillan, 1932."
  - "Reinertsen, D. The Principles of Product Development Flow. Celeritas, 2009."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# SLOs as Contracts **

_You have committed to making tradeoffs explicit through **Explicit Tradeoffs (4)** and your delivery process supports **Progressive Delivery (30)**, which lets you control the blast radius of changes. But how do you decide when to push for speed and when to invest in reliability? Without a principled mechanism, this decision is either political or arbitrary._

---

**Without a quantified agreement on acceptable reliability, teams either over-invest in stability — sacrificing speed for a safety margin nobody asked for — or under-invest — shipping fast until the next outage, then panic-fixing, then shipping fast again. There is no principled way to make the tradeoff between speed and safety.**

---

A Service Level Objective is a target for a measurable aspect of service reliability — availability, latency, error rate — expressed as a percentage over a time window. An error budget is the complement: if the SLO is 99.9% availability over 30 days, the error budget is 0.1%, which translates to roughly 43 minutes of allowed downtime. The error budget is the scarcity premise made measurable. Lionel Robbins defined economics as the study of behaviour under conditions of scarcity. Reliability is scarce — you cannot have infinite reliability and infinite speed simultaneously. The error budget quantifies exactly how much unreliability is acceptable, making the speed-safety tradeoff explicit and governable.

When the error budget is healthy, deploy aggressively. The system has headroom for risk, and the cost of not deploying (delayed features, unrealised value) exceeds the cost of potential instability. When the error budget is exhausted, invest in reliability. The system has consumed its allowance, and further risk-taking has a direct, measurable cost. This is **Explicit Tradeoffs (4)** instantiated for reliability — the SLO framework transforms a fuzzy, emotional argument ("we need to be more careful" versus "we need to ship faster") into a data-driven decision with a clear protocol.

The critical subtlety is choosing the right SLOs. An SLO that is too tight starves the team of error budget and turns every deployment into a risk event. An SLO that is too loose provides no meaningful constraint and fails to protect users. The SLO should reflect what users actually need, not what engineers aspire to. Donald Reinertsen's work on cost of delay provides a framework: the SLO should be set at the point where the marginal cost of improving reliability equals the marginal cost of the speed that improvement consumes.

SLOs also change the conversation between teams. When one team's service depends on another's, the SLO becomes the contract — not an informal promise, but a measurable commitment that both teams can plan around. This is particularly important in a microservices architecture where cascading failures can propagate across service boundaries.

Therefore:

**Define Service Level Objectives for every service that users or other teams depend on. Derive error budgets from those SLOs. Use the error budget as the governing mechanism for the speed-safety tradeoff: when budget is available, prioritise delivery; when it is consumed, prioritise reliability. Set SLOs based on what users actually need, not on what feels aspirational.**

---

_This pattern is completed by **Alerting on Symptoms, Not Causes (52)**, which ensures that the alerting layer is aligned with SLO-meaningful signals rather than low-level system metrics. **Toil Budgets (53)** applies the same scarcity logic to operational work, capping the amount of manual toil a team accepts. Together, these patterns make the economics of reliability explicit and actionable._

## References

- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly, 2016.
- Robbins, L. *An Essay on the Nature and Significance of Economic Science.* Macmillan, 1932.
- Reinertsen, D. *The Principles of Product Development Flow: Second Generation Lean Product Development.* Celeritas, 2009.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
