SPDX-License-Identifier: Community-Spec-1.0

# CreateProcess

## Summary

The CreateProcess refers to the abstract process class that can be used to represent the process of creation of a product.

## Description

The creation process refers to the systematic steps involved in bringing something new into existence. This can apply to products, ideas, businesses, art, software, and even life itself.

Relationship:

For every `CreateProcess`, there exists at least one `/Core/Relationship`
class or subclass with a `relationshipType` of 'hasOutput',
connecting the `CreateProcess` (from)
to a `/Core/Element` class or subclass (to).

## Metadata

- name: CreateProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Abstract

## External properties restrictions

- /Core/Element/description
  - minCount: 1
