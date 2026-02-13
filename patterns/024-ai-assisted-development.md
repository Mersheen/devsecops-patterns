---
id: 24
name: "AI-Assisted Development"
confidence: 0
scale: 4
context_patterns: [1, 2, 8, 22, 23]
completion_patterns: [26, 28, 47]
ai_dimension: true
tags: [ai, development, coding, copilot, llm]
references:
  - "DORA State of DevOps Report, 2024."
  - "Ziegler, A. et al. 'Productivity Assessment of Neural Code Completion.' MAPS 2022."
---

# AI-Assisted Development

_Your teams work within a **Generative Culture (1)** that welcomes new practices, you are building a **Learning Organisation (2)** capable of absorbing change, and your **Stream-Aligned Teams (8)** practise **Continuous Integration (22)** with a commitment to **Test-Driven Development (23)**. Now a new capability emerges: AI systems that can generate, complete, review, and refactor code. The question is not whether to use them, but how to use them without losing what makes your teams effective._

---

**AI code generation tools are powerful enough to change how developers work but unreliable enough to cause serious damage if adopted without discipline. Organisations that adopt them naively see initial speed gains followed by a creeping accumulation of code that nobody fully understands, subtle bugs that evade review, and a gradual erosion of the skills that made the team effective in the first place.**

---

This pattern has no stars. The author believes AI-assisted development is a genuine pattern — it is not going away, and it addresses a real recurring problem (the cost and speed of writing software). But the correct form of the pattern is not yet clear, because the tools are changing faster than anyone can evaluate them rigorously, and the empirical evidence is thin and contradictory.

What is known: developers report higher satisfaction and perceived productivity when using AI code generation tools. The 2024 DORA State of DevOps Report found that AI adoption among surveyed teams was widespread but that early adopters experienced decreased operational performance on some dimensions. This is not necessarily damning — early adoption of any practice shows mixed results — but it should temper the enthusiasm.

The dangers are specific and identifiable. First, AI-generated code has a plausibility problem: it looks correct, compiles, and often passes superficial review, but may contain subtle logical errors, security vulnerabilities, or architectural inconsistencies that a human writing the same code from scratch would have caught through the act of thinking through the problem. Second, over-reliance on AI generation can atrophy a developer's ability to reason about code — learned helplessness is a real phenomenon, and it applies here. Third, AI-generated code tends toward the conventional and the average; it draws from the corpus of existing code, which means it reproduces existing patterns including existing mistakes.

The benefits are also specific. AI is genuinely good at boilerplate, at translating well-understood intent into code, at exploring unfamiliar APIs, at generating test scaffolding, and at accelerating the parts of development that are mechanical rather than creative. A developer who uses AI to handle the tedious parts while staying fully engaged in the design and logic is more productive without the downsides.

The pattern, as best the author can currently formulate it, is about maintaining the developer's agency. The developer must remain the author — understanding, reviewing, and taking responsibility for every line. AI is a tool in the developer's hand, not an autonomous agent producing code that the developer merely approves.

This interacts strongly with existing practices. Test-Driven Development provides a critical safeguard: if the developer writes the test first, AI-generated code must pass a specification the developer already understands. Code review practices must adapt — reviewing AI-generated code requires different attention than reviewing human-written code, because the failure modes are different. And the Deployment Pipeline must be robust enough to catch what human review misses.

Therefore:

**Adopt AI code generation as a development tool, not a development replacement. Require that developers understand and can explain every line of AI-generated code they commit. Use Test-Driven Development as a forcing function: write the test first, then use AI to help implement the solution. Adapt code review practices to account for AI-specific failure modes — plausible-but-wrong logic, security anti-patterns, and architectural drift. Monitor the impact on your DORA metrics and your team's skill development over time, and be prepared to constrain usage if the costs outweigh the benefits.**

---

_AI-assisted development places new demands on **Code Review as Learning (26)** — reviewers must look for different things. It increases throughput into the **Deployment Pipeline (28)**, which must be robust enough to handle the volume. And **Secure AI Integration (47)** addresses the security dimension: AI-generated code may introduce vulnerabilities that follow patterns the AI learned from insecure training data._

## References

- DORA State of DevOps Report, 2024. Google Cloud / DORA team.
- Ziegler, A. et al. "Productivity Assessment of Neural Code Completion." *MAPS 2022.*
- Vaithilingam, P. et al. "Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models." *CHI 2022 Extended Abstracts.*
