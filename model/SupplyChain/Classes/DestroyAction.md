SPDX-License-Identifier: Community-Spec-1.0

# DestroyAction

## Summary

The record of destruction is entered in this action.

## Description

The action of destroying an element is recorded as part of the DestroyAction. To destroy refers to the act of completely eliminating, or rendering something unusable or irretrievable.

## Metadata

- name: DestroyAction
- SubclassOf: /Core/Action
- Instantiability: Concrete

## Properties

- destructionPerformedBy
  - type: /Core/Agent
  - minCount: 1

## External properties restrictions

- /Core/Action/endTime
  - minCount: 1
- /Core/Action/startTime
  - minCount: 1
- /Core/Element/description
  - minCount: 1
