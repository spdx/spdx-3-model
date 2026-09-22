SPDX-License-Identifier: Community-Spec-1.0

# Role

## Summary

A Role defines a specific position, function, or capacity that an entity may assume within any relevant context.

## Description

A Role defines a specific position, function, or capacity that an entity may assume within any relevant context. This context is intentionally broad and adaptable, capable of representing environments including, but not limited to, software builds, system architectures, project management structures, distribution channels, supply chain operations, lifecycle stages, or any other domain where entities perform specific functions. The Role class provides a structured mechanism to model these functional assignments independently of the entities themselves, allowing for reusable and standardized definitions of responsibilities and privileges across different SPDX documents and ecosystems.

## Metadata

- name: Role
- SubclassOf: Element
- Instantiability: Concrete

## Properties

- referenceSpecification
  - type: DefinedType
  - minCount: 0
- roleQualification
  - type: Requirement
  - minCount: 1
- authorization
  - type: xsd:string
  - minCount: 0
- responsibility
  - type: Requirement
  - minCount: 0

## External properties restrictions

- /Core/Element/name
  - minCount: 1
