---
id: 35
name: "Infrastructure as Code"
confidence: 2
scale: 6
context_patterns: [21, 28]
completion_patterns: [36, 34, 42]
ai_dimension: false
tags: [infrastructure, declarative, reproducibility, versioning]
references:
  - "Morris, Kief. Infrastructure as Code, 3rd ed. O'Reilly, 2021."
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Infrastructure as Code **

_You have established **Version Control Everything (21)** as a norm and your changes flow through a **Deployment Pipeline (28)**. But while application code is versioned, tested, and reviewed, the infrastructure it runs on is often provisioned by hand — clicked into existence through web consoles, configured via SSH sessions, and documented only in the memory of the person who did it._

---

**Manually provisioned infrastructure is undocumented, irreproducible, and unreliable. "Snowflake servers" that were hand-configured are both incomprehensible — no one knows their exact state — and fragile — they cannot be recreated. When the only record of your infrastructure is the infrastructure itself, you have no way to audit, reason about, or recover it.**

---

The insight behind Infrastructure as Code is deceptively simple: infrastructure should be subject to the same practices as application code. Define it declaratively, store it in version control, review it through pull requests, test it automatically, and deliver it through the pipeline. The moment you do this, every pattern that applies to code — versioning, branching, code review, automated testing, continuous integration — applies to infrastructure as well.

Kief Morris identifies the central tension as the balance between deterministic execution and adaptive evolution. A declarative infrastructure definition is deterministic: given the same inputs, it produces the same infrastructure every time. This is what makes it reproducible. But infrastructure must also evolve — new services need new resources, security requirements change, cost pressures demand right-sizing. The resolution is that the definition evolves (adaptive) while each application of the definition is exact (deterministic). You change the code, not the running infrastructure.

The most common failure mode is treating Infrastructure as Code as a one-time migration exercise rather than an ongoing discipline. Teams write Terraform or CloudFormation once, deploy it, and then make subsequent changes through the console because "it's faster." The moment they do this, drift begins. The gap between what the code says and what actually exists widens, and the code becomes a historical curiosity rather than a source of truth. The discipline requires that the code is always the authoritative definition — if a change isn't in the code, it doesn't exist.

A subtler failure mode is writing infrastructure code that is correct but incomprehensible. A 3,000-line Terraform module with no abstractions, no documentation, and dozens of implicit dependencies is technically Infrastructure as Code, but it fails the comprehensibility test. Like application code, infrastructure code benefits from modularity, clear naming, sensible abstractions, and the expectation that someone else will need to read it.

Therefore:

**Define all infrastructure declaratively in code. Version it alongside application code using **Version Control Everything (21)**. Test it. Deliver it through the **Deployment Pipeline (28)**. Treat the code as the single source of truth — if a resource is not defined in code, it should not exist. Infrastructure becomes auditable, reproducible, and evolvable.**

---

_This pattern is completed by several more specific patterns. **Immutable Infrastructure (36)** extends the principle by ensuring that running infrastructure is never modified in place — only replaced from the code definition. **Ephemeral Environments (34)** become trivial once infrastructure is defined as code, since spinning up a complete environment is just another pipeline run. **Policy as Code (42)** applies the same declarative, versioned approach to security and compliance rules that govern the infrastructure._

## References

- Morris, Kief. *Infrastructure as Code: Dynamic Systems for the Cloud Age*, 3rd ed. O'Reilly, 2021.
- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
