---
id: 19
name: "Hypothesis-Driven Development"
confidence: 1
scale: 3
context_patterns: [2, 4]
completion_patterns: [17, 30, 48]
ai_dimension: false
tags: [experimentation, feedback, learning, measurement]
references:
  - "Hollnagel, Erik. Safety-II in Practice: Developing the Resilience Potentials. Routledge, 2018."
  - "Deming, W. Edwards. The New Economics for Industry, Government, Education. MIT Press, 1993."
  - "Ries, Eric. The Lean Startup. Crown Business, 2011."
  - "Thomke, Stefan H. Experimentation Works: The Surprising Power of Business Experiments. Harvard Business Review Press, 2020."
---

# Hypothesis-Driven Development *

_When the organisation operates as a **Learning Organisation (2)** and has adopted the discipline of **Explicit Tradeoffs (4)**, it can apply that learning orientation to product development itself — treating every feature as an experiment rather than a certainty._

---

**Building features based on assumptions, without validating those assumptions against reality, risks investing scarce resources in the wrong things. Deterministic roadmaps encode untested beliefs as commitments, and by the time the feature is delivered, the original assumption may have been wrong all along.**

---

The default mode of product development in most organisations is deterministic: a stakeholder requests a feature, it is prioritised, designed, built, and shipped. The implicit assumption is that the stakeholder's request correctly represents what users need and that the proposed solution will achieve the desired outcome. Both assumptions are frequently wrong. Research by Microsoft's experimentation platform found that roughly two-thirds of well-designed features had no measurable positive impact on the metrics they were intended to improve. This is not a failure of execution; it is a fundamental property of complex systems where the relationship between intervention and outcome is uncertain.

Erik Hollnagel's Safety-II framework provides a useful lens. Safety-II reframes safety from "the absence of things that go wrong" to "the presence of the capacity to succeed under varying conditions." This capacity requires experimentation — the ability to try things, observe results, and adapt. Applied to product development, it means that the organisation's ability to succeed depends not on predicting correctly but on learning quickly. Every feature is a probe into an uncertain environment, and the organisation that learns fastest from its probes will outperform the one that plans most carefully.

Deming's Plan-Do-Study-Act (PDSA) cycle provides the operational structure. "Plan" means stating a hypothesis: "We believe that [change] will result in [outcome] as measured by [metric]." "Do" means building the minimum required to test that hypothesis — not the full feature, but the thinnest slice that would generate evidence. "Study" means measuring the result and comparing it to the hypothesis. "Act" means deciding, based on evidence, whether to invest further, pivot, or stop. This is not merely agile development with different vocabulary; it is a fundamental reframing of the relationship between planning and execution. The plan is not a commitment to deliver a feature; it is a commitment to learn whether a feature is worth delivering.

The practical difficulty is cultural. Hypothesis-driven development reframes "failure" — a feature that does not move the target metric — as valuable data rather than wasted effort. This reframing requires the psychological safety of a generative culture. In a pathological or bureaucratic culture, admitting that a feature hypothesis was wrong is career-threatening, so teams ship features regardless of evidence and declare success based on output (we shipped it) rather than outcome (it worked).

Therefore:

**Treat every feature as an experiment. State the hypothesis explicitly — what you believe will happen and how you will measure it. Build the minimum required to test the hypothesis. Measure the result. Decide based on evidence whether to continue, pivot, or stop. Reframe features that do not achieve their intended outcome as valuable learning, not as failures.**

---

_Hypothesis-driven development is completed by **Thin Slice Delivery (17)**, which provides the mechanism for building the minimum required to test each hypothesis. **Progressive Delivery (30)** enables controlled exposure of experiments to subsets of users. And **Observability Over Monitoring (48)** provides the instrumentation needed to measure outcomes and validate or refute hypotheses._

## References

- Hollnagel, Erik. *Safety-II in Practice: Developing the Resilience Potentials.* Routledge, 2018.
- Deming, W. Edwards. *The New Economics for Industry, Government, Education.* MIT Press, 1993.
- Ries, Eric. *The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses.* Crown Business, 2011.
- Thomke, Stefan H. *Experimentation Works: The Surprising Power of Business Experiments.* Harvard Business Review Press, 2020.
