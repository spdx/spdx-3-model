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

- comment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- licenseId
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- name
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- licenseText
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- seeAlso
  - type: xsd:anyURI
  - minCount: 0
- isOsiApproved
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- isFsfLibre
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- standardLicenseHeader
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- standardLicenseTemplate
  - type: xsd:string
  - mincount: 0
  - maxCount: 1
- isDeprecatedLicenseId
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- obsoletedBy
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
