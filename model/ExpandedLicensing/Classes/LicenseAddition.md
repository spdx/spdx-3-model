SPDX-License-Identifier: Community-Spec-1.0

# LicenseAddition

## Summary

Abstract class for additional text intended to be added to a License, but
which is not itself a standalone License.

## Description

A LicenseAddition represents text which is intended to be added to a License
as additional text, but which is not itself intended to be a standalone
License.

It may be an exception which is listed on the SPDX Exceptions List
(ListedLicenseException), or may be any other additional text (as an exception
or otherwise) which is defined by an SPDX data creator (CustomLicenseAddition).

## Metadata

- name: LicenseAddition
- SubclassOf: /Core/Element
- Instantiability: Abstract

## Properties

- additionText
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- standardAdditionTemplate
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- isDeprecatedAdditionId
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- obsoletedBy
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
