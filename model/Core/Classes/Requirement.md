SPDX-License-Identifier: Community-Spec-1.0

# Requirement

## Summary

A distinct unit representing a requirement, as used in systems, software, and hardware engineering.

## Description

A requirement element is a distinct unit that defines an expectation, need, behavior, or design intent of an item that either already exists or is to be created in accordance with this requirement.

A `rationale` is an additional detail used to define the reason or
justification for the existence of the requirement.
The `rationale` is usually less formal than the wording of the
requirement statement itself.

## Metadata

- name: Requirement
- SubclassOf: Element

## Properties

- devLifecycleStage
  - type: LifecycleScopeType
  - minCount: 0
  - maxCount: *
- rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: *
- requirementStatement
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- requirementUUID
  - type: ExternalIdentifier
  - minCount: 0
  - maxCount: 1
