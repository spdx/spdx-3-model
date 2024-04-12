SPDX-License-Identifier: Community-Spec-1.0

# DatasetPackage

## Summary

Specifies a data package and its associated information.

## Description

Metadata information that can be added to a dataset that may be used in a software or to train/test an AI package.

## Metadata

- name: DatasetPackage
- SubclassOf: /Software/Package
- Instantiability: Concrete

## Properties

- datasetType
  - type: DatasetType
  - minCount: 1
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
- sensor
  - type: /Core/DictionaryEntry
  - minCount: 0
- knownBias
  - type: xsd:string
  - minCount: 0
- hasSensitivePersonalInformation
  - type: /Core/PresenceType
  - minCount: 0
  - maxCount: 1
- anonymizationMethodUsed
  - type: xsd:string
  - minCount: 0
- confidentialityLevel
  - type: ConfidentialityLevelType
  - minCount: 0
  - maxCount: 1
- datasetUpdateMechanism
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- datasetAvailability
  - type: DatasetAvailabilityType
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Artifact/originatedBy
  - minCount: 1
  - maxCount: 1
- /Software/Package/downloadLocation
  - minCount: 1
  - maxCount: 1
- /Software/SoftwareArtifact/primaryPurpose
  - minCount: 1
  - maxCount: 1
- /Core/Artifact/releaseTime
  - minCount: 1
  - maxCount: 1
- /Core/Artifact/builtTime
  - minCount: 1
  - maxCount: 1
