SPDX-License-Identifier: Community-Spec-1.0

# UseProcess

## Summary

Use Process defines actions used by elements.

## Description

The UseProcess is an abstract class used to define processes that interact with key elements. Plan, state, and inspection processes plus managing boundaries are critical processes used by elements.

Relationship:

For each `UseProcess` or subclass except the `PlanProcess` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'affects’ on the from and a `/Core/Element` class or subclass on the to.

## Metadata

- name: UseProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Abstract

## External properties restrictions

- /Core/Element/description
  - minCount: 1
