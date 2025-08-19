SPDX-License-Identifier: Community-Spec-1.0

# agentInputModality

## Summary

Indicates the input modalities accepted by the AI agent (e.g., text, structured data, images, audio).

## Description

Describes the forms of input the agent can process when receiving tasks or interacting with users. This includes natural language text, structured data (e.g., JSON, CSV), visual inputs (e.g., images, diagrams), and audio inputs (e.g., speech, sound). Multimodal may be specified if the agent supports more than one input modality.  
If no inputs are accepted or the modality is unknown, set to NONE or NOASSERTION, respectively.
## Metadata
- name: agentInputModality
- Nature: ObjectProperty
- Range: ModalityType
