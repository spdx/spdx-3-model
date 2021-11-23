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

- name: Element
- SubclassOf: none
- Instantiability: Abstract

## Properties

- id
  - type: idString
  - minCount: 1
  - maxCount: 1
- name
  - type: xsd:string
  - maxCount: 1
- summary
  - type: xsd:string
  - maxCount: 1
- description
  - type: xsd:string
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1
- specVersion
  - type: xsd:string
- createdTime
  - type: xsd:dateTime
- createdBy
  - type: Identity
- profile
  - type: ProfileIdentifier
  - minCount: 1
- dataLicense
  - type: xsd:string
- externalReference
  - type: ExternalReference
- extension
  - type: Extension
- verifiedUsing
  - type: IntegrityMethod

