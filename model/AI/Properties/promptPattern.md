SPDX-License-Identifier: Community-Spec-1.0

# promptPattern

## Summary

Identifies a design pattern or structured prompting strategy used within
a prompt to guide a foundation model toward a desired output or enhance
its performance.

## Description

A free-form text field used to record the name of the prompt pattern or
high-level strategy given to the foundation model (e.g., a large language
model).

The purpose of this field is to document the specific technique that governs
the model's behavior during output generation.

This prompt pattern defines the core technique used to enhance the model's
reasoning or cognitive process, control its interaction flow, or ensure the
output adheres to specific criteria and constraints.

Although this is a free-form text field, it is recommended that standardized
terminology be utilized where possible to facilitate consistency and
interoperability.

Examples of possible values:

- `simple`: Use to indicate a prompt without any specific pattern.
- `chain-of-thought`: Explicitly requires sequential, step-by-step reasoning
  before the answer.
- `decomposition`: Breaks a complex task into a collection of simpler
  sub-tasks.
- `flipped-interaction`: Reverses roles, instructing the model to ask
  clarifying questions first.
- `persona`: Instructs the model to adopt a specific role or character.
- `self-consistency`: Generates multiple outputs and selects the most common
  (consensual) answer.
- `self-reflection`: Asks the model to critique and refine its own output or
  steps.
- `tree-of-thought`: Explores and evaluates multiple branching lines of
  reasoning.

## Metadata

- name: promptPattern
- Nature: DataProperty
- Range: xsd:string
