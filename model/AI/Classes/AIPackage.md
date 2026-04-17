SPDX-License-Identifier: Community-Spec-1.0

# AIPackage

## Summary

A Package that contains AI software or an AI model.

## Description

A Package that contains code or a model that provides
artificial intelligence capabilities.

## Metadata

- name: AIPackage
- SubclassOf: /Software/Package
- Instantiability: Concrete

## Properties

- /Core/isoAutomationLevel
  - type: /Core/IsoAutomationLevel
  - minCount: 0
  - maxCount: 1
- autonomyType
  - type: /Core/PresenceType
  - minCount: 0
  - maxCount: 1
- domain
  - type: xsd:string
  - minCount: 0
- energyConsumption
  - type: EnergyConsumption
  - minCount: 0
  - maxCount: 1
- hyperparameter
  - type: /Core/DictionaryEntry
  - minCount: 0
- informationAboutApplication
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- informationAboutTraining
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- limitation
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- metric
  - type: /Core/DictionaryEntry
  - minCount: 0
- metricDecisionThreshold
  - type: /Core/DictionaryEntry
  - minCount: 0
- modelDataPreprocessing
  - type: xsd:string
  - minCount: 0
- modelExplainability
  - type: xsd:string
  - minCount: 0
- safetyRiskAssessment
  - type: SafetyRiskAssessmentType
  - minCount: 0
  - maxCount: 1
- standardCompliance
  - type: xsd:string
  - minCount: 0
- typeOfModel
  - type: xsd:string
  - minCount: 0
- useSensitivePersonalInformation
  - type: /Core/PresenceType
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Software/SoftwareArtifact/primaryPurpose
  - minCount: 1
