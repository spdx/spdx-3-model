SPDX-License-Identifier: Community-Spec-1.0

# ProductSpecification

## Summary

A product specification (product spec) is a detailed document that outlines the technical, functional, and design requirements of a product.

## Description

A product specification (product spec) is a detailed document that outlines the technical, functional, and design requirements of a product. It serves as a guide for engineers, designers, and manufacturers to ensure the final product meets expectations.

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
- modelNumber
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
