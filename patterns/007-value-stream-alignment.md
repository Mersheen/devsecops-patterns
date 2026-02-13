---
id: 7
name: "Value Stream Alignment"
confidence: 2
scale: 2
context_patterns: [1, 3]
completion_patterns: [8, 14, 15]
ai_dimension: false
tags: [value-stream, organisation, flow, alignment]
references:
  - "Deming, W. Edwards. The New Economics for Industry, Government, Education. MIT Press, 1993."
  - "Chandler, Alfred D. Strategy and Structure. MIT Press, 1962."
  - "Womack, James P. and Jones, Daniel T. Lean Thinking. Free Press, 2003."
  - "Skelton, Matthew and Pais, Manuel. Team Topologies. IT Revolution, 2019."
---

# Value Stream Alignment **

_When an organisation has established a **Generative Culture (1)** and committed to **Flow Over Utilisation (3)**, it must decide how to structure itself so that effort is directed toward outcomes that matter._

---

**Functional silos — development, operations, QA, security — optimise locally, creating handoffs that destroy flow and misalign effort with customer value. Each silo pursues its own efficiency while the end-to-end delivery of value suffers.**

---

W. Edwards Deming warned that "left to themselves, components become selfish, competitive, independent profit centres, and thus destroy the system." This observation, from Chapter 3 of *The New Economics*, captures the central failure mode of functionally organised software organisations. When developers are measured on features shipped, operations on uptime, and security on vulnerabilities found, no one is accountable for the speed, safety, and quality of the whole flow from idea to running software.

Alfred Chandler demonstrated that structure follows strategy — or, more precisely, that an organisation's structure must be aligned with what it is trying to achieve. If the strategy is to deliver value to customers quickly and safely, then the structure must be optimised for that flow, not for the accumulation of specialist expertise in departmental silos. Lean value stream mapping makes this concrete: trace the path a unit of work takes from concept to cash, and you will find that most of the elapsed time is spent waiting in queues between functional handoffs, not in value-adding activity.

The practical consequence is that organising around value streams — end-to-end paths from idea to running software — collapses those queues. A value stream contains all the capabilities needed to deliver: development, testing, deployment, operations, and security. This does not mean every person in the stream is a generalist; it means the stream has access to all the specialisms it needs without waiting for another department's prioritisation cycle.

The difficulty lies in identifying the right value streams. Too few, and each stream is so broad that coordination within it recreates the silo problem at a smaller scale. Too many, and the organisation fragments into teams too small to be effective, with excessive inter-stream dependencies. The boundaries should follow the natural contours of the business domain, not the historical accident of how departments were formed. This is a design problem that requires **Explicit Tradeoffs (4)** and ongoing adjustment.

Therefore:

**Organise around the flow of value to the customer, not around technical specialisms. Identify the end-to-end value streams — the paths from idea to running software — and ensure each stream has the capabilities it needs to deliver without structural handoffs. Revisit stream boundaries as the business and its domains evolve.**

---

_Within each value stream, **Stream-Aligned Teams (8)** provide the primary unit of delivery. The streams produce and operate services that should be treated as products in their own right — see **Everything as Product (14)**. The boundaries between streams correspond to **Service Domain Boundaries (15)**, which must be drawn with care to minimise cross-stream coupling._

## References

- Deming, W. Edwards. *The New Economics for Industry, Government, Education.* MIT Press, 1993.
- Chandler, Alfred D. *Strategy and Structure: Chapters in the History of the American Industrial Enterprise.* MIT Press, 1962.
- Womack, James P. and Jones, Daniel T. *Lean Thinking: Banish Waste and Create Wealth in Your Corporation.* Free Press, 2003.
- Skelton, Matthew and Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
