SPDX-License-Identifier: Community-Spec-1.0

# EnergyConsumptionDescription

## Summary

The Class that helps note down the energy consumption value and the unit in which it is recorded.

## Description

The class that helps note down the energy consumption value and the unit in which it is recorded. Value property describes the energy consumption and the unit field describes the units in which it was recorded. 

## Metadata

- name: EnergyConsumptionDescription
- Instantiability: Concrete

## Properties

- value
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- unit
  - type: EnergyConsumptionDescriptionUnitType
  - minCount: 1
  - maxCount: 1
