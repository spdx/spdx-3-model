SPDX-License-Identifier: Community-Spec-1.0

# DefinedType

## Summary

The DefinedType class associates a specific type with its defined source.

## Description

The DefinedType class associates a specific type with its defined source.
It provides a structured way to represent defined types, holds information about the type's identity and the source specification that defines its structure and semantics.

## Metadata

- name: DefinedType
- Instantiability: Concrete

## Properties

- typeFromSource
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- definitionSource
  - type: Specification
  - minCount: 1
  - maxCount: 1
  