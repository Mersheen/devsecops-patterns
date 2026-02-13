---
id: 40
name: "Secrets Management"
confidence: 1
scale: 6
context_patterns: [21, 35]
completion_patterns: [45, 47]
ai_dimension: true
tags: [secrets, security, vaults, rotation, credentials]
references:
  - "Hashicorp. 'Why We Need Dynamic Secrets.' hashicorp.com, 2020."
  - "OWASP. 'Secrets Management Cheat Sheet.' owasp.org, 2023."
  - "Morris, Kief. Infrastructure as Code, 3rd ed. O'Reilly, 2021."
  - "Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. The DevOps Handbook, 2nd ed. IT Revolution, 2021."
---

# Secrets Management *

_Your organisation practises **Version Control Everything (21)** and has adopted **Infrastructure as Code (35)** — configuration and infrastructure definitions live in repositories, pass through pipelines, and are reviewed by multiple people. This transparency, essential for almost every other artefact, creates a specific and dangerous problem for one category of data: secrets._

---

**Secrets — API keys, database credentials, TLS certificates, encryption keys, service account tokens — embedded in code, configuration files, or environment definitions are a persistent, high-impact security risk. They are visible to anyone with repository access, difficult to rotate, and impossible to scope. Manual secret rotation is error-prone and infrequent, meaning that a compromised credential remains exploitable for far longer than it should.**

---

The core principle is separation: secrets must never live where code lives. A password committed to a Git repository is effectively published — even if you delete it in a subsequent commit, it persists in the repository's history. A database credential baked into a container image travels with that image to every environment and every registry. An API key in an environment variable definition checked into version control is readable by every developer with repository access.

The solution is a dedicated secrets management system — a vault — that stores secrets encrypted at rest, controls access through fine-grained policies, delivers secrets to applications at runtime (not build time), and maintains an audit log of every access. The application never sees a configuration file containing a password; it receives the password at startup from the vault, and the vault records who (or what) requested it and when.

Beyond storage, the critical capability is rotation. Static secrets — credentials that never change — are the most dangerous kind, because a single compromise provides indefinite access. Dynamic secrets, generated on demand with a limited lifetime, reduce the blast radius of any individual compromise to the secret's time-to-live. A database credential that expires after one hour is fundamentally different, from a security perspective, than one that was set three years ago and shared across four teams.

The AI dimension deserves specific attention. The proliferation of AI-powered tools and services has multiplied the number of secrets an organisation must manage. LLM API keys, model registry credentials, tool authentication tokens, embedding service keys — each AI integration introduces new secrets that must be stored, rotated, scoped, and audited. Many of these secrets grant access to metered services with significant cost implications, making a leaked AI API key not just a security incident but a financial one. Furthermore, AI-assisted development tools often operate in developer environments where secret hygiene is weakest, increasing the probability that a secret ends up in a prompt, a log, or a commit message.

Therefore:

**Store all secrets in dedicated, encrypted vaults — never in code, configuration files, or version control. Deliver secrets to applications at runtime through the vault's API. Rotate secrets automatically and frequently; prefer short-lived, dynamically generated credentials over static ones. Scope each secret to the minimum set of services and environments that require it. Audit every access.**

---

_Secrets management feeds directly into broader security patterns. **Zero Trust Architecture (45)** depends on robust credential management — you cannot verify every interaction if the credentials used for verification are themselves compromised. **Secure AI Integration (47)** addresses the specific challenges of managing the credentials, keys, and tokens that AI systems require, extending this pattern's principles into the rapidly expanding AI tool landscape._

## References

- Hashicorp. "Why We Need Dynamic Secrets." hashicorp.com, 2020.
- OWASP. "Secrets Management Cheat Sheet." owasp.org, 2023.
- Morris, Kief. *Infrastructure as Code: Dynamic Systems for the Cloud Age*, 3rd ed. O'Reilly, 2021.
- Kim, G., Humble, J., Debois, P., Willis, J., and Forsgren, N. *The DevOps Handbook*, 2nd ed. IT Revolution, 2021.
