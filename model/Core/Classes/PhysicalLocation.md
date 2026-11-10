SPDX-License-Identifier: Community-Spec-1.0

# PhysicalLocation

## Summary

A physical location is a tangible, geographically identifiable place where objects, people, or assets exist or operate.

## Description

A physical location is a tangible, geographically identifiable place where objects, people, or assets exist or operate.

At least one of country, city, streetAddress, geographicPointLocation, or name
shall be provided.

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

## SPARQL

- at_least_one_location_property
  - message: At least one of Core/country, Core/city, Core/streetAddress, Core/geographicPointLocation, or Core/name is required
  - query: <<<
        SELECT $this WHERE {
            FILTER NOT EXISTS { $this <Core/country> ?country . }
            FILTER NOT EXISTS { $this <Core/city> ?city . }
            FILTER NOT EXISTS { $this <Core/streetAddress> ?streetAddress . }
            FILTER NOT EXISTS { $this <Core/geographicPointLocation> ?point . }
            FILTER NOT EXISTS { $this <Core/name> ?name . }
        }
