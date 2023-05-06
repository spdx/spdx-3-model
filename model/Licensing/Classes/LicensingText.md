SPDX-License-Identifier: Community-Spec-1.0

# LicensingText

## Summary

Abstract class representing some licensing text.

## Description

A LicensingText represents a license or addition text.

## Metadata

- name: LicensingText
- SubclassOf: /Core/Element
- Instantiability: Abstract

## Properties

- text
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- seeAlso
  - type: xsd:anyURI
- standardeTemplate
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- isDeprecated
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- obsoletedBy
  - type: LicensingText
  - minCount: 0
  - maxCount: 1

