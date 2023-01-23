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
- comment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- created
  - type: xsd:dateTime
- createdBy
  - type: Actor
  - minCount: 1
- profile
  - type: ProfileIdentifier
  - minCount: 1
- dataLicense
  - type: xsd:string

