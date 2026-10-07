SPDX-License-Identifier: Community-Spec-1.0

# UseAction

## Summary

The base class for actions performed by an agent that involve the use or handling of a product or element.

## Description

UseAction is an abstract class representing action in which an agent uses, interacts with, or applies a product or element.

Relationship:

For each `UseAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'performedBy’ on the from and a `/Core/Agent` class or subclass on the to.

For each `UseAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'affects’ or 'hasInput' on the from and a `/Core/Element` class or subclass on the to.

## Metadata

- name: UseAction
- SubclassOf: /Core/Action
- Instantiability: Abstract

## External properties restrictions

- /Core/Action/startTime
  - minCount: 1
