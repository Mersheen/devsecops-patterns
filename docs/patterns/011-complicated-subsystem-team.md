---
id: 11
name: "Complicated Subsystem Team"
confidence: 1
scale: 2
context_patterns: [7, 8]
completion_patterns: [15, 18]
ai_dimension: false
tags: [teams, specialist, complexity, cognitive-load]
references:
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
  - "Brooks, Frederick P. 'No Silver Bullet: Essence and Accident in Software Engineering.' IEEE Computer 20.4 (1987): 10-19."
  - "Simon, Herbert A. The Sciences of the Artificial. MIT Press, 1996."
---

# Complicated Subsystem Team *

_Within a **Value Stream Alignment (7)** served by **Stream-Aligned Teams (8)**, certain domains demand specialist depth that exceeds what any generalist team can sustain alongside its primary delivery responsibilities._

---

**Some domains — machine learning model development, cryptographic systems, real-time data processing, compiler internals — require specialist knowledge so deep that embedding it in a stream-aligned team would overwhelm that team's cognitive capacity. Forcing this knowledge into generalist teams does not democratise it; it dilutes it.**

---

Frederick Brooks distinguished essential complexity from accidental complexity. A complicated subsystem team exists because certain domains carry irreducible essential complexity. Cryptographic protocol implementation is not complicated because of poor tooling or bad design choices; it is complicated because the domain itself demands deep mathematical knowledge and extreme precision. Similarly, building and tuning machine learning models, designing low-latency data pipelines, or implementing custom consensus algorithms requires years of specialist study that cannot be reasonably expected of a stream-aligned team.

The cognitive load argument from **Stream-Aligned Teams (8)** applies here in reverse. If a stream team is forced to own a deeply specialist subsystem, one of two things happens: either the subsystem receives insufficient attention because the team prioritises its primary stream (leading to subtle, dangerous defects), or the subsystem consumes so much of the team's attention that the primary stream suffers. Neither outcome is acceptable.

The solution is to isolate the specialist knowledge in a dedicated team that provides its capability as a service. The critical constraint is that the boundary between the complicated subsystem team and its consuming stream teams must be a clean API — a well-defined interface at Scale 3 — not an organisational handoff that creates coupling and queuing. If the stream team must file a ticket and wait three sprints for the subsystem team to make a change, the complicated subsystem team has become a bottleneck, not an enabler. The subsystem team should expose its capability through interfaces that stream teams can consume independently, following the same self-service principle that governs the **Platform Team (9)**.

This team type should be used sparingly. The temptation to label any difficult problem as a "complicated subsystem" and create a specialist team around it leads to fragmentation and handoff culture. The test is whether the domain genuinely requires specialist depth that a stream team cannot reasonably acquire, not merely whether it is difficult or unfamiliar.

Therefore:

**When a domain requires specialist depth that would overwhelm a stream-aligned team's cognitive capacity, isolate that knowledge in a dedicated complicated subsystem team. The team exposes its capability through clean, well-defined interfaces that stream teams consume as a service. Use this team type sparingly — only when the essential complexity of the domain genuinely demands it.**

---

_The boundary between the complicated subsystem team and its consumers must be drawn carefully, following the principles of **Service Domain Boundaries (15)**. The interface itself should be governed by **API as Contract (18)**, ensuring that the consuming stream teams can depend on stable, well-documented interfaces without needing to understand the subsystem's internals._

## References

- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- Brooks, Frederick P. "No Silver Bullet: Essence and Accident in Software Engineering." *IEEE Computer* 20.4 (1987): 10-19.
- Simon, Herbert A. *The Sciences of the Artificial*, 3rd ed. MIT Press, 1996.
