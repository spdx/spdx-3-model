SPDX-License-Identifier: Community-Spec-1.0

# agentProtocol

## Summary

Identifies a communication protocol supported by the AI agent for interacting with external tools, data sources, or other agents.

## Description

Specifies the standardized communication protocol(s) that the AI agent implements, enabling consumers, integrators, and automated tooling to determine how the agent can be invoked, composed, or connected within a larger system.

Agent protocols define the rules, formats, and procedures for structured communication between an agent and external entities. Examples of widely adopted agent protocols include: Model Context Protocol (MCP), Agent2Agent (A2A), Agent Network Protocol (ANP), Agent Communication Protocol (AComP), Agent Connect Protocol (AConP), Agent Interaction and Transaction Protocol (AITP), Coral Protocol, and Agora.

Each `agentProtocol` entry is a `DictionaryEntry` where the key is a short, human-readable protocol identifier and the value is the protocol version or a URI pointing to the protocol specification.

*Examples*

```text
MCP: 1.2
```

```text
A2A: https://github.com/google/A2A
```

```text
ANP: https://www.agent-network-protocol.com/
```

```text
AConP: https://spec.acp.agntcy.org/
```

## Metadata

- name: agentProtocol
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
