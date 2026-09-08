SPDX-License-Identifier: Community-Spec-1.0

# AITrainingAction

## Summary

Action representing the temporal execution and resource utilization
of an artificial intelligence model training process.

## Description

The `AITrainingAction` represents a discrete temporal event during which
computational resources are utilized to execute a model training process.
It captures the empirical provenance of a training execution.

An instance of this class should utilize the `hasPlan` relationship
to reference the specific `AITrainingProcess` to which it conforms.

To establish a verifiable audit trail, the action shall record the specific
`/Dataset/DatasetPackage` and `/Software/SoftwareArtifact` utilized as inputs,
and shall record the resultant `AIPackage` as its output.

Quantitative telemetry associated with the execution may be appended
utilizing a `/Core/Observation`.

This class aligns conceptually with the physical execution of the
Model Implementation activities specified in ISO/IEC 5338.

## Metadata

- name: AITrainingAction
- SubclassOf: /Core/Action
- Instantiability: Concrete
