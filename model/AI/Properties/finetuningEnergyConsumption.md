SPDX-License-Identifier: Community-Spec-1.0

# finetuningEnergyConsumption

## Summary

Energy consumed when finetuning the AI model that is
being used in the AI system.

**DEPRECATED in SPDX 3.1.**
Use `/Core/Measurement` instead.

## Description

The field specifies the amount of energy consumed when finetuning the AI model
that is being used in the AI system.

This property is deprecated.
Use a `/Core/Measurement` instead.
If the value is about the AI model, its `subject` is the `AIPackage` and its
`observedProperty` is `/AI/AIObservablePropertyType/finetuningEnergyConsumption`.
If the execution is described, its `subject` is the `AIFinetuningAction` and its
`observedProperty` is `/Core/ObservablePropertyType/energyConsumption`
or a more specific entry.

## Metadata

- name: finetuningEnergyConsumption
- Nature: ObjectProperty
- Range: EnergyConsumptionDescription
