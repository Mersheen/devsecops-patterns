# A Pattern Language for DevOps

## Scale Map — First Draft

This document maps the provisional territory of a pattern language for how software engineering organisations build, deliver, and operate software. It follows Christopher Alexander's method: patterns are ordered from largest scale to smallest, each linking upward to the patterns that set its context and downward to patterns that complete it. AI is not a separate section — it is a force present at every level, just as light and human movement are forces present at every level of Alexander's built environment.

Confidence ratings follow Alexander's convention:
- **\*\*** — the author believes this pattern describes an invariant: every healthy organisation will exhibit some version of it
- **\*** — the author believes this is a true pattern but the evidence or form is not yet certain
- **no star** — a hypothesis; included because the language would be incomplete without it, but the author is not confident in the formulation

---

### Scale 1 — Organisational Philosophy

The largest patterns. These shape everything below them. An organisation that gets these wrong will struggle regardless of its tooling.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 1 | Generative Culture | Westrum's typology as a pattern. High cooperation, messengers trained, bridging encouraged, failure leads to inquiry, novelty implemented. AI modifies this: how does an org maintain generative culture when AI mediates communication and decision-making? |
| 2 | Learning Organisation | Senge's five disciplines reframed. Continuous improvement is not a process — it is a property of the culture. AI as accelerant and risk (learned helplessness). |
| 3 | Flow Over Utilisation | The fundamental Lean insight: optimise for flow of value, not for keeping people busy. Directly challenges traditional management. AI amplifies this by collapsing certain bottlenecks while creating new ones. |
| 4 | Trust and Verify | The security counterpart to generative culture. Not "zero trust" the network architecture, but the organisational principle: default to trusting people, verify through systems. Enables speed without recklessness. |
| 5 | Sustainable Pace | Borrowed from XP but elevated to organisational level. A pattern against burnout culture. AI changes the calculus — does it reduce toil or just raise expectations? |

---

### Scale 2 — Organisational Structure

How the organisation divides and coordinates work. Directly shaped by the philosophy above; directly shapes the teams and processes below.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 6 | Value Stream Alignment | Organise around the flow of value to the customer, not around technical specialisms. From Lean, reinforced by Accelerate's findings. |
| 7 | Stream-Aligned Teams | Team Topologies' core pattern. A team aligned to a single stream of work, empowered end-to-end. AI changes team boundaries — what can a smaller team now own? |
| 8 | Platform Team | Provides internal capabilities as a service to stream-aligned teams. Critical for reducing cognitive load. AI-powered platforms change the economics radically. |
| 9 | Enabling Team | Temporarily assists stream-aligned teams in acquiring new capabilities. Key mechanism for spreading knowledge (including AI skills). |
| 10 | Complicated Subsystem Team | Isolates deep specialist knowledge. AI/ML model development may be the quintessential example. |
| 11 | Inverse Conway Manoeuvre | Design your organisation to produce the architecture you want, not the other way around. |
| 12 | Small Autonomous Teams | Bezos's two-pizza teams. Autonomy bounded by alignment. AI may shift the viable team size downward. |
| 13 | Communities of Practice | Cross-cutting knowledge sharing without structural coupling. Essential when teams are autonomous. |

---

### Scale 3 — Product and Value

How the organisation understands and decomposes what it is building. Bridges organisational structure and technical architecture.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 14 | Everything as Product | Treat platforms, tools, and internal services as products with users, not as projects with end dates. |
| 15 | Thin Slice Delivery | Deliver the thinnest possible end-to-end slice of value. Counters big-batch thinking. AI can help identify slices. |
| 16 | Hypothesis-Driven Development | Every feature is an experiment. Build, measure, learn. AI enables richer measurement. |
| 17 | Service Domain Boundaries | Bounded contexts from DDD applied to service decomposition. Gets the seams right before anything else matters. |
| 18 | API as Contract | APIs are the unit of organisational coupling. Treat them as products. |
| 19 | Evolutionary Architecture | Architecture that supports guided, incremental change. Fitness functions as guardrails. AI-generated fitness functions. |

---

### Scale 4 — Development Practices

