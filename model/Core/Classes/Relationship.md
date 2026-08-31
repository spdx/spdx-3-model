SPDX-License-Identifier: Community-Spec-1.0

# Relationship

## Summary

Describes a relationship between one or more elements.

## Description

A Relationship is a grouping of characteristics unique to an assertion
that one Element is related to one or more other Elements in some way.

To explicitly assert that no such relationships exist, the `to` property
shall contain the NoneElement individual and no other elements.

A relationship that contains NoneElement and additional elements in the `to`
property is not valid.

To explicitly assert that no assertions are being made regarding the
existence of such relationships, the `to` property shall contain the
NoAssertionElement individual.

A relationship can be either directional or non-directional (directionless).
For a directional relationship,
the direction of a relationship is always from the `from` Element to the
`to` Element, as defined by the `relationshipType` property.

A relationship can be temporally scoped by using the optional `startTime` and
`endTime` properties.

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
  - minCount: 1
  - maxCount: 1
- completeness
  - type: RelationshipCompleteness
  - minCount: 0
  - maxCount: 1
- startTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- endTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
