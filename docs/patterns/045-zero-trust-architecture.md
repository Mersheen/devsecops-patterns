---
id: 45
name: "Zero Trust Architecture"
confidence: 1
scale: 7
context_patterns: [5, 36]
completion_patterns: [46, 55]
ai_dimension: false
tags: [security, zero-trust, authentication, network]
references:
  - "Rose, S. et al. Zero Trust Architecture. NIST SP 800-207, 2020."
  - "Ward, R. and Beyer, B. 'BeyondCorp: A New Approach to Enterprise Security.' ;login: 39.6 (2014)."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Zero Trust Architecture *

_You practise **Trust and Verify (5)** at the organisational level — trusting people and verifying through systems. Your infrastructure is defined and deployed as **Immutable Infrastructure (36)**, giving you a known, reproducible substrate. Now the question arises: what trust model should the network itself use?_

---

**Perimeter-based security assumes that the internal network is safe — that anything inside the firewall can be trusted. This deterministic assumption fails catastrophically when the perimeter is breached: an attacker who gains access to one internal system can move laterally to every other system, because the network trusts everything inside the wall.**

---

Google's BeyondCorp programme, published in 2014, demonstrated that a major technology company could operate without a privileged internal network. Every request — whether originating from the corporate office or a coffee shop — is authenticated and authorised based on the identity of the user and the state of the device, not the network location. The NIST Zero Trust Architecture framework (SP 800-207) formalised this approach: never trust, always verify; assume the network is hostile; enforce access control at the application layer.

The philosophical relationship between organisational **Trust and Verify (5)** and network Zero Trust Architecture is inverse and complementary. At the organisational level, we trust people — we assume competence and good intent, and we build transparent verification systems that catch honest mistakes. At the network level, we trust nothing — we assume that any request could be malicious, and we require every request to prove its identity and authorisation. These are not contradictory positions. Trusting people and not trusting network traffic are perfectly consistent: people operate through systems, and the systems must verify that the person behind the request is who they claim to be and is authorised to do what they are asking.

The practical implementation involves several reinforcing practices: strong identity for every service and user (mutual TLS, service mesh identity, short-lived tokens rather than long-lived credentials), fine-grained authorisation (not just "is this user authenticated?" but "is this user authorised to perform this specific action on this specific resource?"), continuous verification (session validity is re-evaluated, not assumed), and encryption of all traffic regardless of network location. **Immutable Infrastructure (36)** supports this by ensuring that the infrastructure itself is known and verifiable — you cannot implement zero trust on infrastructure whose state is uncertain.

The most common failure mode is treating zero trust as a product to purchase rather than an architecture to implement. No single tool delivers zero trust. It is a design philosophy that must be woven into service communication, identity management, authorisation policy, and network architecture. The second failure mode is implementing zero trust so aggressively that developer productivity collapses — every action requiring multiple authentication steps, every service call adding latency. The implementation must be invisible to developers in the common case, surfacing only when something genuinely anomalous occurs.

Therefore:

**Authenticate and authorise every request, regardless of network location. Implement strong identity for all services and users, enforce fine-grained authorisation at the application layer, and encrypt all traffic. Design the system so that a breach of any single component does not grant access to other components. Make zero trust the default network posture — invisible in normal operation, impassable to lateral movement.**

---

_This pattern is completed by **Blast Radius Limitation (46)**, which provides the containment principles that zero trust enables — least privilege, network segmentation, and service isolation ensure that even an authenticated, authorised request cannot do more damage than its scope permits. **Graceful Degradation (55)** addresses the operational question of what happens when zero trust verification systems themselves experience failures — the system must degrade safely rather than either failing open (insecure) or failing closed (unavailable)._

## References

- Rose, S. et al. *Zero Trust Architecture.* NIST SP 800-207, 2020.
- Ward, R. and Beyer, B. "BeyondCorp: A New Approach to Enterprise Security." *;login:* 39.6 (2014).
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
