SPDX-License-Identifier: Community-Spec-1.0

# AIObservablePropertyType

## Summary

Recommended observable properties for observations of artificial intelligence
models and their training, finetuning, and inference.

## Description

The `AIObservablePropertyType` vocabulary provides identifiers for
properties that are specific to a stage of the lifecycle of an
artificial intelligence model.

The IRI of an entry of this vocabulary may be used as the value of
the `/Core/observedProperty` property of a `/Core/Observation`.

When the subject of the observation is an `AITrainingAction`,
`AIFinetuningAction`, or `AIInferenceAction`, the stage is already given
by the subject, and the generic entries of
`/Core/ObservablePropertyType` may be used instead.
The stage-specific entries of this vocabulary are intended for observations
whose subject is an `AIPackage`, for example to record values declared
in a model card.

A `/Core/Measurement` of inference energy consumption whose subject is not
an `AIInferenceAction` shall state what the value is per, using the
`/Core/referenceQuantity` and `/Core/referenceProperty` properties
(for example, per 1000 tokens).
`legacyInferenceEnergyConsumption` shall be used only for values migrated
from the deprecated `inferenceEnergyConsumption` property, where that is not known.

Each entry is a QUDT quantity kind that is a specialization (`skos:broader`)
of a QUDT quantity kind or of an entry of `/Core/ObservablePropertyType`.

## Metadata

- name: AIObservablePropertyType
- entryType: http://qudt.org/schema/qudt/QuantityKind

## Entries

- finetuningEnergyConsumption: Energy consumed to finetune the model.
  - broader: /Core/ObservablePropertyType/energyConsumption
- inferenceCount: Number of inferences performed by the model.
  - broader: http://qudt.org/vocab/quantitykind/Count
- inferenceEnergyConsumption: Energy consumed by the model to perform inference.
  - broader: /Core/ObservablePropertyType/energyConsumption
- inferenceLatency: Time from the receipt of an inference request to the delivery of its complete response.
  - broader: http://qudt.org/vocab/quantitykind/Time
- legacyInferenceEnergyConsumption: Energy consumed during inference, with an unknown reference quantity; migrated from the deprecated inferenceEnergyConsumption property.
  - broader: /AI/AIObservablePropertyType/inferenceEnergyConsumption
- trainingComputeOperations: Number of arithmetic operations performed to train the model.
  - broader: /Core/ObservablePropertyType/computeOperations
- trainingDuration: Elapsed time taken to train the model.
  - broader: http://qudt.org/vocab/quantitykind/Time
- trainingEnergyConsumption: Energy consumed to train the model.
  - broader: /Core/ObservablePropertyType/energyConsumption