How code is written, reviewed, and integrated. Heavily affected by AI.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 20 | Trunk-Based Development | Short-lived branches or none. Enables continuous integration. Foundational. |
| 21 | Version Control Everything | Marques & Correia's pattern. Code, config, infrastructure, policy, documentation — all versioned. |
| 22 | Continuous Integration | Not the tool — the practice. Integrate to mainline at least daily. Verified by automated build and test. |
| 23 | Pair and Ensemble Programming | Shared code ownership and real-time review. AI as a pairing partner changes the dynamics. |
| 24 | AI-Assisted Development | Using AI for code generation, completion, review, and refactoring. A pattern, not just a tool — requires discipline, verification, and understanding of failure modes. |
| 25 | Test-Driven Development | Write the test first. AI can generate tests but the discipline of thinking about behaviour before implementation remains human. |
| 26 | Living Documentation | Documentation generated from or verified against the running system. AI can maintain and query it. |
| 27 | Code Review as Learning | Review as knowledge sharing, not gatekeeping. AI-assisted review changes what humans focus on. |

---

### Scale 5 — Delivery Pipeline

The mechanisms that move code from commit to production. The deployment pipeline is the central organising metaphor.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 28 | Deployment Pipeline | Humble & Farley's foundational pattern. Every change goes through the same automated path to production. |
| 29 | Build Once, Deploy Many | A single immutable artefact promoted through environments. No environment-specific builds. |
| 30 | Ephemeral Environments | On-demand, short-lived environments for testing and review. Enabled by IaC and containers. AI can provision intelligently. |
| 31 | Progressive Delivery | Canary releases, feature flags, blue-green deployments as a unified pattern. Decouple deployment from release. |
| 32 | GitOps | Desired state in Git, reconciled by automation. The pipeline is a pull-based reconciliation loop. |
| 33 | Pipeline as Code | Pipeline definitions versioned and tested like application code. |
| 34 | Automated Change Approval | Replace heavyweight change advisory boards with automated policy gates. AI-assisted risk assessment. |
| 35 | Deployment Frequency as Signal | Not a target — a diagnostic. Low frequency reveals friction; artificially high frequency reveals gaming. |

---

### Scale 6 — Quality and Testing

How the organisation builds and maintains confidence in its software.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 36 | Shift Left, Expand Right | Move testing earlier AND extend it into production. Not just "shift left." |
| 37 | Test Pyramid | Unit → Integration → E2E in decreasing volume. Still valid but AI may reshape the economics. |
| 38 | Contract Testing | Verify service interfaces independently. Decouples team testing schedules. |
| 39 | Chaos Engineering | Inject failure deliberately. Build confidence through controlled experiments. AI-driven chaos. |
| 40 | AI-Augmented Testing | AI generates tests, identifies gaps, prioritises test suites, detects flaky tests. A distinct pattern from AI-assisted development. |
| 41 | Production Testing | Synthetic transactions, smoke tests in production. Acknowledges that staging never fully replicates production. |
| 42 | Quality Gates with Escape Hatches | Automated quality enforcement that can be overridden with accountability, not bureaucracy. |

---

### Scale 7 — Infrastructure and Platform

The substrate everything runs on. Treated as code, delivered as product.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 43 | Infrastructure as Code | Morris's core principle. All infrastructure defined declaratively, versioned, tested, and delivered through the pipeline. |
| 44 | Immutable Infrastructure | Never patch a running server. Replace it. Phoenix servers, not snowflakes. |
| 45 | Containerised Workloads | Package application and dependencies as a unit. Enables portability and immutability. |
| 46 | Platform as Product | The internal platform, operated by the platform team, consumed as self-service by stream-aligned teams. |
| 47 | Service Mesh | Infrastructure-layer communication management. Observability, security, and routing without application code changes. |
| 48 | Secrets Management | Secrets never in code, rotated automatically, scoped minimally. AI implications: LLM API keys, model credentials. |
| 49 | Multi-Cloud as Strategy vs Reality | When multi-cloud is a genuine pattern vs when it is accidental complexity. Honest assessment. |

---

### Scale 8 — Security

Security as a property of the system, not a phase or a team. Woven through everything above.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 50 | Security as Shared Responsibility | Not a team that approves — a capability everyone exercises. Enabled by tooling, culture, and education. |
| 51 | Policy as Code | Security policies expressed as code, versioned, tested, enforced automatically. OPA, Sentinel, etc. |
| 52 | Supply Chain Security | SBOM, signed artefacts, verified provenance. Includes AI model supply chain. |
| 53 | Automated Vulnerability Management | Scan, triage, remediate, verify — continuously. AI-assisted prioritisation. |
| 54 | Zero Trust Architecture | Network-level trust model. Every request authenticated and authorised. |
| 55 | Threat Modelling as Practice | Regular, lightweight threat modelling integrated into development. Not annual compliance theatre. AI-assisted threat identification. |
| 56 | Secure AI Integration | Guardrails, prompt injection defence, model provenance, output validation. The security dimension of every AI-touching pattern above. |
| 57 | Blast Radius Limitation | Design for breach containment. Bulkheads, least privilege, segmentation. |

