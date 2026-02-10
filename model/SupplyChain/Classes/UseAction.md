SPDX-License-Identifier: Community-Spec-1.0

# UseAction

## Summary

The action of product use.

## Description

This is the specific action of product use.

Relationship:

For each `UseAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'performedBy’ on the from and a `/Core/Agent` class or subclass on the to.

For each `UseAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'affects’ on the from and a `/Core/Element` class or subclass on the to.

## Metadata

- name: UseAction
- SubclassOf: /Core/Action
- Instantiability: Abstract

## External properties restrictions

- /Core/Action/startTime
  - minCount: 1
