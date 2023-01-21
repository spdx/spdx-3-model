SPDX-License-Identifier: Community-Spec-1.0

# Relationship

## Summary

Describes a relationship between one or more elements.

## Description

A Relationship is a grouping of characteristics unique to an assertion
that one Element is related to one or more other Elements in some way.


## Metadata

- name: Relationship
- SubclassOf: Element
- Instantiability: Concrete


## Properties

- from
  - type: Element
  - minCount: 1
  - maxCount: 1
- to
  - type: Element
  - minCount: 1
- relationshipType
  - type: RelationshipType
  - maxCount: 1
- completeness
  - type: RelationshipCompleteness
  - minCount: 0
  - maxCount: 1

