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

An instance of this class should utilize the `hasPlan` relationship
to reference the specific `AIFinetuningProcess` to which it conforms.

To establish a verifiable audit trail, the action shall record the specific
`/Dataset/DatasetPackage`, `/Software/SoftwareArtifact`,
and an existing `AIPackage` (representing the base model) utilized as inputs,
and shall record the resultant `AIPackage` (representing the adapted weights)
as its output.

Quantitative telemetry associated with the execution may be appended
utilizing a `/Core/Observation`.

This class aligns conceptually with the physical execution of the
Model Tuning activities specified in ISO/IEC 5338.

## Metadata

- name: AIFinetuningAction
- SubclassOf: AITrainingAction
- Instantiability: Concrete
