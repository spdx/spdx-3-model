SPDX-License-Identifier: Community-Spec-1.0

# agentCommunicationProtocol

## Summary

Identifies a standardized communication protocol implemented by the AI agent
for interacting with external tools, data sources, or other agents.

## Description

Specifies the standardized communication protocol(s) that the AI agent
implements, enabling consumers, integrators, and automated tooling to determine
how the agent can be invoked, composed, or connected within a larger system.

<!-- Agent communication protocols define the message formats, interaction patterns,
and transport rules governing structured exchanges between an agent and external
entities—whether tools (agent-to-tool) or other agents (agent-to-agent).
Examples of widely adopted agent communication protocols include: Model Context
Protocol (MCP), Agent2Agent (A2A), Agent Network Protocol (ANP), Agent
Communication Protocol (AComP), Agent Connect Protocol (AConP), Agent
Interaction and Transaction Protocol (AITP), Coral Protocol, and Agora. -->

Each `agentCommunicationProtocol` entry is a `DictionaryEntry` where the key is
a short, human-readable protocol identifier and the value is the protocol
version or a URI pointing to the protocol specification.

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

- name: agentCommunicationProtocol
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
