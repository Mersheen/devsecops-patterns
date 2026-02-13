---
id: 21
name: "Version Control Everything"
confidence: 2
scale: 4
context_patterns: [16, 17]
completion_patterns: [31, 32, 35, 42]
ai_dimension: false
tags: [version-control, git, auditability, single-source-of-truth]
references:
  - "Marques, F. and Correia, F. 'DevOps Patterns and Antipatterns for Continuous Software Evolution.' *PLoP 2022.*"
  - "Humble, J. and Farley, D. *Continuous Delivery.* Addison-Wesley, 2010."
  - "Kim, G. et al. *The DevOps Handbook.* IT Revolution Press, 2016."
---

# Version Control Everything **

_You are pursuing an **Evolutionary Architecture (16)** that must change safely over time, and delivering in **Thin Slices (17)** that require confidence in what has changed and what can be rolled back. The question is: what artefacts deserve the discipline of version control?_

---

**Unversioned changes to code, configuration, infrastructure, or policy are invisible, irreversible, and unauditable. This makes the system both less deterministic — you cannot know what state it is in — and less adaptive — you cannot safely roll back to a known-good state when something goes wrong.**

---

The default assumption in most organisations is that version control is for application code. Everything else — infrastructure definitions, configuration files, policy rules, pipeline definitions, documentation — lives somewhere else: a wiki, a shared drive, a configuration management database, or worst of all, in someone's head. The result is a system whose application code is versioned and recoverable but whose actual behaviour depends on dozens of unversioned, manually managed artefacts that no one can reconstruct after the fact.

This is not merely an inconvenience. It is a fundamental impediment to the practices that make modern software delivery work. You cannot do continuous integration if your build depends on configuration that is not in version control. You cannot do infrastructure as code if your infrastructure definitions are edited by hand on running servers. You cannot audit your security posture if your policies exist as tribal knowledge. You cannot perform a blameless postmortem if you cannot reconstruct the state of the system at the time of the incident.

The principle is simple and, once stated, almost self-evident: version control all artefacts that affect the behaviour of the system. Application code, infrastructure definitions, configuration, policy, documentation, pipeline definitions, database schemas — all of it. The version history becomes the single source of truth for what the system is and was. Every change is attributable, reviewable, and reversible.

Marques and Correia identified this as a foundational DevOps pattern: without it, nearly every other pattern in the delivery pipeline becomes unreliable or impossible. It is the bedrock on which determinism and adaptability are simultaneously built.

Therefore:

**Version control all artefacts that affect the behaviour of the system: application code, infrastructure definitions, configuration, policy rules, pipeline definitions, database schemas, and documentation. The version history is the single source of truth for what the system is and was. If it is not in version control, it does not officially exist.**

---

_This pattern is completed by the practices that put specific artefact types under version control: **Pipeline as Code (31)** for delivery pipelines, **GitOps (32)** for deployment declarations, **Infrastructure as Code (35)** for infrastructure definitions, and **Policy as Code (42)** for security and compliance rules._

## References

- Marques, F. and Correia, F. "DevOps Patterns and Antipatterns for Continuous Software Evolution." *PLoP 2022.*
- Humble, J. and Farley, D. *Continuous Delivery.* Addison-Wesley, 2010.
- Kim, G. et al. *The DevOps Handbook.* IT Revolution Press, 2016.
