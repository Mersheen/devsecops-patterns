---
id: 32
name: "GitOps"
confidence: 1
scale: 5
context_patterns: [21, 28]
completion_patterns: [35, 36]
ai_dimension: false
tags: [gitops, reconciliation, desired-state, feedback-loop]
references:
  - "Wiener, N. Cybernetics: Or Control and Communication in the Animal and the Machine, 2nd ed. MIT Press, 1961."
  - "Ashby, W.R. An Introduction to Cybernetics. Chapman and Hall, 1956."
  - "Limoncelli, T., Hogan, C., and Chalup, S. The Practice of Cloud System Administration. Addison-Wesley, 2014."
---

# GitOps *

_You practise **Version Control Everything (21)** and your **Deployment Pipeline (28)** automates the path from commit to production. But how do deployments actually happen at the end of that pipeline? If the final step is an imperative command — "run this script," "execute this deployment" — you have a pipeline that is declarative in its definition but imperative in its most critical moment._

---

**Imperative deployments — where a process pushes changes to an environment by executing commands — are difficult to audit, prone to drift between desired and actual state, and fragile in the face of partial failures. When the desired state exists only in the mind of the person or script performing the deployment, there is no mechanism for the system to self-correct.**

---

GitOps resolves this by making Git the single source of truth for desired system state. The desired state of every environment — what should be running, at what version, with what configuration — is declared in a Git repository. An automated reconciliation agent running inside the target environment continuously compares actual state against desired state and corrects any divergence. Deployment is not an action you perform; it is a state you declare. The system converges on that state automatically.

This is pure cybernetic control. Norbert Wiener described the fundamental principle of feedback-controlled systems in 1948: a system measures its actual state, compares it to its desired state, and applies corrections proportional to the difference. The GitOps reconciliation loop is exactly this — Wiener's negative feedback applied to infrastructure. W. Ross Ashby formalised this further as error-controlled regulation: the system does not need to understand the full complexity of its environment, only the difference between where it is and where it should be.

The pull-based model is what makes GitOps self-correcting in a way that push-based deployment cannot be. In a push model, if a deployment partially fails, the system is left in an indeterminate state and a human must intervene. In a pull model, the reconciliation agent will detect the divergence on its next cycle and attempt to correct it. If someone manually modifies a running environment (a common source of drift), the agent reverts the change. The declared state in Git is not merely documentation — it is an active constraint that the system continuously enforces.

There is a subtlety worth noting: GitOps does not eliminate the need for a deployment pipeline. The pipeline still builds, tests, and produces artefacts. What GitOps changes is the final delivery mechanism. Instead of the pipeline pushing artefacts into an environment, the pipeline updates the desired state declaration in Git, and the reconciliation agent pulls the change into the environment. The pipeline remains deterministic; the delivery mechanism gains self-healing properties.

Therefore:

**Declare the desired state of every environment in Git. Deploy an automated reconciliation agent that continuously compares actual state to desired state and corrects drift. Make Git commits the sole mechanism for changing what runs in production. Treat manual changes as drift to be automatically reverted, not as valid deployment actions.**

---

_The desired-state declarations in Git typically describe infrastructure, which means GitOps depends on and reinforces **Infrastructure as Code (35)**. The environments themselves benefit from **Immutable Infrastructure (36)** — when infrastructure components are replaced rather than modified, the reconciliation loop becomes simpler and more reliable._

## References

- Wiener, N. *Cybernetics: Or Control and Communication in the Animal and the Machine*, 2nd ed. MIT Press, 1961.
- Ashby, W.R. *An Introduction to Cybernetics.* Chapman and Hall, 1956.
- Limoncelli, T., Hogan, C., and Chalup, S. *The Practice of Cloud System Administration.* Addison-Wesley, 2014.
