SPDX-License-Identifier: Community-Spec-1.0

# PhysicalHardware

## Summary

Class that describes a physical instance of Hardware.

## Description

A PhysicalHardware artifact describes a distinct physical unit.

## Metadata

- name: PhysicalHardware
- SubclassOf: Hardware
- Instantiability: Concrete

## Properties

- massOfHardware
  - type: /Core/MeasureOfMass
  - minCount: 0
  - maxCount: 1
- dimensions
  - type: Dimensions
  - maxCount: 1  
- centerOfMass
  - type: Dimensions
  - maxCount: 1
