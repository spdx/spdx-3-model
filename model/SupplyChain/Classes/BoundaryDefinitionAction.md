SPDX-License-Identifier: Community-Spec-1.0

# BoundaryDefinitionAction

## Summary

The boundary definition is used to define boundaries.

## Description

Boundaries can be physical or abstract. This is the act of defining the boundaries.

Relationship:

For each `BoundaryDefinitionAction` there is one and only one `/Core/Relationship` class or subclass with the relationshipType of `createdBy` on the to and a `/Core/Agent` class or subclass on the from.

## Metadata

- name: BoundaryDefinitionAction
- SubclassOf: /Core/Action
- Instantiability: Concrete

## Properties

- boundaryParameter
  - type: /Core/DictionaryEntry
  - minCount: 1

## External properties restrictions

- /Core/Element/description
  - minCount: 1
