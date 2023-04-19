SPDX-License-Identifier: Community-Spec-1.0

# AIPackage

## Summary

Provides information about the fields in the AI package profile.

## Description

Metadata information that can be added to a package to describe an AI application or trained AI model. 

## Metadata

- name: AIPackage
- SubclassOf: /Software/Package
- Instatiability: Concrete

## Properties

- energyConsumption
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- standardsCompliance
  - type: xsd:string
  - minCount: 0
- limitations
  - type: xsd:string
  - minCount: 0
  - maxCount:1
- typeOfModel
  - type: xsd:string
  - minCount: 0
- informationAboutTraining
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- informationAboutApplication
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- hyperparameters
  - type: /Core/DictionaryEntry
  - minCount: 0
- dataPreprocessingSteps
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- modelExplainabilityMechanisms
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- sensitivePersonalInformation
  - type: PresenceType
  - minCount: 0
  - maxCount: 1
- metricsDecisionThresholds
  - type: /Core/DictionaryEntry
  - minCount: 0
- metrics
  - type: /Core/DictionaryEntry
  - minCount: 0
- domain
  - type: xsd:string
  - minCount: 0
- autonomyType
  - type: PresenceType
  - minCount: 0
  - maxCount: 1
- safetyRiskAssessment
  - type: SafetyRiskAssessmentType
  - minCount: 0
  - maxCount: 1
