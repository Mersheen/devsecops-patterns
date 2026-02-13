---
id: 18
name: "API as Contract"
confidence: 1
scale: 3
context_patterns: [14, 15]
completion_patterns: [38, 39]
ai_dimension: false
tags: [api, contract, coupling, autonomy, interface]
references:
  - "Simon, Herbert A. 'The Architecture of Complexity.' Proceedings of the American Philosophical Society 106.6 (1962): 467-482."
  - "Hayek, Friedrich A. 'The Use of Knowledge in Society.' American Economic Review 35.4 (1945): 519-530."
  - "Parnas, David L. 'On the Criteria To Be Used in Decomposing Systems into Modules.' Communications of the ACM 15.12 (1972): 1053-1058."
  - "Fielding, Roy T. 'Architectural Styles and the Design of Network-based Software Architectures.' PhD dissertation, University of California, Irvine, 2000."
---

# API as Contract *

_When internal capabilities are managed as products through **Everything as Product (14)** and the system has been decomposed along **Service Domain Boundaries (15)**, the question arises of how teams interact across those boundaries without creating tight coupling._

---

**Without stable interfaces, autonomous teams cannot evolve independently — every change risks breaking consumers. With overly rigid interfaces, adaptation is stifled and the architecture calcifies. The challenge is to provide enough stability for independence while retaining enough flexibility for evolution.**

---

Herbert Simon's near-decomposability provides the theoretical foundation: in a well-designed complex system, the interactions between subsystems are weaker than the interactions within them. APIs are the mechanism through which this property is realised in software. The API defines the "weak interaction" — a narrow, stable surface across which two subsystems communicate. Everything behind the API is autonomous; the owning team can refactor, rewrite, or re-platform without affecting consumers, provided the contract is honoured.

Friedrich Hayek's analysis of the price system illuminates a deeper parallel. In a market economy, prices serve as a signalling mechanism that coordinates the behaviour of millions of independent actors without requiring any central authority to understand the whole. APIs serve the same function in a software ecosystem. A well-designed API tells consumers what a service can do, what it expects, and what it promises — without requiring consumers to understand how the service works internally. This is information hiding at the organisational scale, and it is what makes large-scale software development with autonomous teams possible.

David Parnas made the case for information hiding in 1972: modules should be designed to hide design decisions that are likely to change. APIs operationalise this principle across service boundaries. The contract — the set of endpoints, data shapes, error codes, and performance guarantees — is the stable part. The implementation behind it is the changeable part. When this separation is maintained, teams can deploy independently, which is the single most important enabler of delivery speed in a distributed system.

The practical challenges are versioning and evolution. A contract that can never change is a contract that eventually becomes a liability. Effective API management requires explicit versioning policies, deprecation timelines, and consumer-driven contract testing. Treating APIs as products — with users, feedback loops, and roadmaps — ensures that these concerns are managed proactively rather than discovered in production when a breaking change is deployed.

Therefore:

**Treat APIs as the unit of organisational coupling. Define explicit contracts with clear versioning and deprecation policies. Invest in consumer-driven contract testing to ensure that changes do not break consumers. Allow teams full autonomy behind the contract while holding the contract itself to product-level standards of reliability and evolution.**

---

_APIs connect services deployed as **Containerised Workloads (38)**, and a **Service Mesh (39)** provides the infrastructure-level mechanisms for managing cross-service communication, security, and observability at the API layer._

## References

- Simon, Herbert A. "The Architecture of Complexity." *Proceedings of the American Philosophical Society* 106.6 (1962): 467-482.
- Hayek, Friedrich A. "The Use of Knowledge in Society." *American Economic Review* 35.4 (1945): 519-530.
- Parnas, David L. "On the Criteria To Be Used in Decomposing Systems into Modules." *Communications of the ACM* 15.12 (1972): 1053-1058.
- Fielding, Roy T. "Architectural Styles and the Design of Network-based Software Architectures." PhD dissertation, University of California, Irvine, 2000.
