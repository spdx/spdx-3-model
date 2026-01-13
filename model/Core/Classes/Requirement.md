SPDX-License-Identifier: Community-Spec-1.0

# Requirement

## Summary

A distinct unit representing a requirement, as used in systems, software, and hardware engineering.

## Description

A requirement element is a distinct unit that defines an expectation, need, behavior, or design intent of an item that either already exists or is to be created in accordance with this requirement.

## Metadata

- name: Requirement
- SubclassOf: Element

## Properties

- requirementUUID
  - type: ExternalIdentifier
  - minCount: 0
  - maxCount: 1
- devLifecycleStage
  - type: LifecycleScopeType
  - minCount: 0
  - maxCount: *
- requirementStatement
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- requirementRationale
  - type: xsd:string
  - minCount: 0
  - maxCount: *
