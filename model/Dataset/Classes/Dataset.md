SPDX-License-Identifier: Community-Spec-1.0

# Dataset

## Summary

Provides information about the fields in the Dataset profile.

## Description

Metadata information that can be added to a dataset that may be used in a software or to train/test an AI package.

## Metadata

- name: Dataset
- SubclassOf: /Software/Package
- Instantiability: Concrete

## Properties

- dataCollectionProcess
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- intendedUse
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- datasetSize
  - type: xsd:nonNegativeInteger
  - minCount: 0
  - maxCount: 1
- datasetNoise
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- dataPreprocessing
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- sensor
  - type: /Core/DictionaryEntry
  - minCount: 0
- knownBias
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
- datasetAvailability
  - type: DatasetAvailabilityType
  - minCount: 0
  - maxCount: 1
