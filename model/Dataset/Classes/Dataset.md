SPDX-License-Identifier: Community-Spec-1.0

# Dataset

## Summary

Provides information about the fields in the Dataset profile.

## Description

Metadata information that can be added to a a dataset that maybe used in a software or to train/test an AI package

## Metadata

- name: Dataset
- SubclassOf: Software:Package
- Instatiability: Concrete

## Properties

- dataCollectionProcess
  - type: xsd:string
  - minCount: 0
  - maxCount:1
- intendedUse
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- datasetSize
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- datasetNoise
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- dataPreprocessingSteps
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- sensors
  - type: xsd:string
  - minCount: 0
- knownBiases
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- sensitivePersonalInformationType
  - type: PresenceType
  - minCount: 0
- anonymizationMethodUsed
  - type: xsd:string
  - minCount: 0
- confidentialityLevelType
  - type: ConfidentialityLevelType
  - minCount: 0
- datasetUpdateMechanism
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
