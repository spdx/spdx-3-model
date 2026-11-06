SPDX-License-Identifier: Community-Spec-1.0

# agentTrustLevel

## Summary

Indicates the degree of external verification applied to the AI agent's
identity, behavioral claims, and declared capabilities.

## Description

Specifies the trust level assigned to an AI agent, reflecting how rigorously
its identity and behavior have been verified by external parties. Trust level
informs consumers, orchestrators, and access-control systems about the
confidence they can place in the agent's declared properties and the scope of
resources or operations the agent may be permitted to access.

The four levels progress from `unverified` (no assessment performed) through
`selfDeclared` (developer or operator claims only) and `thirdPartyReviewed`
(independent audit) to `certified` (formal certification by a recognized
standards body).

An agent declares at most one trust level. When no value is present, consumers
should treat the agent as unverified.

## Metadata

- name: agentTrustLevel
- Nature: ObjectProperty
- Range: AgentTrustLevel
