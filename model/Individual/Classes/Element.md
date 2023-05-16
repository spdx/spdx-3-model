SPDX-License-Identifier: Community-Spec-1.0

# Element

## Summary

Base domain class from which all other SPDX-3.0 domain classes derive.

## Description

An Element is a representation of a fundamental concept either directly inherent
to the Bill of Materials (BOM) domain or indirectly related to the BOM domain
and necessary for contextually characterizing BOM concepts and relationships.
Within SPDX-3.0 structure this is the base class acting as a consistent,
unifying, and interoperable foundation for all explicit
and inter-relatable content objects.

## Metadata

- name: /Core/Element/Element
- SubclassOf: /Core/Element/Payload
- Instantiability: Abstract

## Properties

## External properties restrictions

- creationInfo
  - type: /Core/Element/CreationInfo
  - minCount: 1
  - maxCount: 1


