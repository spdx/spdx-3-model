SPDX-License-Identifier: Community-Spec-1.0

# inferenceEnergyConsumption

## Summary

Energy consumed during inference time by an AI model
that is being used in the AI system.

**DEPRECATED in SPDX 3.1.**
Use `/Core/Measurement` instead.

## Description

The field specifies the amount of energy consumed during inference time by an
AI model that is being used in the AI system.

This property is deprecated.
Use a `/Core/Measurement` instead, with an `observedProperty` of
`/AI/AIObservablePropertyType/inferenceEnergyConsumption`,
and a `referenceQuantity` and `referenceProperty` that state what the value
is per (for example, per 1000 tokens).
Values migrated from this property, for which that is not known, use
`/AI/AIObservablePropertyType/legacyInferenceEnergyConsumption` instead.

## Metadata

- name: inferenceEnergyConsumption
- Nature: ObjectProperty
- Range: EnergyConsumptionDescription
