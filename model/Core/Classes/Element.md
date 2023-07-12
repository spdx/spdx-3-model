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
- SubclassOf: owl:Thing
- Instantiability: Abstract

## Properties

- spdxId
  - type: xsd:anyURI
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
- creationInfo
  - type: CreationInfo
  - minCount: 1
  - maxCount: 1
- verifiedUsing
  - type: IntegrityMethod
- externalReference
  - type: ExternalReference
  - minCount: 0
- externalIdentifier
  - type: ExternalIdentifier
  - minCount: 0
- extension
  - type: Extension
  - minCount: 0

