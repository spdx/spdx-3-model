SPDX-License-Identifier: Community-Spec-1.0

# Hardware

## Summary

Class that describes an instance of Hardware.

## Description

A hardware artifact is a distinct unit related to hardware.

## Metadata

- name: Hardware
- SubclassOf: /Core/Artifact
- Instantiability: Abstract

## Properties

- productAgent
  - type: /Core/Agent
  - minCount: 1
  - maxCount: 1
- hardwareVersion
  - type: xsd:string
  - maxCount: 1
- partNumber
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- releaseDate
  - type: /Core/DateTime
  - maxCount: 1
- serialNumber
  - type: xsd:string
  - maxCount: 1
- batchNumber
  - type: xsd:string
  - maxCount: 1
- hazard
  - type: /Core/DefinedType
- category
  - type: /Core/DefinedType
- additionalInformationSpecification
  - type: /Core/Specification
- additionalInformation
  - type: /Core/DictionaryEntry
  - minCount: 0

## External properties restrictions

- /Core/Artifact/originatedBy
  - maxCount: 0
- /Core/Artifact/suppliedBy
  - maxCount: 0
- /Core/Artifact/builtTime
  - maxCount: 0
- /Core/Artifact/releaseTime
  - maxCount: 0
- /Core/Artifact/standardName
  - maxCount: 0
- /Core/Artifact/supportLevel
  - maxCount: 0
