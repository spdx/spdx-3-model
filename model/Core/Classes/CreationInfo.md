SPDX-License-Identifier: Community-Spec-1.0

# CreationInfo

## Summary

Provides information about the creation of the Element.

## Description

The CreationInfo provides information about who created the Element, and when and how it was created. 

The dateTime created is often the date of last change (e.g., a git commit date), not the date when the SPDX data was created, as doing so supports reproducible builds.

## Metadata

- name: CreationInfo
- Instantiability: Concrete

## Properties

- specVersion
  - type: SemVer
  - minCount: 1
  - maxCount: 1
- comment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- created
  - type: DateTime
  - minCount: 1
  - maxCount: 1
- createdBy
  - type: Agent
  - minCount: 1
- createdUsing
  - type: Tool
  - minCount: 0
- dataLicense
  - type: xsd:string
  - minCount: 1
  - maxCount: 1

