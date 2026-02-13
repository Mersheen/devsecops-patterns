---
id: 48
name: "Observability Over Monitoring"
confidence: 2
scale: 8
context_patterns: [37, 28]
completion_patterns: [52, 56]
ai_dimension: false
tags: [observability, telemetry, tracing, instrumentation]
references:
  - "Ashby, W. R. An Introduction to Cybernetics. Chapman & Hall, 1956."
  - "Hollnagel, E. Safety-II in Practice. Routledge, 2018."
  - "Majors, C., Fong-Jones, L., and Miranda, G. Observability Engineering. O'Reilly, 2022."
  - "Sridharan, C. Distributed Systems Observability. O'Reilly, 2018."
---

# Observability Over Monitoring **

_You have built a **Platform as Product (37)** and changes flow through a **Deployment Pipeline (28)** into production. The question now is how you understand what those systems are doing once they are running._

---

**Traditional monitoring — predefined dashboards, threshold-based alerts, static health checks — is deterministic: it watches for known failure modes. But distributed systems fail in novel ways. Monitoring that only checks for anticipated problems misses the unknown-unknowns, and these are precisely the failures that cause the worst outages.**

---

The distinction between monitoring and observability is not a branding exercise. Monitoring asks "is this thing I already know about still working?" Observability asks "what is happening, and why?" Monitoring is a closed-ended query against a predefined model of system health. Observability is an open-ended investigation capability that allows an operator to ask questions that were not anticipated when the instrumentation was designed.

This distinction matters because complex distributed systems exhibit emergent behaviour. A microservices architecture with dozens of services, multiple data stores, asynchronous message queues, and external dependencies has a state space so large that no finite set of predefined checks can cover it. The failures you will encounter next month are almost certainly not the failures you encountered last month. This is Ashby's Law of Requisite Variety applied to operations: your observation system must have at least as much variety as your system's failure modes. A static dashboard does not meet this requirement. A system that emits structured events with high-cardinality fields — and that can be queried interactively, in real time, against those fields — does.

The practical implication is a shift in instrumentation strategy. Rather than asking "what metrics should we track?" the question becomes "what structured events should we emit so that any future question can be answered?" Distributed tracing, structured logging with rich context, and high-cardinality event stores become the foundational layer. Dashboards and alerts are still valuable, but they are views on the data, not the data itself. They are a starting point for investigation, not a substitute for it.

Erik Hollnagel's Safety-II framework reinforces this shift. Safety-I asks "what went wrong?" and tries to prevent recurrence. Safety-II asks "what goes right?" and tries to understand normal performance variability. An observability-first approach supports both: the same instrumentation that helps you diagnose an outage also lets you understand why the system performs well on most days, which is far more informative for improving reliability than studying failures alone.

Therefore:

**Instrument systems for exploratory investigation, not just predefined checks. Emit structured events with high-cardinality fields. Deploy distributed tracing across service boundaries. Store telemetry in a form that supports ad hoc querying. Treat dashboards and alerts as useful views on the data, not as the observation system itself. The goal is to be able to answer questions about system behaviour that you did not think to ask in advance.**

---

_This pattern is completed by two more specific practices. **Alerting on Symptoms, Not Causes (52)** applies the observability principle to the alerting layer — ensuring that alerts communicate user-visible impact rather than low-level system events. **AI-Augmented Observability (56)** extends the pattern by using AI to process telemetry volumes that exceed human capacity, while maintaining the interpretability that observability requires._

## References

- Ashby, W. R. *An Introduction to Cybernetics.* Chapman & Hall, 1956.
- Hollnagel, E. *Safety-II in Practice: Developing the Resilience Potentials.* Routledge, 2018.
- Majors, C., Fong-Jones, L., and Miranda, G. *Observability Engineering.* O'Reilly, 2022.
- Sridharan, C. *Distributed Systems Observability.* O'Reilly, 2018.
