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

In terms of ISO/IEC 5338:2023, this class records a performance of
transfer learning (6.4.9.4) in the design and development stage,
or of retraining as part of the maintenance process (6.4.16)
in the operation and monitoring stage (Figure 3).
The base model is the reused system element that is adapted, and the output
is the adapted element (ISO/IEC/IEEE 15288:2023, 6.4.7.3 b 1).
It does not record the model tuning activity of ISO/IEC 5338:2023
(6.4.9.3 c); see `AIFinetuningProcess`.

## Metadata

- name: AIFinetuningAction
- SubclassOf: AITrainingAction
- Instantiability: Concrete
