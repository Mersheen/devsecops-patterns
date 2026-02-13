---
id: 42
name: "Policy as Code"
confidence: 2
scale: 7
context_patterns: [21, 41]
completion_patterns: [33, 43]
ai_dimension: false
tags: [security, policy, automation, compliance, governance]
references:
  - "Weber, Max. Economy and Society, ed. Guenther Roth and Claus Wittich. University of California Press, 1978 [1922]."
  - "Garfinkel, S. and Spafford, G. Web Security, Privacy and Commerce, 2nd ed. O'Reilly, 2002."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Policy as Code **

_You have established **Version Control Everything (21)** as a norm, so that all definitions of your system are versioned and reviewable. You have committed to **Security as Shared Responsibility (41)**, which means security cannot depend on a central team manually reviewing every change. The question is how to enforce security policies consistently, at speed, without creating human bottlenecks._

---

**Written security policies are deterministic in intent but adaptive in practice — humans interpret them inconsistently. Manual policy enforcement creates bottlenecks that teams route around under time pressure, and unwritten policies exist only in the memory of whoever wrote them. The result is inconsistent enforcement: the same policy is applied strictly in one team and ignored in another.**

---

Max Weber described the ideal bureaucracy as one where rules are applied impersonally — the same rule produces the same outcome regardless of who applies it. This is precisely what manual policy enforcement fails to achieve. A security policy that says "all S3 buckets must be encrypted" means something different to the reviewer who checks every pull request carefully and the reviewer who is approving twenty changes on a Friday afternoon. The policy's intent is deterministic; its enforcement is anything but.

The resolution is to express security policies as code. Tools like Open Policy Agent (OPA), HashiCorp Sentinel, AWS Config Rules, and Kubernetes admission controllers allow organisations to define policies in a language that machines can evaluate. The policy becomes a programme: given the current state of a resource or a proposed change, does it comply? The answer is yes or no, every time, with no variation based on who is reviewing or how busy they are.

This is not Weber's iron cage — the fear that bureaucratic rules, once codified, become impossible to change. Policy as code is more flexible than written policy precisely because it is code. It lives in version control (completing the loop with **Version Control Everything (21)**). Changes to policy go through pull requests, are reviewed, tested, and deployed through the same pipeline as any other change. The history of every policy decision is preserved in the commit log. When a policy is wrong or outdated, it can be changed through the same process that created it — and the change takes effect immediately and universally, rather than requiring every reviewer to be retrained.

The most common failure mode is writing policies that are too strict or too numerous, creating a wall of automated rejections that developers learn to work around rather than with. Good policy as code follows the same principle as good legislation: it should encode the important constraints clearly and leave room for teams to operate within those constraints. A policy that says "no public S3 buckets" is clear and enforceable. A policy that prescribes the exact IAM role structure for every service is probably too rigid — it will need constant exceptions, and exception management becomes its own bureaucracy.

Therefore:

**Express security and compliance policies as code: versioned, tested, and enforced automatically in the deployment pipeline. Use tools like OPA, Sentinel, or admission controllers to evaluate every change against organisational policy. Treat policy code with the same rigour as application code — review it, test it, and evolve it. Keep policies focused on what matters: the constraints that genuinely protect the organisation, not an exhaustive catalogue of preferences.**

---

_This pattern is completed by **Quality Gates with Escape Hatches (33)**, which addresses how to handle the inevitable cases where a legitimate change conflicts with an automated policy — the escape hatch prevents policy enforcement from becoming the very bottleneck it was designed to replace. **Supply Chain Security (43)** extends policy enforcement to the dependencies and artefacts the organisation consumes, applying the same automated verification to the software supply chain._

## References

- Weber, Max. *Economy and Society*, ed. Guenther Roth and Claus Wittich. University of California Press, 1978 [1922].
- Garfinkel, S. and Spafford, G. *Web Security, Privacy and Commerce*, 2nd ed. O'Reilly, 2002.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
