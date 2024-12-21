SPDX-License-Identifier: Community-Spec-1.0

# Process

## Summary

Class that describes a process.

## Description

Processes define a set of tasks needed to perform a procedure. The step to assemble a table is an is a process.

## Metadata

- name: Process
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- version
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- rationale 
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- status
  - type: documentState
  - minCount: 0
  - maxCount: 1
- typeOfProcess
  - type: processType
  - minCount: 1
  - maxCount: 1
