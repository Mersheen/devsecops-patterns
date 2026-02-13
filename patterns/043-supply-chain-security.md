---
id: 43
name: "Supply Chain Security"
confidence: 1
scale: 7
context_patterns: [42, 28]
completion_patterns: [47, 29]
ai_dimension: true
tags: [security, supply-chain, dependencies, sbom, provenance]
references:
  - "SLSA Framework. Supply-chain Levels for Software Artifacts. https://slsa.dev."
  - "Wheeler, D. A. 'Countering Trusting Trust through Diverse Double-Compiling.' ACSAC 2005."
  - "Ohm, M. et al. 'Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks.' DIMVA 2020."
---

# Supply Chain Security *

_You enforce organisational policies automatically through **Policy as Code (42)** and your changes flow through a **Deployment Pipeline (28)**. But the policies and pipeline verify code your organisation wrote. The vast majority of code running in production was written by strangers — the open source libraries, container base images, and transitive dependencies your software depends on._

---

**Modern software depends on thousands of transitive dependencies, any one of which can be compromised. The scope of the supply chain exceeds any human's ability to audit manually, and a single compromised dependency — a malicious package update, a hijacked maintainer account, a trojanised base image — can compromise the entire system.**

---

Ken Thompson's 1984 Turing Award lecture, "Reflections on Trusting Trust," demonstrated that you cannot fully trust code you did not write yourself — and even then, you must trust the compiler. This was a theoretical observation for decades. It became an operational reality with the SolarWinds breach in 2020, the event-stream npm incident in 2018, and the steady drumbeat of dependency confusion and typosquatting attacks that followed. The supply chain is now a primary attack vector, and it is one that traditional perimeter-based security completely ignores.

The challenge is one of scope versus comprehensibility. A typical web application has hundreds of direct dependencies and thousands of transitive ones. No team can audit them all manually, and even automated scanning struggles with the volume. The response must be layered: generate Software Bills of Materials (SBOMs) so that you know what you depend on, sign artefacts and verify provenance so that you know where they came from, scan dependencies for known vulnerabilities so that you know what risks you carry, and pin or lock dependency versions so that updates are deliberate rather than automatic. Frameworks like SLSA (Supply-chain Levels for Software Artifacts) provide a graduated maturity model for these practices.

AI introduces a new dimension to supply chain risk. AI model supply chains carry the same vulnerabilities as software supply chains — and some novel ones. Model provenance (who trained this model, on what data, with what objectives?) is the AI equivalent of package provenance. Training data integrity (was the training data poisoned?) parallels dependency integrity. And dependency on third-party model APIs introduces a supply chain risk that is both operational (the API changes or disappears) and security-related (the model's behaviour is outside your control). Organisations that consume AI models — whether open-weight models or API-based services — need the same rigour around model provenance and integrity that they apply to software dependencies.

The most common failure mode is treating supply chain security as a one-time audit rather than a continuous practice. Dependencies change constantly — new vulnerabilities are discovered, maintainers change, packages are deprecated or hijacked. Supply chain security must be woven into the pipeline, not performed as a quarterly exercise.

Therefore:

**Make the software supply chain visible and verifiable. Generate SBOMs for every build. Sign artefacts and verify their provenance. Scan dependencies continuously for known vulnerabilities. Pin dependency versions and treat updates as deliberate, reviewed changes. Apply the same rigour to AI model supply chains — verify model provenance, audit training data integrity, and treat third-party model APIs as dependencies with security implications.**

---

_This pattern is completed by **Secure AI Integration (47)**, which addresses the specific security challenges of AI systems that supply chain security surfaces but does not fully resolve. **Build Once, Deploy Many (29)** ensures that the artefact you verified is the same artefact that reaches production — provenance verification is meaningless if the artefact is rebuilt between environments._

## References

- SLSA Framework. *Supply-chain Levels for Software Artifacts.* https://slsa.dev.
- Wheeler, D. A. "Countering Trusting Trust through Diverse Double-Compiling." *ACSAC 2005.*
- Ohm, M. et al. "Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks." *DIMVA 2020.*
- Thompson, K. "Reflections on Trusting Trust." *Communications of the ACM* 27.8 (1984): 761-763.
