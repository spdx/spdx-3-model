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

This class aligns conceptually with the planned methodology for the
Model Implementation stage defined in ISO/IEC 5338.

## Metadata

- name: AITrainingProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Concrete
