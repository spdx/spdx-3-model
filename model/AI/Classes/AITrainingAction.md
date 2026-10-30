SPDX-License-Identifier: Community-Spec-1.0

# AITrainingAction

## Summary

Action representing the temporal execution and resource utilization
of an artificial intelligence model training process.

## Description

The `AITrainingAction` represents a discrete temporal event during which
computational resources are utilized to execute a model training process.
It captures the empirical provenance of a training execution.

An instance of this class should use the `followsProcess` relationship
to reference the `AITrainingProcess` it executes.

To establish a verifiable audit trail, the action shall record the specific
`/Dataset/DatasetPackage` and `/Software/SoftwareArtifact` utilized as inputs,
and shall record the resultant `AIPackage` as its output.

Results of the execution, such as the energy consumed or the duration,
are recorded using a `/Core/Measurement` whose `subject` is the action.
Since the action gives the stage of the lifecycle, the generic entries of
`/Core/ObservablePropertyType` (such as `energyConsumption`) may be used.

In terms of ISO/IEC 5338:2023, this class records a performance of the
model training activity of the implementation process (6.4.9.3 b)
in the design and development stage,
or of retraining as part of the maintenance process (6.4.16)
in the operation and monitoring stage (Figure 3).
The output `AIPackage` is the working AI model produced by the
AI model engineering part of the implementation process (6.4.9.2 a).
Recording the inputs and outputs of the action supports the traceability
outcome of the implementation process (ISO/IEC/IEEE 15288:2023, 6.4.7.2 e),
and configuration management of the model together with the data it was
trained with (ISO/IEC 5338:2023, 6.3.5.3).
Measurements of the action record implementation results
(ISO/IEC/IEEE 15288:2023, 6.4.7.3 c), such as the computing resources and
power used, which ISO/IEC 5338:2023 identifies as an AI-specific
consideration (6.4.15.3).

## Metadata

- name: AITrainingAction
- SubclassOf: /Core/Action
- Instantiability: Concrete
