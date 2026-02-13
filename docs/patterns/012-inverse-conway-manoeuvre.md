---
id: 12
name: "Inverse Conway Manoeuvre"
confidence: 1
scale: 2
context_patterns: [4, 7]
completion_patterns: [15, 8]
ai_dimension: false
tags: [conways-law, organisation, architecture, structure]
references:
  - "Conway, Melvin E. 'How Do Committees Invent?' Datamation, April 1968."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
  - "MacCormack, Alan, Baldwin, Carliss, and Rusnak, John. 'Exploring the Duality between Product and Organizational Architectures.' Research Policy 41.8 (2012): 1309-1324."
---

# Inverse Conway Manoeuvre *

_When the organisation has committed to **Explicit Tradeoffs (4)** and established **Value Stream Alignment (7)**, it can confront a deeper structural question: is the current team structure producing the architecture we actually want?_

---

**Conway's Law means that organisational structure produces system structure, whether or not that structure is desirable. If your teams are misaligned with the architecture you need, the architecture you get will be misaligned with your goals — and no amount of architectural aspiration will overcome the organisational reality.**

---

Melvin Conway observed in 1968 that "any organisation that designs a system will produce a design whose structure is a copy of the organisation's communication structure." This was not a recommendation; it was a diagnosis. Decades of empirical research have confirmed it. MacCormack, Baldwin, and Rusnak studied open-source and commercial software products and found strong correlations between organisational coupling and architectural coupling. The DORA research programme found that loosely coupled architectures — which require loosely coupled teams — are a predictor of high software delivery performance.

The naive response to Conway's Law is to ignore it: draw the ideal architecture on a whiteboard and instruct teams to build it. This fails because the communication patterns required to build a tightly integrated component will not emerge naturally across team boundaries. If two services must share data intimately, the teams that own them must communicate intimately — and if those teams are structurally separated, the integration will be awkward, delayed, or simply wrong.

The inverse Conway manoeuvre turns the law from a constraint into a tool. Instead of letting the existing organisational structure dictate the architecture, you deliberately design team boundaries to produce the architecture you want. If you want independent, loosely coupled services, you create independent, loosely coupled teams. If you want a unified platform, you create a unified platform team. The architecture follows.

This requires **Explicit Tradeoffs (4)** because reorganisation is not free. Moving people between teams disrupts relationships, destroys team-specific tacit knowledge, and creates a period of reduced productivity while new teams form. The architectural target must justify these real costs. It also requires honesty: if the organisation is unwilling to change its team structure, it should stop pretending it can change its architecture. The two are coupled, and wishing otherwise does not make it so.

Therefore:

**Deliberately design team boundaries to produce the system architecture you want, rather than allowing the existing organisational structure to dictate the architecture by default. Recognise that reorganisation has real costs and ensure the architectural target justifies them. When the desired architecture and the team structure are misaligned, change the teams — the architecture will follow.**

---

_The inverse Conway manoeuvre produces its effect through the boundaries it creates. **Service Domain Boundaries (15)** provides the principles for drawing those boundaries well. The teams that emerge from the manoeuvre should be **Stream-Aligned Teams (8)**, each with enough autonomy and bounded enough scope to own their part of the architecture end-to-end._

## References

- Conway, Melvin E. "How Do Committees Invent?" *Datamation*, April 1968.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- MacCormack, Alan, Baldwin, Carliss, and Rusnak, John. "Exploring the Duality between Product and Organizational Architectures: A Test of the Mirroring Hypothesis." *Research Policy* 41.8 (2012): 1309-1324.
