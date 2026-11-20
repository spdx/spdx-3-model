SPDX-License-Identifier: Community-Spec-1.0

# Prompt

## Summary

Represents a prompt — instructions and directly accompanying content
provided to an AI system by an external entity to guide its output.

## Description

A prompt is instructions, including directly accompanying natural language
text, documents, code, and/or media, provided to an AI system by an external
entity (human or otherwise), beyond the AI system's static models, programming,
and configuration files, to inform its output.

Prompts are categorized by their role (see `promptRole`):

- A **user prompt** is provided by a user (human or AI agent) and is associated
  with a single query.
- A **system prompt** is provided by the system's owner or administrator to
  inform the system's overall behavior for every query or instruction.
  In agentic contexts, system prompts are sometimes referred to as
  "instructions."

Context is the structured set of information provided to an AI system, model,
or agent at inference time — for example, the system prompt, the user prompt,
context history (including past prompts, outputs, and other session data that
may be compressed or windowed), and relevant grounding documents — that
influences the AI system's outputs and behaviour.

Properties and relationship types can be used for describing the prompt.
For example:

- The `promptRole` property can be used to indicate whether this is a
  `user` or `system` prompt.
- The `/Software/primaryPurpose` and `/Software/additionalPurpose` properties
  can be used to describe the purpose of the prompt. For example, a system
  prompt's purpose might be described as `configuration` or `specification`.
- The `/Software/contentIdentifier` property can be used to identify the
  prompt's content(s). Every `Prompt` must have at least one content
  identifier.
- The `/Core/contentModality` property can be used to describe the modality
  intended for the communication of the prompt content,
  such as `audio`, `image`, `text`, or `video`.
- The `/Core/contentType` property can be used to describe the prompt's
  physical content type, as stored in a computer memory, such as
  `application/json`, `image/png`, `text/markdown`, or `text/plain`.
- The `/Dataset/confidentialityLevel` property can be used to record the
  confidentiality of the prompt, for example when a system prompt is a
  proprietary trade secret.
- When `isContextAugmented` is set to `true`, a Relationship of type `usesTool`
  can be optionally used to describe the context augmentation mechanism or tool
  employed (e.g., referencing a retrieval-augmented generation tool).

## Metadata

- name: Prompt
- SubclassOf: /Software/SoftwareArtifact
- Instantiability: Concrete

## Properties

- /Core/inLanguage
  - type: /Core/LanguageTag
  - minCount: 0
- /Core/contentModality
  - type: /Core/Modality
  - minCount: 0
- /Core/contentType
  - type: /Core/MediaType
  - minCount: 0
- /Dataset/dataCollectionProcess
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- /Dataset/dataPreprocessing
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- /Dataset/hasSensitivePersonalInformation
  - type: /Core/PresenceType
  - minCount: 0
  - maxCount: 1
- /Dataset/confidentialityLevel
  - type: /Dataset/ConfidentialityLevelType
  - minCount: 0
  - maxCount: 1
- isContextAugmented
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- promptPattern
  - type: xsd:string
  - minCount: 0
- promptRole
  - type: PromptRoleType
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Software/SoftwareArtifact/contentIdentifier
  - type: /Software/ContentIdentifier
  - minCount: 1
