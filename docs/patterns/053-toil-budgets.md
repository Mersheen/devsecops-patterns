---
id: 53
name: "Toil Budgets"
confidence: 1
scale: 8
context_patterns: [4, 6]
completion_patterns: []
ai_dimension: false
tags: [toil, automation, sustainability, operations]
references:
  - "Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. Site Reliability Engineering. O'Reilly, 2016."
  - "Bainbridge, L. 'Ironies of Automation.' Automatica 19.6 (1983): 775-779."
  - "Robbins, L. An Essay on the Nature and Significance of Economic Science. Macmillan, 1932."
  - "Simon, H. A. 'Designing Organizations for an Information-Rich World.' 1971."
---

# Toil Budgets *

_You have committed to **Explicit Tradeoffs (4)** as a decision-making principle and to **Sustainable Pace (6)** as a constraint on how your teams work. Operations generates manual, repetitive work. The question is how much of that work is acceptable and how you decide what to automate._

---

**Operational toil — manual, repetitive, automatable work that scales linearly with service size — consumes the scarcest resource in a software organisation: human attention. Left unchecked, toil expands to fill all available time, crowding out the engineering work that would reduce future toil. But the naive response — automate everything — introduces its own risks.**

---

Lionel Robbins defined economics as the study of how scarce means are allocated among competing ends. Herbert Simon extended this to organisations, arguing that attention is the ultimate scarce resource. Operational toil consumes attention: every hour spent on manual deployments, ticket-driven access provisioning, or hand-tuned capacity adjustments is an hour not spent on building automation, improving reliability, or developing new capabilities. When toil exceeds a threshold — Google's SRE practice suggests 50% — the team is no longer an engineering team. It is an operations team that occasionally gets to do engineering, and its systems will stagnate.

However, Lisanne Bainbridge's "ironies of automation" present a crucial counterpoint. When you automate a process completely, the humans who used to perform it lose their understanding of how it works. When the automation fails — and it will — those humans lack the skill and knowledge to intervene effectively. The more reliable the automation, the worse this problem becomes, because the humans have less practice with manual operation. This is not a theoretical concern: it is a documented failure mode in aviation, nuclear power, and software operations alike.

The resolution is a toil budget: a deliberate, measured cap on the amount of manual operational work a team performs. The budget makes the cost of toil visible and creates a forcing function for prioritising automation. But the budget also implies choice: not all toil should be automated. High-volume, low-judgement toil (restarting services, rotating logs, provisioning standard environments) should be automated aggressively. Low-volume, high-judgement toil (investigating unusual performance patterns, making capacity decisions, handling novel failure modes) should be preserved as manual engagement, because it maintains the human understanding that effective incident response requires.

Measuring toil requires categorisation. Work that is manual, repetitive, automatable, tactical (reacting rather than planning), and that scales with service growth is toil. Work that requires judgement, produces lasting value, or builds understanding is engineering. The boundary is not always crisp, but the act of categorising forces the team to be honest about where its time goes.

Therefore:

**Measure operational toil explicitly. Cap it as a percentage of team time — no more than 50% — and treat the cap as a policy constraint, not a guideline. Prioritise automation for toil that is high-volume and low-judgement. Deliberately preserve manual engagement for activities that maintain human understanding of the system. When the toil budget is exceeded, it is a signal to invest in engineering, not to hire more operators.**

---

_This is an operational practice that feeds back to organisational philosophy. The toil budget instantiates the economics of **Explicit Tradeoffs (4)** for operational work and directly supports **Sustainable Pace (6)** by preventing toil from consuming the team's capacity for meaningful engineering._

## References

- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly, 2016.
- Bainbridge, L. "Ironies of Automation." *Automatica* 19.6 (1983): 775-779.
- Robbins, L. *An Essay on the Nature and Significance of Economic Science.* Macmillan, 1932.
- Simon, H. A. "Designing Organizations for an Information-Rich World." In *Computers, Communications, and the Public Interest*, 1971.
