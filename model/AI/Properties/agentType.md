SPDX-License-Identifier: Community-Spec-1.0

# agentType

## Summary

Indicates the structural role of the AI agent within a multi-agent system.

## Description

Specifies the interaction role that an AI agent assumes within a multi-agent
system (MAS) or agentic workflow. The agent type characterizes how the agent
relates to other agents and to the overall task structure, determining its
responsibilities with respect to task initiation, delegation, coordination,
and execution.

An agent may declare multiple values (e.g., an agent that acts as a worker
toward an upstream orchestrator but itself orchestrates a sub-group of
specialist agents).

## Metadata

- name: agentType
- Nature: ObjectProperty
- Range: AgentType
