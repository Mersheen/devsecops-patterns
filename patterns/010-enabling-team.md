---
id: 10
name: "Enabling Team"
confidence: 1
scale: 2
context_patterns: [2, 7]
completion_patterns: [24, 27]
ai_dimension: false
tags: [teams, learning, tacit-knowledge, capability]
references:
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
  - "Polanyi, Michael. The Tacit Dimension. University of Chicago Press, 1966."
  - "Klein, Gary. Sources of Power: How People Make Decisions. MIT Press, 1998."
  - "Nonaka, Ikujiro and Takeuchi, Hirotaka. The Knowledge-Creating Company. Oxford University Press, 1995."
---

# Enabling Team *

_When an organisation operates as a **Learning Organisation (2)** and has structured itself around **Value Stream Alignment (7)**, it faces a persistent challenge: how to spread new capabilities across autonomous teams without creating dependencies or bottlenecks._

---

**Deterministic knowledge transfer — documentation, standards documents, recorded presentations — fails for tacit knowledge. New capabilities, including AI adoption, observability practices, and security techniques, require hands-on, contextual learning that cannot be reduced to a wiki page.**

---

Michael Polanyi articulated the problem precisely: "we can know more than we can tell." A developer who has internalised test-driven development, or an SRE who can read a dashboard and immediately sense that something is wrong, possesses knowledge that resists codification. Written guides capture the explicit component — the steps, the syntax, the configuration — but not the judgement, the timing, or the feel for when a practice is being applied well versus mechanically.

This is where enabling teams earn their place in the organisational structure. An enabling team temporarily embeds with a stream-aligned team to help it acquire a new capability. The enabling team does not do the work for the stream team; it works alongside the stream team, pairing on real problems in the stream team's actual codebase and production environment. The knowledge transfer happens through practice, not presentation. Gary Klein's research on recognition-primed decision-making supports this approach: expertise is built through exposure to varied situations with feedback, not through abstract instruction.

The critical word is "temporarily." An enabling team that permanently embeds with a stream team has become a dependency, not an enabler. The interaction follows a pattern: the enabling team assesses the gap, embeds for a bounded period (typically weeks, not months), transfers the capability through joint work, and then withdraws. The stream team should be self-sufficient in the new capability after the engagement. If it is not, either the capability is too complex for the stream team's cognitive load — suggesting a **Complicated Subsystem Team (11)** is needed instead — or the engagement was too short.

Enabling teams are the organisation's adaptive learning mechanism. When a new technology arrives, when a security practice must be adopted, when AI-assisted development tools need to be integrated into workflows, the enabling team is how the organisation spreads that capability without mandating it from above or leaving each team to figure it out alone. They complement the deterministic knowledge captured in **Living Documentation (27)** with the tacit, contextual knowledge that documentation cannot convey.

Therefore:

**Create enabling teams that temporarily embed with stream-aligned teams to help them acquire new capabilities. The enabling team works alongside the stream team on real problems, transfers knowledge through practice, and then withdraws. Measure success by whether the stream team is self-sufficient after the engagement, not by the number of engagements completed.**

---

_Enabling teams are particularly valuable when stream-aligned teams are adopting **AI-Assisted Development (24)** practices, where the gap between using a tool and using it well is large. The explicit knowledge that enabling teams help create should be captured in **Living Documentation (27)** for future reference, even though the documentation alone would not have been sufficient for the initial learning._

## References

- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- Polanyi, Michael. *The Tacit Dimension.* University of Chicago Press, 1966.
- Klein, Gary. *Sources of Power: How People Make Decisions.* MIT Press, 1998.
- Nonaka, Ikujiro and Takeuchi, Hirotaka. *The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation.* Oxford University Press, 1995.