---

### Scale 9 — Observability and Feedback

How the organisation sees what is happening and learns from it.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 58 | Observability Over Monitoring | Instrument for unknown-unknowns, not just known-knowns. Structured events over metrics-and-logs. |
| 59 | The Four Golden Signals | Google SRE's latency, traffic, errors, saturation as baseline operational telemetry. |
| 60 | SLOs as Contracts | Error budgets as the governance mechanism between reliability and velocity. |
| 61 | Blameless Postmortems | Learning from failure without punishment. A cultural pattern enabled by process. |
| 62 | Alerting on Symptoms, Not Causes | Alert on user-visible impact, investigate causes. Reduces noise, increases signal. |
| 63 | AI-Augmented Observability | AIOps: anomaly detection, log analysis, root cause suggestion, predictive alerting. Powerful but requires trust calibration. |
| 64 | Feedback Loops at Every Scale | From sub-second (compiler errors) to quarterly (retrospectives). Every pattern above should have a feedback mechanism. |

---

### Scale 10 — Operational Excellence

How the organisation runs software in production, day to day.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 65 | You Build It, You Run It | The team that builds the service operates it. Full ownership. |
| 66 | Toil Budgets | Measure and cap toil. Automate what recurs. AI can identify and automate toil. |
| 67 | Incident Response as Practice | Not a document — a rehearsed capability. Game days, on-call rotations, runbooks. |
| 68 | Runbook Automation | Start with documented procedures, progressively automate. AI can execute and adapt runbooks. |
| 69 | Graceful Degradation | Design for partial failure. Circuit breakers, bulkheads, fallbacks. |
| 70 | Capacity Planning as Continuous Activity | Not annual — ongoing. AI-driven demand prediction. |

---

### Cross-Cutting Patterns

Some patterns do not sit neatly at one scale. They are forces that shape decisions across multiple levels.

| # | Provisional Name | Notes |
|---|-----------------|-------|
| 71 | Reduce Cognitive Load | The meta-pattern behind platform teams, good APIs, clear boundaries, and automation. Everything should reduce, not increase, the cognitive burden on the humans in the system. |
| 72 | Make Work Visible | Kanban boards, deployment dashboards, value stream maps. You cannot improve what you cannot see. |
| 73 | Automate Repetition, Not Judgement | A principle for AI integration: automate the repetitive, keep humans in the loop for judgement. But the boundary moves over time. |
| 74 | Measure What Matters | DORA metrics, but also the discipline of not measuring everything. Goodhart's Law as a force. |
| 75 | Continuous Improvement | Not a standalone activity — a property of every pattern above. Kaizen. Retrospectives. Data-driven refinement. |

---

## Notes on this map

**This is a rough scaffold, not a finished structure.** Expected changes:

- Pattern numbers will change. Alexander's numbering was stable because he published a finished book. This is a living document.
- Some patterns will merge, split, or be discarded as individual patterns are written and their forces become clearer.
- Cross-references between patterns are not yet mapped — this is the most important structural work to come.
- The AI thread needs to be examined pattern by pattern: for each, what changes when AI is present? Is it a modifying force, or does it create an entirely new pattern?
- Patterns around data, data engineering, and ML model lifecycle may need their own scale level or may distribute across existing levels.
- Governance, compliance, and audit patterns are underrepresented. This is a gap.
- The relationship between this language and existing frameworks (DORA, Team Topologies, CNCF landscape) needs to be made explicit in each pattern's references.

## Format for individual patterns

Each pattern, when written, will follow Alexander's structure:

1. **Pattern name and confidence rating** (\*\*, \*, or no star)
2. **Opening context** — links to larger patterns that set the stage for this one
3. **Problem statement** — in bold, a concise statement of the recurring problem
4. **Body** — the empirical evidence, discussion, and reasoning. This is where forces (the tensions and trade-offs) are discussed, though not under that label.
5. **Solution statement** — in bold, the core of the pattern: what to do
6. **Diagram or illustration** — where helpful
7. **Closing cross-references** — links to smaller patterns that complete this one

### Additions to Alexander's format

- **References** — published sources supporting or challenging the pattern
- **AI dimension** — how AI modifies the forces, applicability, or consequences of this pattern (where relevant; not forced where it isn't)
