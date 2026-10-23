SPDX-License-Identifier: Community-Spec-1.0

# Element

## Summary

Base domain class from which all other SPDX 3 domain classes derive.

## Description

An Element is a representation of a fundamental concept either directly inherent
to the Bill of Materials (BOM) domain or indirectly related to the BOM domain
and necessary for contextually characterizing BOM concepts and relationships.

Within the SPDX 3 structure, this is the base class that acts as a consistent,
unifying, and interoperable foundation for all explicit
and inter-relatable content objects.

An Element may have one or more names.
If a primary name is specified, it shall be recorded using the `name` property.
Any additional names shall be recorded using the `additionalName` property.

## Metadata

- name: Element
- SubclassOf: none
- Instantiability: Abstract

## Properties

- spdxId
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- name
  - type: xsd:string
  - maxCount: 1
- additionalName
  - type: xsd:string
- summary
  - type: xsd:string
  - maxCount: 1
- description
  - type: xsd:string
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1
- creationInfo
  - type: CreationInfo
  - minCount: 1
  - maxCount: 1
- verifiedUsing
  - type: IntegrityMethod
- externalRef
  - type: ExternalRef
  - minCount: 0
- externalIdentifier
  - type: ExternalIdentifier
  - minCount: 0
- extension
  - type: /Extension/Extension
  - minCount: 0
