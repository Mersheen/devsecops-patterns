---
id: 29
name: "Build Once, Deploy Many"
confidence: 2
scale: 5
context_patterns: [28, 22]
completion_patterns: [36, 38]
ai_dimension: false
tags: [artefact, immutability, deployment, determinism]
references:
  - "Humble, J. and Farley, D. Continuous Delivery. Addison-Wesley, 2010."
  - "Taleb, N.N. Antifragile: Things That Gain from Disorder. Random House, 2012."
  - "Forsgren, N., Humble, J., and Kim, G. Accelerate. IT Revolution, 2018."
---

# Build Once, Deploy Many **

_Your **Deployment Pipeline (28)** moves changes from commit to production, and **Continuous Integration (22)** ensures that code is integrated and tested frequently. But what exactly is being promoted through the pipeline's stages? If you rebuild the artefact for each environment, you have introduced a variable you cannot control._

---

**Environment-specific builds introduce variance. If what you tested is not what you deploy, your tests prove nothing. Every rebuild is a fresh opportunity for non-determinism — different dependency resolutions, different compiler flags, different timestamps — and each difference erodes the confidence your pipeline was designed to build.**

---

The temptation to rebuild per environment is understandable. Different environments need different database connection strings, different feature flags, different API endpoints. The naive solution is to bake these differences into the build itself: one build for staging, another for production. This is precisely backwards. It conflates two things that should be kept ruthlessly separate: the artefact (which should be invariant) and its configuration (which should vary).

The correct approach follows what Nassim Taleb calls a barbell strategy: extreme safety in the base combined with controlled variability at the edges. The immutable artefact is the safe base — it is the same binary, the same container image, the same bundle that passed every test in your pipeline. Configuration is the controlled variability — environment variables, configuration files, secrets injected at deployment time. The artefact is deterministic; the configuration is adaptive. Together they give you both reliability and flexibility.

This pattern has a practical corollary: your build process must produce a single artefact with a unique identifier (a content-addressable hash, a semantic version, a build number) that can be traced from the commit that produced it through every environment it traverses. If you cannot point to a specific artefact and say "this exact thing ran in staging, and this exact thing is now running in production," you do not have a pipeline — you have a hope.

The discipline extends beyond application code. Infrastructure modules, database migration scripts, and deployment manifests should all follow the same principle: define them once, parameterise what varies, and promote the definition unchanged. The pattern is fractal — it applies at every level of the system.

Therefore:

**Build a single immutable artefact and promote it unchanged through every environment. Configuration varies by environment; the artefact does not. Tag each artefact with a unique, traceable identifier. Treat any environment-specific rebuild as a defect in your pipeline design.**

---

_The immutable artefact finds its natural home on **Immutable Infrastructure (36)**, where the principle of "never modify, only replace" extends from the artefact to the infrastructure that hosts it. **Containerised Workloads (38)** provide a practical packaging format that makes build-once-deploy-many straightforward to implement._

## References

- Humble, J. and Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley, 2010.
- Taleb, N.N. *Antifragile: Things That Gain from Disorder.* Random House, 2012.
- Forsgren, N., Humble, J., and Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
