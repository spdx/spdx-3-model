SPDX-License-Identifier: Community-Spec-1.0

# PhysicalLocation

## Summary

A physical location is a tangible, geographically identifiable place where objects, people, or assets exist or operate.

## Description

A physical location is a tangible, geographically identifiable place where objects, people, or assets exist or operate.

## Metadata

- name: PhysicalLocation
- SubclassOf: Location
- Instantiability: Concrete

## Properties

- country
  - type: CountryCodeAlpha3
  - minCount: 0
  - maxCount: 1
- countyCode
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- city
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- postalCode
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- postalName
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- postOfficeBoxNumber
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- provinceStateCode
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- streetAddress
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- geographicPointLocation
  - type: xsd:string
  - minCount: 0
