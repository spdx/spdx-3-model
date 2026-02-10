SPDX-License-Identifier: Community-Spec-1.0

# CreateAction

## Summary

CreationAction represents an event of product creation.

## Description

CreationAction represents the lifecycle event of Product creation. A product could be manufactured, assembled, mined/extracted directly from the nature etc.

Relationship:

For each `CreateAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'hasOutput’ on the from and a `/Core/Element` class or subclass on the to.

## Metadata

- name: CreateAction
- SubclassOf: /Core/Action
- Instantiability: Abstract

## External properties restrictions

- /Core/Action/startTime
  - minCount: 1
