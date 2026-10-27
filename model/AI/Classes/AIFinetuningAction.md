SPDX-License-Identifier: Community-Spec-1.0

# AIFinetuningAction

## Summary

Action representing the temporal execution and resource utilization
of a finetuning process upon a pre-trained artificial intelligence model.

## Description

The `AIFinetuningAction` represents a discrete temporal event during which
computational resources are utilized to adapt or refine an existing
artificial intelligence model.
It captures the empirical provenance of a finetuning execution.

An instance of this class should use the `followsProcess` relationship
to reference the `AIFinetuningProcess` it executes.

To establish a verifiable audit trail, the action shall record the specific
`/Dataset/DatasetPackage`, `/Software/SoftwareArtifact`,
and an existing `AIPackage` (representing the base model) utilized as inputs,
and shall record the resultant `AIPackage` (representing the adapted weights)
as its output.

Results of the execution, such as the energy consumed or the duration,
are recorded using a `/Core/Measurement` whose `subject` is the action.
Since the action gives the stage of the lifecycle, the generic entries of
`/Core/ObservablePropertyType` (such as `energyConsumption`) may be used.

This class aligns conceptually with the physical execution of the
Model Tuning activities specified in ISO/IEC 5338.

## Metadata

- name: AIFinetuningAction
- SubclassOf: AITrainingAction
- Instantiability: Concrete
