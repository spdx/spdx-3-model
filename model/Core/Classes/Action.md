SPDX-License-Identifier: Community-Spec-1.0

# Action

## Summary

Class that describes an action that has occurred.

## Description

Action defines an event that has occurred. This is an Abstract Action.

`startTime` is the time at which an action starts or triggered.
`endTime` is the time at which an action stops or finishes.

## Metadata

- name: Action
- SubclassOf: Artifact
- Instantiability: Abstract

## Properties

- actionLocation
  - type: Location
  - minCount: 0
- additionalInformation
  - type: DictionaryEntry
  - minCount: 0
- endTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- startTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Artifact/originatedBy
  - minCount: 1
