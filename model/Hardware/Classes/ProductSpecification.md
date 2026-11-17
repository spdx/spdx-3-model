SPDX-License-Identifier: Community-Spec-1.0

# ProductSpecification

## Summary

A document that defines requirements for a hardware product.

## Description

A ProductSpecification represents a document that defines the technical, functional, and design requirements for a hardware product. It can identify the applicable product by part number, record the specification version, and describe hazards associated with the product.

Product specifications provide requirements and constraints used by engineers, designers, manufacturers, and other parties throughout the product lifecycle.

## Metadata

- name: ProductSpecification
- SubclassOf: /Core/Specification
- Instantiability: Concrete

## Properties

- /Core/version
  - type: xsd:string
- hazard
  - type: /Core/DefinedType
- partNumber
  - type: xsd:string
  - minCount: 1
