---
id: 23
name: "Test-Driven Development"
confidence: 1
scale: 4
context_patterns: [16, 22]
completion_patterns: [28, 33]
ai_dimension: true
tags: [testing, tdd, specification, feedback]
references:
  - "Beck, K. *Test-Driven Development: By Example.* Addison-Wesley, 2003."
  - "Wickelgren, W. A. 'Speed-Accuracy Tradeoff and Information Processing Dynamics.' *Acta Psychologica* 41, 1977."
  - "Bainbridge, L. 'Ironies of Automation.' *Automatica* 19(6), 1983."
  - "Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution Press, 2018."
---

# Test-Driven Development *

_You are working within an **Evolutionary Architecture (16)** that must change safely over time, and you practise **Continuous Integration (22)** so that every change is verified automatically. The question is: when do you write the tests that CI depends upon, and what role do those tests play?_

---

**Writing tests after code inverts the feedback loop — you verify what you built rather than specifying what you need. Untested code is a system whose behaviour is undetermined until it fails in production.**

---

The conventional approach is to write code first and tests afterward. This feels natural — you build the thing, then check that it works. But this ordering has a subtle and pervasive cost. When the test comes after the code, the test is shaped by the implementation: it verifies what was built rather than specifying what was needed. Edge cases that the developer did not think of during implementation are equally unlikely to appear in the test. The test becomes a mirror of the code rather than an independent specification of expected behaviour.

Test-driven development inverts this relationship. The test is written first, as a deterministic specification of what the code should do. The implementation is then an adaptive response to that specification — it can take any form, so long as the test passes. This separation between specification (what) and implementation (how) is powerful because it forces the developer to think about behaviour before thinking about mechanism. It is Wickelgren's speed-accuracy tradeoff applied constructively: investing in accuracy up front (the test) reduces total time by preventing the rework that comes from building the wrong thing.

The discipline also addresses Bainbridge's irony of automation in reverse. Bainbridge observed that automation degrades the skills of the operators who must intervene when it fails. TDD prevents this degradation by keeping the developer actively engaged in reasoning about behaviour. The developer who writes tests first maintains a deep understanding of what the system is supposed to do, which is precisely the understanding needed when something unexpected occurs.

AI changes the dynamics of TDD in an important way. AI tools can generate test implementations and even suggest test cases, which can accelerate the mechanical aspects of the practice. But the discipline of thinking about behaviour before implementation — of choosing *what* to test — remains a human judgement act. The developer must decide what matters, what the edge cases are, what constitutes correct behaviour in ambiguous situations. Automating test generation without this discipline produces coverage without comprehension: a test suite that exercises the code but does not specify the intent.

Therefore:

**Write the test first. Let the test serve as a deterministic specification of expected behaviour; let the implementation be an adaptive response to that specification. This balances determinism — the test defines what the system must do — with adaptability — the implementation is free to take any form that satisfies the specification. When using AI to assist with test or implementation generation, ensure that the human developer has first reasoned about and specified the expected behaviour.**

---

_Tests feed into the **Deployment Pipeline (28)** as the first line of automated verification, and the standards for what must pass are defined by **Quality Gates with Escape Hatches (33)**._

## References

- Beck, K. *Test-Driven Development: By Example.* Addison-Wesley, 2003.
- Wickelgren, W. A. "Speed-Accuracy Tradeoff and Information Processing Dynamics." *Acta Psychologica* 41, 1977.
- Bainbridge, L. "Ironies of Automation." *Automatica* 19(6), 1983.
- Forsgren, N., Humble, J. and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution Press, 2018.
