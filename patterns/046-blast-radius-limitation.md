---
id: 46
name: "Blast Radius Limitation"
confidence: 1
scale: 7
context_patterns: [15, 45]
completion_patterns: [55, 54]
ai_dimension: false
tags: [security, containment, isolation, resilience]
references:
  - "Perrow, C. Normal Accidents: Living with High-Risk Technologies. Princeton University Press, 1999 [1984]."
  - "Simon, H. A. 'The Architecture of Complexity.' Proceedings of the American Philosophical Society 106.6 (1962): 467-482."
  - "Nygard, M. Release It!, 2nd ed. Pragmatic Bookshelf, 2018."
---

# Blast Radius Limitation *

_You have defined clear **Service Domain Boundaries (15)** that decompose the system into comprehensible parts. You are implementing **Zero Trust Architecture (45)**, which means no component automatically trusts any other. Now the question is how to ensure that when something goes wrong — a breach, a bug, a failure — the damage stays contained._

---

**A breach or failure that can propagate to the entire system is catastrophic. The larger the blast radius, the more damage is done, the longer recovery takes, and the harder the failure is to comprehend. Systems that lack containment boundaries turn every incident into a potential total-system event.**

---

Charles Perrow's study of "normal accidents" in complex systems identified tight coupling as the key factor that turns small failures into large disasters. In a tightly coupled system, a failure in one component immediately propagates to dependent components, which propagate to their dependents, in a cascade that outpaces any human ability to intervene. The Three Mile Island accident, Perrow's central case, was not caused by a single catastrophic failure but by a series of small failures in a tightly coupled system, each one triggering the next before operators could understand what was happening.

Herbert Simon's concept of near-decomposability provides the architectural response. A near-decomposable system is one in which components interact strongly within boundaries and weakly across them. This means that a failure within one component stays mostly within that component — it may degrade the service that component provides, but it does not cascade into an uncontrollable system-wide failure. The interactions across boundaries are weak enough that there is time to detect, understand, and respond before the damage spreads.

The practical techniques are well understood: least privilege (every component has only the permissions it needs, so a compromised component can only do what that component was authorised to do), network segmentation (components can only communicate with the specific other components they need to reach), service isolation (a failure in one service does not exhaust shared resources like connection pools or thread pools), and bulkheads (borrowed from ship design — compartments that can flood independently without sinking the vessel). Michael Nygard's stability patterns — bulkheads, circuit breakers, timeouts — are the implementation mechanisms.

Every boundary serves a dual purpose: it limits the scope of damage and it limits the scope of investigation. When an incident occurs in a system with strong containment boundaries, the team can immediately narrow the investigation to the affected component. In a system without boundaries, every incident requires investigating everything, because everything might be involved. Containment makes incidents not just less damaging but more comprehensible — and comprehensibility is what enables fast recovery.

Therefore:

**Design for containment at every level. Apply least privilege so that no component has more authority than it needs. Segment networks so that components can only reach what they must. Isolate services so that failures do not cascade through shared resources. Treat every boundary as both a damage limitation mechanism and an investigation aid. The goal is not to prevent all failures — that is impossible — but to ensure that every failure is a small failure.**

---

_This pattern is completed by **Graceful Degradation (55)**, which addresses how the system behaves when a contained failure reduces capacity — the system should continue to provide reduced service rather than failing entirely. **Incident Response as Practice (54)** provides the human process that operates within the boundaries this pattern creates: when the blast radius has been limited, the incident response team can focus on the affected area rather than scrambling across the entire system._

## References

- Perrow, C. *Normal Accidents: Living with High-Risk Technologies.* Princeton University Press, 1999 [1984].
- Simon, H. A. "The Architecture of Complexity." *Proceedings of the American Philosophical Society* 106.6 (1962): 467-482.
- Nygard, M. *Release It!: Design and Deploy Production-Ready Software*, 2nd ed. Pragmatic Bookshelf, 2018.
