SPDX-License-Identifier: Community-Spec-1.0

# agentCommunicationProtocol

## Summary

Identifies a standardized communication protocol implemented by the AI agent
for interacting with external tools, data sources, or other agents.

## Description

Specifies the standardized communication protocol(s) that the AI agent
implements, enabling consumers, integrators, and automated tooling to determine
how the agent can be invoked, composed, or connected within a larger system.

Each `agentCommunicationProtocol` entry references a `Specification` Element
that describes the protocol. The `Specification`'s `name` identifies the
protocol, its `externalIdentifier` (e.g., a `webpage` identifier) locates the
protocol's authoritative definition or version.

*Examples*

Protocols that can be described this way include the Model Context Protocol
(MCP), Agent2Agent (A2A), the Agent Network Protocol (ANP), and the Agent
Connect Protocol (AConP).

## Metadata

- name: agentCommunicationProtocol
- Nature: ObjectProperty
- Range: /Core/Specification
