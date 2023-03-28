SPDX-License-Identifier: Community-Spec-1.0

# CreationInformation

## Summary

TODO

## Description

TODO

## Metadata

- name: CreationInformation
- Instantiability: Concrete

## Properties

- specVersion
  - type: SemVer
- created
  - type: xsd:dateTime
- createdBy
  - type: Entity
  - minCount: 1
- createdUsing
  - type: Tool
  - minCount: 0
- profile
  - type: ProfileIdentifier
  - minCount: 1
- dataLicense
  - type: xsd:string

