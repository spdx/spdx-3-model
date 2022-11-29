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
  - type: Actor
  - minCount: 1
- profile
  - type: ProfileIdentifier
  - minCount: 1
- dataLicense
  - type: xsd:string

