---
id: 41
name: "Security as Shared Responsibility"
confidence: 2
scale: 7
context_patterns: [5, 1]
completion_patterns: [42, 44, 48]
ai_dimension: false
tags: [security, culture, ownership, enablement]
references:
  - "Hayek, F. A. 'The Use of Knowledge in Society.' American Economic Review 35.4 (1945): 519-530."
  - "Deming, W. Edwards. Out of the Crisis. MIT Press, 1986."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
  - "Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. The DevOps Handbook, 2nd ed. IT Revolution, 2021."
---

# Security as Shared Responsibility **

_You have established **Trust and Verify (5)** as a governance philosophy and operate within a **Generative Culture (1)** where information — including bad news about vulnerabilities and risks — flows freely. The question now is where security responsibility lives._

---

**Organisations tend toward one of two failure modes. A dedicated security team that approves everything creates a bottleneck — the approvers cannot know the system as well as the builders, so their reviews are either superficial or slow, and developers learn to route around them. An organisation with no security oversight at all is reckless — speed without safety is just moving faster toward the next breach.**

---

Friedrich Hayek argued that knowledge about particular circumstances of time and place is distributed across many individuals, and that no central authority can aggregate it effectively. Security knowledge follows the same pattern. The developers who build a service understand its data flows, trust boundaries, and failure modes better than any external reviewer ever could. A centralised security team reviewing pull requests for dozens of teams cannot possibly hold the context needed to make good security judgements at scale. They become either a rubber stamp or a bottleneck — and often oscillate between the two.

Deming's third point — "Cease dependence on inspection to achieve quality" — applies directly. Inspection-based security (penetration tests, annual audits, change approval boards) catches problems after they are built. It is expensive, slow, and demoralising: developers experience security as a punishment rather than a capability. Worse, it creates a false sense of safety. If the security team approved it, it must be secure — a belief that persists right up to the moment of the breach.

The resolution is to make security a capability that everyone exercises, not a team that approves. This does not mean dissolving the security team. It means changing the security team's role from gatekeeper to enabler — the same transformation that **Enabling Team (10)** describes at a structural level. The security team builds tools, writes libraries, creates guardrails, develops training, conducts threat modelling exercises, and responds to incidents. What it does not do is sit in the critical path of every deployment, approving changes it cannot fully understand.

This requires investment in three areas: tooling (automated security checks in the pipeline so that developers get fast feedback), culture (a generative culture where reporting a vulnerability is rewarded, not punished), and education (developers need enough security knowledge to make reasonable decisions, not to become security experts). The security team's success is measured not by how many things it blocks, but by how rarely security problems reach production — a leading indicator, not a lagging gate.

Therefore:

**Make security a capability everyone exercises, not a team that approves. Transform the security function from gatekeeper to enabler: build tooling, create guardrails, invest in education, and embed security thinking into development rather than bolting it on afterward. Measure success by outcomes — fewer vulnerabilities in production — not by activity — more reviews conducted.**

---

_This pattern is completed by several more specific practices. **Policy as Code (42)** provides the automated enforcement mechanism that makes shared responsibility practical — encoding security rules as machine-enforceable checks rather than manual review gates. **Threat Modelling as Practice (44)** gives development teams a structured way to think about security in their domain. And **Observability Over Monitoring (48)** ensures that the organisation can see when security problems do occur, closing the feedback loop that makes distributed responsibility accountable._

## References

- Hayek, F. A. "The Use of Knowledge in Society." *American Economic Review* 35.4 (1945): 519-530.
- Deming, W. Edwards. *Out of the Crisis.* MIT Press, 1986.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
- Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. *The DevOps Handbook*, 2nd ed. IT Revolution, 2021.
