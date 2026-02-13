---
id: 22
name: "Continuous Integration"
confidence: 2
scale: 4
context_patterns: [20, 17]
completion_patterns: [28, 33]
ai_dimension: false
tags: [integration, automation, testing, feedback]
references:
  - "Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution Press, 2018."
  - "Fowler, M. 'Continuous Integration.' martinfowler.com, 2006."
  - "Deming, W. E. *Out of the Crisis.* MIT Press, 1986."
  - "Ohno, T. *Toyota Production System: Beyond Large-Scale Production.* Productivity Press, 1988."
---

# Continuous Integration **

_You have adopted **Trunk-Based Development (20)** so that developers work on a shared mainline, and you deliver in **Thin Slices (17)** so that changes are small and frequent. Now the question is: how do you know that each change is safe to integrate?_

---

**If integration is deferred, defects compound. The longer the interval between integrations, the harder it is to locate the source of a failure — the scope of investigation grows combinatorially with the number of changes since the last successful integration.**

---

Continuous integration is the practice that resolves the apparent tension between speed and safety at the development level. Before CI became widespread, the received wisdom was that going faster meant accepting more risk — that you could have rapid development or careful verification, but not both. CI demonstrated that this is a false dilemma: by integrating and verifying constantly, you go faster *because* you invest in safety, not in spite of it.

The mechanism is straightforward. Every developer integrates their work to the mainline at least once a day. Each integration triggers an automated build and test cycle. If the build or tests fail, the team stops and fixes the problem immediately — before more changes pile on top of the broken state. This is Toyota's jidoka principle applied to software: stop the line when a defect is detected, because the cost of fixing a defect rises steeply the further it travels from its point of origin.

Deming's chain reaction applies here with particular force: improve quality, and costs decrease while productivity increases. The team that runs CI rigorously spends less time debugging integration problems, less time investigating production incidents caused by integration defects, and less time in painful merge exercises. The upfront investment in automated testing and build infrastructure pays for itself many times over.

The practice requires real discipline. CI means that every commit must be small enough to integrate safely, that the automated test suite must be fast enough to run on every commit, and that fixing a broken build takes priority over new work. Half-measures — running CI nightly, or ignoring failing tests — provide the appearance of integration without the benefit. The build must be genuinely green, genuinely fast, and genuinely authoritative.

Therefore:

**Integrate every developer's work to the mainline at least once per day, verified by an automated build and test cycle that runs on every commit. When the build breaks, fixing it takes priority over all other work. The build result is authoritative: if it passes, the change is safe to proceed; if it fails, the team stops and investigates immediately.**

---

_Continuous integration feeds changes into the **Deployment Pipeline (28)**, which carries them through further stages of verification toward production. **Quality Gates with Escape Hatches (33)** define how to balance thoroughness with flow when the pipeline must make go/no-go decisions._

## References

- Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution Press, 2018.
- Fowler, M. "Continuous Integration." martinfowler.com, 2006.
- Deming, W. E. *Out of the Crisis.* MIT Press, 1986.
- Ohno, T. *Toyota Production System: Beyond Large-Scale Production.* Productivity Press, 1988.
