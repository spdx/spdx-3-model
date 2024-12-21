SPDX-License-Identifier: Community-Spec-1.0

# HBOMPhysical

## Summary

Class that describes a instance of HBOMPhysical.

## Description

Describes the physical characteristics of hardware. 
Physical characteristics include dimensions, mass, units and related items.

## Metadata

- name: HBOMPhysical
- Instantiability: Concrete

## Properties

- dimensions
  - type: /Hardware/HBOMDimensions
  - maxCount: 1
- mass 
  - type: xsd:Number
  - maxCount: 1
- massUnit
  - type: xsd:string
  - maxCount: 1
- centerofMass
  - type: xsd:/Hardware/HBOMDimensions
  - maxCount: 1
