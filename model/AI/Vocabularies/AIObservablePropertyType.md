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

The unit of the observed value shall have the same dimension as the
quantity kind that the entry specializes:

- `finetuningEnergyConsumption`, `inferenceEnergyConsumption`, and
  `trainingEnergyConsumption` specialize
  `/Core/ObservablePropertyType/energyConsumption`, and
  `legacyInferenceEnergyConsumption` specializes
  `inferenceEnergyConsumption`.
- `trainingComputeOperations` specializes
  `/Core/ObservablePropertyType/computeOperations`.
- `inferenceCount` specializes the QUDT quantity kind
  <http://qudt.org/vocab/quantitykind/Count>.
- `inferenceLatency` and `trainingDuration` specialize the QUDT quantity kind
  <http://qudt.org/vocab/quantitykind/Time>.

<!--
TODO: When spec-parser supports vocabulary entry attributes, add back:
- in Metadata: `- entryType: http://qudt.org/schema/qudt/QuantityKind`
  (emitted as rdf:type of each entry);
- under each entry: `  - broader: <IRI or /Namespace/Vocabulary/entry>`
  (emitted as skos:broader), using the quantity kinds listed above.
Removed from PR #1246 because spec-parser main rejects them.
-->

## Metadata

- name: AIObservablePropertyType

## Entries

- finetuningEnergyConsumption: Energy consumed to finetune the model.
- inferenceCount: Number of inferences performed by the model.
- inferenceEnergyConsumption: Energy consumed by the model to perform inference.
- inferenceLatency: Time from the receipt of an inference request to the delivery of its complete response.
- legacyInferenceEnergyConsumption: Energy consumed during inference, with an unknown reference quantity; migrated from the deprecated inferenceEnergyConsumption property.
- trainingComputeOperations: Number of arithmetic operations performed to train the model.
- trainingDuration: Elapsed time taken to train the model.
- trainingEnergyConsumption: Energy consumed to train the model.
