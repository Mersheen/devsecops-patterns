---
id: 31
name: "Pipeline as Code"
confidence: 1
scale: 5
context_patterns: [28, 21]
completion_patterns: [35, 32]
ai_dimension: false
tags: [pipeline, version-control, automation, autonomy]
references:
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
  - "Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. The DevOps Handbook, 2nd ed. IT Revolution, 2021."
  - "Skelton, M. and Pais, M. Team Topologies. IT Revolution, 2019."
---

# Pipeline as Code *

_Your **Deployment Pipeline (28)** orchestrates the journey from commit to production, and you have committed to **Version Control Everything (21)** as a foundational practice. But if the pipeline definition itself lives outside version control — configured through a UI, maintained by a specialist team, or passed down as tribal knowledge — it becomes the single most important thing in your delivery process that cannot be reviewed, tested, or reproduced._

---

**Pipelines configured through graphical interfaces are opaque, unreproducible, and prone to drift between teams. Pipeline definitions hardcoded by a central platform team stifle the autonomy that stream-aligned teams need to deliver effectively. In both cases, the pipeline — the thing that defines how quality is enforced — is itself exempt from quality enforcement.**

---

The solution is to treat pipeline definitions as code: versioned, reviewed, tested, and owned by the teams that use them. A pipeline definition sits in the same repository as the application it builds and deploys, or in a repository the team controls. It passes through code review. It can be run locally or in a sandbox. When it breaks, the team can diagnose and fix it without filing a ticket with a central team.

This creates an apparent tension between autonomy and alignment. If every team defines its own pipeline from scratch, you get fragmentation: different security scanning tools, different deployment strategies, inconsistent quality gates. If a central team dictates the pipeline, you get bottlenecks and one-size-fits-all constraints that slow teams down. The resolution is a layered model. A platform team provides pipeline building blocks — reusable stages, shared libraries, composable templates — that encode organisational standards. Stream-aligned teams compose these blocks into pipelines that serve their specific needs. The building blocks provide alignment; the composition provides autonomy.

Version control of pipeline definitions has a secondary benefit that is easily overlooked: it makes the pipeline's history legible. When a deployment starts failing, you can correlate the failure with recent changes to the pipeline definition, not just to the application code. You can review who changed what, when, and why. You can revert a pipeline change as easily as you revert an application change. The pipeline becomes a first-class citizen of your engineering practice, subject to the same discipline as everything else.

The practical test is simple: could you reproduce your entire delivery pipeline from scratch using only what is in version control? If the answer is no — if reproducing it requires clicking through UIs, consulting wikis, or asking someone who has been here for years — then your pipeline is not code, it is folklore.

Therefore:

**Define pipeline configurations in version-controlled files alongside the code they build and deploy. Provide shared, composable building blocks from the platform team for organisational standards, and let stream-aligned teams own the composition. Review and test pipeline changes with the same rigour as application changes.**

---

_Pipeline as Code naturally extends into **Infrastructure as Code (35)**, where the same principle — declare it, version it, automate it — applies to the environments the pipeline deploys into. **GitOps (32)** takes this further by making the version-controlled declaration the single source of truth for desired system state._

## References

- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
- Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. *The DevOps Handbook*, 2nd ed. IT Revolution, 2021.
- Skelton, M. and Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
