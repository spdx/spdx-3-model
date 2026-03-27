SPDX-License-Identifier: Community-Spec-1.0

# Requirement

## Summary

A distinct unit representing an assumption associated with an item's use in a systems.

## Description

A assumption element is a distinct unit that defines an constraints imposed by intended design, requirement context or operational context, for correct operation of an item in a system context. 

A `rationale` is an additional detail used to define the reason or justification for the existence of the assumption.
The `rationale` is usually less formal than the wording of the assumption statement itself.

## Metadata

- name: Assumption
- SubclassOf: /Core/Element

## Properties

- devLifecycleStage
  - type: LifecycleScopeType
  - minCount: 0
  - maxCount: *
- rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: *
- assumptionStatement
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- assumptionUUID
  - type: ExternalIdentifier
  - minCount: 0
  - maxCount: 1
