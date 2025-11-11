SPDX-License-Identifier: Community-Spec-1.0

# StateAction

## Summary

This is the state of an affected Element at a specific moment in time.

## Description

The state of a specific Element is defined, measured or observed in this class at a specific moment in time.
The stateaction is defined by the method used by the definedstaeproces to produce an outcome.

## Metadata

- name: StateAction
- SubclassOf: UseAction
- Instantiability: Concrete

## Properties

- currentState
  - type: State
  - minCount: 1
  - maxCount: 1
- decisionProcess
  - type: DefinedStateProcess
  - minCount: 1
  - maxCount: 1
