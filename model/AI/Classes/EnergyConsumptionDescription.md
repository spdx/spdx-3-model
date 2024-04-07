SPDX-License-Identifier: Community-Spec-1.0

# EnergyConsumptionDescription

## Summary

The class that helps note down the quantity of energy consumption and the unit
used for measurement.

## Description

This class is designed to store energy consumption data, including the quantity
and the unit of measurement.

The energyQuantity property stores the amount of energy consumed,
and the energyUnit property stores the unit used for measurement.

## Metadata

- name: EnergyConsumptionDescription
- Instantiability: Concrete

## Properties

- energyQuantity
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- energyUnit
  - type: EnergyUnitType
  - minCount: 1
  - maxCount: 1
