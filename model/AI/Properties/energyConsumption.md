SPDX-License-Identifier: Community-Spec-1.0

# energyConsumption

## Summary

Energy consumption incurred by an AI model.

**DEPRECATED in SPDX 3.1.**
Use `/Core/Observation` instead.

## Description

Energy consumption of an AI model, either known or estimated.

In the absence of direct measurements, an SPDX data creator may choose to
estimate the energy consumption based on information about computational
resources (e.g., number of floating-point operations), training time, and other
relevant training details.

This property is deprecated.
Use `/Core/Observation` with appropriate `Action` or `DefinedProcess` instead.

## Metadata

- name: energyConsumption
- Nature: ObjectProperty
- Range: EnergyConsumption
