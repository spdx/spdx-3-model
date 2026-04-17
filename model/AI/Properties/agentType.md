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

This property captures a structural and architectural fact about the agent as
deployed, distinct from:

- `agentCapability`, which lists what tasks the agent can perform;
- `automationLevel`, which characterizes the agent's degree of autonomy relative
  to human oversight;
- `agentProtocol`, which records the communication protocol(s) the agent
  supports.

Recognized role values are defined in `AgentType`:

- An `orchestrator` agent decomposes a high-level goal into sub-tasks and
  delegates them to other agents, then aggregates the results. It controls the
  overall workflow. In inter-agent protocol terminology (A2A: client agent;
  Coral: coordinator), this is the agent that initiates task assignment.

- A `worker` agent receives a delegated task from an orchestrator, executes it
  using its capabilities and tools, and returns the result. It does not
  typically direct other agents. In inter-agent protocol terminology (A2A:
  remote agent; AConP: invoked agent), this is the agent that fulfills task
  requests.

- A `peer` agent participates in symmetric, decentralized multi-agent
  collaboration without a fixed coordinator or worker hierarchy. Any peer can
  initiate interactions with any other peer. In inter-agent protocol terminology
  (ANP: agent-on-the-internet; Agora: networked LLM node), peers negotiate
  communication protocols and coordinate as equals.

An agent may declare multiple values (e.g., an agent that acts as a worker
toward an upstream orchestrator but itself orchestrates a sub-group of
specialist agents).

## Metadata

- name: agentType
- Nature: ObjectProperty
- Range: AgentType
