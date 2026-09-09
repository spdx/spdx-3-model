SPDX-License-Identifier: Community-Spec-1.0

# AIAgent

## Summary

Specifies an AI agent and its associated metadata.

## Description

An AI agent is a software entity that uses artificial intelligence techniques to perceive its environment, reason about its state, use available tools, and take actions to achieve specified goals.

The following relationship types are also used to describe an AI agent's functionalities and interactions:

- invokedBy: Describes a relationship from any Element back to the Agent that initiated its execution (e.g., a Package is invokedBy an AIAgent; an AIAgent is invokedBy a Person).
- usesTool: Describes a relationship from the AIAgent to an Element that the agent uses as a tool to extend its capabilities. This also covers external resources, APIs, services, or knowledge bases that the agent can access or invoke: model the resource as a `/Core/Tool` and use its `externalRef` property to point to the URI, package URL, or other reference that locates the resource's definition or specification.
- usesModel: Describes a relationship from the AIAgent to an AIPackage that represents the underlying AI model the agent relies on (e.g., its model weights, training data, and safety assessments), enabling BOM consumers to trace from an agent to its associated model artifacts.

## Metadata

- name: AIAgent
- SubclassOf: /Core/SoftwareAgent
- Instantiability: Concrete

## Properties

- /Software/inputModality
  - type: /Core/Modality
  - minCount: 0
- /Software/outputModality
  - type: /Core/Modality
  - minCount: 0
- agentCapability
  - type: xsd:string
  - minCount: 0
- agentCommunicationProtocol
  - type: /Core/Specification
  - minCount: 0
- agentMemoryMode
  - type: AgentMemoryMode
  - minCount: 0
- agentTrustLevel
  - type: AgentTrustLevel
  - minCount: 0
  - maxCount: 1
- limitation
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- safetyRiskAssessment
  - type: SafetyRiskAssessmentType
  - minCount: 0
  - maxCount: 1
