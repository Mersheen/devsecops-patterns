---
id: 26
name: "Code Review as Learning"
confidence: 1
scale: 4
context_patterns: [13, 22]
completion_patterns: [28]
ai_dimension: true
tags: [code-review, knowledge-sharing, alignment, learning]
references:
  - "Hayek, F. A. 'The Use of Knowledge in Society.' *American Economic Review* 35(4), 1945."
  - "Bacchelli, A. and Bird, C. 'Expectations, Outcomes, and Challenges of Modern Code Review.' *ICSE 2013.*"
  - "Sadowski, C. et al. 'Modern Code Review: A Case Study at Google.' *ICSE-SEIP 2018.*"
---

# Code Review as Learning *

_Your teams participate in **Communities of Practice (13)** that spread knowledge across organisational boundaries, and you practise **Continuous Integration (22)** so that every change is verified by automated tests before review. The question is: what is code review actually for?_

---

**Review-as-gatekeeping creates bottlenecks — a central approval step that throttles flow — and focuses on defect detection, which automated testing and CI handle far more reliably and quickly than human inspection.**

---

The traditional framing of code review is quality assurance: a senior developer examines the code, finds bugs, and approves or rejects the change. This framing is both inefficient and incomplete. Research by Bacchelli and Bird found that while developers expect code review to catch defects, the actual primary benefit is knowledge transfer. Sadowski et al.'s study at Google confirmed this: the most frequently cited outcome of code review was improved code comprehension across the team, not defect detection.

When review is framed as gatekeeping, it creates predictable dysfunctions. Review queues grow because a small number of senior developers become bottlenecks. Reviewers focus on superficial issues (style, naming, formatting) because those are easy to spot, while deeper design problems slip through. Authors feel defensive about their code; reviewers feel burdened by the volume. The result is a process that slows delivery without proportionally improving quality.

Reframing review as learning changes everything. The primary purpose of review becomes spreading comprehension of the codebase across the team — Hayek's insight that distributed knowledge improves through circulation, not centralisation. A review comment that says "I didn't know we handled this case — interesting approach" is as valuable as one that says "this will fail on null input." Review catches design problems that automated tests cannot (is this the right abstraction? does this fit the architecture? will the next developer understand this?), spreads context about why decisions were made, and aligns approaches without mandating uniformity.

AI-assisted review handles the mechanical checks that humans do poorly: style consistency, common bug patterns, security anti-patterns, performance issues. This is a genuine improvement — AI is tireless, consistent, and fast at pattern matching. But it frees human reviewers to focus on what AI cannot yet judge well: design intent, domain logic, comprehensibility, and architectural fit. The combination of AI for mechanical review and humans for design review is more effective than either alone.

Therefore:

**Reframe code review as knowledge sharing. The primary purpose is spreading comprehension of the codebase across the team and aligning on design approaches. Use automated tools and AI-assisted review for mechanical checks — style, common bugs, security patterns — and reserve human review time for design intent, domain logic, and comprehensibility. Review should be a conversation, not a gate.**

---

_Reviews that are completed feed changes into the **Deployment Pipeline (28)**, carrying shared understanding forward into the delivery process._

## References

- Hayek, F. A. "The Use of Knowledge in Society." *American Economic Review* 35(4), 1945.
- Bacchelli, A. and Bird, C. "Expectations, Outcomes, and Challenges of Modern Code Review." *ICSE 2013.*
- Sadowski, C. et al. "Modern Code Review: A Case Study at Google." *ICSE-SEIP 2018.*
