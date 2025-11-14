SPDX-License-Identifier: Community-Spec-1.0

# Action

## Summary

Class that describes an action that has occurred.

## Description

Action defines an event that has occurred. This is an Abstract Action. 

## Metadata

- name: Action
- SubclassOf: Artifact
- Instantiability: Abstract

## Properties

- actionStartTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- actionEndTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- actionLocation
  - type: Location
  - minCount: 0
- additionalInformation
  - type: DictionaryEntry
  - minCount: 0
  
## External properties restrictions

- /Core/Artifact/originatedBy
  - minCount: 1
