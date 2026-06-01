SPDX-License-Identifier: Community-Spec-1.0

# agentCommunicationProtocol

## Summary

Identifies a standardized communication protocol implemented by the AI agent
for interacting with external tools, data sources, or other agents.

## Description

Specifies the standardized communication protocol(s) that the AI agent
implements, enabling consumers, integrators, and automated tooling to determine
how the agent can be invoked, composed, or connected within a larger system.

Each `agentCommunicationProtocol` entry is a `DictionaryEntry` where the key is
a human-readable protocol identifier and the value is the protocol
version or a URI pointing to the protocol specification.

*Examples*

```text
Model Context Protocol (MCP): 1.2
```

```text
Agent2Agent (A2A): https://github.com/google/A2A
```

```text
Agent Network Protocol (ANP): https://www.agent-network-protocol.com/
```

```text
Agent Connect Protocol (AConP): https://spec.acp.agntcy.org/
```

## Metadata

- name: agentCommunicationProtocol
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
