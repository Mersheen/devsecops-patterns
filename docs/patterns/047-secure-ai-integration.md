---
id: 47
name: "Secure AI Integration"
confidence: 0
scale: 7
context_patterns: [24, 42, 43]
completion_patterns: [56, 48]
ai_dimension: true
tags: [security, ai, guardrails, prompt-injection]
references:
  - "Bainbridge, L. 'Ironies of Automation.' Automatica 19.6 (1983): 775-779."
  - "OWASP. Top 10 for Large Language Model Applications. 2023."
  - "Greshake, K. et al. 'Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.' AISec 2023."
---

# Secure AI Integration

_You have adopted **AI-Assisted Development (24)** and your teams use AI systems in development and operations. You enforce security policies through **Policy as Code (42)** and verify the provenance of your dependencies through **Supply Chain Security (43)**. But AI systems introduce a novel security surface that existing patterns do not fully address._

---

**AI systems are neither fully deterministic — their outputs are not predictable from their inputs in the way traditional software is — nor fully adaptive in a transparent way — their reasoning is opaque. This creates security challenges that have no precedent in traditional software: prompt injection, model poisoning, data exfiltration through model outputs, and uncontrolled information disclosure.**

---

This pattern has no confidence stars. The threat landscape for AI systems is evolving so rapidly that any specific formulation would be outdated within months. What the author can offer is a framework for thinking about AI security, not a stable set of best practices.

The novel security surface of AI systems has several dimensions. Prompt injection — where an attacker crafts input that causes an AI system to deviate from its intended behaviour — is the most widely discussed, but it is only one vector. Model poisoning (corrupting the training data or fine-tuning process to create predictable misbehaviour) is harder to detect and potentially more damaging. Data exfiltration through model outputs (an AI system that has been given access to sensitive data may reveal that data in its responses, either through direct disclosure or through inference attacks) is a confidentiality risk that traditional access control models were not designed to handle. And the authority problem — what actions should an AI system be permitted to take autonomously? — is a question that most organisations have not yet answered clearly.

Lisanne Bainbridge identified the "ironies of automation" in 1983: the more advanced the automation, the more crucial the human operator's contribution — and the more difficult it becomes for that operator to provide it. AI security embodies this irony perfectly. The security controls around AI must be comprehensible to humans who cannot fully comprehend the AI itself. A developer can read the source code of a traditional application and understand what it does. No one can read the weights of a neural network and understand what it will do. This means that AI security must rely more heavily on behavioural boundaries (what the system is allowed to do) rather than code-level understanding (what the system actually does).

The practical response is defence in depth, applied to AI specifically: input validation (sanitise and constrain what the AI system receives), output filtering (validate and constrain what the AI system produces), authority limits (restrict what actions AI systems can take, especially irreversible ones), model provenance verification (know where your models come from and what they were trained on), monitoring (observe AI system behaviour for anomalies), and prompt injection defences (separate trusted instructions from untrusted user input). None of these is sufficient alone. Together, they create a security posture that acknowledges the opacity of AI systems while limiting the damage that opacity can cause.

Therefore:

**Secure AI systems through defence in depth: validate inputs, filter outputs, limit authority, verify model provenance, and monitor behaviour. Establish explicit boundaries on what AI systems are permitted to do autonomously, and enforce those boundaries through technical controls rather than policy alone. Accept that AI security controls must be designed for systems whose internal reasoning cannot be fully inspected, and compensate with strong behavioural boundaries and continuous monitoring.**

---

_This pattern is completed by **AI-Augmented Observability (56)**, which provides the monitoring capability needed to detect when AI systems behave anomalously — an essential feedback loop given that AI behaviour cannot be fully predicted from inspection. **Observability Over Monitoring (48)** provides the broader observability foundation that makes AI-specific monitoring possible and meaningful._

## References

- Bainbridge, L. "Ironies of Automation." *Automatica* 19.6 (1983): 775-779.
- OWASP. *Top 10 for Large Language Model Applications.* 2023.
- Greshake, K. et al. "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." *AISec 2023.*
