SPDX-License-Identifier: Community-Spec-1.0

# AIFinetuningProcess

## Summary

Process definition specifying the methodology for the adaptation, alignment,
or refinement of a pre-trained artificial intelligence model.

## Description

The `AIFinetuningProcess` establishes the blueprint and planned methodology
for modifying an existing artificial intelligence model to perform specific
tasks or adhere to safety alignments.

As a specialized subclass of `AITrainingProcess`, it acts as the static
template for an intended execution, defining the necessary inputs
(including a pre-trained base model, target datasets, and source code)
alongside the intended hyperparameter configurations and system constraints.
This class details procedural steps and parameters, but does not represent
a temporal event or the utilization of physical computational resources.

A `/Core/Measurement` whose `subject` is the process records a nominal or
typical value for an execution of the process, and shall be a rate unless
its `observationProcedure` states that the value is per execution.
A required threshold, such as a maximum energy, is not an Observation:
it is a `/Core/Requirement` whose subject is the process, and
a Measurement that shows it is met may be linked as evidence.

In terms of ISO/IEC 5338:2023, finetuning is a form of transfer learning,
in which an existing machine learning model is the starting point for
further training (6.4.9.4), as part of the implementation process
in the design and development stage.
When a deployed model is finetuned to keep it performing as required,
it is retraining as part of the maintenance process (6.4.16)
in the operation and monitoring stage (Figure 3).
This class does not correspond to the model tuning activity of
ISO/IEC 5338:2023 (6.4.9.3 c), which is the search for the hyperparameters
that give the best performance on validation data.

The base model is a reused system element that is adapted, so the
implementation strategy should determine its source and suitability
(ISO/IEC/IEEE 15288:2023, 6.4.7.3 a 1 and b 1;
ISO/IEC/IEEE 12207:2017, 6.4.7.3 a 1 ii).

## Metadata

- name: AIFinetuningProcess
- SubclassOf: AITrainingProcess
- Instantiability: Concrete
