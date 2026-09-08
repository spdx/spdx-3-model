SPDX-License-Identifier: Community-Spec-1.0

# ModifyAction

## Summary

An actual alteration of a product.

## Description

A ModifyAction is an action that alters a product, such as a change to its configuration or its location.

Relationship:

For each `ModifyAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of `hasOutput` on the `from` and a `/Core/Element` subclass on the `to`.

For each `ModifyAction` there is at least one `/Core/Relationship` class or subclass with the relationshipType of `performedBy` on the `from` and a `/Core/Element` subclass on the `to`.

## Metadata

- name: ModifyAction
- SubclassOf: /Core/Action
- Instantiability: Abstract

## External properties restrictions

- /Core/Action/startTime
  - minCount: 1
