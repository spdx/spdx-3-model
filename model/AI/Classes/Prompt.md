SPDX-License-Identifier: Community-Spec-1.0

# Prompt

## Summary

Specifies a prompt content and its associated information.

## Description

Specifies a prompt content and its associated information.

A prompt is the input text, instruction, or data given to an AI model to
initiate and guide its generated output.

Properties and relationship types can be used for describing the prompt.
For example:

- The `/Software/primaryPurpose` and `/Software/additionalPurpose` properties
  can be used to describe the purpose of the prompt. For example, a system
  prompt's purpose might be described as "configuration" or "specification."
- The `/Software/contentIdentifier` property can be used to identify the
  prompt's content(s).
- The `/Core/contentModality` property can be used to describe the modality
  intended for the communication of the prompt content,
  such as `audio`, `image`, `text`, or `video`.
- The `/Core/contentType` property can be used to describe the prompt's
  physical content type, as stored in a computer memory, such as
  `application/json`, `image/png`, `text/markdown`, or `text/plain`.
- When `isContextAugmented` is set to `true`, a Relationship of type `usesTool`
  can be optionally used to describe the context augmentation mechanism or tool
  employed (e.g., referencing a retrieval-augmented generation tool).
  Context is the information provided to the model that shapes or influences
  its generated output.

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
- isContextAugmented
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- promptPattern
  - type: xsd:string
  - minCount: 0

## External properties restrictions

- /Software/SoftwareArtifact/contentIdentifier
  - type: /Software/ContentIdentifier
  - minCount: 1