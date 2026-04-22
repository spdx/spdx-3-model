SPDX-License-Identifier: Community-Spec-1.0

# AgentType

## Summary

Defines the structural role of an AI agent within a multi-agent system.

## Description

AgentType is an enumeration that categorizes the interaction role of an AI agent within a multi-agent system (MAS) or agentic workflow. It describes the agent's position in the task delegation hierarchy, independent of its capabilities or degree of automation.

AgentType is informed by established inter-agent protocol specifications, including Google's Agent2Agent Protocol (A2A), the Agent Network Protocol (ANP), the Agent Connect Protocol (AConP), the Coral Protocol, and the Agora meta-protocol, and is consistent with the two-dimensional taxonomy of agent protocols.

## Metadata

- name: AgentType

## Entries

- orchestrator: The agent initiates and decomposes high-level goals into sub-tasks, delegates those sub-tasks to other agents, and aggregates their results into a final outcome. The orchestrator controls the overall workflow and is responsible for task assignment and result synthesis. Corresponds to the client agent role in A2A and the coordinator role in the Coral Protocol.
- worker: The agent receives a delegated task from an orchestrator or controller, executes it using its own capabilities and tools, and returns the result. The worker does not direct other agents in the context of the delegated task. Corresponds to the remote agent role in A2A and the invoked agent role in AConP.
- peer: The agent participates in symmetric, decentralized multi-agent collaboration without a fixed coordinator or worker hierarchy. Any peer may initiate interactions with any other peer; communication protocols and task assignments are negotiated dynamically. Corresponds to agents-on-the-internet in ANP and networked LLM nodes in Agora.
