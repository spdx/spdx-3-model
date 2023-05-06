SPDX-License-Identifier: Community-Spec-1.0

# License

## Summary

Abstract class for the portion of an AnyLicenseInfo representing a license.

## Description

A License represents a license text, whether listed on the SPDX License List
(ListedLicense) or defined by an SPDX data creator (CustomLicense).

## Metadata

- name: License
- SubclassOf: AnyLicenseInfo
- Instantiability: Abstract

## Properties

- isOsiApproved
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- isFsfLibre
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- standardHeader
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

