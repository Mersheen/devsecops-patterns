---
id: 37
name: "Platform as Product"
confidence: 2
scale: 6
context_patterns: [9, 14]
completion_patterns: [38, 39, 48]
ai_dimension: false
tags: [platform, product-thinking, self-service, developer-experience]
references:
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
  - "Simon, Herbert A. The Sciences of the Artificial. MIT Press, 1996."
  - "Hayek, F.A. 'The Use of Knowledge in Society.' American Economic Review, 1945."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Platform as Product **

_A **Platform Team (9)** exists to provide shared capabilities, and the organisation has committed to treating **Everything as Product (14)** — including internal tools and services. But the existence of a platform team does not guarantee a usable platform. Without product discipline, the platform becomes either a neglected collection of scripts or an imposed mandate that teams resent and route around._

---

**Without a well-designed platform, every stream-aligned team must independently solve infrastructure provisioning, security, observability, and deployment. This duplication wastes scarce engineering resources and forces teams to comprehend problems far outside their core domain. But a platform imposed without product thinking — without user research, clear interfaces, documentation, and feedback loops — becomes an unwanted mandate that reintroduces the handoffs and bottlenecks the organisation was trying to eliminate.**

---

The distinction between a platform and a platform-as-product is the difference between a mandate and a market. A mandated platform says: "You must use this." A platform as product says: "This is so good you will want to use it." The platform team, operating as described in **Platform Team (9)**, must adopt the same discipline that any product team would: understand their users (stream-aligned teams), identify their needs (paved paths for deployment, security, observability), build solutions that are self-service, iterate based on feedback, and measure success by adoption and outcomes rather than by features shipped.

Herbert Simon's hierarchy of nearly decomposable systems provides the architectural justification. The platform is a stable lower layer that absorbs complexity and presents well-defined interfaces to the faster-changing layers above it. Stream teams interact with the platform through these interfaces — APIs, CLIs, templates, documentation — without needing to understand the platform's internals. The interfaces are the product. If they are poorly designed, the hierarchy collapses: stream teams must reach into the platform's internals to get anything done, coupling themselves to implementation details that the platform team will eventually need to change.

Friedrich Hayek's insight about distributed knowledge reinforces the product approach. No central team can possess all the knowledge needed to make optimal decisions for every stream team. The platform as product solves this by providing capabilities and constraints — "price signals" in Hayek's terms — that enable decentralised decisions. A good platform tells stream teams: "Here is how to provision a database, here is the cost, here are the security constraints, here is the SLA." Armed with this information, stream teams make their own decisions. A bad platform says: "File a ticket and we will provision a database when we get to it."

The most common failure mode is building the platform that the platform team wants rather than the platform that stream teams need. The remedy is the same as for any product: talk to your users, watch them struggle, measure adoption (not just availability), and treat low adoption as a product problem, not a compliance problem.

Therefore:

**Treat the internal platform as a product, not a project. The **Platform Team (9)** operates it; product thinking governs it. Design for self-service: stream-aligned teams consume platform capabilities through clear APIs, templates, and documentation, on their own schedule, without filing tickets. Measure the platform by whether stream teams can ship faster and safer, and iterate based on their feedback.**

---

_The platform's capabilities are expressed through the patterns it enables. **Containerised Workloads (38)** provide the standard packaging and execution unit the platform offers. **Service Mesh (39)** handles cross-cutting communication concerns at the platform layer so that stream teams do not have to. **Observability Over Monitoring (48)** becomes practical when the platform provides observability as a built-in capability rather than leaving each team to instrument independently._

## References

- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- Simon, Herbert A. *The Sciences of the Artificial*, 3rd ed. MIT Press, 1996.
- Hayek, F.A. "The Use of Knowledge in Society." *American Economic Review* 35, no. 4 (1945): 519-530.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
