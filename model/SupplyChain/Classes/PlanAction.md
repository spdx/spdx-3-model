SPDX-License-Identifier: Community-Spec-1.0

# PlanAction

## Summary

A PlanAction involves the execution of a plan in relation to a PlanProcess.

## Description

A PlanAction involves the execution of a plan in relation to a PlanProcess.

The description of the PlanAction is a mandatory property.

Relationship:

For each `PlanAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'generates’ on the to and a `PlanProcess` class or subclass on the from.

## Metadata

- name: PlanAction
- SubclassOf: UseAction
- Instantiability: Concrete

## External properties restrictions

- /Core/Element/description
  - minCount: 1
