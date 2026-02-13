---
id: 44
name: "Threat Modelling as Practice"
confidence: 1
scale: 7
context_patterns: [41, 19]
completion_patterns: [46, 54]
ai_dimension: false
tags: [security, threat-modelling, risk, practice]
references:
  - "Shostack, A. Threat Modeling: Designing for Security. Wiley, 2014."
  - "Klein, G. Sources of Power: How People Make Decisions. MIT Press, 1998."
  - "Polanyi, M. The Tacit Dimension. University of Chicago Press, 1966."
---

# Threat Modelling as Practice *

_You have committed to **Security as Shared Responsibility (41)**, which means development teams — not just the security team — must think about threats in their domain. You practise **Hypothesis-Driven Development (19)**, which means you are accustomed to making assumptions explicit and testing them. Now the question is how teams systematically reason about the threats their systems face._

---

**Annual threat modelling exercises are compliance theatre — too infrequent to remain relevant as the system evolves, too heavyweight to integrate into the rhythm of development. But abandoning structured threat analysis entirely means risks are discovered only when they are exploited in production.**

---

The word "practice" in the pattern name is deliberate. Threat modelling is not an event or a document — it is a recurring practice, like code review or retrospectives. Adam Shostack, who led threat modelling at Microsoft, emphasises that the value comes from the conversation, not the artefact. A threat model document that sits in a wiki and is never updated is worthless. A thirty-minute conversation in which a team sketches its system's trust boundaries, asks "what could go wrong?", and identifies the top three risks is immensely valuable — even if it produces nothing more than a whiteboard photo and three backlog items.

The structure matters, but lightly. Frameworks like STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) provide a checklist that ensures teams consider categories of threat they might otherwise overlook. The checklist is deterministic — it is the same every time. But identifying which threats are relevant, how likely they are, and what to do about them requires human creativity and domain knowledge. Gary Klein's research on recognition-primed decision-making shows that experienced practitioners do not reason about threats analytically — they recognise patterns from prior experience and then verify their intuition through deliberate analysis. The structured framework elicits this tacit knowledge by giving it categories to attach to.

Michael Polanyi's observation that "we know more than we can tell" applies directly. A developer who has been working on a service for months has an intuitive sense of where the fragile points are, which data flows feel risky, and which assumptions are most likely to break. This knowledge is tacit — it is not written down anywhere and the developer may not be able to articulate it unprompted. A structured threat modelling practice draws this knowledge out by asking specific questions in a safe setting. The generative culture that **Security as Shared Responsibility (41)** depends on is what makes the setting safe: no one is punished for identifying a risk that should have been caught earlier.

The cadence should match the development rhythm. A lightweight threat model at the start of significant new work, revisited when the architecture changes, and referenced during incident reviews. Not a quarterly ceremony, not an annual audit, but an ongoing practice as natural as writing tests.

Therefore:

**Practise threat modelling regularly and lightly — integrated into the development rhythm rather than performed as an annual ceremony. Use structured frameworks like STRIDE to ensure completeness, but keep sessions short and focused on conversation, not documentation. Capture outcomes as actionable backlog items, not shelf-ware reports. Revisit the threat model whenever the system's architecture or trust boundaries change.**

---

_This pattern is completed by **Blast Radius Limitation (46)**, which provides the design principles that threat modelling identifies as necessary — containment, least privilege, and isolation. **Incident Response as Practice (54)** closes the loop: when the threats that were modelled (or missed) materialise, the incident response practice provides the structured response, and the lessons feed back into the next threat modelling session._

## References

- Shostack, A. *Threat Modeling: Designing for Security.* Wiley, 2014.
- Klein, G. *Sources of Power: How People Make Decisions.* MIT Press, 1998.
- Polanyi, M. *The Tacit Dimension.* University of Chicago Press, 1966.
