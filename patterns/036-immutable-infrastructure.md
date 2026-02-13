---
id: 36
name: "Immutable Infrastructure"
confidence: 2
scale: 6
context_patterns: [35, 29]
completion_patterns: [38, 45]
ai_dimension: false
tags: [immutability, infrastructure, drift, determinism, phoenix-servers]
references:
  - "Morris, Kief. Infrastructure as Code, 3rd ed. O'Reilly, 2021."
  - "Fowler, Martin. 'PhoenixServer.' martinfowler.com, 2012."
  - "Taleb, N.N. Antifragile: Things That Gain from Disorder. Random House, 2012."
  - "Perrow, Charles. Normal Accidents: Living with High-Risk Technologies. Princeton University Press, 1999."
---

# Immutable Infrastructure **

_You have adopted **Infrastructure as Code (35)** — your infrastructure is defined declaratively and versioned. Your artefacts follow the **Build Once, Deploy Many (29)** principle. But even with infrastructure defined as code, there is a temptation to modify running systems in place: applying patches, tweaking configurations, installing hotfixes. Each modification moves the running infrastructure further from its declared state._

---

**Mutable infrastructure accumulates configuration drift — the gap between what you think is running and what is actually running widens over time. Patching a running server is a bet that the patch will work in the server's current, incompletely known state. The longer a system runs and the more it is modified in place, the less anyone can reason about it.**

---

Martin Fowler drew the distinction sharply: you want Phoenix Servers, not Snowflake Servers. A snowflake server is unique, hand-crafted, and irreplaceable — if it dies, so does the knowledge of its configuration. A phoenix server rises from the ashes of a known-good definition every time it is deployed. You do not repair it; you replace it. The server's identity is its definition, not its running state.

The case for immutability follows from Nassim Taleb's barbell strategy: extreme determinism in the base combined with controlled variability at the edges. The infrastructure itself is the base — it must be completely predictable. Configuration that varies by environment is the edge — it is injected at deployment time, not baked into a running system. When you commit to never modifying running infrastructure, you eliminate an entire class of problems: configuration drift, partial updates, inconsistent patching, and the slow accumulation of undocumented changes that eventually make a system impossible to understand.

Charles Perrow's work on normal accidents provides further motivation. In complex, tightly coupled systems, small interactions between components produce unexpected failures. Mutable infrastructure increases the number of these interactions — every patch, every in-place update, every manual fix adds a new variable to an already complex system. Immutability reduces interactive complexity by ensuring that the running system is always a faithful reproduction of a known, tested definition.

The practical implementation follows naturally: every deployment creates fresh infrastructure from the code definition. If a security patch is needed, you update the definition, build a new image, test it through the pipeline, and replace the running infrastructure. The old instances are destroyed, not patched. This may seem wasteful, but the cost of rebuilding is far less than the cost of reasoning about drift, debugging partial updates, or recovering from a patch that interacted badly with an unknown system state.

Therefore:

**Never patch a running server. Replace it. Every deployment creates fresh infrastructure from a known-good, tested definition. Treat running infrastructure as disposable — its value lies in the definition that produced it, not in the instance itself. When something needs to change, change the definition, test the new definition, and deploy a replacement.**

---

_Immutable infrastructure finds its most natural expression in **Containerised Workloads (38)**, where the container image is the immutable unit of deployment. The principle of replacing rather than modifying extends into the security domain through **Zero Trust Architecture (45)**, where no running component is trusted based on its history — only on its current, verifiable state._

## References

- Morris, Kief. *Infrastructure as Code: Dynamic Systems for the Cloud Age*, 3rd ed. O'Reilly, 2021.
- Fowler, Martin. "PhoenixServer." martinfowler.com, 2012.
- Taleb, N.N. *Antifragile: Things That Gain from Disorder.* Random House, 2012.
- Perrow, Charles. *Normal Accidents: Living with High-Risk Technologies.* Princeton University Press, 1999.
