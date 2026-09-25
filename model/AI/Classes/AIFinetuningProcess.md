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

Expected quantitative metrics or threshold boundaries associated with
the planned methodology may be appended utilizing an `Observation`.

This class aligns conceptually with the planned methodology for the
Model Tuning stage defined in ISO/IEC 5338.

## Metadata

- name: AIFinetuningProcess
- SubclassOf: AITrainingProcess
- Instantiability: Concrete
