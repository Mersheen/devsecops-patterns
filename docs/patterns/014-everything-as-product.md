---
id: 14
name: "Everything as Product"
confidence: 2
scale: 3
context_patterns: [8, 9]
completion_patterns: [37, 18]
ai_dimension: false
tags: [product-thinking, platform, ownership, feedback]
references:
  - "Robbins, Lionel. An Essay on the Nature and Significance of Economic Science. Macmillan, 1932."
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
  - "Cagan, Marty. Inspired: How to Create Tech Products Customers Love, 2nd ed. Wiley, 2018."
---

# Everything as Product **

_When **Stream-Aligned Teams (8)** depend on internal capabilities and a **Platform Team (9)** exists to provide them, the question arises of how those internal capabilities should be managed over time._

---

**Internal services, platforms, and tools treated as "projects" — with end dates and no ongoing ownership — degrade over time, accumulate debt, and become burdens rather than enablers. The project metaphor creates orphaned software that no one is responsible for once the initial build is done.**

---

The project model assumes that software is finished when it is first delivered. A team is assembled, a budget is allocated, a deadline is set, and when the deadline passes the team disperses. But software is never finished. It must be operated, maintained, adapted to changing requirements, and eventually retired. When no one owns that lifecycle, the software rots. Users work around its deficiencies rather than requesting improvements, because there is no one to request them from.

The product metaphor corrects this by introducing three elements that the project metaphor lacks: a persistent owner, an explicit set of users, and a feedback loop. A product has someone accountable for its ongoing success. It has users whose needs must be understood and served. And it has mechanisms — usage metrics, support channels, roadmap discussions — through which those users can shape the product's evolution. Lionel Robbins's definition of economics as "the science which studies human behaviour as a relationship between ends and scarce means which have alternative uses" applies directly: product thinking forces prioritisation because it makes explicit that the team's capacity is finite and must be allocated among competing demands.

This applies not only to customer-facing software but to every internal capability: the CI/CD pipeline, the observability stack, the identity service, the developer portal. When these are treated as products, their quality improves because someone is accountable. When they are treated as projects, they are built once and left to decay. The effect compounds: a decaying platform degrades every team that depends on it, multiplying the cost across the organisation.

The practical challenge is that product thinking requires investment — a dedicated team, ongoing funding, and management attention. Organisations accustomed to the project model resist this because it looks like overhead. The counter-argument is that the overhead already exists; it is simply hidden in the friction, workarounds, and lost productivity that every team experiences when depending on unmaintained internal tools.

Therefore:

**Treat every internal capability — every service, platform, tool, and shared component — as a product with identified users, a dedicated owner, a roadmap, and a feedback loop. Fund it as an ongoing concern, not a one-off project. Measure its success by the success of the teams that depend on it.**

---

_This pattern is completed by **Platform as Product (37)**, which applies product thinking specifically to the internal developer platform, and by **API as Contract (18)**, which provides the mechanism through which product boundaries are expressed technically._

## References

- Robbins, Lionel. *An Essay on the Nature and Significance of Economic Science.* Macmillan, 1932.
- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- Cagan, Marty. *Inspired: How to Create Tech Products Customers Love*, 2nd ed. Wiley, 2018.
