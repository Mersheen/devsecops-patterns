---
id: 9
name: "Platform Team"
confidence: 2
scale: 2
context_patterns: [7, 3]
completion_patterns: [37, 14]
ai_dimension: false
tags: [platform, teams, self-service, subsidiarity]
references:
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
  - "Simon, Herbert A. The Sciences of the Artificial. MIT Press, 1996."
  - "Pope Pius XI. Quadragesimo Anno. 1931."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Platform Team **

_Within a **Value Stream Alignment (7)** where stream-aligned teams deliver value end-to-end, and the organisation has committed to **Flow Over Utilisation (3)**, a recurring problem emerges: every stream team faces the same infrastructure, tooling, and operational challenges._

---

**Stream-aligned teams cannot each independently solve infrastructure provisioning, security tooling, observability, deployment automation, and developer experience. The resulting duplication wastes scarce resources, and forcing every team to comprehend problems outside their core domain overloads their cognitive capacity.**

---

The argument for a platform team follows from two observations. First, certain capabilities — container orchestration, CI/CD infrastructure, secrets management, monitoring stacks, identity and access management — are genuinely shared. Every stream team needs them, but no stream team's value proposition depends on building them from scratch. Second, these capabilities require deep specialist knowledge that is expensive to maintain and dangerous to get wrong. A stream team that configures its own TLS termination or builds its own secrets rotation is likely to do it worse than a dedicated team, and the consequences of failure are severe.

The principle of subsidiarity — that a higher-level body should not perform functions that can be effectively carried out at a lower level — might seem to argue against a platform team. But subsidiarity also has its complement: the higher-level body should handle what individual lower-level bodies cannot efficiently accomplish alone. A platform team is this complement in action. It absorbs complexity that would otherwise be distributed across every stream team, reducing their cognitive load and freeing them to focus on their domain.

The critical design constraint is that the platform must be a product, not a mandate. If the platform team operates as a gatekeeper — stream teams must file tickets and wait — it recreates the very handoffs that **Value Stream Alignment (7)** was designed to eliminate. The platform must be self-service: stream teams consume its capabilities through APIs, CLIs, and documentation, on their own schedule, without waiting for the platform team's sprint cycle. This is what distinguishes a platform team from a traditional operations or infrastructure department.

Herbert Simon's hierarchy of nearly decomposable systems provides the theoretical underpinning. The platform is a stable lower layer that changes slowly, providing well-defined interfaces to the faster-changing stream teams above it. The interfaces are the key: they must be clear enough that stream teams can use the platform without understanding its internals, but flexible enough that the platform does not become a constraint on what stream teams can build.

Therefore:

**Create a dedicated platform team that provides shared capabilities — infrastructure, tooling, security primitives, observability, developer experience — as a self-service internal product. The platform absorbs complexity so that stream-aligned teams do not have to. Measure the platform team by whether stream teams can move faster and more safely, not by the platform's own feature velocity.**

---

_The platform team's output should be managed as a product in its own right, following **Platform as Product (37)**. The broader principle that every team's output — whether customer-facing or internal — benefits from product thinking is captured in **Everything as Product (14)**._

## References

- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- Simon, Herbert A. *The Sciences of the Artificial*, 3rd ed. MIT Press, 1996.
- Pope Pius XI. *Quadragesimo Anno*. 1931. Paragraphs 79-80 on the principle of subsidiarity.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
