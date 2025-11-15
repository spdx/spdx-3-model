SPDX-License-Identifier: Community-Spec-1.0

# State

## Summary

A state is an instance that describes what a system, component, subsystem, process, or project has achieved at any given time.

## Description

A state is an instance that describes what a system, component, subsystem, process, or project has achieved at any given time. States are used to describe different conditions within a system and provide information about its current status. They help us understand the behavior of systems or product by showing their progression through various states over time.

States describe what a project has achieved (or not) as opposed to describing actions taken by people involved with the project, or activities performed during development of that project.

## Metadata

- name: State
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## External properties restrictions

- /Core/Artifact/validUntilTime
  - maxCount: 0
- /Core/Element/name
  - minCount: 1
- /Core/Element/description
  - minCount: 1
