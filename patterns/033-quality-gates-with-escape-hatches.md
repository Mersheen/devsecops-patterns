---
id: 33
name: "Quality Gates with Escape Hatches"
confidence: 1
scale: 5
context_patterns: [28, 5]
completion_patterns: [42, 49]
ai_dimension: false
tags: [quality, governance, automation, accountability, override]
references:
  - "Burns, T. and Stalker, G.M. The Management of Innovation. Tavistock, 1961."
  - "Bainbridge, L. 'Ironies of Automation.' Automatica 19(6), 1983."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
---

# Quality Gates with Escape Hatches *

_Your **Deployment Pipeline (28)** enforces quality standards automatically as changes move toward production, and you operate under a **Trust and Verify (5)** philosophy — trusting teams to make good decisions while verifying outcomes. But the question arises: what happens when the gate says "no" and the team has a legitimate reason to proceed anyway?_

---

**Fully deterministic gates — where nothing passes without meeting every criterion — block legitimate exceptions and create pressure to game the metrics or bypass the pipeline entirely. Fully adaptive approval — where a human exercises judgement on every change — creates bottlenecks and negates the speed advantage of automation. Neither extreme serves the organisation well.**

---

The tension here is between determinism and adaptability, and it maps directly to Burns and Stalker's foundational distinction between mechanistic and organic management structures. Mechanistic systems (rigid rules, hierarchical approval) work well for stable, predictable conditions. Organic systems (flexible judgement, distributed authority) work well for novel, uncertain conditions. The insight is that a healthy organisation needs both, and more importantly, needs clear mechanisms for switching between them.

A quality gate encodes what the organisation has learned about what "good" looks like: test coverage thresholds, security scan results, performance benchmarks, compliance checks. These are valuable precisely because they are deterministic — they apply the same standard to every change, every time, without fatigue or favouritism. But any fixed rule will eventually encounter a legitimate exception. A critical security patch may need to bypass a slow integration test suite. A business-critical feature may ship with a known minor issue and a plan to address it. When the gate has no override mechanism, teams route around it — shadow pipelines, manual deployments, "temporary" exceptions that become permanent.

The escape hatch resolves this by making the override visible, not impossible. When a team overrides a quality gate, the override is logged, attributed to a specific person, and accompanied by a justification. The override is visible in dashboards and audit trails. It may trigger an alert or a follow-up action. The point is not to prevent overrides but to ensure they happen in the light rather than in the shadows.

Lisanne Bainbridge's "Ironies of Automation" warns of a related danger: when an automated system handles routine decisions, the humans who are supposed to oversee it lose the skill and context needed to intervene effectively. Quality gates that are never overridden may look like a sign of health, but they may also mean that the override mechanism is too cumbersome to use, that teams are gaming the metrics to avoid needing overrides, or that the humans who should be exercising judgement have been deskilled. A healthy escape hatch is one that is used occasionally — often enough that the skill of exercising judgement remains sharp, rarely enough that the gates are doing their job.

Therefore:

**Automate quality enforcement as pipeline gates that block promotion by default. Provide a visible override mechanism that requires attribution and justification but not bureaucratic approval. Log and surface all overrides. Review override patterns regularly to distinguish healthy exceptions from systemic problems or overly rigid gates.**

---

_The quality standards encoded in gates often originate as **Policy as Code (42)** — organisational policies expressed in executable form rather than PDF documents. The criteria against which gates evaluate changes are informed by **SLOs as Contracts (49)**, which provide objective, agreed-upon thresholds for what constitutes acceptable quality._

## References

- Burns, T. and Stalker, G.M. *The Management of Innovation.* Tavistock, 1961.
- Bainbridge, L. "Ironies of Automation." *Automatica* 19(6), 1983.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
