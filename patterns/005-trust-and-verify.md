---
id: 5
name: "Trust and Verify"
confidence: 1
scale: 1
context_patterns: [1]
completion_patterns: [8, 42, 45]
ai_dimension: false
tags: [trust, autonomy, governance, verification]
references:
  - "Locke, J. Two Treatises of Government, ed. Peter Laslett. Cambridge University Press, 1988 [1689]."
  - "Berlin, I. 'Two Concepts of Liberty.' In Four Essays on Liberty. Oxford University Press, 1969."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Trust and Verify *

_When a **Generative Culture (1)** has established psychological safety and information flows freely, the organisation faces a governance question: how much autonomy should teams have, and how should the organisation assure itself that autonomy is being used well?_

---

**Organisations oscillate between two failure modes. Naive trust — few controls, broad permissions, minimal oversight — leaves the organisation vulnerable to errors and breaches. Paranoid control — everything locked down, every change gated by a review board — destroys speed and demoralises the people closest to the work. Neither extreme is stable.**

---

John Locke argued that legitimate authority is constrained authority — government is justified only insofar as it protects the rights and freedoms of those it governs. Applied to organisations, this means that governance mechanisms are legitimate only insofar as they enable teams to do good work safely. A change approval board that adds three days of latency to every deployment is not governance — it is friction masquerading as control, and the DORA research consistently shows that such heavyweight approval processes correlate with worse outcomes, not better ones.

Isaiah Berlin's distinction between negative liberty (freedom from interference) and positive liberty (freedom to achieve) illuminates the balance this pattern seeks. Teams need negative liberty — freedom from unnecessary bureaucratic interference — to move quickly and respond to their context. But they also need the organisational structures that make positive liberty possible: clear standards, automated guardrails, and transparent verification that catches problems without blocking flow.

The resolution is to default to trusting people and teams while verifying through automated, transparent systems. Trust means giving teams deployment authority, technology choice within guardrails, and the autonomy to decide how to solve the problems they are closest to. Verify means building automated systems — policy checks, security scans, compliance audits, observability — that provide continuous assurance without requiring human gatekeepers in the critical path. The verification must be transparent: teams should be able to see what is being checked, why, and what the results are. Opaque verification destroys the trust it claims to support.

This pattern is distinct from "zero trust" as a network architecture concept (which appears at Scale 7 as **Zero Trust Architecture (45)**). Zero trust the network principle assumes the network is hostile and verifies every request. Trust and verify the organisational principle assumes people are competent and well-intentioned, and builds systems that catch honest mistakes and surface risks without treating every engineer as a potential threat.

Therefore:

**Default to trusting people and teams. Verify through automated, transparent systems that provide continuous assurance without blocking flow. Build governance that enables speed and safety simultaneously, rather than trading one for the other.**

---

_This philosophy takes concrete form at several scales. **Stream-Aligned Teams (8)** require the trust to own their domain end-to-end. **Policy as Code (42)** automates the verification side — encoding organisational standards as machine-enforceable rules rather than manual review gates. **Zero Trust Architecture (45)** applies the complementary network-level principle, ensuring that infrastructure verification does not depend on perimeter trust._

## References

- Locke, J. *Two Treatises of Government*, ed. Peter Laslett. Cambridge University Press, 1988 [1689].
- Berlin, I. "Two Concepts of Liberty." In *Four Essays on Liberty.* Oxford University Press, 1969.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
