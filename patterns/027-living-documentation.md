---
id: 27
name: "Living Documentation"
confidence: 1
scale: 4
context_patterns: [21, 13]
completion_patterns: [18, 48]
ai_dimension: false
tags: [documentation, architecture-decision-records, api-specs, comprehensibility]
references:
  - "Brooks, F. P. 'No Silver Bullet: Essence and Accidents of Software Engineering.' *Computer* 20(4), 1987."
  - "Simon, H. A. *The Sciences of the Artificial.* MIT Press, 1969."
  - "Nygard, M. 'Documenting Architecture Decisions.' cognitect.com, 2011."
  - "Martraire, C. *Living Documentation: Continuous Knowledge Sharing by Design.* Addison-Wesley, 2019."
---

# Living Documentation *

_You have adopted **Version Control Everything (21)** so that all artefacts are tracked and recoverable, and your **Communities of Practice (13)** create channels for knowledge to flow across teams. The question remains: how do you make the system comprehensible to those who did not build it?_

---

**Documentation that is separate from the system it describes drifts out of sync — deterministic in form (written once, stored in a wiki) but unreliable in practice (never updated). Undocumented systems are comprehensible only to those who built them, and that comprehension erodes with time and turnover.**

---

Brooks identified the essential difficulty of software as its invisibility: unlike a building or a circuit, software has no natural geometric representation that the eye can grasp. You cannot look at a running system and see its structure. Documentation is the traditional remedy — write down what the system does and how it is organised. But traditional documentation suffers from a fatal flaw: it is a separate artefact, maintained by separate effort, with no automatic connection to the system it describes. The moment the system changes and the documentation does not, the documentation becomes a lie that looks like the truth.

Simon's concept of near-decomposability suggests a path forward. A well-structured system can be understood at multiple levels of abstraction, with each level largely independent. Documentation should mirror this structure — not as a separate monolith, but as small, focused artefacts that live alongside the code they describe and are verified against the system they document.

The concrete forms are well established. Tests serve as executable specifications of behaviour: a well-written test suite tells you what the system does more reliably than any prose description. Architecture decision records (ADRs), versioned alongside the code, capture not just what was decided but why — the context and trade-offs that shaped the design. API specifications generated from implementations (or verified against them) ensure that the contract between services is always accurate. README files that are checked by CI remain current because a failing check forces an update.

The key insight is that documentation should be adaptive — it changes with the system — while remaining deterministic in a different sense: it is provably accurate because it is generated from or verified against the running system. This is the opposite of traditional documentation, which is deterministic in form (written once) but adaptive in the worst sense (it decays silently).

Therefore:

**Generate documentation from or verify it against the running system. Use tests as executable specifications of behaviour, architecture decision records versioned with code to capture design rationale, and API specs generated from implementations. Documentation that cannot drift out of sync does not need to be separately maintained — it is a living property of the system itself.**

---

_Living documentation supports **API as Contract (18)** by ensuring that service interfaces are always accurately described, and feeds into **Observability Over Monitoring (48)** by making the system's intended behaviour explicit and comparable to its actual behaviour._

## References

- Brooks, F. P. "No Silver Bullet: Essence and Accidents of Software Engineering." *Computer* 20(4), 1987.
- Simon, H. A. *The Sciences of the Artificial.* MIT Press, 1969.
- Nygard, M. "Documenting Architecture Decisions." cognitect.com, 2011.
- Martraire, C. *Living Documentation: Continuous Knowledge Sharing by Design.* Addison-Wesley, 2019.
