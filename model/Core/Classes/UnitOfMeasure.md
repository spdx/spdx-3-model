SPDX-License-Identifier: Community-Spec-1.0

# UnitOfMeasure

## Summary

A class that represents a measured quantity paired with a unit of measure from the QUDT ontology.

## Description

UnitOfMeasure class provides a structured way to express measurements: such as size, weight, volume, or other quantities.
It combines a numerical value `quantity` with a unit reference `unitQUDT` that points to a URI in the QUDT (Quantity, Unit, Dimension and Type) ontology.
The QUDT ontology and specifications are available at [www.qudt.org](https://www.qudt.org/).

## Metadata

- name: UnitOfMeasure
- Instantiability: Concrete

## Properties

- quantity
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- unitQUDT
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
