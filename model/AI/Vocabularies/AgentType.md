SPDX-License-Identifier: Community-Spec-1.0

# AgentType

## Summary

Classifies the communication and interaction role of an AI agent within a
multi-agent system or agentic workflow.

## Description

AgentType is an enumeration that categorizes the structural role an AI agent
assumes in terms of how it communicates and interacts with other agents and
orchestration systems.

## Metadata

- name: AgentType

## Entries

- orchestrator: The agent initiates and decomposes high-level goals into sub-tasks, delegates those sub-tasks to other agents, and aggregates their results into a final outcome.
- worker: The agent receives a delegated task from an orchestrator or controller, executes it using its own capabilities and tools, and returns the result.
- peer: The agent participates in symmetric, decentralized multi-agent collaboration without a fixed coordinator or worker hierarchy.
