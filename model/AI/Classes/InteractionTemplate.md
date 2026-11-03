SPDX-License-Identifier: Community-Spec-1.0

# InteractionTemplate

## Summary

An artifact that defines the structure, formatting, and variable placeholders for AI model interactions.

## Description

Represents a parameterized template specification used to construct prompts, payloads, or structured requests for AI models. It supports flexible template instantiation through either a raw text string with placeholder syntax or a structured dictionary of variables and configuration parameters.

If the template’s role is:

- Inference (chat) template: `from` /AI/AIPackage or /AI/AIAgent via a /Core/LifecycleScopedRelationship with `relationshipType` = 'configures'. The `scope` = 'runtime', and `to` a class of type /AI/InteractionTemplate.
- training template: `from` /AI/AIPackage or /AI/AIAgent via a /Core/LifecycleScopedRelationship with `relationshipType` = 'trainedOn'. The `scope` = 'runtime', and `to` a class of type /AI/InteractionTemplate.
- pretrained template: `from` /AI/AIPackage or /AI/AIAgent via a /Core/LifecycleScopedRelationship with `relationshipType` = 'pretrainedOn'. The `scope` = 'runtime', and  `to` a class of type /AI/InteractionTemplate.
- finetuned template: `from` /AI/AIPackage or /AI/AIAgent via a /Core/LifecycleScopedRelationship with `relationshipType` = 'finetunedOn'. The `scope` = 'runtime', and `to` a class of type /AI/InteractionTemplate.

## Metadata

- name: InteractionTemplate
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- interactionTemplateString
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- interactionTemplateDictionary
  - type: /Core/DictionaryEntry
  - minCount: 0
