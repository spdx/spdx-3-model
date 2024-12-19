SPDX-License-Identifier: Community-Spec-1.0

# Hardware

## Summary

The Hardware Profile provides additional metadata, that is useful for hardware.

## Description

The Hardware namespace defines concepts related to hardware, including VuHardware
preparation process, its characteristics, and its access methods.

## Metadata

- id: https://spdx.org/rdf/3.1.0/terms/Hardware
- name: Hardware

## Profile conformance

For an element collection to be conformant with this profile,
the following has to hold:


1. for every `/Hardware/Hardware` The property listed under the physical are not available if virtualFlag = true

2. for every `/Core/Process` with the processType = 'Instantiation' there MUST exist exactly one
   `/Core/Relationship` of type `instantiation` having that element as its
   `from` property and a `/Hardware/Hardware` as its `to`
    property with that element virtualFlag = true.
    
3. for every `/Hardware/HBOMPhysical` If the property mass is defined then massUnit must be defined.

4. For evert `/Hardware/HBOMPhysical` If the property dimensions and centerofMass is defined then both centerofMass and dimensions have the same coordinateorientationType for x, y, and z.
