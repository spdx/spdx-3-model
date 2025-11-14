SPDX-License-Identifier: Community-Spec-1.0

# UnitOfMeasure

## Summary

UnitofMeasure specify information structures through industry standards for Units of Measure, Quantity Kinds, Dimensions and Data Types.

## Description

The QUDT, or "Quantity, Unit, Dimension and Type" schema defines the base classes properties, and restrictions used for modeling physical quantities, units of measure, and their dimensions in various measurement systems.

## Metadata

- name: UnitOfMeasure
- Instantiability: Concrete

## Properties

- quantity
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- unitQUDT
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
