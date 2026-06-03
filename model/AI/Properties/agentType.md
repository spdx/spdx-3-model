SPDX-License-Identifier: Community-Spec-1.0

# agentType

## Summary

Classifies the communication and interaction role of the AI agent within a
multi-agent system or agentic workflow.

## Description

A controlled classification that describes the structural role an AI agent
assumes in terms of how it communicates and interacts with other agents and
orchestration systems. Analogous to `typeOfModel` for AI models, `agentType`
answers "what kind of agent is this?" from an interaction standpoint, not from
a capability or task standpoint.

An agent may declare multiple values when it simultaneously holds more than one
role (e.g., a worker toward an upstream orchestrator that itself orchestrates
a sub-group of specialist agents).

Domain-level task abilities (what the agent can do) are recorded separately
using `agentCapability`.

**Values:** see `AI/AgentType` vocabulary.

## Metadata

- name: agentType
- Nature: ObjectProperty
- Range: AgentType
