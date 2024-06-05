SPDX-License-Identifier: Community-Spec-1.0

# energyConsumption

## Summary

Indicates the amount of energy consumption incurred by an AI model.

## Description

Captures the energy consumption of an AI model, either known or estimated.

In the absence of direct measurements, one can estimate the energy consumption
based on information about computational resources (e.g. number of floating
point operations), training time, and other relevant training details.

## Metadata

- name: energyConsumption
- Nature: ObjectProperty
- Range: EnergyConsumption
