---
id: 38
name: "Containerised Workloads"
confidence: 1
scale: 6
context_patterns: [37, 15]
completion_patterns: [39, 45]
ai_dimension: false
tags: [containers, packaging, deployment, boundaries]
references:
  - "Burns, Brendan et al. 'Borg, Omega, and Kubernetes.' ACM Queue, 2016."
  - "Simon, Herbert A. The Sciences of the Artificial. MIT Press, 1996."
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
---

# Containerised Workloads *

_A **Platform as Product (37)** provides shared infrastructure capabilities to stream-aligned teams, and **Service Domain Boundaries (15)** have established clear lines of responsibility between services. But the question remains: how should these services be packaged and deployed? Without a standard packaging unit, the platform must accommodate the unique deployment requirements of every application, and teams must negotiate ad hoc arrangements for each new service._

---

**Without a standard unit of deployment, every application has unique runtime requirements — different language versions, different system libraries, different dependency trees. This creates an n-by-m matrix of application-environment combinations that exceeds anyone's ability to comprehend or manage. Deployment becomes a bespoke exercise for each service, and "it works on my machine" becomes the defining experience of delivery.**

---

The container — a lightweight, isolated unit that packages an application with its dependencies into a single, portable artefact — resolves this tension. The insight is not primarily technological; it is organisational. The container is a boundary in Herbert Simon's sense of near-decomposability: what is inside the container (language, framework, dependencies) is the team's business; what is outside the container (orchestration, networking, resource allocation) is the platform's business. This separation means that teams retain autonomy over their runtime choices while the platform provides a standard execution environment.

Before containers, achieving this separation required either heavy-weight virtualisation (too slow, too expensive for the number of services a modern organisation runs) or convention-based deployment (too fragile, too reliant on tribal knowledge). Containers occupy a productive middle ground: lightweight enough to run hundreds on a single host, isolated enough to prevent one service's dependencies from interfering with another's, and standardised enough that the platform can manage them uniformly.

The practical benefits are significant. A containerised workload can be built once and run in any environment that supports the container runtime — a developer's laptop, a CI server, a staging cluster, production. This naturally reinforces **Build Once, Deploy Many (29)**. The container image, identified by a content-addressable hash, is the immutable artefact that travels through the pipeline unchanged. The container also provides a natural health-check and lifecycle interface: the platform can start, stop, restart, and monitor containers through a uniform API regardless of what runs inside them.

The failure modes are worth noting. Containers do not eliminate complexity — they relocate it. Container orchestration (Kubernetes being the dominant example) introduces its own substantial complexity, and organisations that adopt containers without a well-functioning platform team often find they have traded one set of problems for a harder set. The container is a tool, not a solution; it delivers its value only when embedded in a platform that manages orchestration, networking, storage, and observability on behalf of stream-aligned teams.

Therefore:

**Package each service and its dependencies as a container — a standard, portable unit of deployment. Teams choose their runtime internals; the platform provides a standard execution environment. Use the container boundary as a near-decomposability boundary: what is inside belongs to the team, what is outside belongs to the platform.**

---

_Containerised workloads set the stage for further platform capabilities. **Service Mesh (39)** provides infrastructure-layer management of communication between containers, handling cross-cutting concerns without requiring changes to the application code inside the container. **Zero Trust Architecture (45)** extends the isolation principle by ensuring that no container is implicitly trusted based on its network location — every interaction is verified._

## References

- Burns, Brendan, Grant, Brian, Oppenheimer, David, Brewer, Eric, and Wilkes, John. "Borg, Omega, and Kubernetes." *ACM Queue* 14, no. 1 (2016): 70-93.
- Simon, Herbert A. *The Sciences of the Artificial*, 3rd ed. MIT Press, 1996.
- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
