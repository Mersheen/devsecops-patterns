---
id: 52
name: "Alerting on Symptoms, Not Causes"
confidence: 1
scale: 8
context_patterns: [48, 49]
completion_patterns: []
ai_dimension: false
tags: [alerting, on-call, symptoms, cognitive-load]
references:
  - "Miller, G. A. 'The Magical Number Seven, Plus or Minus Two.' Psychological Review 63.2 (1956): 81-97."
  - "Simon, H. A. 'Designing Organizations for an Information-Rich World.' 1971."
  - "Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. Site Reliability Engineering. O'Reilly, 2016."
  - "Sloss, B. T., Quinlan, S., and Beyer, B. The Site Reliability Workbook. O'Reilly, 2018."
---

# Alerting on Symptoms, Not Causes *

_You have built an **Observability Over Monitoring (48)** capability and defined **SLOs as Contracts (49)** that quantify acceptable reliability. The observability platform produces rich telemetry. The SLOs define what matters. Now the question is: what should wake up the on-call engineer at 3 a.m.?_

---

**Alerting on low-level causes — CPU usage, memory pressure, disk utilisation, individual process failures — generates noise that overwhelms operators. Too many alerts fire, each requiring investigation to determine whether users are actually affected. Alert fatigue sets in, and the on-call engineer stops trusting the system — either ignoring alerts or, worse, developing a learned helplessness that delays response to genuine incidents.**

---

George Miller's research on working memory established that humans can hold roughly seven items (plus or minus two) in short-term memory at any given time. More recent work by Nelson Cowan suggests the effective limit is closer to four chunks. An on-call engineer responding to an incident is already under cognitive load — they are dealing with uncertainty, time pressure, and interrupted sleep. An alerting system that fires dozens of cause-level alerts during an incident does not help; it overwhelms. The engineer cannot distinguish signal from noise when every low-level metric is screaming simultaneously.

Herbert Simon's concept of bounded rationality is directly applicable: human decision-making is limited by the information available, the cognitive limitations of the decision-maker, and the finite time available to make the decision. An effective alerting system works within these bounds rather than against them. It communicates what matters — are users affected, and how badly? — rather than everything that moved.

The practical rule is straightforward: alert on symptoms, investigate causes. A symptom-based alert fires when users experience elevated error rates, increased latency, or reduced availability — conditions that directly map to SLO violations. Cause-level data (CPU, memory, disk, queue depth, thread pool exhaustion) is invaluable for investigation once the engineer is engaged, but it should not be the trigger. If CPU is at 100% but users are unaffected, that is not an alert — it is a data point for tomorrow's capacity planning. If error rates spike but CPU is nominal, that is an alert — something the users care about has gone wrong.

This approach also naturally reduces alert volume. There are hundreds of potential cause-level metrics but relatively few symptom-level signals. By alerting on symptoms and SLO burn rates, teams move from hundreds of alert rules to a manageable set of meaningful signals, each of which directly communicates "users are being harmed."

Therefore:

**Alert on user-visible symptoms — error rates, latency, throughput, availability — not on low-level infrastructure causes. Tie alerts to SLO burn rates so that every alert communicates a meaningful impact on users. Use cause-level metrics for investigation and diagnosis, not for alerting. Keep the total number of alert rules small enough that every alert is actionable and trusted.**

---

_This is a terminal pattern at Scale 8. It feeds information back into the development and delivery process: when a symptom-based alert fires, the investigation that follows uses the observability platform built by **Observability Over Monitoring (48)**, and the response follows the error budget logic of **SLOs as Contracts (49)**. The loop closes when the findings from incident response inform future development priorities._

## References

- Miller, G. A. "The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information." *Psychological Review* 63.2 (1956): 81-97.
- Simon, H. A. "Designing Organizations for an Information-Rich World." In *Computers, Communications, and the Public Interest*, 1971.
- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly, 2016.
- Sloss, B. T., Quinlan, S., and Beyer, B. *The Site Reliability Workbook.* O'Reilly, 2018.
