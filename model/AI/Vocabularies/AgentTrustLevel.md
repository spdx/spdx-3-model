SPDX-License-Identifier: Community-Spec-1.0

# AgentTrustLevel

## Summary

Defines the trust level of an AI agent based on the degree of external
verification applied to its identity, behavior, and capabilities.

## Description

AgentTrustLevel is an enumeration that categorizes the confidence a consumer
can place in an AI agent's declared identity and behavioral claims, based on
the rigor of verification performed. Trust levels progress from no formal
verification (Level 0) to formal third-party certification (Level 3), and
determine the scope of resources an agent may be permitted to access and the
types of operations it may be authorized to execute.

This enumeration is informed by the NIST AI Agent Standards Initiative trust
framework, which establishes four verification tiers as a basis for
authorization and access control decisions in multi-agent systems.

## Metadata

- name: AgentTrustLevel

## Entries

- unverified: Level 0 — The agent has not been reviewed or assessed by any party. No claims about its identity, capabilities, or behavior have been independently examined. Access and operational scope should be maximally restricted.
- selfDeclared: Level 1 — Trust is based solely on claims made by the agent's developer or operator. No external review has been conducted. Suitable for low-stakes, sandboxed, or internal-only deployments where the declaring party is known and accountable.
- thirdPartyReviewed: Level 2 — The agent has been independently reviewed or audited by a third party, but has not undergone formal certification against a recognized standard. Provides higher confidence than self-declaration for use in controlled production environments.
- certified: Level 3 — The agent has been formally certified by a recognized standards or certification body against defined criteria for identity, capability accuracy, and behavioral compliance. Suitable for high-stakes deployments requiring verified accountability and regulatory alignment.
