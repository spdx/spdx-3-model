SPDX-License-Identifier: Community-Spec-1.0

# AITrainingProcess

## Summary

Process definition establishing the methodology, architecture,
and configuration necessary to train an artificial intelligence model.

## Description

The `AITrainingProcess` establishes the blueprint and planned methodology
for training an artificial intelligence model.
It acts as the static template for an intended execution,
defining the necessary inputs (including target datasets and source code)
alongside the intended hyperparameter configurations and system constraints.

This class details procedural steps and parameters, but does not represent
a temporal event or the utilization of physical computational resources.

A `/Core/Measurement` whose `subject` is the process records a nominal or
typical value for an execution of the process, and shall be a rate unless
its `observationProcedure` states that the value is per execution.
A required threshold, such as a maximum energy, is not an Observation:
it is a `/Core/Requirement` whose subject is the process, and
a Measurement that shows it is met may be linked as evidence.

In terms of ISO/IEC 5338:2023, this class describes how the model training
activity of the implementation process (6.4.9.3 b) is to be performed.
Training is not a life cycle stage in that document, but an activity of
AI model engineering, which is part of the implementation process and
takes place in the design and development stage (Figure 3).
The procedures, tools, and enabling systems defined by the process
correspond to those identified when preparing for implementation
(ISO/IEC/IEEE 15288:2023, 6.4.7.3 a).
The hyperparameter configuration it defines is typically the result of the
algorithm selection and model tuning activities (ISO/IEC 5338:2023,
6.4.9.3 a and c).
The same process may also be followed to retrain a model as part of the
maintenance process (ISO/IEC 5338:2023, 6.4.16), which takes place in the
operation and monitoring stage.

## Metadata

- name: AITrainingProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Concrete
