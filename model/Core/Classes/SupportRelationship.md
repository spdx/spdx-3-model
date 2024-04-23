SPDX-License-Identifier: Community-Spec-1.0

# SupportRelationship

## Summary

Describes how an Agent Provides Support for an Element

## Description

Specifies how an Agent supports a given Element. The Relationship Type must be
`providesSupportFor`. The `from` of the relationship is the `Agent` providing
support, and the `to` are the `Artifact` for which support is being provided.

`startTime` and `endTime` are mandatory when using this class.

## Metadata

- name: SupportRelationship
- SubclassOf: Relationship
- Instantiability: Concrete

## Properties

- supportLevel
  - type: SupportType
  - minCount: 1
  - maxCount: 1

## External properties restrictions

- /Core/Relationship/startTime
  - minCount: 1
  - maxCount: 1
- /Core/Relationship/endTime
  - minCount: 1
  - maxCount: 1
