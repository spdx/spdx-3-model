SPDX-License-Identifier: Community-Spec-1.0

# AIAgent

## Summary

An AI agent.

## Description

An AI agent is a software agent that uses artificial intelligence techniques to guide its behavior. It typically incorporates a perception-action cycle, utilizing models and heuristics to perform goal-directed activities.

An AI agent's actions can involve varying degrees of automation or human oversight.

The following relationship types are also used to describe an AI agent's functionalities and interactions:

- hasPersistentMemory: Describes a relationship from the Agent to an element that functions as a persistent or long-term memory store.
- invokedBy: Describes a relationship from any Element back to the Agent that initiated its use or execution. (e.g., a Package is invokedBy an AIAgent; an AIAgent is invokedBy a Person).
- usesTool: Describes a relationship from the AIAgent to an Element that functions as a tool to expand the agent's capabilities.

## Metadata

- name: AIAgent
- SubclassOf: /Core/SoftwareAgent
- Instantiability: Concrete

## Properties

- /Core/suppliedBy
  - type: /Core/Agent
  - minCount: 0
- /Software/enabledByDefault
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- /Software/inputModality
  - type: /Core/Modality
  - minCount: 0
- /Software/outputModality
  - type: /Core/Modality
  - minCount: 0
- agentCapability
  - type: xsd:string
  - minCount: 0
- agentMemoryMode
  - type: xsd:string
  - minCount: 0
- automationLevel
  - type: AutomationLevel
  - minCount: 0
  - maxCount: 1