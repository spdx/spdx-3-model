SPDX-License-Identifier: Community-Spec-1.0

# AIInferenceAction

## Summary

Action representing the execution of inference by an artificial intelligence
model over a period of time.

## Description

The `AIInferenceAction` represents a period during which an artificial
intelligence model performs inference, such as a benchmark run or one month
of serving requests in production.
The `startTime` and `endTime` properties give the period.

An instance of this class should use the `followsProcess` relationship
to reference the `AIInferenceProcess` it executes.
The model used should be recorded as an input of the action.

Results of the execution, such as the energy consumed, the number of tokens
processed, or the number of inferences performed, are recorded using
a `/Core/Measurement` whose `subject` is the action.
Since the action gives the stage of the lifecycle, the generic entries of
`/Core/ObservablePropertyType` (such as `energyConsumption`) may be used.
A value per inference can be derived by dividing by a Measurement of
`/AI/AIObservablePropertyType/inferenceCount` on the same action.

In terms of ISO/IEC 5338:2023, this class records a period of use of the
model in the operation process (6.4.15), or a run of the model to test it,
such as a benchmark, in the verification (6.4.11) or continuous validation
(6.4.14) processes.
These processes take place in the operation and monitoring,
verification and validation, and continuous validation stages,
respectively (Figure 3).
Measurements of the action can record the computing resources and power
used (6.4.15.3), and the performance that the continuous validation process
monitors over time (6.4.14.3).

See `AIInferenceProcess` for an example.

## Metadata

- name: AIInferenceAction
- SubclassOf: /Core/Action
- Instantiability: Concrete
