SPDX-License-Identifier: Community-Spec-1.0

# SupportRelationship

## Summary

Describes how an Agent provides support for an Artifact.

## Description

Specifies how an Agent supports a given Artifact. The relationship type shall be
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
- /Core/Relationship/endTime
  - minCount: 1
