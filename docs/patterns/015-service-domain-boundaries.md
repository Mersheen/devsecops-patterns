---
id: 15
name: "Service Domain Boundaries"
confidence: 2
scale: 3
context_patterns: [8, 12]
completion_patterns: [18, 38, 46]
ai_dimension: false
tags: [domain-driven-design, bounded-context, coupling, cohesion]
references:
  - "Simon, Herbert A. 'The Architecture of Complexity.' Proceedings of the American Philosophical Society 106.6 (1962): 467-482."
  - "Evans, Eric. Domain-Driven Design: Tackling Complexity in the Heart of Software. Addison-Wesley, 2003."
  - "Stevens, Wayne P., Myers, Glenford J., and Constantine, Larry L. 'Structured Design.' IBM Systems Journal 13.2 (1974): 115-139."
  - "Conway, Melvin E. 'How Do Committees Invent?' Datamation 14.4 (1968): 28-31."
---

# Service Domain Boundaries **

_When **Stream-Aligned Teams (8)** are in place and the organisation has applied the **Inverse Conway Manoeuvre (12)** to shape its team structure around desired architectural outcomes, the critical question becomes where to draw the boundaries between services and domains._

---

**A system without clear boundaries becomes incomprehensible: every change risks unexpected cascading effects, and no one can reason about the whole. Conversely, boundaries drawn in the wrong places create artificial coupling that forces teams to coordinate on every change, destroying the autonomy the team structure was designed to provide.**

---

Herbert Simon, in "The Architecture of Complexity," observed that complex systems that endure are nearly decomposable: they consist of subsystems whose internal interactions are strong while their interactions with other subsystems are comparatively weak. This property — near-decomposability — is what makes a complex system comprehensible and evolvable. You can understand and modify one subsystem without understanding all the others, provided you understand the interfaces between them.

Eric Evans operationalised this insight for software through the concept of bounded contexts in Domain-Driven Design. A bounded context is a region of a system within which a particular domain model is consistent and meaningful. At the boundary, models from different contexts meet and must be translated. The key insight is that trying to create a single, unified model for an entire complex domain is not merely difficult — it is counterproductive. Different parts of the business use the same words to mean different things, and forcing a shared model creates a muddled abstraction that serves no one well.

Stevens, Myers, and Constantine formalised the same principle from a different angle: coupling and cohesion. Good design maximises cohesion within modules (things that change together live together) and minimises coupling between them (a change in one module does not force changes in others). When service boundaries align with natural domain seams — the places where interaction between concepts is weakest — the resulting architecture inherits these properties. When boundaries are drawn along technical layers instead (a "service" for the database, another for the UI), coupling remains high because every business change cuts across all layers.

Conway's Law ensures that these boundaries propagate into the organisation and back again. If the architecture has high coupling between services A and B, the teams owning A and B will be forced into constant communication. If the organisation places those teams in different time zones with no shared working hours, the architecture will drift toward reducing that coupling — or delivery will grind to a halt. Getting the boundaries right is therefore not purely a technical decision; it is a sociotechnical one that must account for both domain structure and team structure.

Therefore:

**Apply Domain-Driven Design bounded contexts to identify the natural seams in your system — the places where interaction between domains is weaker than interaction within them. Draw service boundaries along those seams. Validate the boundaries against team structure and communication patterns, and adjust when Conway's Law reveals a mismatch. Get the seams right before optimising anything else, because wrong boundaries compound into every subsequent decision.**

---

_Once boundaries are established, **API as Contract (18)** provides the mechanism for managing interactions across them. Services within those boundaries are deployed as **Containerised Workloads (38)**, and the boundaries themselves enable **Blast Radius Limitation (46)** by constraining the scope of any single failure._

## References

- Simon, Herbert A. "The Architecture of Complexity." *Proceedings of the American Philosophical Society* 106.6 (1962): 467-482.
- Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Addison-Wesley, 2003.
- Stevens, Wayne P., Myers, Glenford J., and Constantine, Larry L. "Structured Design." *IBM Systems Journal* 13.2 (1974): 115-139.
- Conway, Melvin E. "How Do Committees Invent?" *Datamation* 14.4 (1968): 28-31.
