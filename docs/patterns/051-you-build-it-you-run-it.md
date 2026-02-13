---
id: 51
name: "You Build It, You Run It"
confidence: 2
scale: 8
context_patterns: [8, 7]
completion_patterns: [52, 54]
ai_dimension: false
tags: [ownership, operations, teams, accountability]
references:
  - "Hayek, F. A. 'The Use of Knowledge in Society.' American Economic Review 35.4 (1945): 519-530."
  - "Klein, G. Sources of Power: How People Make Decisions. MIT Press, 1999."
  - "Skelton, M. and Pais, M. Team Topologies. IT Revolution, 2019."
  - "Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. Site Reliability Engineering. O'Reilly, 2016."
---

# You Build It, You Run It **

_You have organised around **Stream-Aligned Teams (8)** within a broader **Value Stream Alignment (7)** structure. Teams own their services end-to-end from ideation to delivery. But does that ownership extend into production? If a separate operations team is paged at 3 a.m. when the service fails, the ownership model is incomplete._

---

**Handoffs between development and operations teams destroy context. The operators do not understand why the system was built this way; the developers do not see how it behaves in production. This gap is both an alignment failure — different teams with different incentives — and a comprehensibility failure — critical knowledge about the system split across organisational boundaries.**

---

Friedrich Hayek argued that the most relevant knowledge for any decision is local, particular, and difficult to communicate. The team that built a service understands its design decisions, its edge cases, its known weaknesses, and the compromises that were made under pressure. This knowledge is largely tacit — it lives in the heads of the builders and in the commit history they authored. Transferring this knowledge to a separate operations team through documentation, runbooks, and handoff meetings is an exercise in information loss. The operations team receives a fraction of the relevant context, and even that fraction decays over time as the service evolves.

Gary Klein's research on recognition-primed decision-making shows that experienced practitioners recognise patterns and make rapid, effective decisions in complex situations — but only in domains where they have deep experience. An operator who built the system has a mental model of its behaviour that enables recognition-primed diagnosis. An operator who received a handoff document has a checklist that may or may not match the failure mode they are facing.

The practical implication is that the team that builds the service should operate it. This is not about punishing developers with on-call duties. It is about closing the feedback loop: when the people who write the code also get paged when it fails, they experience the operational consequences of their design decisions. This creates a powerful incentive to write operable software — good instrumentation, graceful degradation, clear error messages, sensible defaults. Without this feedback loop, developers are insulated from the consequences of their choices, and operability becomes someone else's problem.

This does not mean that every team must become expert in infrastructure and operations from scratch. **Platform Team (9)** provides the shared operational platform that makes running services tractable. **Enabling Team (10)** can help build operational capability. But the responsibility for a service in production — the on-call rotation, the incident response, the understanding of its behaviour under load — belongs to the team that builds it.

Therefore:

**The team that builds a service operates it. Give stream-aligned teams full end-to-end ownership, including production operations, on-call responsibility, and incident response. Align incentives by ensuring that the people who make design decisions experience the operational consequences of those decisions. Support this ownership with platform capabilities so that teams are empowered to operate their services without needing to become infrastructure specialists.**

---

_This pattern is completed by **Alerting on Symptoms, Not Causes (52)**, which ensures that the on-call team receives actionable, user-focused alerts rather than a flood of low-level system noise. **Incident Response as Practice (54)** builds the rehearsed response capability that the owning team needs to handle incidents effectively._

## References

- Hayek, F. A. "The Use of Knowledge in Society." *American Economic Review* 35.4 (1945): 519-530.
- Klein, G. *Sources of Power: How People Make Decisions.* MIT Press, 1999.
- Skelton, M. and Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly, 2016.
