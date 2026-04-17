SPDX-License-Identifier: Community-Spec-1.0

# ModifyProcess

## Summary

A prescribed alteration of a product.

## Description

A ModifyProcess is a process that will result in the alteration of a product, such as a change to its configuration or its location.

Relationship:

For each `ModifyProcess` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'hasOutput’ on the `from` and a `/Core/Element` subclass on the `to`.

For each `ModifyProcess` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'hasInput’ on the `from` and a `/Core/Element` subclass on the `to`.

## Metadata

- name: ModifyProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Abstract

## External properties restrictions

- /Core/Element/description
  - minCount: 1
