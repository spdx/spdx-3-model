SPDX-License-Identifier: Community-Spec-1.0

# ResolutionAction

## Summary

Products out of specification require a resolution action. This is the action of resolution.

## Description

Products out of specification require a resolution action. This is the action of resolution.

Relationship:
For each `ResolutionAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'resolved’ on the from and an `OutOfSpecAction` class or subclass on the to.

## Metadata

- name: ResolutionAction
- SubclassOf: UseAction
- Instantiability: Concrete

## External properties restrictions

- /Core/Element/description
  - minCount: 1
