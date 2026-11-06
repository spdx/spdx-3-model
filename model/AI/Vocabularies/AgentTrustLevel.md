SPDX-License-Identifier: Community-Spec-1.0

# AgentTrustLevel

## Summary

How much the agent's identity and behavior have been independently verified.

## Description

Indicates how rigorously an AI agent has been checked by external parties.
The four levels progress from no verification at all to formal certification,
and can be used by orchestrators or access-control systems to decide what the
agent is allowed to do.

## Metadata

- name: AgentTrustLevel

## Entries

- unverified: No review has been performed. The agent's identity, capabilities, and behavior are entirely unconfirmed. Treat with maximum caution and restrict access accordingly.
- selfDeclared: The agent's developer or operator has described its behavior, but no one else has checked those claims. Suitable for internal or sandboxed use where the declaring party is trusted.
- thirdPartyReviewed: An independent party has audited the agent, but it has not been formally certified. Offers more confidence than self-declaration; suitable for controlled production use.
- certified: A recognized standards or certification body has formally verified the agent against defined criteria. Appropriate for high-stakes or regulated deployments.
